# The Beast: small steps (v2)

Use with `beast.py`. One step at a time. Each step has:
- **Say**: one or two sentences to explain to the class.
- **Paste**: a short prompt for your AI chat (tiny enough for a small model).
- **Review**: what you look at before you accept the change.

Standing rules, say them once: **(1) One step, one change. (2) You read the diff before you keep anything. (3) Tests green or you undo.**

---

## The review kit (teach this first, 5 minutes)

Five commands. You will use them after every AI step.

| Command | What it answers |
|---|---|
| `git status` | Which files did anything touch? |
| `git diff` | Exactly which lines changed? |
| `git diff --stat` | How big was the change? |
| `git restore <file>` | Undo this file, back to the last commit. |
| `git commit -am "step N: ..."` | Save a good step so you can always return to it. |

Nice extras: `git log --oneline` (the story so far), `git diff HEAD~1` (what the last step changed), `git add -p` (accept a change one piece at a time).

**How to read a diff**
- Lines starting with `-` were removed (red). Lines starting with `+` were added (green). Everything else is context.
- `@@ ... @@` marks where in the file you are.
- Three questions for every diff: *What changed? Why? What proves it is safe?*

**Red flags: stop and look closer**
- `git diff --stat` shows more files or lines than you asked for.
- A test file changed when you only asked for code to change (or the other way around).
- A test was deleted, loosened, or "fixed" so it passes.
- The AI renamed things you did not ask about.
- You cannot explain a changed line in one sentence.

**Review habit:** run `git status`, then `git diff --stat`, then `git diff`. Only then run the tests. Only then commit.

---

# Part A. Set up and take stock

## 00. A safe workspace (no AI)
**Say:** Git is our undo button. We start by saving the program exactly as given.
**Do:** copy the `refactor_beast` folder somewhere outside the course repo, then:
```
cd beast_copy
git init
git add beast.py
git commit -m "beast as given"
git switch -c refactor
```
**Review:** `git log --oneline` shows one commit.

## 01. Run it (no AI)
**Say:** Before we change anything, we watch it work.
**Do:** `python beast.py`, then open the `out/` folder.
**Review:** which files appeared? (`git status` shows `out/` is new.)

## 02. What does it do?
**Say:** First job for the AI is only to read.
**Paste:**
```
Read this Python program. In 5 short sentences, say what it does from start to finish. Do not suggest changes.
[paste beast.py]
```
**Review:** does it match what you saw in step 01?

## 03. List the functions
**Paste:**
```
List every function in this program with a one-line description of each. Do not change anything.
[paste beast.py]
```
**Review:** count them yourself. Did it miss any?

## 04. List the globals
**Say:** Globals are the hidden wires. They are why this is hard to change.
**Paste:**
```
List every global variable in this program (module-level names that functions change with the "global" keyword). For each, say which functions change it. Do not change anything.
[paste beast.py]
```
**Review:** you should find three counters (`C`, `S`, `P`) and one dictionary (`R`).

## 05. What changes between runs?
**Paste:**
```
This program writes files into out/. Which of them would be different if I run it twice, and why? Look at the code for random numbers and timing. Do not change anything.
[paste beast.py]
```
**Review:** run it twice and check with `git diff --no-index` or a file compare. Is `timings.csv` the odd one out?

## 06. The "before" map
**Paste:**
```
Draw a Mermaid flowchart of this program showing which functions call which functions. Do not suggest improvements.
[paste beast.py]
```
**Review:** save the diagram as `before_map.md`. Does it match steps 03 and 04?

---

# Part B. Lock in the baseline

## 07. Save the baseline
**Say:** The baseline is our definition of "still works."
**Do (no AI):**
```
mkdir baseline
cp out/sort_counts.csv out/search_counts.csv out/report.tex baseline/
```
**Review:** these three files only. Not `timings.csv`. Not the PDF.

