# Week 16 Farkle + ML — Implementation Plan

## Working doctrine

> **Ask to do it once: leave breadcrumbs.**  
> **Ask to do it twice: script it.**  
> **Ask to do it three times: tie it into automation.**

This plan applies that rule to course development itself.

The first Farkle build left reports and code breadcrumbs in CS1. CS2 is the second serious course-specific implementation, so validation and evidence capture must become scripted. If a third course needs the same repeatable build/validation path, promote the stable pieces into shared automation rather than copying another command list.

## Phase 0 — Freeze current truth

Deliverables:

- `sidecar/reports/014_week16_farkle_ml_current_state_report.md`
- `planning/week-16-farkle-ml-target-map.md`
- this plan

Acceptance:

- current CS1 source and unresolved hardening state recorded;
- current CS2 gaps named;
- Architecture ideas separated from CS2 ownership;
- no implementation begins from memory alone.

## Phase 1 — Reconcile the CS1 baseline

Goal: do not import known-bad comparison semantics.

Work:

1. inspect CS1 Prompt 100 findings against current code;
2. land the narrow hardening fixes in CS1 or consume their landed results if another worker has already done so;
3. record exact upstream commit/provenance;
4. freeze only the public contract CS2 actually needs.

Acceptance:

- fair starter treatment in repeated comparisons;
- player-specific Farkle-rate denominator;
- printed learner preference equals actual greedy decision;
- arbitrary human bank threshold is a truthful supported path;
- CS1 tests updated for these guarantees.

## Phase 2 — Build the CS2 experiment bench

Goal: a small real software system, not disconnected examples.

Create under a course-consistent Week 16 package path:

- provenance/shared-baseline adapter or vendored snapshot;
- explicit strategy contract;
- function adapter for CS1-compatible strategies;
- measured/timed wrapper;
- experiment configuration;
- experiment result;
- experiment runner;
- fixed strategy/configuration menu;
- trained transparent learner path;
- bounded simulation strategy if it stays humane;
- CSV/JSON result persistence.

Acceptance:

- Farkle engine rules are not independently reimplemented;
- strategies are interchangeable through one contract;
- invalid actions fail loudly;
- deterministic configurations reproduce results;
- two fixed strategies can be compared end to end;
- result files contain provenance and cost/effectiveness fields.

## Phase 3 — Add CS2-native evidence/storytelling

Goal: Week 16 visibly pays off Weeks 6–14.

Create:

- one honest plotting path from saved evidence;
- one bounded result-ordering/ranking path;
- optional FIFO experiment queue only if it simplifies batch execution;
- optional read-only/tiny model-view viewer only if it remains nearly free.

Acceptance:

- chart is generated from saved data, not hand-entered numbers;
- axes/context are labeled honestly;
- a result can be ordered by at least two objectives without pretending one universal winner exists;
- model remains independently testable from any GUI.

## Phase 4 — Author the human experience

Create:

- Week 16 student lesson;
- instructor guide;
- short experiment/design receipt;
- sample/fallback result data;
- updated `planning/week-16.md`;
- minimal gate/rubric reconciliation.

Student cognitive load target:

1. run baseline;
2. identify contract;
3. choose two provided strategies/configurations;
4. predict cost/effectiveness;
5. run one experiment bundle;
6. inspect/save evidence;
7. read/generate one plot;
8. make one defensible ship/no-ship decision.

Acceptance:

- no new technical prerequisite;
- no Checkpoint 4;
- no giant report;
- no requirement to write Farkle from scratch;
- no GPU/cloud/paid tooling required.

## Phase 5 — Script validation and receipt capture

Because this is the second course-specific Farkle build, validation must be scripted.

Create a repo-owned validation entry point, preferably:

`python scripts/validate_week16_farkle.py`

It should:

1. print runtime/source context;
2. run the Week 16 test suite;
3. run a fixed baseline comparison;
4. run the fixed learner training/evaluation smoke path;
5. run one CS2 experiment bundle;
6. write machine-readable result files;
7. generate the plot when plotting dependencies are available;
8. emit a timestamped raw receipt under `sidecar/runs/`;
9. exit nonzero on correctness/test failures.

The script must not silently install packages or change machine configuration.

Acceptance:

- one command validates the implemented Week 16 surface;
- output names/paths are predictable;
- failures are visible and actionable;
- raw evidence can be attached to the postmortem.

## Phase 6 — Postmortem and closure

Write:

`sidecar/reports/014_build_cs2_week16_farkle_ml_postmortem.md`

Include:

- what the current-state report got right/wrong;
- final architecture;
- exact CS1 provenance;
- files created/changed;
- tests/validation run and results;
- sample experiment observations;
- student friction estimate;
- what was deliberately omitted;
- remaining yellows;
- what should be promoted to shared automation if DSCT or another course asks for the same workflow again;
- final commit SHAs.

## Prompt decomposition

Prompts document the work orders and acceptance tests; they are not the final product.

- **014A** — reconcile and freeze hardened CS1 baseline
- **014B** — build CS2 experiment bench and tests
- **014C** — build visualization + student/instructor package
- **014D** — scripted validation and raw receipts
- **014E** — postmortem / closure audit

The parent Prompt 014 remains the umbrella design contract.

## Stop conditions

Stop and report rather than inventing infrastructure if:

- CS1 contract changes materially during the build;
- sharing code requires a package registry/monorepo/submodule project;
- Monte Carlo strategy makes the student experience substantially harder;
- plotting becomes a dependency-management project;
- classroom container availability is still unverified;
- a new grading weight is required;
- production Canvas/Savnac changes would be needed.

A useful YELLOW with an exact next action is preferable to hiding a dependency.
