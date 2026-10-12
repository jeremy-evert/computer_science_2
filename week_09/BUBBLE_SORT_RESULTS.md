# Week 9 -- Bubble Sort Benchmark Results

Goal: find the biggest list bubble sort finishes inside a 2-minute budget.
Answer on this machine: **n = 60,000 in about 109 s**; n = 80,000 was
projected at about 193 s and skipped.

Graphs and a local web report: open `report/index.html` (built by
`bubble_sort_report.py` from `bubble_sort_results.json`). The graph of bubble
sort time against input size is `report/bubble_vs_n.png`.

## Machine profile

```
Processor: Intel64 Family 6 Model 183 Stepping 1, GenuineIntel
Logical cores: 24
OS: Windows 11
Run timestamp: 2026-10-12T13:29:51.705338

All assertions passed.

  done n=100
  done n=250
  done n=500
  done n=1000
  done n=2500
  done n=5000
  done n=10000
  done n=20000
  done n=30000
  done n=40000
  done n=50000
  done n=60000
  done n=80000
```

## Results table

```
      n |   bubble (s) |    merge (s) |   python (s) |  bubble/python
--------+--------------+--------------+--------------+---------------
    100 |       0.0002 |       0.0001 |       0.0000 |            29x
    250 |       0.0012 |       0.0002 |       0.0000 |            91x
    500 |       0.0051 |       0.0004 |       0.0000 |           181x
   1000 |       0.0234 |       0.0009 |       0.0001 |           376x
   2500 |       0.1539 |       0.0026 |       0.0002 |           921x
   5000 |       0.6325 |       0.0055 |       0.0003 |         1,828x
  10000 |       2.5411 |       0.0116 |       0.0007 |         3,458x
  20000 |      10.1886 |       0.0258 |       0.0016 |         6,271x
  30000 |      35.0337 |       0.0381 |       0.0027 |        12,967x
  40000 |      45.1527 |       0.1094 |       0.0059 |         7,689x
  50000 |      68.0462 |       0.0681 |       0.0045 |        15,225x
  60000 |     108.7889 |       0.0890 |       0.0061 |        17,883x
  80000 |            - |       0.1140 |       0.0075 |              -

Bubble sort halted: exceeded 2-minute budget at n=80000 (projected 193s from n=60000).

Biggest bubble sort that finished: n=60,000 in 108.8s.
```

## Big O reality check

```
        n1 -> n2 |  actual bubble ratio |  theoretical n^2 |  actual merge ratio |  theoretical n log n
      100 -> 250 |                 5.98 |             6.25 |                2.46 |                 3.00
      250 -> 500 |                 4.17 |             4.00 |                2.10 |                 2.25
     500 -> 1000 |                 4.59 |             4.00 |                2.23 |                 2.22
    1000 -> 2500 |                 6.58 |             6.25 |                2.76 |                 2.83
    2500 -> 5000 |                 4.11 |             4.00 |                2.15 |                 2.18
   5000 -> 10000 |                 4.02 |             4.00 |                2.10 |                 2.16
  10000 -> 20000 |                 4.01 |             4.00 |                2.23 |                 2.15
  20000 -> 30000 |                 3.44 |             2.25 |                1.48 |                 1.56
  30000 -> 40000 |                 1.29 |             1.78 |                2.87 |                 1.37
  40000 -> 50000 |                 1.51 |             1.56 |                0.62 |                 1.28
  50000 -> 60000 |                 1.60 |             1.44 |                1.31 |                 1.22
```

Noise caveat: the 20,000 -> 30,000 and 30,000 -> 40,000 bubble rows and the
merge row at 40,000 are distorted by other activity on the machine during this
run (an earlier run of the same script gave 23.8 s at n=30,000 and 42.2 s at
n=40,000, and tracked n^2 cleanly). Timings vary roughly 10-50 % between runs
at the large sizes; the trend is the lesson.

## Summary

Bubble sort compares adjacent pairs again and again, so doubling the list roughly quadruples the work; at tens of thousands of items that is minutes, not milliseconds.
The ratio table shows Big O is a real prediction: when n grows by some factor, bubble sort's measured time grows by about that factor squared, while merge sort grows only a little faster than linearly.
O(n^2) sorts are still fine for tiny lists, or for nearly sorted data where the early-exit check finishes after one pass.
Merge sort costs more code and extra memory for the merged lists, but it scales dramatically better; Python's built-in sort is faster still because it is written in C and exploits existing order.

## World Bible entry

```
Adds: bubble sort benchmark and Big O reality check against merge sort and Python's sorted().
Hardware: Intel64 Family 6 Model 183 Stepping 1, GenuineIntel | 24 cores | Run: 2026-10-12T13:29:51.705338
Debt: bubble sort is impractical past ~60,000 items on this machine (n=60,000 took 109s).
```
