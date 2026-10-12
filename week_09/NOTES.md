# Week 9 benchmark notes

Everything here was run on one machine (Intel64 Family 6 Model 183, 24 logical
cores, Windows 11, Python 3.12.10) on 2026-10-12. Numbers are tied to that
machine; other machines will differ.

## Files

| Script | What it does | Output |
| --- | --- | --- |
| `week_09_gate.py` | Hardware profile, linear vs sort+bisect lookup, World Bible line | `benchmark_output.txt`, `BENCHMARK_RESULTS.md` |
| `bubble_sort_benchmark.py` | Bubble vs merge vs `sorted()` to the 2-minute limit, Big O ratios | `bubble_sort_results.json`, `BUBBLE_SORT_RESULTS.md` |
| `bubble_sort_report.py` | Charts and local HTML report from the JSON | `report/index.html`, `report/*.png` |
| `variance_study.py` | Same list sorted 20 times at 5k/10k/30k, CV | `variance_study_results.json`, `VARIANCE_STUDY_RESULTS.md` |
| `timsort_vs_bubble.py` | Bubble vs Timsort on random, nearly sorted, reverse data; appends two charts to the report | `timsort_results.json`, `TIMSORT_RESULTS.md` |

## Requirements

- The benchmarks are stdlib only.
- The report steps need `pip install matplotlib seaborn`. (Seaborn prints a
  harmless SciPy/NumPy version warning on this machine.)
- Open `report/index.html` in a browser to see the graphs.
- Full re-run takes roughly 20-25 minutes. Single-threaded: it pegs one core
  (about 4% of 24 cores in Task Manager). Run nothing else while timing.

## Findings

- Biggest bubble sort inside 2 minutes: n = 60,000, about 109 s.
- Bubble sort tracks n^2 (ratio about 4.0 per doubling); Timsort tracks
  n log n once n is large enough that timer resolution stops dominating.
- Timsort's speedup on random data first exceeds 1,000x at n = 2,500 and
  reaches about 14,000x at n = 50,000.
- Run-to-run noise on a fixed list was about 1.5-2.7% CV. The "small jobs are
  noisier" prediction was not confirmed in one 20-trial run per size.
- The odd n = 30,000 timing in the first bubble benchmark (35 s against about
  24 s typical) was a one-off interference event (`pip install` ran during
  that run), far outside the normal spread.

## Decisions and caveats

- `week_09_gate.py` did not exist when asked to "extend" it, so it was created.
- `wmic` is gone on current Windows 11: free memory uses `GlobalMemoryStatusEx`
  via `ctypes`, with `wmic` only as a fallback.
- Bubble sort uses an early-exit check. Halt rules differ by script: the main
  benchmark skips a size when the O(n^2) projection exceeds 120 s;
  `timsort_vs_bubble.py` stops after any random-data run over 30 s, and that
  halt applies to all three scenarios.
- Timsort times are the best of 5 repeats (microsecond jobs); bubble times are
  a single run.
- The CPU loop proxy in `week_09_gate.py` is a rough relative number only.
- `variance_study.py` measures timer noise on one fixed list, not algorithmic
  variance across different data (different seeds would be a separate study).
- Still untested: insertion sort and heap sort.
