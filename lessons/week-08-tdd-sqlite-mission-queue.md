# Week 8 Lab Guide: Test-Driven Data Management with SQLite

**A MissionQueue built one red-green-refactor step at a time, driven by Claude Code.**

> Instructor guide, student walkthrough, and process record in one file.
> Built live on 2026-10-09 and written up the same afternoon. Code listings are
> reproduced from that session; the durability ladder in section 5.5 was
> re-run and verified afterward (Python 3.13, with the session itself on
> Python 3.12.10, Windows PowerShell, pytest 9.1.1).

---

## 0. At a glance

| | |
|---|---|
| **Topic** | Data management: schema, parameterized SQL, transactions, durability |
| **Method** | Strict test-driven development (red, green, refactor), one test at a time |
| **Paradigm** | Object-oriented: a class whose public interface hides its storage |
| **Storage** | SQLite via Python's built-in `sqlite3` (no install) |
| **Tools** | Python 3.12+, pytest, git, Claude Code (optional but used throughout) |
| **Project folder** | `week_08/starship_project/` |
| **Time** | About 90 minutes for cycles 1 to 3; a full session with the concept notes |

**One-sentence version:** write a failing test, make it pass with the least code,
clean up, and let each new test force the design (including the moment a test
finally *requires* a real database on disk).

---

## 1. Learning outcomes

By the end, a student can:

1. Run a strict TDD loop and explain why each phase (red, green, refactor) exists.
2. Explain why a test must fail **for the right reason** before any code is written.
3. Build a class whose public interface (`enqueue`, `is_empty`, ...) hides its storage engine.
4. Use `sqlite3` with **parameterized queries** and explain what goes wrong without them.
5. Explain the difference between an **in-memory** database and a **durable** one, and prove durability with a test that crosses a process boundary.
6. Explain why SQLite needs `commit()` and what is lost without it.
7. Explain binary vs. text files and raster vs. vector images, and what each means for performance and for version control.
8. Keep a clean git history for a TDD project (commit on green, never on red; ignore generated files).

---

## 2. Why this lesson exists (and what we changed from the first draft)

The starting point was a "Starship Mission Log" write-up: a FIFO `MissionQueue`
and a LIFO `AlertStack`, both backed by SQLite, 11 tests, "all green". It was a
good start. Flipping `ORDER BY id ASC` to `DESC` to get a queue vs. a stack from
the same table is a genuinely nice lesson.

The review found one big problem and a few smaller ones:

| Issue | Why it matters | What we did |
|---|---|---|
| It was a data **structures** lesson wearing a data **management** hat | SQLite was a hidden list with a hard drive: one table, one column that mattered, no constraints, no transactions | New spine: each cycle introduces a data-management idea (schema, parameters, transactions, durability) |
| Several tests were written in a batch, then described as red/green | A retroactive red/green table is a "TDD costume party"; students learn the story, not the discipline | Rebuilt from scratch, **one test at a time**, with the real failure shown each time |
| "Swap the implementation, zero client changes" was asserted, never proven | An untested claim | Planned: run one contract test suite against a list-backed and a SQLite-backed queue (see section 5.7) |
| `dequeue` as `SELECT` then `DELETE` is not atomic | Two ships could grab the same mission | Planned: status column plus atomic update (section 5.7) |

So the project restarted at test number one. That decision is the most
important teaching move in the whole session.

---

## 3. Environment setup (Windows)

### 3.1 Python and pytest

```powershell
python --version          # 3.12 or newer is fine
pip install pytest
python -m pytest --version
```

Use `python -m pytest` rather than bare `pytest`. It guarantees pytest runs under
the same Python you just installed it into, and it puts the current folder on the
import path (which our `from starship_log import MissionQueue` relies on).

### 3.2 Install Claude Code

Claude Code is a terminal program. You will drive the TDD loop by giving it short,
strict prompts. The official instructions live at
<https://code.claude.com/docs/en/setup>. For Windows PowerShell (a prompt that
starts with `PS C:\`), either of these works. No administrator rights are needed.

**Option A: native installer (recommended; auto-updates)**

```powershell
irm https://claude.ai/install.ps1 | iex
```

It prints no progress while downloading, so give it a minute.

**Option B: WinGet (does not auto-update)**

```powershell
winget install Anthropic.ClaudeCode
winget upgrade Anthropic.ClaudeCode      # run now and then to update
```

> Claude Code needs a Pro, Max, Team, Enterprise, or Console account. The free
> claude.ai plan does not include it.

### 3.3 Verify, and fix `claude : The term 'claude' is not recognized`

**Close PowerShell completely and open a new window.** Installers change PATH, and
only new terminals see the change. Then:

```powershell
claude --version        # prints a version number if it worked
claude doctor           # read-only diagnostics if it did not
```

If the command is still not found:

```powershell
# 1. Did the installer put the file there?
Test-Path "$env:USERPROFILE\.local\bin\claude.exe"

