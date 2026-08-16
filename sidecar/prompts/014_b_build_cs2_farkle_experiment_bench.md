# Prompt 014B — Build the CS2 Farkle experiment bench

**Status:** WAITING ON 014A GREEN  
**Parent:** Prompt 014

## Mission

Build the actual CS2 Week 16 software surface described by:

- `planning/week-16-farkle-ml-target-map.md`
- `planning/week-16-farkle-ml-implementation-plan.md`

## Required work

- consume the hardened CS1 baseline with explicit provenance;
- preserve one Farkle rules contract;
- implement an explicit swappable strategy contract;
- adapt CS1-compatible function strategies;
- add experiment configuration/result objects;
- add a reproducible experiment runner;
- expose a fixed menu with heuristic + trained transparent learner + bounded simulation strategy when humane;
- capture preparation/runtime/effectiveness/software-complexity evidence;
- persist JSON/CSV results;
- add real CS2 tests.

## Validation

Tests must cover at least:

- upstream compatibility/provenance surface;
- strategy substitution;
- invalid-action rejection;
- deterministic replay;
- full-game completion;
- saved result round-trip/shape;
- fair comparison semantics inherited from CS1;
- one controlled state where richer/composed behavior differs;
- no magic exact stochastic win-rate assertion.

## Scope fence

No second independent rules engine, formal RL unit, required GPU/cloud, Kubernetes platform, giant GUI, or new checkpoint.

## Receipt

Write a raw implementation receipt under `sidecar/runs/` with file list, design decisions, commands/tests run, and exact commit/provenance.
