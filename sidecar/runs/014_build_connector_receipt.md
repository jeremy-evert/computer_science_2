# Raw Work Receipt — CS2 Week 16 Farkle + ML build

**Date:** 2026-08-16  
**Execution surface:** connected GitHub writes; shell cannot clone private GitHub in this environment  
**Status:** IMPLEMENTED / REAL-CHECKOUT VALIDATION YELLOW

## Pre-build breadcrumbs

- `sidecar/reports/014_week16_farkle_ml_current_state_report.md`
- `planning/week-16-farkle-ml-target-map.md`
- `planning/week-16-farkle-ml-implementation-plan.md`

## Work-order breadcrumbs

- parent Prompt 014
- Prompt 014A — hardened CS1 baseline
- Prompt 014B — experiment bench/tests
- Prompt 014C — student/instructor package
- Prompt 014D — scripted validation/receipts
- Prompt 014E — postmortem/closure

## Upstream CS1 dependency repaired

CS1 Prompt 100 seams were implemented before CS2 vendoring:

- dynamic `bank_at_N` threshold strategies;
- alternating starters in repeated comparisons;
- Farkle-rate denominator per strategy's own turns;
- learner displayed preference aligned with actual greedy policy;
- regression tests.

Pinned CS1 source state used by CS2: `b546ca2f846ea0c788ad17e5667b8b471efb33fa`.

CS1 hardening report: `computer_science_1/sidecar/reports/100_harden_week16_farkle_ml_evidence.md`.

## CS2 source implemented

### Shared/provenance layer

- `lessons/code/farkle_week16/vendor_cs1/PROVENANCE.md`
- `lessons/code/farkle_week16/vendor_cs1/UPSTREAM_MANIFEST.json`
- vendored `engine.py`, `strategies.py`, `learner.py`, `simulate.py`

### CS2 experiment bench

- `lessons/code/farkle_week16/contract.py`
- `lessons/code/farkle_week16/strategies.py`
- `lessons/code/farkle_week16/experiment.py`
- `lessons/code/farkle_week16/cli.py`
- `lessons/code/farkle_week16/plot_results.py`
- `lessons/code/farkle_week16/README.md`

Strategy families:

1. human threshold (`bank_at_N`);
2. transparent trained learner (`learner:N`);
3. bounded one-step rollout (`rollout:N`).

Evidence currencies remain separate:

- effectiveness;
- preparation/training;
- operating/runtime;
- software complexity/maintenance.

### Tests and scripted validation

- `tests/test_week16_farkle.py`
- `scripts/validate_week16_farkle.py`

The validator is intentionally one command because this is the second serious course-specific Farkle build:

```text
python scripts/validate_week16_farkle.py
```

It runs tests, runs a fixed experiment suite, writes JSON/CSV, attempts the plot, and writes a timestamped receipt under `sidecar/runs/`.

### Teaching package

- `lessons/week-16-farkle-ml-experiment-bench.md`
- `docs/curriculum/week-16-farkle-ml-instructor-guide.md`
- `assignments/W16-farkle-ml-design-receipt.md`
- updated `planning/week-16.md`
- reconciled retired Week 16 gate/rubric

## Key implementation commits

- `4a7a5f414edef52382af16bf2453e5394cc40ce4` — strategy contract
- `b23f614861b3ab803d01cc0b947eac15a89fa105` — strategy families
- `6e4e8848a4ed1ed55f82331911f97421e88031f7` — experiment runner/result receipts
- `d4f60f41d8405b582ed04e72517dd8b2351c2b5a` — CLI
- `5a7c5f35b70cd8194114fba79e7a022d74c9c9b4` — plotter
- `d6076d6af456f0c7e4235b358ddae13042972ada` — tests
- `f5a47fe219bebeae6b77eb33accf13121c064663` — one-command validator
- `a5165673f68459a9ee989cb59e36bb5a02acff6f` — student lesson
- `0eb5aa5c4787243a5cd0f3d880b2569792e1b13b` — instructor guide
- `bc4c91b313daabfe79619a99f8de52b2de09f63f` — Week 16 source reconciliation
- `a992745a00b6550f856c9382dc8b84b2065e0e3a` — upstream source manifest
- `5da07401afd0bcc7be22cd33e742386d3efa9ee7` — workflow/status documentation

## Named validation yellow

This environment cannot execute the private repository after writing it. Therefore:

- no test-pass count is claimed;
- no numeric sample win-rate/timing evidence is invented;
- no fake fallback CSV/plot is checked in.

A real checkout must run `python scripts/validate_week16_farkle.py`. The resulting timestamped receipt is the evidence required to promote the build from IMPLEMENTED WITH VALIDATION YELLOW to GREEN.

## Automation escalation note

This build scripts the repeated validation pattern. If DSCT or a third course asks for the same cross-course Farkle validation/receipt orchestration, promote the stable runner/result contract into shared automation rather than hand-copying this validator again.
