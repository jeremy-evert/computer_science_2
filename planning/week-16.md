# Week 16 — Shared Farkle + Machine Learning Applied Fun

## Status

**Implemented source package; real-checkout validation receipt still required before release is fully GREEN.**

Week 16 is a playful synthesis week, not a new technical checkpoint.

## Weekly focus

> **How do we inherit a trustworthy program, preserve its contracts, compare different ways of making a Farkle decision, and decide whether added complexity and computation earned their keep?**

CS1 owns the canonical Farkle rules/baseline learning experience. CS2 consumes a provenance-tracked hardened snapshot and adds a CS2-native experiment bench.

Student lesson:

- `lessons/week-16-farkle-ml-experiment-bench.md`

Instructor guide:

- `docs/curriculum/week-16-farkle-ml-instructor-guide.md`

Evidence receipt:

- `assignments/W16-farkle-ml-design-receipt.md`

Implementation:

- `lessons/code/farkle_week16/`

One-command validation:

- `python scripts/validate_week16_farkle.py`

## CS2 synthesis

The week brings back course ideas only where they fit naturally:

- explicit contracts and swappable collaborators;
- composition around inherited behavior;
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

## Release yellow

The source, tests, validator, lesson, guide, and receipt are authored. A real checkout must execute `python scripts/validate_week16_farkle.py` and commit/retain the resulting raw receipt before the Week 16 implementation is advertised as fully validated.
