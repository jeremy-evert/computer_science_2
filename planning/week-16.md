# Week 16 — Shared Farkle + Machine Learning Applied Fun

## Status

**GREEN — canonical shared-core consumer validated on Brandy after legacy-vendor retirement.**

Week 16 is a playful synthesis week, not a new technical checkpoint.

## Weekly focus

> **How do we inherit a trustworthy program, preserve its contracts, compare different ways of making a Farkle decision, and decide whether added complexity and computation earned their keep?**

The canonical `Farkle_and_Machine_Learning` repository owns the shared rules, engine, transparent learner, strategy contract, rollout machinery, and fair simulation. CS2 consumes a generated provenance-pinned snapshot under `lessons/code/farkle_ml/` and owns the course-specific experiment bench, visualization, and software-design interpretation.

Student lesson:

- `lessons/week-16-farkle-ml-experiment-bench.md`

Instructor guide:

- `docs/curriculum/week-16-farkle-ml-instructor-guide.md`

Evidence receipt:

- `assignments/W16-farkle-ml-design-receipt.md`

Implementation:

- canonical generated machine: `lessons/code/farkle_ml/`
- CS2 course layer: `lessons/code/farkle_week16/`

One-command validation:

- `python scripts/validate_week16_farkle.py`

## CS2 synthesis

The week brings back course ideas only where they fit naturally:

- explicit contracts and swappable collaborators;
- thin adapters/facades around shared behavior;
- software ownership and maintenance boundaries;
- reproducible experiment configuration/result objects;
- fixed strategy families with different preparation/runtime costs;
- result ordering under different declared objectives;
- honest visualization/storytelling from saved evidence;
- testing, provenance, review, and reproducibility.

Computer Architecture contributes the useful question "what does a better decision cost?" CS2 adds software complexity/maintenance as a separate currency.

## Required path

- ordinary CPU;
- free/open tooling;
- no paid AI/API requirement;
- no GPU/cloud/Kubernetes requirement;
- bounded experiment choices;
- short judgment receipt.

## Explicit boundaries

- no Reasoning Odyssey Checkpoint 4;
- no formal reinforcement-learning mathematics;
- no Farkle engine rewrite;
- no giant GUI/dashboard;
- no Architecture tournament-platform requirement;
- no new grading weight invented here.

## Migration evidence

Pre-migration Brandy receipt:

`sidecar/runs/014_validation_20260817T000431Z.md`

The original CS2 implementation passed its regression tests and fixed suite before ownership changed.

After switching active imports from the historical `vendor_cs1` snapshot to the generated canonical `farkle_ml` package, Brandy validation produced the same deterministic fixed-suite win rates for all five strategy configurations:

- `bank_at_300`: 0.640
- `learner:2000`: 0.630
- `learner:20000`: 0.670
- `rollout:25`: 0.690
- `rollout:100`: 0.680

The old `vendor_cs1` compatibility directory was then retired and the strengthened validator was run again on Brandy.

Final post-retirement receipt:

`sidecar/runs/014_validation_20260817T001507Z.md`

Final required checks were all GREEN:

- generated shared snapshot hashes/provenance match the manifest;
- active CS2 source/tests contain no `vendor_cs1` imports;
- the legacy `vendor_cs1` snapshot is absent;
- regression tests pass;
- fixed-suite win rates exactly match the pre-migration Brandy behavioral fingerprint.

Plotting remained an optional YELLOW because matplotlib was unavailable on Brandy. JSON/CSV evidence and required correctness remained GREEN.

**Release classification: GREEN.**