# 2. Is that folder on PATH?
$env:PATH -split ';' | Select-String '\.local\\bin'
```

| Result | Meaning | Fix |
|---|---|---|
| #1 is `False` | The install never finished | Re-run the installer; watch for red error text |
| #1 `True`, #2 prints nothing | Installed, but PATH is missing the folder | Add it (below), then open a new terminal |
| #1 `True`, #2 shows a match | You are in an old terminal that predates the install | Open a new terminal |

```powershell
$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
```

Quick workaround that skips PATH entirely:

```powershell
& "$env:USERPROFILE\.local\bin\claude.exe"
```

Optional: install **Git for Windows**. Without it, Claude Code uses PowerShell as
its shell tool; with it, it also gets a Bash tool.

### 3.4 First run

```powershell
cd <path-to>\computer_science_2\week_08\starship_project
claude
```

The first launch opens a browser to log in. After that, `claude` in any project
folder starts a session there.

---

## 4. Ground rules for strict TDD

Write these on the board. They are also the opening prompt for Claude Code
(Appendix A, prompt 1), because an AI assistant will happily race ahead unless you
build the brakes into the conversation.

1. **One failing test at a time.** Never write two new tests in one step.
2. **RED:** write the test, run it, read the failure, and **stop**.
3. The failure must be **the right reason**. `ModuleNotFoundError` for a module that does not exist yet is right. A typo in the test is not.
4. **GREEN:** write the **smallest** code that passes. Hardcoding is legal.
5. **REFACTOR:** clean up with the tests green, only when there is something worth cleaning. "Nothing to refactor yet" is a valid answer.
6. **Commit on green and after refactors. Never commit a red suite.**
7. Never get ahead of the driver. The human says "green" and "refactor".

### Why "fake it till you make it" is not cheating

The first green in this lesson is literally:

```python
class MissionQueue:
    def is_empty(self):
        return True
```

That is a deliberate lie. It passes the only test that exists. The *next* test
(`not is_empty()` after an enqueue) cannot pass with that lie, so the test suite
**forces** honest code. Students see the tests, not the teacher, being the one
who demands the real implementation.

---

## 5. The cycles

### Status board

| # | Behavior | Red (right reason) | Green | State |
|---|---|---|---|---|
| 1 | A new queue is empty | `ModuleNotFoundError: No module named 'starship_log'` | `return True` | Done |
| 2 | Not empty after `enqueue` | `AttributeError: ... no attribute 'enqueue'` | `sqlite3` in memory, parameterized insert | Done |
| R | Story demo (`__main__`) | n/a (refactor) | `show_table` plus three-chapter script | Done |
| C | Catch-up characterization tests | n/a (written after the code) | 7 tests, all passed first run | Done (see 5.4) |
| 3 | Data survives a separate Python process | `TypeError: __init__() takes 1 positional argument but 2 were given` (inside the child process) | `db_path`, `close()`, `IF NOT EXISTS`, `commit()` | **Red confirmed; ladder pending** |
| 4+ | FIFO `dequeue`, `peek`, `size`, `EmptyError`, ... | | | Next |

### 5.1 Cycle 1: a new queue is empty

**Test** (`test_starship_log.py`):

```python
from starship_log import MissionQueue


def test_new_queue_is_empty():
    queue = MissionQueue()
    assert queue.is_empty()
```

**Red.** `python -m pytest test_starship_log.py` gives
`ModuleNotFoundError: No module named 'starship_log'`. The test asks for
something that does not exist: the right reason.

**Green** (`starship_log.py`):

```python
class MissionQueue:
    def is_empty(self):
        return True
```

**Refactor check:** nothing worth changing. Say so out loud; it models honesty.

Teaching point: **a test you have never seen fail has not proven anything.**

### 5.2 Cycle 2: not empty after enqueue (and the SQLite decision)

**Test:**

```python
def test_queue_is_not_empty_after_enqueue():
    queue = MissionQueue()
    queue.enqueue("Scan Nebula-7")
    assert not queue.is_empty()
```

**Red:** `AttributeError: 'MissionQueue' object has no attribute 'enqueue'`.
Test 1 stays green, which is the safety net: `1 failed, 1 passed`.

**A design decision, stated honestly.** This test does *not* demand SQLite. A
plain list, or even a boolean flag, would pass. We chose SQLite because it is the
learning goal, and we said so in the code. A purist would wait for a test that
forces a database; the durability test in cycle 3 is that test. Teaching both
options is better than pretending the test made us do it.

**Green** (what Claude Code produced under the "use sqlite3 with `:memory:`"
instruction):

```python
import sqlite3


class MissionQueue:
    # Design decision: SQLite (in memory) is our choice, not something the
    # tests demand yet. A plain list would also pass the current tests.
    def __init__(self):
        self._connection = sqlite3.connect(":memory:")
        self._connection.execute(
            "CREATE TABLE missions ("
            "id INTEGER PRIMARY KEY, "
            "title TEXT NOT NULL)"
        )

    def enqueue(self, title):
        self._connection.execute(
            "INSERT INTO missions (title) VALUES (?)", (title,)
        )

    def is_empty(self):
        row = self._connection.execute(
            "SELECT COUNT(*) FROM missions"
        ).fetchone()
        return row[0] == 0
