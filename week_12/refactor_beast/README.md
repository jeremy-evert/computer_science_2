# The Beast: refactor it without breaking it (Week 12)

`beast.py` is a working, ugly program. It runs five sorting algorithms on three kinds of input, runs two searches, then writes tables (CSV), plots (PNG) and a LaTeX report into `out/`. Everything is in one function, with global counters and copy-pasted code. It works. Your job is to make it *good* while it keeps working.

## Rule 0: the output is the spec
Before you change anything, you must be able to say "this is what it does now." Then every change has to leave that true.

## Steps
1. **Run it.** `python beast.py` from this folder. Look at `out/`. (No LaTeX installed? `out/report.tex` is still written. No matplotlib? The plots are skipped and the report says "plot missing.")
2. **Save the baseline.** Copy `out/sort_counts.csv`, `out/search_counts.csv` and `out/report.tex` to a folder called `baseline/`. Do not copy `timings.csv`: it changes every run. Why?
3. **Map it.** On paper or in a drawing tool, before touching code: which functions exist, which call which, what global state they share, where the mess is. This is your "before" map.
4. **Write tests first** (`test_beast.py`, pytest). Start with `lin`, `binr`, and the sorts: they sort correctly, and counts for a tiny known list match what you computed by hand. Then add a test that re-runs the whole program and compares the CSVs and `report.tex` to `baseline/`. A test that pins down what the program does *today*, even if odd, is a characterization test.
5. **Refactor in small steps.** After every step run the tests. Green means keep going. Red means undo that step. Ideas: remove the globals, make one sort function per file or one shared "count" helper, separate computing from writing files, build the LaTeX from a template or helper functions, name the magic numbers, remove duplicated code.
6. **Use a coding assistant if you like**, but you decide each step, and the tests decide if it was allowed.
7. **Rerun and compare.** Run the program again, diff the output against `baseline/`, and check what changed. Anything that changed on purpose, explain. Anything that changed by accident, fix.
8. **Map it again** (your "after" map) and write four sentences: what you changed, what the tests caught, one thing you decided *not* to change and why, and what you would do with another hour.

## Hand in
Your before map, your after map, the four sentences, and a link to your repo or branch with the tests. Post in the class discussion so classmates can see each other's approach.

## Refactored entry point

The extracted implementation lives in `src/`. Run it from this folder with:

```powershell
python -m src.main
```

It writes the CSV files, plots, LaTeX report, and (when `pdflatex` is
available) PDF into `out/`. The original `beast.py` remains available as the
comparison version while the refactor is developed.

## Looking back: what could work better next time

Before extracting algorithms, agree on their shared contract: whether they
mutate the input, what they return, and how comparisons, swaps, and search
probes are counted. We added those counting hooks after the standalone sorts
were already in place, so deciding that interface earlier could have avoided
a later pass through every sort. It would also help to establish the
end-to-end baseline check as soon as collection and output are connected,
while keeping timing results out of exact comparisons because they vary from
run to run.
