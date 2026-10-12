# Week 9 chat notes: what the benchmark data told us

Cleaned from a raw chat dump (a Copilot conversation with pasted Claude Code
terminal output). Duplicated pastes, terminal chrome, and the full prompts are
removed; the prompts' content lives in the scripts. Corrections to what the
chat said are marked **Correction**. Raw numbers are in `NOTES.md` and the
`*_RESULTS.md` files.

## 1. "We got lied to a little"

The first bubble sort benchmark (`BUBBLE_SORT_RESULTS.md`) tracked n^2 closely
at most sizes, but two rows did not:

| Transition | Actual ratio | Theory (n^2) |
| --- | --- | --- |
| 5,000 -> 10,000 | 4.02 | 4.00 |
| 10,000 -> 20,000 | 4.01 | 4.00 |
| 20,000 -> 30,000 | 3.44 | 2.25 |
| 30,000 -> 40,000 | 1.29 | 1.78 |

The algorithm did not change between rows, so the machine did: one timing
(n = 30,000) was inflated and the next row then looked artificially fast. A
`pip install` was running during that benchmark run, stealing CPU time.

Plan that came out of it: pick a few sizes, time the same list repeatedly, and
measure how much the time varies and why. That became `variance_study.py`
(n = 5,000, 10,000, 30,000; 20 trials each).

## 2. What the variance study found

Details in `VARIANCE_STUDY_RESULTS.md`.

- CV was 2.07% (n=5,000), 1.53% (n=10,000), 2.66% (n=30,000).
- The prediction that short jobs are relatively noisier (a fixed OS hiccup is a
  larger share of a short run) was **not** confirmed by one 20-trial run per
  size. The differences are small and could be chance.
- Typical spread at n=30,000 was 23.0-25.0 s. The original 35 s was far
  outside that, so it was a one-off interference event, not ordinary noise.
- Likely noise sources, not individually measured here: OS scheduling, cache
  and branch-predictor warm-up (trial 1 was slowest at 5k and 10k), thermal
  throttling, and other programs. Garbage collection is an unlikely culprit
  because bubble sort allocates almost nothing.

## 3. Why htop in WSL could not see the job

- The scripts were run with the **Windows** Python (3.12.10, under
  `AppData\Local\Programs\Python\Python312`), not a WSL Python. WSL's `htop`
  only sees Linux processes inside the WSL kernel, so it showed an idle
  machine (load average 0.00) while the Windows process ran.
- To watch it: Windows Task Manager (Details tab, `python.exe`), or
  `Get-Process python` in PowerShell, or run the script from inside WSL so
  `htop` sees it.
- Task Manager's overall CPU graph barely moved because the benchmark uses one
  core: about 1/24 of 24 logical processors (about 4%). Switch the graph to
  "Logical processors" and one core is pegged.

**Correction.** The chat blamed the Python GIL and quoted a
`python3.13.exe` path and an i7-13700. The GIL only limits threads inside one
interpreter; this script is simply single-threaded, so it uses one core
regardless. The interpreter is Python 3.12.10, and CPU model detail beyond
"Intel64 Family 6 Model 183, 24 logical cores" is not recorded by the scripts.
Using more cores would need `multiprocessing` and a different experiment.

## 4. Bubble sort vs Timsort

Python's `sorted()` is Timsort: O(n log n) worst case, close to O(n) on data
that is already mostly ordered, implemented in C. Expected on a log-log plot:
bubble sort slope about 2, Timsort slope slightly above 1.

The head-to-head (`timsort_vs_bubble.py`, results in `TIMSORT_RESULTS.md`)
used three input scenarios: random, nearly sorted (2% swaps), reverse sorted.

Measured on this machine:

- Timsort's speedup on random data first passed 1,000x at n = 2,500 and was
  about 14,000x at n = 50,000.
- Bubble sort averaged 4.6% from n^2 theory; Timsort was within about 2-6% of
  n log n once n >= 5,000 (the small-n rows are dominated by timer
  resolution).
- Timsort was about 5-6x faster on nearly sorted than random data.

**Correction.** The chat predicted "15,000x+ at n=60,000" and described reverse
data as bubble sort's worst case with the early-exit check making nearly sorted
data much faster. Measured: bubble sort was only about 1.7x faster on nearly
sorted data and about 1.28x slower on reverse than on random. Bubble sort on
n=60,000 was not part of the Timsort run (halt rule stopped bubble sort after
n=50,000).

## 5. Open ideas (not done)

- Different random seeds in the variance study (this one fixed the list).
- Insertion sort and heap sort in the head-to-head.
- A `multiprocessing` run so several cores light up in Task Manager.
- Warm-up runs and repeated trials for bubble sort in the Timsort benchmark.
