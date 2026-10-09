# Starship MissionQueue: TDD session notes

Instructor record of a strict-TDD session (2026-10-09), kept so the teaching
can be improved next time. Not yet student-facing. If any of this becomes
Canvas material it must be a graded discussion, and peers will see the work
(see `../../AGENTS.md`).

## Session rules (set by Jeremy)

1. One failing test at a time. Never more than one new test per step.
2. RED: write the test, run it, show the failure, STOP.
3. Wait for "green" before any production code.
4. GREEN: smallest code that passes (hardcoding is fine), run it, STOP.
5. Wait for "refactor" before cleaning up.
6. Never get ahead.

## Cycle log

| # | Step | What happened | Result |
|---|------|---------------|--------|
| 1 | RED | `test_new_queue_is_empty`; `starship_log.py` does not exist | `ModuleNotFoundError: No module named 'starship_log'` (a collection error, still a valid red) |
| 1 | GREEN | `is_empty()` returns hardcoded `True` | 1 passed |
| 1 | REFACTOR | Nothing worth changing | none |
| 2 | RED | `test_queue_is_not_empty_after_enqueue` | `AttributeError: no attribute 'enqueue'` |
| 2 | GREEN | `sqlite3` with `:memory:`, `missions(id, title)`, parameterized INSERT, `COUNT(*)` | 2 passed |
| 2 | REFACTOR | Added `show_table()` and an `if __name__ == "__main__"` three-chapter story | 2 passed |
| - | CATCH-UP | 7 characterization tests written after the code (never red) | 9 passed |
| 3 | RED | `test_data_survives_a_separate_python_process` | `TypeError: MissionQueue.__init__() takes 1 positional argument but 2 were given` (child process exits 1, `CalledProcessError` in parent) |

State at the time of writing: **9 passed, 1 failing (the persistence test, on purpose).**

## Teaching points worth keeping

- **A test only forces what it needs.** "Enqueue, then not empty" does not
  force SQLite; a counter or list passes. SQLite was a *design decision we
  made*, and the code says so in a comment. The test that does force a
  database is the persistence test.
- **Right reason to be red.** A missing module, then a missing method, then a
  wrong assertion are different reds. Each should name the one thing missing.
  An `AttributeError` on `enqueue` is a fine red, but it is not the red for
  "needs storage"; the next red (`assert not is_empty()`) is.
- **Hardcoding is a legitimate GREEN.** `return True` passes test 1 and
  becomes impossible once test 2 exists. That is the point of the cycle.
- **Parameterized queries (`?`).** The driver treats the value as data, never
  as SQL, so a title like `x'); DROP TABLE missions;--` is stored as text.
  The catch-up test `test_enqueue_treats_sql_in_a_title_as_plain_text` locks
  this in.
- **Cross-process persistence is stronger than reopening in one process.**
  In one process, objects, caches, and open transactions can fake
  persistence. A separate interpreter shares no memory, so only bytes on disk
  can carry the data.
- **Expected failure sequence for the persistence test:**
  1. `TypeError`: `__init__` takes no path.
  2. `AttributeError`: no `close()`.
  3. Reopen fails with `sqlite3.OperationalError: table missions already
     exists` (fix: `CREATE TABLE IF NOT EXISTS`).
  4. **Commit trap:** `sqlite3` opens a transaction on INSERT; closing without
     `commit()` silently discards the row. File and table exist, but
     `is_empty()` is still True. The failure message gives no hint why.
- **Characterization tests are not TDD.** The 7 catch-up tests passed on the
  first run, so they prove current behavior but have never been seen to fail.
  To trust one, break the code on purpose (e.g. swap `?` for string
  formatting) and watch the right test go red.
- **Tests that read a private `_connection`** are a smell. When `dequeue`
  arrives, rewrite them against a public method.

## Why data is not tracked in git

- Git diffs, merges, and stores text in small deltas; a SQLite file is
  binary, so changes are opaque, unmergeable, and bloat the repo.
- History is permanent. A committed database stays in every clone forever,
  and deleting the file later does not remove it. This matters for any
  student data.
- Code and data have different lifecycles: code changes when a developer
  decides; data changes every run. Mixing them makes `git checkout` of an old
  commit capable of rolling back real data.
- Tests should create and discard their own data (`tmp_path`), so a fresh
  clone gives the same result.
- `.gitignore` now excludes `.pytest_cache/`, `*.db`, `*.sqlite`, `*.sqlite3`.

**Where data goes instead:** backups outside git (use SQLite's backup API, not
a file copy of an open database); commit the schema and migrations, not the
contents; commit small fake seed data on purpose; text exports (`.dump`, CSV,
JSON) when a snapshot must be versioned and is safe to publish; Git LFS, DVC,
or versioned object storage for large datasets.

## What went sideways (process notes)

- Jeremy sent his exact test text mid-turn after a near-duplicate was already
  written; it was swapped so only one new test existed. Lesson: when a step
  is dictated, write the dictated text verbatim.
- The catch-up tests broke the one-test-at-a-time rule at Jeremy's request.
  They are labeled as characterization tests in the test file.
- The earlier explanation of "next RED" suggested a test that would not have
  forced SQLite; it was corrected in the same session.

## Next steps

1. GREEN for the persistence test, one failure at a time (sequence above).
2. FIFO `dequeue` returning the oldest title; enqueue two different titles so
   a hardcoded or last-in answer cannot pass.
3. Replace the catch-up tests' use of `_connection` with public methods.