```

Concepts packed into 20 lines:

- **Schema.** `id INTEGER PRIMARY KEY` auto-assigns 1, 2, 3 in insertion order,
  which is exactly the property a FIFO queue will need. `title TEXT NOT NULL` is a
  constraint: bad data is rejected by the database, not by hope.
- **Parameterized query.** The `?` placeholder sends the value separately from the
  SQL text. See the injection demo below.
- **Encapsulation.** Callers see `enqueue` and `is_empty`. Nobody outside the class
  writes SQL. That is the "interface vs. implementation" promise.
- **`:memory:`.** A private database that vanishes when the connection closes.
  Each `MissionQueue()` gets its own.

**Peek at the real table** (one line; paste it as *one* line, see pitfalls):

```powershell
python -c "from starship_log import MissionQueue as M; q=M(); q.enqueue('Scan Nebula-7'); q.enqueue('Survey Kepler-442b'); print(q._connection.execute('SELECT * FROM missions').fetchall())"
```

```
[(1, 'Scan Nebula-7'), (2, 'Survey Kepler-442b')]
```

**Demo: why the `?` matters.** Verified output of the same hostile title through
both approaches:

```python
evil = "x'); DROP TABLE missions;--"

# parameterized: stored as plain text
con.execute("INSERT INTO missions (title) VALUES (?)", (evil,))
#   -> [("x'); DROP TABLE missions;--",)]

# string formatting: the title becomes SQL and the table is destroyed
con.executescript(f"INSERT INTO missions (title) VALUES ('{evil}')")
#   -> OperationalError: no such table: missions
```

### 5.3 Refactor: make the demo tell a story

The instructor asked for a human narrative instead of a throwaway one-liner:
a `show_table` helper and an `if __name__ == "__main__":` block.

```python
def show_table(queue):
    # Demo only: peeks at the private connection so we can see the database.
    rows = queue._connection.execute("SELECT id, title FROM missions").fetchall()
    print(f"  is_empty() -> {queue.is_empty()}")
    if not rows:
        print("  missions table: (no rows)")
    for mission_id, title in rows:
        print(f"  missions table: id={mission_id}  title={title!r}")


if __name__ == "__main__":
    print("Chapter 1: A brand new mission queue")
    queue = MissionQueue()
    show_table(queue)

    print("\nChapter 2: The first mission is added")
    queue.enqueue("Scan Nebula-7")
    show_table(queue)

    print("\nChapter 3: A second mission joins the line behind it")
    queue.enqueue("Survey Kepler-442b")
    show_table(queue)
```

Run with `python starship_log.py`:

```
Chapter 1: A brand new mission queue
  is_empty() -> True
  missions table: (no rows)

Chapter 2: The first mission is added
  is_empty() -> False
  missions table: id=1  title='Scan Nebula-7'

Chapter 3: A second mission joins the line behind it
  is_empty() -> False
  missions table: id=1  title='Scan Nebula-7'
  missions table: id=2  title='Survey Kepler-442b'
```

Notes worth saying out loud:

- `if __name__ == "__main__":` means "run this only when the file is executed
  directly, not when it is imported". Tests import the module and must not trigger
  the story.
- Claude Code deliberately **did not** add a public `missions()` method for the
  demo. No test had asked for one. It marked `show_table` as demo-only because it
  reaches into a private attribute. That restraint is the discipline we want.

### 5.4 Catch-up tests (and an honest label for them)

After the refactor the instructor said, in effect: "I got the rotation wrong;
write the tests that cover everything we now have." Claude Code added seven:

| Test | What it pins down |
|---|---|
| `test_enqueue_stores_the_title_in_the_missions_table` | A title lands in the table with id 1 |
| `test_enqueue_keeps_missions_in_insertion_order_with_rising_ids` | Ids go 1, 2 in order (the property FIFO will rely on) |
| `test_enqueue_treats_sql_in_a_title_as_plain_text` | The `?` placeholder guarantee |
| `test_each_queue_has_its_own_separate_database` | Two `:memory:` queues do not share data |
| `test_show_table_reports_an_empty_queue` | Demo helper output when empty |
| `test_show_table_lists_each_mission_with_its_id` | Demo helper output with rows |
| `test_running_the_module_tells_the_three_chapter_story` | Running as `__main__` prints chapters in order |

Suite total: **9 passing**.

**These are characterization tests, not TDD.** They were written *after* the code,
so they passed on the first run and never failed. Claude Code said so plainly:
they show the current behavior is right today, not that they *can* fail. Good
practice, and a good exercise, is a **mutation check**: break the code on purpose
(swap `?` for an f-string, say) and confirm the matching test goes red. Mention
that the storage tests read the private `_connection`; when `dequeue` and `peek`
exist they should be rewritten to use the public interface.

> Lesson for students: "I fell out of rotation" is recoverable, and *labeling*
> the recovery honestly (characterization tests, not red-first) is what keeps the
> history trustworthy.

### 5.5 Cycle 3: data that survives outside Python

**The question:** "I want a durable database on disk that survives outside of
Python. How do we get a red test for that?"

There are three strengths of "durable", and each is a different test:

| Level | Test | Weakness |
|---|---|---|
| 1 | Same process: enqueue, `close()`, reopen the file | The object might be cached in memory somewhere |
| 2 | The `.db` file exists | It could exist and be empty |
| 3 | **A separate Python process writes, then this process reads** | Hard to fake: only a real file can pass |

Level 3 is the strongest and the best lesson. A second Python starts, writes a
mission, and **exits completely**, taking all of its memory with it. Whatever the
test then reads can only have come from disk.

**The test:**

```python
import subprocess
import sys
from pathlib import Path