## 08. Prove the baseline is stable
**Do:** run `python beast.py` again, then:
```
diff -r baseline/sort_counts.csv out/sort_counts.csv
diff baseline/search_counts.csv out/search_counts.csv
diff baseline/report.tex out/report.tex
```
**Review:** no output means identical. Commit the baseline: `git add baseline before_map.md` then `git commit -m "baseline and before map"`.

---

# Part C. Unit tests (code stays untouched)

## 09. One tiny test
**Say:** One real test, run once, is worth more than ten pages of plans.
**Paste:**
```
Create a file test_beast.py. Using pytest, write ONE test: lin([4, 7, 9], 7) should return 1. Import from beast. Do not edit beast.py. Show only the new file.
```
**Review:** `git status` should show only `test_beast.py` as new. Run `pytest`. Green.

## 10. Linear search, more cases
**Paste:**
```
Add 3 more tests for lin in test_beast.py: item at the start, item at the end, item missing (should return -1). Do not edit beast.py or the existing test.
```
**Review:** `git diff` shows only added lines in the test file. Run `pytest`.

## 11. Binary search tests
**Paste:**
```
Add tests for binr in test_beast.py on the sorted list [1, 3, 5, 7, 9]: finds 1, finds 9, finds 5, and returns -1 for 4. Do not edit beast.py.
```
**Review:** `git diff --stat`: only the test file. Run `pytest`.

## 12. One sort, five inputs
**Paste:**
```
Add tests for bs (bubble sort) in test_beast.py. Each should check the result equals sorted(input) for: an empty list, one item, already sorted, reversed, and a list with duplicates. Do not edit beast.py.
```
**Review:** read one test aloud. What does it protect?

## 13. The other sorts
**Paste:**
```
Add the same five checks for ins and sel in test_beast.py. Do not edit beast.py.
```
**Review:** `git diff --stat`, then `pytest`. Commit: `git commit -am "step 13: sort tests"`.

## 14. Counting by hand
**Say:** The counters are part of the behavior, so we test them too.
**Do (no AI, as a class):** for the list `[3, 1, 2]`, work out how many comparisons and swaps `bs` makes. Write the numbers on the board.
**Paste:**
```
In test_beast.py, add a test that runs bs on [3, 1, 2] and checks the comparison count (variable C) and swap count (variable S) equal these numbers: [YOUR NUMBERS]. Reset C and S to 0 before the call. Do not edit beast.py.
```
**Review:** if it fails, who is wrong: your hand count or the code? Find out before you change anything.

## 15. The whole-program test
**Say:** One test that protects everything: run the whole program and compare to the baseline.
**Paste:**
```
Add one pytest test that runs beast.go() inside a temporary directory (use pytest's tmp_path and monkeypatch.chdir) and checks that out/sort_counts.csv, out/search_counts.csv and out/report.tex are identical to the files in the baseline folder. Ignore timings.csv. Do not edit beast.py.
```
**Review:** it should pass. `git diff --stat` shows only the test file.

## 16. Break it on purpose
**Say:** A test you have never seen fail is a test you cannot trust.
**Do (no AI):** change `T = 5` to `T = 4` in `beast.py`, run `pytest`. Watch it go red. Then undo with `git restore beast.py`.
**Review:** `git status` is clean again. Commit the tests: `git commit -am "step 16: whole-program test"`.

---

# Part D. Refactor the tests

## 17. Names that explain
**Paste:**
```
Rename the tests in test_beast.py so each name says what it protects, like test_lin_returns_minus_one_when_missing. Only rename. Do not change what any test checks. Do not edit beast.py.
```
**Review:** `git diff` should show only name lines changed. Same number of tests when you run `pytest`?

## 18. One repeated test becomes a table
**Paste:**
```
In test_beast.py, the five sort-checks are repeated for bs. Combine them into one test using @pytest.mark.parametrize. Keep the same five cases. Do not edit beast.py.
```
**Review:** count: five cases still run? (`pytest -v` lists them.)

