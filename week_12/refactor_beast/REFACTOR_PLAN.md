# `beast.py` Refactor Plan

## Goal

Make the sorting and searching experiment easier to understand, change, and
verify while preserving its defined behavior. The saved baseline in `baseline/`
is the reference for deterministic outputs. `timings.csv` is excluded because
elapsed times vary between runs.

## Plan

1. **Record current behavior.** Describe the algorithms, inputs, seeded
   experiments, metrics, generated files, and optional plotting/PDF behavior.
   Keep the baseline files protected and use them to characterize existing
   behavior before changing implementation.
2. **Build unit tests.** Test each sort on empty, one-item, sorted, reverse,
   duplicate, and negative-value inputs; check in-place behavior and operation
   counts on small hand-calculated cases. Test searches for present and absent
   values, including probe counts. Test data generation, CSV/report rendering,
   plotting, and the top-level run separately.
3. **Improve readability.** Use descriptive names, consistent formatting,
   small functions with one clear responsibility, and named constants instead
   of unexplained values. Remove obsolete aliases and duplicated logic only
   when doing so does not break an established interface.
4. **Improve modularity.** Separate algorithm implementations and metrics
   from input generation/experiment collection, output writing, plotting,
   report generation, and orchestration. Keep a clear entry point and pass
   dependencies or output paths explicitly instead of relying on hidden global
   state.
5. **Document the design.** Update the README with how to run the program and
   tests, the output files, optional dependencies, module responsibilities,
   algorithm/metrics contracts, and how the baseline is used. Add focused
   docstrings where a function's contract or a non-obvious choice needs
   explanation.
6. **Refactor incrementally.** Make one cohesive change at a time. Run relevant
   unit tests after each change and the full test suite at each milestone. Do
   not refresh the baseline merely to silence a mismatch; explain any
   intentional behavior change and update its specification and tests.

## How we will know it is right

- **Correctness:** unit tests cover each algorithm's results, mutation/return
  contract, and metrics, plus the data and output helpers.
- **Behavior preserved:** running the original comparison program and the
  refactored entry point produces byte-identical `sort_counts.csv`,
  `search_counts.csv`, and `report.tex` against the saved baseline. Timing data
  and generated PDF bytes are not exact-match criteria.
- **Integration:** an end-to-end test runs into a temporary output directory,
  verifies expected files and report content, and checks plots when plotting is
  available. PDF compilation is handled gracefully when `pdflatex` is absent.
- **Readability and modularity:** each module has a focused responsibility;
  orchestration is visible at the entry point; names and interfaces are
  consistent; a reader can find where algorithms, measurement, output, and
  reporting happen without tracing one large script.
- **Documentation:** a new reader can follow the README to install or identify
  optional dependencies, run the program and tests, understand generated
  artifacts, and locate the main code responsibilities.

## Completion checklist

- [ ] Unit tests cover algorithms, metrics, helpers, and end-to-end behavior.
- [ ] Deterministic output comparisons pass against `baseline/`.
- [ ] Code is divided into clear modules with a small orchestration entry point.
- [ ] README and docstrings explain usage, contracts, outputs, and design.
- [ ] Full test suite passes; the changes are committed and pushed.