def test_data_survives_a_separate_python_process(tmp_path):
    db_file = tmp_path / "starship.db"
    writer = (
        "import sys; from starship_log import MissionQueue; "
        "q = MissionQueue(sys.argv[1]); q.enqueue('Scan Nebula-7'); q.close()"
    )
    subprocess.run(
        [sys.executable, "-c", writer, str(db_file)],
        check=True,
        cwd=Path(__file__).parent,
    )
    assert db_file.exists()
    reopened = MissionQueue(db_file)
    assert not reopened.is_empty()
```

`tmp_path` is a pytest fixture: a fresh throwaway folder per test run, so no stray
`.db` ever lands in the project.

**Red (confirmed in the session).** The failure appears in the *child* process's
captured stderr:

```
TypeError: MissionQueue.__init__() takes 1 positional argument but 2 were given
1 failed, 9 passed
```

All nine existing tests stayed green.

#### The failure ladder (verified)

The technique is **move the failure forward by one**. Make the smallest change that
fixes the *current* failure, run again, and let the test show the next one. Do not
write all four fixes at once. Verified by running each step:

| Step | Change | Next failure | Lesson |
|---|---|---|---|
| 0 | (start) | `TypeError` in the child: constructor takes no path | The class has no way to point at a file |
| 1 | `__init__(self, db_path=":memory:")` and `sqlite3.connect(db_path)` | `AttributeError: ... no attribute 'close'` in the child | Files need to be closed |
| 2 | Add `close()` | `sqlite3.OperationalError: table missions already exists` | The file has a table from the first run; creating it again fails |
| 3 | `CREATE TABLE IF NOT EXISTS` | `assert not True` (the file exists but `is_empty()` is `True`) | **The commit trap**: the insert was rolled back |
| 4 | `self._connection.commit()` after the insert | **3 passed** | Writes are not durable until committed |

Two details students find surprising:

- The `default=":memory:"` keeps every earlier test green, since they call
  `MissionQueue()` with no argument.
- **Step 3 is the big one.** `CREATE TABLE` takes effect immediately, so the file
  exists with the right table. But `INSERT` opens a transaction, and
  `close()` without `commit()` silently throws it away. No error, no warning, just
  an empty queue. That is why we test durability with a real second process.

(An earlier version of this guide's plan listed the commit trap before the
"table already exists" error. Running it showed the order above; the tests are the
authority, not our predictions. Worth telling students.)

**Final code after cycle 3 (verified, 3 tests passing in a scratch copy):**

```python
import sqlite3


class MissionQueue:
    def __init__(self, db_path=":memory:"):
        self._connection = sqlite3.connect(db_path)
        self._connection.execute(
            "CREATE TABLE IF NOT EXISTS missions ("
            "id INTEGER PRIMARY KEY, "
            "title TEXT NOT NULL)"
        )

    def enqueue(self, title):
        self._connection.execute(
            "INSERT INTO missions (title) VALUES (?)", (title,)
        )
        self._connection.commit()

    def is_empty(self):
        row = self._connection.execute(
            "SELECT COUNT(*) FROM missions"
        ).fetchone()
        return row[0] == 0

    def close(self):
        self._connection.close()
```

**Look at the real file.** After a durable run:

```
size on disk: 8192 bytes
first 16 bytes: b'SQLite format 3\x00'
```

Eight kilobytes for two rows is not waste; SQLite stores data in fixed-size pages
(`PRAGMA page_size` reports 4096 here and `PRAGMA page_count` reports 2: one page
for the schema, one for the data). Students can check both pragmas themselves. A
text view of the same database, via `iterdump()`:

```sql
BEGIN TRANSACTION;
CREATE TABLE missions (id INTEGER PRIMARY KEY, title TEXT NOT NULL);
INSERT INTO "missions" VALUES(1,'Scan Nebula-7');
INSERT INTO "missions" VALUES(2,'Survey Kepler-442b');
COMMIT;
```

**Optional "Chapter 4" for the story script** (proposed, not yet built; it would
need its own failing test first):

```python
import os, tempfile, sqlite3

