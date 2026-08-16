# CS2 Week 16 Farkle + ML experiment bench

This package is the executable companion to `lessons/week-16-farkle-ml-experiment-bench.md`.

## Quick start

From repo root:

```bash
PYTHONPATH=lessons/code python3 -m farkle_week16.cli menu
PYTHONPATH=lessons/code python3 -m farkle_week16.cli compare --strategy-a learner:2000 --games 500 --seed 6262
PYTHONPATH=lessons/code python3 -m farkle_week16.cli suite --games 200 --seed 6262 --out-dir artifacts/week16_farkle/demo
```

Plot a declared cost currency:

```bash
PYTHONPATH=lessons/code python3 -m farkle_week16.plot_results artifacts/week16_farkle/demo/suite_results.csv artifacts/week16_farkle/demo/tradeoff.png --x preparation_seconds_a
```

Validate the whole Week 16 surface:

```bash
python scripts/validate_week16_farkle.py
```

## Modules

- `vendor_cs1/` — provenance-tracked hardened CS1 baseline. CS1 remains canonical for Farkle rules.
- `contract.py` — explicit swappable strategy collaborator contract and adapters.
- `strategies.py` — CS2 strategy objects, including bounded rollout.
- `experiment.py` — config/result objects, preparation/runtime measurement, JSON/CSV persistence.
- `cli.py` — required student/instructor command path.
- `plot_results.py` — honest cost-vs-effectiveness plot from saved evidence.

## Design rule

The game stays stable. Strategy implementation and experiment configuration may vary through explicit contracts.

The result schema keeps multiple currencies separate: effectiveness, preparation, operation, and software complexity. Do not collapse them into one universal score.
