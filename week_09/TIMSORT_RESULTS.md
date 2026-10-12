# Week 9 -- Timsort vs Bubble Sort

Run on the instructor machine, 2026-10-12. Charts: `report/index.html`
(`timsort_vs_bubble_loglog.png`, `speedup.png`). Raw data:
`timsort_results.json`.

## Machine profile

```
Processor: Intel64 Family 6 Model 183 Stepping 1, GenuineIntel
Logical cores: 24
OS: Windows 11
Run timestamp: 2026-10-12T13:50:18.361796

All assertions passed.

  done n=100
  done n=500
  done n=1,000
  done n=2,500
  done n=5,000
  done n=10,000
  done n=20,000
  done n=50,000
  done n=100,000
```

## Results: random data

```
       n |   bubble (s) |  timsort (s) |      speedup
---------+--------------+--------------+-------------
     100 |     0.000202 |     0.000001 |         145x
     500 |     0.005023 |     0.000015 |         342x
   1,000 |     0.022629 |     0.000046 |         495x
   2,500 |     0.150232 |     0.000142 |       1,055x
   5,000 |     0.641321 |     0.000322 |       1,992x
  10,000 |     2.506018 |     0.000715 |       3,503x
  20,000 |    10.004483 |     0.001574 |       6,357x
  50,000 |    64.844837 |     0.004572 |      14,183x
 100,000 |            - |     0.009805 |            -
```

## Results: nearly sorted data

```
       n |   bubble (s) |  timsort (s) |      speedup
---------+--------------+--------------+-------------
     100 |     0.000093 |     0.000001 |         132x
     500 |     0.003011 |     0.000005 |         669x
   1,000 |     0.012730 |     0.000009 |       1,430x
   2,500 |     0.092249 |     0.000022 |       4,193x
   5,000 |     0.363045 |     0.000051 |       7,175x
  10,000 |     1.487741 |     0.000119 |      12,471x
  20,000 |     5.857622 |     0.000261 |      22,443x
  50,000 |            - |     0.000940 |            -
 100,000 |            - |     0.001843 |            -
```

## Results: reverse sorted data

```
       n |   bubble (s) |  timsort (s) |      speedup
---------+--------------+--------------+-------------
     100 |     0.000262 |     0.000001 |         524x
     500 |     0.006667 |     0.000002 |       3,704x
   1,000 |     0.028423 |     0.000004 |       7,895x
   2,500 |     0.189807 |     0.000009 |      21,817x
   5,000 |     0.804071 |     0.000018 |      45,428x
  10,000 |     3.202090 |     0.000039 |      81,895x
  20,000 |    12.794402 |     0.000069 |     185,158x
  50,000 |            - |     0.000267 |            -
 100,000 |            - |     0.000382 |            -

Bubble sort halted after n=50,000: random data took 64.8s (> 30s limit).
```

Bubble sort halted after n=50,000: random data took 64.8s (> 30s limit).
The halt rule is global, so nearly sorted and reverse bubble results also stop
after n=20,000 (n=50,000 would have been run on those only if random had not
tripped the limit).

## Big O reality check

```
        n1 -> n2 |   bubble |      n^2 |       off |  timsort |  n log n |       off
      100 -> 500 |    24.81 |    25.00 |     0.8% |    10.50 |     6.75 |    55.6%
    500 -> 1,000 |     4.50 |     4.00 |    12.6% |     3.11 |     2.22 |    39.8%
  1,000 -> 2,500 |     6.64 |     6.25 |     6.2% |     3.12 |     2.83 |    10.0%
  2,500 -> 5,000 |     4.27 |     4.00 |     6.7% |     2.26 |     2.18 |     3.9%
 5,000 -> 10,000 |     3.91 |     4.00 |     2.3% |     2.22 |     2.16 |     2.7%
10,000 -> 20,000 |     3.99 |     4.00 |     0.2% |     2.20 |     2.15 |     2.3%
20,000 -> 50,000 |     6.48 |     6.25 |     3.7% |     2.91 |     2.73 |     6.4%

Bubble sort: average 4.6% from n^2 theory
Timsort: average 17.2% from n log n theory
(Small-n rows are dominated by timer resolution and fixed overhead, so they sit far from theory.)
```

## Timsort scenario comparison

```
       n |   random (s) | nearly sorted (s) |  reverse (s) | random/nearly
---------+--------------+-------------------+--------------+--------------
     100 |     0.000001 |          0.000001 |     0.000001 |          2.0x
     500 |     0.000015 |          0.000005 |     0.000002 |          3.3x
   1,000 |     0.000046 |          0.000009 |     0.000004 |          5.1x
   2,500 |     0.000142 |          0.000022 |     0.000009 |          6.5x
   5,000 |     0.000322 |          0.000051 |     0.000018 |          6.4x
  10,000 |     0.000715 |          0.000119 |     0.000039 |          6.0x
  20,000 |     0.001574 |          0.000261 |     0.000069 |          6.0x
  50,000 |     0.004572 |          0.000940 |     0.000267 |          4.9x
 100,000 |     0.009805 |          0.001843 |     0.000382 |          5.3x

Timsort detects existing order (runs) and skips work it does not need to do. This is why O(n log n) is a WORST CASE bound -- on real-world data that is often partially sorted, Timsort approaches O(n).
```

## What Big O is really saying

Big O describes how the cost of an algorithm scales as the input grows, not how fast any single run is. For bubble sort the cost is proportional to n squared, so doubling n quadruples the work, which is why a random list of 50,000 items took 65 seconds on this machine. For an n log n sort, doubling n only slightly more than doubles the work, because log2(2n) = log2(n) + 1 and that extra term barely grows. Timsort also has a much smaller constant factor, since it is written in C and works on memory in a cache-friendly way that a Python loop cannot. The ratio table is evidence that Big O is a real prediction and not just notation: when theory says about 4x and the measurement says about 4x, that is the model working. Merge sort and Timsort share the same Big O class, yet Timsort wins again on constant factor, cache behavior, and because it adapts to order already present in the input. Big O tells you which algorithm survives growth; the constant tells you who is faster today.

## Observations worth discussing

- Bubble sort with an early-exit check was only about 1.7x faster on nearly
  sorted data (2% swapped pairs still leave many elements out of place), and
  reverse sorted data cost about 1.28x random: n^2 either way.
- Timsort's reverse-sorted time is *lower* than random because it detects one
  descending run and reverses it, not because reverse data is "easy" for every
  algorithm.
- Timsort's average distance from n log n theory (17%) is dominated by the
  small-n rows; from n=5,000 up it is within about 2-6%.
- Timsort times are the best of 5 repeats (microsecond jobs); bubble sort times
  are a single run.

## World Bible entry

```
Adds: bubble vs Timsort on random, nearly sorted and reverse data, a Big O reality check, and charts.
Hardware: Intel64 Family 6 Model 183 Stepping 1, GenuineIntel | 24 cores | Run: 2026-10-12T13:50:18.361796
Key finding: Timsort's speedup on random data first exceeds 1,000x at n=2,500.
Debt: insertion sort (also O(n^2), smaller constant) and heap sort (O(n log n), worse cache behavior) were not tested.
```