path = os.path.join(tempfile.mkdtemp(), "starship.db")
q = MissionQueue(path)
q.enqueue("Scan Nebula-7")
q.close()
print("size on disk:", os.path.getsize(path), "bytes")
print("first 16 bytes:", open(path, "rb").read(16))
print("\n".join(sqlite3.connect(path).iterdump()))
```

### 5.6 What the passing suite means at each stage

| Moment | Meaning |
|---|---|
| Green after cycle 1 | A fake that satisfies one test |
| Green after cycle 2 | Real (in-memory) state; the fake is dead |
| Green after cycle 3 | State survives the process that wrote it |

### 5.7 Roadmap: the next cycles

In rough order, one red test each:

1. **FIFO `dequeue`.** Enqueue two different titles; `dequeue()` returns the first. (Use two different titles so returning the last one or a hardcoded value cannot pass by accident.)
2. **`peek`** (look without removing) and **`size`**. Then rewrite the storage tests to use them instead of `_connection`.
3. **`EmptyError`** on dequeue from an empty queue. Wrap `sqlite3.Error` in your own exception so SQL never leaks out of the interface.
4. **`AlertStack`** (LIFO) and the same-input, opposite-order demo.
5. **Refactor to a shared base class** (template method: subclasses supply the `ORDER BY` string). Green stays green. Add context-manager support (`with MissionQueue(path) as q:`).
6. **Contract tests.** Build a trivial list-backed queue and run the *same* test suite against both implementations with `pytest.mark.parametrize`. This proves the "swap the storage, zero client changes" claim instead of asserting it.
7. **Status column** instead of deleting rows (`pending`, `launched`, `aborted`, with a `CHECK` constraint). Gives an audit trail and real queries ("which missions waited longest?").
8. **Atomic dequeue** with a concurrency test (two connections racing). Watch the naive `SELECT` then `UPDATE` fail first.
9. **Priority**: `ORDER BY priority DESC, id ASC`.
10. **A second table** (`ships`, with a foreign key from missions to the assigned ship): joins and normalization. This is where it becomes a data management course, not a queue course.

---

## 6. Concept notes: files, formats, and what they cost

These came up as a side question mid-session and belong in every data-management
unit.

### 6.1 Binary vs. plain text

Every file is bytes. A **text file** is bytes that decode into characters through
an agreed encoding (usually UTF-8) and are organized in lines. A **binary file**
is bytes laid out for a specific program, with no human-readable layer.

| Usually text | Usually binary |
|---|---|
| `.py`, `.sql`, `.json`, `.csv`, `.md`, `.svg` | `.db` (SQLite), `.png`, `.jpg`, `.pyc`, `.exe` |
| `.docx` and `.xlsx` sit in between: zipped bundles of XML | |

It is a spectrum, not two camps. `starship.db` is binary, yet its first 16 bytes
read `SQLite format 3`.

### 6.2 Raster vs. vector

- **Raster** (PNG, JPG, GIF, WebP): a grid of pixels. Resolution-dependent, blurry
  when enlarged, excellent for photos. Cost scales with pixel count: a
  4000 by 3000 image is roughly 48 MB in memory regardless of its file size on disk.
- **Vector** (SVG, fonts, most PDF graphics): shapes described as math. Resolution
  independent and tiny for logos and diagrams, poor for photos. Cost scales with the
  number of shapes; a map with a million paths can render *slower* than a bitmap.
- **SVG is vector *and* text**, so it diffs in git, can be searched with `grep`,
  and an AI can write it directly. A PNG is binary, and no one hand-writes one.

### 6.3 Performance

- Binary is usually smaller and faster to use. SQLite's page and B-tree layout can
  jump to one row without reading the file; a large JSON file must be parsed from
  the top.
- Text is bulkier but compresses well, streams easily, and works with simple tools.
- Rule of thumb: text wins on convenience and inspection; binary wins on lookups,
  size, and speed once data gets big. At three missions it does not matter.
  **Measure before optimizing.**

### 6.4 Traceability (this drives our git rules)

Git diffs line by line. A text change reads "line 12 changed", and merge, blame,
and code review all work. A binary change reads "binary files differ": you cannot
review it, you cannot merge it, and every version bloats the repository.

So we **version the recipe, not the cake**: commit the schema, the code that makes
the data, and the tests. Ignore the live `.db`. When a text snapshot is needed,
`iterdump()` (or `sqlite3 file.db .dump`) produces readable SQL.

Windows adds one wrinkle: CRLF vs. LF line endings can create phantom diffs in text
files (git's `autocrlf` setting).

### 6.5 What this means when working with an AI assistant

- **Text is the shared language** between you, git, and the assistant. Prompts,
  tests, diffs, and reviews all depend on it. Dumping a binary into an AI's context
  wastes tokens on noise.
- **Binary artifacts get an interface**: queries, dumps, checksums, tests. This is
  exactly why the durability test reads the database through `MissionQueue`.

### 6.6 Rules worth teaching

1. Source of truth in text; derived output in binary. Commit source, not build output.
2. Never version a live database. Version the schema and the code that makes it.
3. Choose the format by who reads it: humans and diffs, or programs and speed.
4. Measure before optimizing.
5. Binary is not automatically fragile. SQLite's file format is stable and
   cross-platform; it is just opaque.

---

## 7. Source control habits for TDD

- **Commit on green and after each refactor; never commit a red suite.** The
  history should read as a story: "empty queue", "enqueue", "demo", "durability".
- Commit messages describe **behavior added**, not files touched:
  `TDD: MissionQueue persists to disk across processes`.
- This repository's `.gitignore` already covers what a TDD project generates:

  ```
  .venv/
  __pycache__/
  *.pyc
  .pytest_cache/
  *.db
  *.sqlite
  *.sqlite3
  ```

  A durable `starship.db` must never be committed; `tmp_path` keeps test databases
  out of the project folder anyway.
- Do not push in the middle of a red state. A red test is a work-in-progress note
  to yourself, not something to publish.
- A fast safety check before every commit: `git status`, then
  `python -m pytest -q`, then commit.

---

## 8. Working with Claude Code: patterns that worked

1. **Open with the rules, then one tiny task.** The long "ground rules" prompt (Appendix A) set the rhythm for the whole session.
2. **Say "stop" explicitly.** Every prompt ended with "then stop and wait for me." The assistant respected it every time.
3. **Ask it to predict.** "Tell me why it fails and what I should expect next" turns each red into a lesson and lets you check its understanding.
4. **Ask for the command to run yourself.** You verify in your own terminal instead of trusting a summary.
5. **Name design decisions as decisions.** "Use sqlite3 with `:memory:`; say so in a comment" keeps the code honest about what the tests did and did not demand.
6. **Move the failure forward one step.** "Fix only the current failure, then show me the next one."
7. **Let it say "nothing to refactor."** Refactor-check prompts that invite inventing work produce churn.
8. **Notice its honesty flags.** It reported "I haven't committed or pushed" and "these tests never went red". Both are the habits you want students to copy.
9. **Know your permission mode.** The session ran in an auto-approve mode (commands ran without prompting). Fine for a throwaway lab; students should know which mode they are in and what it can do without asking.
10. **Commit only when you say so.** It did not commit or push until told.

---

## 9. Pitfalls and lessons learned

| What happened | Why | Fix |
|---|---|---|
| `claude : The term 'claude' is not recognized` | Claude Code was not installed yet (or the terminal predates the install) | Install (section 3.2), open a **new** terminal, check PATH (section 3.3) |
| A pasted one-liner failed with `unterminated string literal` | The terminal inserted a line break into a long `python -c "..."` | Paste it as one line, or put it in a script file |
| A "plan" listed the commit trap before "table already exists" | The prediction was wrong; running the ladder showed the real order | Trust the tests; verify predictions |
| Tests written after code were passing from the start | Characterization tests never go red | Label them honestly; do a mutation check |
| The project folder had no visible `.gitignore` | It lives at the repository root, not in the lab folder | `git status` to confirm what is tracked |
| Test needs `starship_log` importable from a child process | The child inherits the working directory only if told | Pass `cwd=Path(__file__).parent` to `subprocess.run` |
| Data "saved" but missing after reopening | Missing `commit()` | Commit after writes; test with a real second process |

---

## 10. Teaching notes

### Discussion questions

1. The first green was `return True`. Is that cheating? What would happen if we never wrote the second test?
2. Why does the `?` placeholder stop `DROP TABLE` from running? Where does the value travel instead?
3. Why does `close()` without `commit()` lose data silently? What would a good error message look like?
4. If `CREATE TABLE` happens immediately but `INSERT` does not, what does that tell you about transactions?
5. Our storage tests read `_connection` directly. What is the cost of that, and when do we fix it?
6. Which would you version in git: `starship.db`, or the code that builds it? Why?
7. A photo, a logo, and a chart: raster or vector for each? What happens when you print them poster-size?

### Exercises

- **Mutation check.** Swap `?` for an f-string and watch the injection test fail. Restore it.
- **Break the commit.** Remove `commit()` and rerun the durability test. Read the failure.
- **Look inside.** Print the first 16 bytes of your own `.db`. Open it in a hex viewer. Find your mission title.
- **Dump it.** Use `iterdump()` to produce a text version; commit the *dump* (not the `.db`) to a scratch repo and look at the diff after adding a row.
- **Two implementations.** Write a list-backed queue and run the same tests against both.
- **Extend.** Add a `status` column with a `CHECK` constraint and write the red test first.

### Assessment ideas

- Submit the git log showing red-before-green history (commit messages alone should tell the story).
- A short reflection: one place the test failed for a reason you did not expect, and what you learned.
- A mutation check write-up: which change did you break, which test caught it?

### Pacing

Cycles 1 and 2 are about 25 minutes including setup. The refactor and catch-up tests
are about 15. Cycle 3 and its ladder are about 25. Concept notes (section 6) fit as
a 15-minute discussion or a homework reading.

---

## 11. World Bible entry (draft)

> **Week 8, Mission Queue (durable).**
> **What changed:** A SQLite-backed `MissionQueue` built test-first: `is_empty`,
> `enqueue`, and a story demo, with a durability test that spawns a separate Python
> process. Public methods only; no SQL escapes the class.
> **Evidence:** `python -m pytest -v` shows 9 tests passing before the durability
> test was added; the durability test was observed red for the right reason
> (`TypeError` for a missing `db_path`). `python starship_log.py` prints the
> three-chapter story.
> **Why better than a list:** a database gives schema constraints (`NOT NULL`),
> parameterized queries, transactions, and persistence that a list cannot.
> **Remaining debt:** `dequeue`/FIFO, `peek`, `size`, error wrapping, `AlertStack`,
> status column, atomic dequeue, priority, a second table. Update this entry when
> cycle 3 is green.

---

## Appendix A: Prompt library

These are the exact prompts used, lightly cleaned. Paste them into Claude Code in
the project folder.

### A1. Opening prompt: RED only

```
We're doing strict TDD in this folder, building a SQLite-backed MissionQueue
(a FIFO queue for starship missions) in Python. Rules for the whole session:

