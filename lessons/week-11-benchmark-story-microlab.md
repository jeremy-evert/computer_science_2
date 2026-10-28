# Week 11 optional micro-lab — Benchmark sorting and searching, then tell the story

**Optional and experimental.** The required Week 11 work is unchanged: *Honest
Visualization from Project Data* (see `planning/week-11.md` and
`lessons/week-11-data-storytelling-micro-lab.md`). This is a second, ready-made
dataset you can use for the same Odyssey gate if your own project data is thin
— or just for the fun of seeing your own machine's numbers.

## The idea

Week 9 told you bubble sort is O(n²) and Python's sort is fast. Now **measure
it on your own machine** and decide what a reader should believe. Your laptop,
a classmate's Mac, and a WSL shell will give different numbers. Is the *story*
the same?

## Run it (about 1–2 minutes)

From the repository root:

```text
cd lessons/code/week11_benchmark
python benchmark.py --quick          # a few seconds, sanity check
python benchmark.py                  # full run, writes results_<your-host>.csv
python -m pip install matplotlib     # once, if you don't have it
python plot_benchmark.py results_<your-host>.csv --outdir charts
```

Windows PowerShell: use `py -3` where these say `python` if needed. WSL/Linux/Mac:
`python3`. `sample_results.csv` is a ready-made example run, so you can try the
charts before your own run finishes.

The CSV records, per row: OS, OS release, CPU architecture, Python version and
implementation, CPU count, algorithm, sort or search, input ordering (random,
sorted, reversed), list size `n`, repeats, and best time in seconds. No username
or hostname goes inside the file (the hostname only appears in the *file name* —
rename it before sharing if you prefer).

## What it measures

Sorts: bubble, insertion, merge (all written by hand) and Python's built-in
`sorted`. Searches: linear, hand-written binary, and the library `bisect`.
Bubble and insertion stop at n = 5,000 so nobody waits minutes. Each time is the
**best of several repeats** using `time.perf_counter()`.

## The story to tell (fits the Week 11 gate)

| Gate part | For this micro-lab |
|---|---|
| **Question** | One answerable question, e.g. "How much faster is binary search than linear search once the list is 100,000 long on my machine?" or "Does the same merge sort behave the same on Windows and WSL?" |
| **Visual** | One labeled chart from `plot_benchmark.py` (or your own). Axis labels with units, a title that states a claim, a legend. |
| **Rationale** | Why this chart type and these axes. Log-log is honest here because growth rate is the point; say so. |
| **Limitation** | What the data cannot show: one run, one machine, background programs, best-of-N timing, `n` capped, built-in `sorted` is C code and hand-written sorts are Python. Do not claim a cause you did not test. |
| **Evidence** | Your CSV, the command you ran, and `charts/3_PITFALL_linear_axis.png` named as the **misleading alternative**, with one sentence on what it hides. |

The harness ships the pitfall for you: the same data on linear axes starting at
zero, where the two slow sorts set the scale and the fast ones are flattened
against the bottom. Your job is to say *why* chart 1 is the honest one.

## Share by discussion

Post your chart, one-paragraph story, and your platform line (OS, Python
version, CPU count — the CSV has it) in the Week 11 discussion. Read at least
two classmates' posts and compare: what changed between machines, and what
stayed the same? Peer work is a shared learning resource in this course; do not
post anything private (no usernames, no file paths with your name).

## Honest cautions

- Timings are noisy. Close other programs; run twice if a number looks odd.
- Do not compare a hand-written sort to `sorted` and call it "Windows vs Linux".
  Compare the **same algorithm** across machines.
- Only claim what the numbers show. "Binary search was 1,000x faster here at
  n = 100,000" is a claim. "Linux is faster than Windows" is not.

Optional reps: add a size to `benchmark.py`; compare `random`, `sorted`, and
`reversed` ordering for insertion sort and explain the difference; export a
second chart of your own and defend it.
