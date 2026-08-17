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

## Ownership

The canonical computational machine is the generated package:

`lessons/code/farkle_ml/`

It is synchronized from `jeremy-evert/Farkle_and_Machine_Learning` and carries `_SHARED_PROVENANCE.json` with source hashes and the pinned shared source commit.

CS2 does **not** own another Farkle engine, learner, simulator, or rollout implementation. The former `vendor_cs1/` compatibility snapshot was retired after a real Brandy migration run proved deterministic parity with the pre-migration CS2 baseline.

CS2 owns the course-facing engineering lens:

- `contract.py` — thin stable import surface for the canonical swappable strategy contract;
- `strategies.py` — thin stable import surface for canonical learned-table and rollout strategy objects;
- `experiment.py` — CS2 fixed suite, result schema, preparation/runtime measurement, and JSON/CSV persistence;
- `cli.py` — required student/instructor command path;
- `plot_results.py` — honest cost-vs-effectiveness plot from saved evidence.

## Design rule

The game and shared decision machinery stay stable. CS2 varies experiment configuration and asks what additional software/computational complexity bought.

The result schema keeps multiple currencies separate: effectiveness, preparation, operation, and software complexity. Do not collapse them into one universal score.

## Migration safety rail

The original CS2 implementation was first validated on Brandy. After switching the active path to `farkle_ml`, the same fixed suite produced the same deterministic win rates for all five strategy configurations. Timing is observed rather than required to match.

The validator now also rejects:

- shared-package hash/provenance drift;
- any active `vendor_cs1` import;
- reappearance of the retired `vendor_cs1` directory;
- fixed-suite behavioral drift.