1. One failing test at a time. Never write more than one new test per step.
2. RED: write the test, run it, show me the failure, then STOP.
3. Wait for me to say "green" before writing any production code.
4. GREEN: write the smallest code that passes (hardcoding is fine), run it, then STOP.
5. Wait for me to say "refactor" before cleaning anything up.
6. Never get ahead of me.

Do the RED step for the first test only:
- Create test_starship_log.py with one test, test_new_queue_is_empty, that
  imports MissionQueue from starship_log, creates MissionQueue(), and asserts
  queue.is_empty().
- Do NOT create starship_log.py yet. The test should fail because that module
  doesn't exist.
- Make sure pytest is installed, then run the test and show me the failure.

When you're done, tell me exactly what command I run myself to see the test
fail, what failure message I should expect, and why that's the right reason
to be red. Then stop and wait for me.
```

### A2. GREEN plus refactor check

```
green

Do the GREEN step, then the REFACTOR check, then stop.

GREEN:
- Create starship_log.py with the smallest code that makes
  test_new_queue_is_empty pass. A hardcoded return value is fine here. Do not
  add SQLite, extra methods, or anything the test doesn't demand yet.
- Run: python -m pytest test_starship_log.py
- Show me the passing output.

REFACTOR CHECK:
- Look at the code and the test and tell me honestly whether there is anything
  worth refactoring right now. If there isn't, say so. Don't invent work.
