# Legacy `beast.py` behavior

This document records the behavior of the original, single-file experiment
program before refactoring. The deterministic reference outputs are
`baseline/sort_counts.csv`, `baseline/search_counts.csv`, and
`baseline/report.tex`. `timings.csv` is deliberately excluded because elapsed
time varies between runs.

## Run command

From the repository root, run:

```powershell
python beast.py
```

The script writes to the relative `out/` directory. The baseline was captured
with Python 3.13.15. Matplotlib is optional: the import is guarded, and plots
are skipped if importing it fails. PDF compilation is also optional: the
script attempts to call `pdflatex`; if that call raises an exception, it prints
a message and leaves `report.tex` available. A nonzero `pdflatex` return code
is printed but does not stop the program.

## Algorithms and aliases

The five registered sorting algorithms are:

- `bubble_sort` (`bs`): bubble sort.
- `bubble_sort_early_exit` (`bs2`): bubble sort that stops after a pass with no
  swaps.
- `insertion_sort` (`ins`): insertion sort.
- `selection_sort` (`sel`): selection sort.
- `python_sort` (`pysort`): Python's in-place list sort with a comparison-counting
  comparator.

The searches are `linear_search` (`lin`) and `binary_search` (`binr`). The
program entry point `main` is also aliased as `go`.

## Experiment settings

- Sizes: 10, 20, 40, 80, and 160 (`SIZES`).
- Sorting trials per case: 5 (`T`).
- Search lookups per size: 200 (`LOOK`), alternating between a present value
  and a half-integer target intended to be absent.
- Sorting input kinds: `random`, `sorted`, and `reversed` (`KINDS`).
- Random input generation uses seeded `random.Random` instances so count and
  report outputs are repeatable.

## Generated files

The program creates `out/` when needed and writes:

- `sort_counts.csv`: average comparisons and swaps for each sort, input kind,
  and size.
- `timings.csv`: average elapsed time for each sort case; this is variable and
  is not part of the deterministic baseline.
- `search_counts.csv`: average linear and binary search probe counts per size.
- `sort_counts.png` and `search_probes.png`: plots, when Matplotlib imported
  successfully.
- `report.tex`: LaTeX report based on the experiment results.
- `report.pdf` and LaTeX auxiliary/log files may be produced by `pdflatex`.

## Return, mutation, and metric behavior

Each sort mutates the supplied list and returns that same list. With no metrics
argument, a sort returns only the list. If a metrics object is supplied, it
returns `(list, metrics)` and updates that object.

Each search returns the matching index or `-1` when no match is found. Without
a metrics argument it returns only that integer; with a supplied
`SearchMetrics`, it returns `(index, metrics)` and updates the supplied object.
Binary search assumes its input is sorted. Duplicate matches are not specified
to return the first matching index.

Metric fields have legacy, algorithm-specific meanings:

- `SortMetrics.comparisons` counts key comparisons made by the algorithm. The
  built-in-sort wrapper counts comparator calls, not necessarily every internal
  comparison performed by Python's sorting implementation.
- `SortMetrics.swaps` counts exchanges in bubble and selection sort. In
  insertion sort it counts rightward shifts, which are writes rather than
  exchanges. In Python sort it remains zero because internal list operations
  are not instrumented.
- `SearchMetrics.probes` counts inspected list elements in linear search. In
  binary search, equality is checked once per midpoint and the ordering check
  adds a second probe on a non-match. Consequently, one binary-search loop
  iteration can count two probes, so the binary and linear totals do not have
  a fully consistent definition.

These inconsistencies are captured as legacy behavior. Any later correction
should be explicit and versioned rather than silently changing this reference.