## 19. Repeat for the other sorts
**Paste:**
```
Do the same parametrize change for the ins and sel tests, so one table of cases is shared by all the sorts (bs, ins, sel). Keep every case. Do not edit beast.py.
```
**Review:** `pytest -v`: nothing lost, and fewer lines. Commit: `git commit -am "step 19: tidy tests"`.

---

# Part E. Refactor the code (small, safe moves first)

## 20. Delete what is unused
**Paste:**
```
In beast.py, find imports that are never used and variables that are assigned but never read. List them first. Do not change anything yet.
```
**Review:** check each one yourself with a text search before you trust it.

## 21. Remove the unused imports
**Paste:**
```
Remove only these unused imports: [PASTE THE ONES YOU VERIFIED]. Change nothing else.
```
**Review:** `git diff` is 1–3 lines. `pytest`. Commit.

## 22. Name the magic numbers
**Paste:**
```
In beast.py, the numbers 10 and 1000 in the random-data code are unexplained. Replace each with a named constant at the top of the file with a clear name. Change nothing else. The program's output must stay identical.
```
**Review:** read the diff. Are the names honest? `pytest` green? Commit.

## 23. Remove one global: the sort `ins`
**Say:** We take the hidden wires out one at a time, starting with one function.
**Paste:**
```
Change ONLY the function ins in beast.py so it returns (sorted_list, comparisons, swaps) instead of changing the globals C and S. Do not change any other function. Update only the call to ins inside go(). Show the diff.
```
**Review:** the old tests for `ins` will go red. That is correct. Update only those tests to unpack the new return values. `pytest` green. Commit.

## 24. Same change, next sort
**Paste:**
```
Do the same change for sel only: return (sorted_list, comparisons, swaps) and update its call in go() and its tests. Nothing else.
```
**Review:** diff, tests, commit. Repeat later for `bs`, `bs2`, `pysort`.

## 25. The search functions
**Paste:**
```
Change ONLY lin and binr so each returns (index, probes) instead of changing the global P. Update their calls in go() and their tests. Nothing else.
```
**Review:** `pytest` green. Does `binr` still report double probes? It should. The baseline says so.

## 26. Split the work from the writing
**Paste:**
```
In beast.py, the function go() both runs the experiments and writes files. Move ONLY the code that runs the sorting experiments into a new function run_sort_experiments() that returns the results and writes no files. go() should call it and keep doing the file writing as before. Show the diff.
```
**Review:** the whole-program test must stay green. Commit.

## 27. The report builder
**Paste:**
```
In go(), the LaTeX text is built by gluing strings together. Move only that code into a function build_report(results, search_results) that returns the text. go() should write it to out/report.tex as before. Output must stay byte-identical.
```
**Review:** the whole-program test is the judge. Commit.

---

# Part F. Compare and reflect

## 28. Rerun and diff against baseline
**Do:**
```
python beast.py
diff baseline/sort_counts.csv out/sort_counts.csv
diff baseline/report.tex out/report.tex
git log --oneline
git diff <first-commit>..HEAD --stat
```
**Review:** no diffs in the outputs. The last command shows how much code you changed in total.

## 29. The "after" map
**Paste:**
```
Draw a Mermaid flowchart of this program as it is now, in the same style as before. Then list every difference between the two maps in plain language.
[paste beast.py and your before_map.md]
```
**Review:** do the differences match your commit list?

## 30. Your four sentences
**Paste:**
```
Do not write this for me. Ask me four questions that help me write: (1) what I changed, (2) what the tests caught, (3) one thing I chose NOT to change and why, (4) what I would do with another hour.
```
**Review:** write the four sentences yourself.

---

Bonus
- `binr` counts two probes per loop. Is that a bug? What would you change in the baseline, and what would you tell the next reader?
- Remove the duplicate sort (`bs` vs `bs2`). Which tests would you want first?
- Use `git add -p` to accept only half of an AI change.