- If there is something, name it, but don't change anything until I say "refactor".

Then stop. Do NOT write the next test. When you're done, tell me:
1. The exact command to run the tests myself
2. What a green run should look like
3. What the next RED test should be, and why it will force us to replace
   the hardcoded return with real storage. Just describe it. Don't write it.
```

### A3. Next RED: enqueue

```
Next cycle. RED step only.

Add ONE new test to test_starship_log.py:

def test_queue_is_not_empty_after_enqueue():
    queue = MissionQueue()
    queue.enqueue("Scan Nebula-7")
    assert not queue.is_empty()

Do not touch starship_log.py. Run: python -m pytest test_starship_log.py
Show me the failure.

Then tell me:
1. Why it fails (what exactly is missing) and why that's the right reason
2. Why the current hardcoded `return True` can never pass this test, so
   this test forces us to store real state
3. The command to run it myself

Then stop and wait for me. Do not write production code.
```

### A4. GREEN with SQLite as a named design choice

```
green, use sqlite3 with :memory:

Do the GREEN step, then the REFACTOR check, then stop.

GREEN:
- Update starship_log.py so BOTH tests pass, using Python's built-in sqlite3
  module with an in-memory database (":memory:"). Say plainly in a comment or
  in your report that SQLite is a design decision we made, not something the
  tests demanded yet.
- Smallest code that passes:
  * __init__ opens the connection and creates a `missions` table
    (an INTEGER PRIMARY KEY id and a TEXT NOT NULL title; nothing else yet)
  * enqueue(title) inserts a row
  * is_empty() checks whether the table has any rows
- No dequeue, peek, size, close, db_path, or error handling. Nothing a test
  hasn't asked for.
- Use parameterized queries (? placeholders) for the INSERT, never string
  formatting. Explain in one sentence why.
- Run: python -m pytest test_starship_log.py
- Show me the passing output.

REFACTOR CHECK:
- Tell me honestly whether anything is worth refactoring. Don't invent work.
  If you see something, name it, but don't change it until I say "refactor".

Then stop. Do NOT write the next test. Tell me:
1. The command to run the tests myself
2. Show me the contents of the sqlite table after an enqueue, using a short
   throwaway python -c command I can paste into PowerShell, so I can see
   the database working
