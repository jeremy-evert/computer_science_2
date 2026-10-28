# Week 11 optional micro-lab, part 2 — The story of Big O

Expansion of `week-11-benchmark-story-microlab.md`. Theme: visualize the
**process**, not just the result. You know Bubble sort ends at n²; here is how it
begins, and how to check the claim with evidence.

## Story arc
1. **Naive code.** Read the simple bubble sort.
2. **Highlight the drivers.** Two nested loops plus compare and swap; derive n(n-1)/2.
3. **Mark what Big O ignores.** Copy, `len()`, per-pass reset, flag assignments.
4. **Count.** An instrumented sort counts outer iterations, inner iterations, comparisons,
   swaps, index reads/writes, flag sets and bookkeeping. Compare count is exactly n(n-1)/2.
5. **Graph it.** Operations vs n and wall-clock vs n, log and linear axes, with a fitted exponent.
6. **Was ignoring them right?** Lower-order terms shrink toward 0% of the work. Constant-factor
   work stays a fixed share: it changes speed, never shape.
7. **Bigger n / predict.** Fit on small n, check on large n.
8. **Another CPU.** Run the harness elsewhere: operation counts identical, time different.
9. **Less naive.** Early exit (helps the sorted best case only), insertion (about half the work),
   merge sort (n log n). Find the crossover in the time chart.
10. **Pitfall.** A truncated axis makes 4x look like 40x. Keep it as your "misleading alternative".

## Run it
```text
cd lessons/code/week11_benchmark
python count_and_time.py --quick            # seconds
python count_and_time.py                    # about 20 s to a minute, writes story_<host>.csv
python -m pip install matplotlib            # once
python story_charts.py story_<host>.csv --outdir story_charts
python story_charts.py story_<host>.csv friend.csv --outdir story_charts   # adds the hardware chart
```
`story_sample.csv` is a ready example. Timing always uses the uncounted copy of each sort,
because counting itself slows a program down.

## Honest cautions
One run, one machine, best-of-3, noisy at tiny n. The counters are exact; the times are not.
Merge sort's counts are n log n, but Python's overhead for slicing makes its constant large.
Claim only what the numbers show. Deck: `presentations/beamer/week11_bigo_story/`.
