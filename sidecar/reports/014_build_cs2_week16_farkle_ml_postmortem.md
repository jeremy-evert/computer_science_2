# Postmortem — CS2 Week 16 Farkle + ML experiment bench

**Date:** 2026-08-16  
**Status:** SHARED-CORE MIGRATION VALIDATED; FINAL RETIREMENT RECEIPT REQUIRED BEFORE `main`

## Outcome

CS2 Week 16 is no longer a course-local Farkle machine built on a vendored CS1 snapshot.

The final ownership boundary is:

```text
jeremy-evert/Farkle_and_Machine_Learning
          canonical computational machine
                    |
                    v
       generated lessons/code/farkle_ml/
                    |
                    v
       CS2 course-facing experiment layer
   contract facade / fixed suite / CLI / plotter
                    |
                    v
       engineering tradeoff + ship judgment
```

The shared repository owns the game rules, engine, fair simulation, transparent learner, strategy contract, threshold strategies, bounded rollout machinery, and common evidence semantics.

CS2 owns what makes the week CS2:

- a stable course-facing contract/strategy seam;
- the richer fixed classroom suite including `learner:20000` and `rollout:100`;
- experiment configuration/result objects and cost currencies;
- JSON/CSV evidence persistence;
- optional honest plotting;
- software complexity/maintenance interpretation;
- the final engineering judgment about whether extra complexity earned its keep.

## Why this migration was safe

The migration used a before/after safety rail rather than replacing working code on faith.

### 1. Pre-migration Brandy baseline

The historical CS2 implementation was validated unchanged on Brandy with:

```text
python scripts/validate_week16_farkle.py
```

Retained receipt:

`sidecar/runs/014_validation_20260817T000431Z.md`

Observed fixed-suite win rates versus `bank_at_425`:

| strategy | win rate |
|---|---:|
| bank_at_300 | 0.640 |
| learner:2000 | 0.630 |
| learner:20000 | 0.670 |
| rollout:25 | 0.690 |
| rollout:100 | 0.680 |

Plotting was YELLOW because matplotlib was unavailable. That is optional enrichment, not a correctness dependency.

### 2. Canonical package synchronized

The shared sync tool generated:

`lessons/code/farkle_ml/`

The `_SHARED_PROVENANCE.json` manifest pins:

- repository `jeremy-evert/Farkle_and_Machine_Learning`;
- source path `src/farkle_ml`;
- shared source commit `d3a1ed379a652731b0b6237c33b4fe42c518ac9e`;
- synchronization-time shared repository head;
- SHA-256 hashes for every generated source file.

### 3. Active CS2 path migrated

The old dependency chain was:

```text
CS2 experiment layer -> vendor_cs1 -> Farkle machine
```

The new dependency chain is:

```text
CS2 experiment layer -> farkle_ml -> canonical Farkle machine
```

`farkle_week16/contract.py` and `farkle_week16/strategies.py` are now thin stable facades over canonical shared classes rather than duplicate implementations.

`farkle_week16/experiment.py` remains course-owned because its fixed suite and result interpretation are part of the CS2 teaching lens, but it now imports the machine from `farkle_ml`.

### 4. Post-migration behavioral parity proved

A second real Brandy run after the active-path migration produced:

- status **GREEN**;
- shared hashes/provenance GREEN;
- no active `vendor_cs1` imports;
- regression tests GREEN;
- fixed-suite parity GREEN.

The deterministic win rates were exactly the same five values as the pre-migration baseline. Timing changed slightly, as wall-clock timing naturally can, but timing was never required to match.

That is the important result: **computational ownership changed without changing the deterministic classroom behavior.**

## Legacy vendor retirement

Only after the shared-core migration passed on Brandy was the historical:

`lessons/code/farkle_week16/vendor_cs1/`

snapshot removed.

The validator is now stricter and goes RED if:

- the generated shared-package hashes drift from the manifest;
- active CS2 source/tests import `vendor_cs1`;
- the retired `vendor_cs1` directory reappears;
- regression tests fail;
- the fixed deterministic suite no longer matches the retained pre-migration behavioral fingerprint.

This follows the migration rule:

> **copy -> reconcile -> verify shared -> adopt consumer -> verify consumer -> retire duplicate**

## Teaching interpretation

The migration improves the CS2 lesson rather than merely cleaning code.

Students can now see a real software ownership boundary:

- a shared library owns computational truth;
- a course-specific facade provides a stable seam;
- CS2 composes experiment and interpretation around that shared behavior;
- provenance and validation prove what was inherited;
- maintenance cost includes avoiding unnecessary forks.

The Week 16 question remains:

> **What did the extra complexity buy, and was it enough?**

The required path remains CPU-first, free/open, bounded, and independent of GPU/cloud/Kubernetes access.

## What remains before promotion to `main`

Run the strengthened validator once more on Brandy after the legacy vendor retirement:

```text
python scripts/validate_week16_farkle.py
```

Retain the resulting GREEN `sidecar/runs/014_validation_<timestamp>.md` receipt. If that gate passes, the migration is ready to promote to `main`.

No additional Farkle architecture work is required in CS2 after that closure step.