3. What the next RED test should be (just describe it, don't write it)
```

### A5. Source control check

```
Source control check, no code changes.

1. Run git status and tell me whether this folder is inside a git repo.
2. Create or update a .gitignore (at the appropriate level) so these are ignored:
   __pycache__/, .pytest_cache/, *.db
3. Commit starship_log.py, test_starship_log.py and .gitignore with a
   message like: "TDD: MissionQueue is_empty and enqueue backed by in-memory SQLite"
4. Show me git log --oneline.

From now on: after every GREEN and every REFACTOR step, commit with a short
message describing the behavior added. Don't push anything. Then stop.
```

### A6. Durability: RED

```
Next cycle. RED step only.

Add ONE new test to test_starship_log.py (add `import subprocess, sys` and
`from pathlib import Path` at the top if they're missing):

def test_data_survives_a_separate_python_process(tmp_path):
    db_file = tmp_path / "starship.db"
    writer = (
        "import sys; from starship_log import MissionQueue; "
        "q = MissionQueue(sys.argv[1]); q.enqueue('Scan Nebula-7'); q.close()"
    )
    subprocess.run(
        [sys.executable, "-c", writer, str(db_file)],
        check=True,
        cwd=Path(__file__).parent,
    )
    assert db_file.exists()
    reopened = MissionQueue(db_file)
    assert not reopened.is_empty()

Do not touch starship_log.py. Run: python -m pytest test_starship_log.py -v
Show me the failure.

Then tell me:
1. Exactly why it fails right now
2. Why this test is stronger than reopening inside one process
3. The sequence of failures I should expect as we fix them one at a time,
   including the commit trap and the "table already exists" trap
4. Whether *.db is in .gitignore, since a durable database file is something
   we should not accidentally commit

Then stop. No production code.
```

### A7. Durability: move the failure forward one step

```
green, but only for the CURRENT failure

Do a partial GREEN: fix only the TypeError, then show me the next failure.

1. Change MissionQueue.__init__ to accept an optional db_path, defaulting to
   ":memory:", and pass it to sqlite3.connect(). The default matters: all 9
   existing tests must stay green.
2. Do NOT add close(), commit(), or CREATE TABLE IF NOT EXISTS. Those
   aren't failing yet.
3. Run: python -m pytest test_starship_log.py -v
4. Show me the new failure for test_data_survives_a_separate_python_process.
   I expect the child process to now die on a missing close() method.
   Tell me if the actual failure is different.
5. Do NOT commit. We never commit a red test suite. We commit when
   everything is green.

Then stop and explain, in two sentences, why moving the failure forward one
step at a time is better than writing all four fixes at once. Do not fix the
next failure until I say "green" again.
```

*Follow-ups for the remaining ladder steps:* say `green` and name the next
failure (`close()`, then `CREATE TABLE IF NOT EXISTS`, then `commit()`), one per
prompt, and commit once the whole suite is green.

### A8. Story demo and catch-up tests (instructor's own wording)

```
I want the code to get refactored. I want the if name is main divider and then
I want this to be a story. I want it to be like "empty queue." and then "add
first item" then print and show and then add second item, print it and show it.
So this is human storytelling and not just a throwaway one-liner.
```

```
Can you catch up the tests that would test to make sure all of that is working
the way that we wanted it to work?
```

---

## Appendix B: Session timeline

All times US Central, 2026-10-09.

| Time | What happened |
|---|---|
| 13:11 | Goal stated: study data management, using TDD, to see OOP, with SQLite. A first-draft "Starship Mission Log" write-up reviewed (section 2) |
| 13:11 | Decision: "one step at a time, red then green then refactor" |
| 13:12 | Question: which file first, and what structure? Answer: the test file; start flat |
| 13:14 | `claude` not recognized: the install had not happened yet |
| 13:16 | PATH diagnosis with `Test-Path` and `$env:PATH` checks |
| 13:17 | WinGet chosen as the install route |
| 13:18 | First Claude Code prompt written (RED only) |
| 13:26 | First RED confirmed in the learner's terminal; GREEN prompt requested |
| 13:29 | Test 1 green (`1 passed`); discussion of whether SQLite can be a "next red test" |
| 13:33 | Test 2 red: `AttributeError: no attribute 'enqueue'` |
| 13:36 | Test 2 green with SQLite `:memory:`; one-liner failed from a line break |
| 13:45 | Story demo refactor, seven catch-up tests (9 passing), commit and push requested; durable-database question raised |
| 13:53 | Durability test red: `TypeError` from the child process |
| 13:55 | Side discussion: binary vs. text, raster vs. vector (section 6) |
| 13:59 | This guide requested, and then written, with the failure ladder re-run to verify the order |

---

## Appendix C: Glossary

- **Red / green / refactor:** fail first, pass with minimal code, then clean up.
- **Characterization test:** a test written *after* the code to pin down current behavior.
- **Mutation check:** deliberately breaking code to confirm a test can fail.
- **Parameterized query:** SQL with `?` placeholders; values travel separately from the SQL text.
- **SQL injection:** untrusted text interpreted as SQL because it was glued into the query string.
- **Transaction:** a group of changes that succeed or vanish together; `commit()` makes them permanent.
- **In-memory database (`:memory:`):** exists only inside one connection; gone on close.
- **Durable:** survives the process that wrote it.
- **`tmp_path`:** a pytest fixture giving each test its own temporary folder.
- **Encapsulation:** hiding the storage behind a small public interface.
- **Binary / text file:** bytes for a program vs. bytes meant to be read as characters.
- **Raster / vector:** pixel grid vs. shapes described mathematically.
- **Dump (`iterdump`):** a text rendering of a database as SQL.

---

## Sources

- Claude Code setup and system requirements: <https://code.claude.com/docs/en/setup>
- Claude Code install troubleshooting (PATH fix): <https://code.claude.com/docs/en/troubleshoot-install>
- Python `sqlite3` module: <https://docs.python.org/3/library/sqlite3.html>
- pytest `tmp_path` fixture: <https://docs.pytest.org/en/stable/how-to/tmp_path.html>
- SQLite file format (page size, header): <https://www.sqlite.org/fileformat.html>
