# Refactor Beast: Conversation Record

This note records the initial characterization work on `beast.py` and the baseline-first refactoring workflow. It is intended to keep the decisions and evidence available in the repository after the chat ends.

## Starting point

The task was to understand the existing sorting and searching experiment before changing its implementation. `beast.py` benchmarks bubble sort, early-exit bubble sort, insertion sort, selection sort, and Python's built-in sort on random, sorted, and reversed inputs. It also compares linear and binary search probes. It generates CSV data, optional plots, LaTeX source, and a compiled PDF when `pdflatex` is available.

The source inspection identified module-level mutable state: `C` counts comparisons, `S` counts swaps or insertion shifts, `P` counts search probes, and `R` stores sorting results keyed by input kind, algorithm, and size. The `go()` function coordinates data generation, benchmark runs, output files, plots, report construction, and PDF compilation.

## Characterization documents

- `maps/before_map.md` contains two source-based Mermaid diagrams: the function call/shared-state map and the ordered jobs and outputs in `go()`.
- `maps/before_map_viewing_guide.md` explains how to render the diagrams in VS Code or GitHub.
- `maps/008_prove_baseline_stable.md` records why stable generated artifacts are compared against a fixed baseline.
- `maps/009_baseline_comparison_results.md` records the observed output comparison and explains run-dependent artifacts.

## Baseline and evidence

The program was run to create the baseline from `sort_counts.csv`, `search_counts.csv`, and `report.tex`. `SHA256SUMS.txt` records their hashes, and all four baseline files were marked read-only. The baseline was committed by itself as `0d1b21b` and pushed to `origin/refactor`.

A later run compared each baseline file to its generated counterpart. All three matched exactly. A hash comparison of the existing `out/` files found that `timings.csv`, `report.log`, and `report.pdf` changed. The count plots, `report.aux`, `report.tex`, and other existing summary documents were unchanged. The timing differences come from measuring elapsed time; the compiler log and PDF can vary between compilations even while the report source and counts remain identical.

## First unit test

`test_beast.py` contains exactly one test: it imports `lin` and checks that searching `[4, 7, 9]` for `7` returns index `1`. This is a small characterization of a known behavior. The file was created, but this record does not claim that pytest was run or that the test was deliberately made to fail and restored. Those are review steps in the exercise.

## Guardrails and next learning step

The baseline represents the current output contract. Do not modify, regenerate, or delete anything in `baseline/` or `beast_as_given.py`. Future changes should be checked against the saved deterministic outputs; timing values and compiled PDF bytes are unsuitable for exact-match checks.

The first test establishes the test shape for a simple search case. The exercise's fail-on-purpose step is meant to show that a test can detect a behavior mismatch, and restoring the expected value should make it pass again. Subsequent tests can characterize more search and sorting behavior before refactoring begins.
