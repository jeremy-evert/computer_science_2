# Postmortem — CS2 Week 16 Farkle + ML experiment bench

**Date:** 2026-08-16  
**Status:** IMPLEMENTED WITH NAMED REAL-CHECKOUT VALIDATION YELLOW

## What we set out to do

The original CS2 Week 16 source was only a reservation wrapper. The goal became larger and more disciplined:

1. catch up completely with the strongest CS1 Farkle work;
2. import the useful Computer Architecture cost/effectiveness framing;
3. make Week 16 feel unmistakably like the actual CS2 course;
4. build executable source, tests, teaching artifacts, and repeatable validation rather than stopping at a prompt.

The development workflow itself was also formalized:

> report -> map -> plan -> prompts/work orders -> implementation + raw receipts -> postmortem

with the operating doctrine:

> Ask once: breadcrumbs. Ask twice: script it. Ask three times: automate it.

## What the current-state report got right

The pre-build report correctly found that CS2 had planning/gate/rubric placeholders but no real Week 16 code or tests. It also correctly identified CS1 as the canonical game/learner baseline and Architecture Prompt 005 as a useful source of cost/effectiveness language.

It found one important dependency that changed the implementation order: CS1's Prompt 100 existed but had not been executed.

## Dependency work completed first

Rather than copy known-bad semantics, the CS1 hardening was implemented:

- fair alternating starters;
- per-player-turn Farkle-rate denominators;
- learner displayed preference aligned with actual greedy policy;
- arbitrary positive `bank_at_N` threshold support;
- regression tests.

CS2 then pinned the corrected source state and recorded source blob provenance.

## Final package architecture

```text
hardened/provenance-tracked CS1 baseline
                 |
                 v
          explicit Strategy contract
        /            |             \
 human threshold  trained table  one-step rollout
        \            |             /
             ExperimentConfig
                    |
              ExperimentRunner
                    |
              ExperimentResult
               /          \
            JSON          CSV
               \          /
              honest plot
                    |
             CS2 ship decision
```

CS1 remains canonical for game rules. CS2 owns the explicit collaboration/experiment layer.

## What CS2 added

### Contracts and swappable collaborators

The inherited CS1 strategy-function idea is made explicit as a CS2 `Strategy` contract. Function strategies are adapted rather than rewritten. Invalid strategy actions are rejected at the CS2 boundary.

### Three cost shapes

The fixed menu includes three intentionally different ways to buy a decision:

1. **human threshold** — negligible preparation/runtime complexity;
2. **transparent trained learner** — pay preparation/training cost, then play cheaply;
3. **bounded one-step rollout** — little preparation, explicit per-decision simulation cost.

### Experiment infrastructure

The package adds configuration/result objects, deterministic seed handling, preparation timing, evaluation timing, training budget, model-size evidence, JSON/CSV persistence, and explicit execution-context labels.

### Honest visualization/storytelling

The plotter requires a declared x-axis cost currency. It does not invent a universal efficiency score. Supported cost axes include preparation time, seconds/game, model size, and training turns.

### Professional workflow

The result rather than terminal memory is the evidence of record. Provenance, configuration, seed, sample size, and execution context travel with the saved experiment.

## Architecture ideas reused carefully

Reused:

- fixed workload / fixed strategy menu;
- preparation versus operation cost;
- effectiveness as a separate currency;
- bounded CPU-first path;
- optional future controlled hardware/container/NRP comparison.

Not imported:

- a hardware tournament as the required lab;
- Kubernetes orchestration;
- GPU requirement;
- cost leaderboard infrastructure;
- Machine Dossier work.

The specifically CS2 additional currency is **software complexity/maintenance cost**.

## CS2 course concepts that reappear

- object responsibility boundaries;
- composition around inherited behavior;
- contracts/swappable collaborators;
- result ordering under different objectives;
- honest data visualization/storytelling;
- testing/review/provenance/reproducibility.

Queue and GUI ideas were intentionally left optional rather than forced into the required path. They did not earn enough instructional value for the added Week 16 complexity.

## Teaching package created

- student lesson;
- instructor guide;
- short design/evidence receipt;
- real Week 16 planning links;
- retired gate/rubric reconciliation;
- package README.

The required student path is deliberately smaller than the implementation:

1. trust baseline;
2. find contract;
3. choose two provided options;
4. predict;
5. run bounded evidence;
6. save result;
7. read/generate one honest plot;
8. make one ship decision.

## Testing and validation

Automated standard-library tests are present in:

`tests/test_week16_farkle.py`

The second-repeat doctrine produced a one-command validator:

```text
python scripts/validate_week16_farkle.py
```

The validator is designed to:

- run tests;
- execute the fixed suite;
- save JSON/CSV;
- attempt the plot;
- write a timestamped raw receipt;
- fail nonzero on required correctness failures;
- install nothing.

## What we cannot truthfully claim yet

This assistant environment could write to the private GitHub repository but could not clone/execute it locally. Therefore this postmortem does **not** claim:

- a test-pass count;
- measured training/runtime values;
- sample win rates;
- a generated plot;
- a fully GREEN physical/runtime validation.

No sample evidence was fabricated to make the report look complete.

## Current yellows

### YELLOW 1 — real-checkout validator has not run

Required next action:

```text
python scripts/validate_week16_farkle.py
```

Run from a current `computer_science_2` checkout. Preserve the resulting `sidecar/runs/014_validation_<timestamp>.md` receipt.

### YELLOW 2 — matplotlib availability may vary

Plotting is part of CS2's existing course path, but the validator treats missing matplotlib as an explicit plotting YELLOW rather than silently installing it. JSON/CSV evidence remains required.

### YELLOW 3 — optional container/hardware lane

No container/hardware/NRP comparison is required. It may be added only after the separate platform work is actually verified and useful.

## What we deliberately did not build

- second canonical Farkle rules engine;
- formal Q-learning/SARSA/Bellman unit;
- neural network;
- giant GUI/dashboard;
- database experiment tracker;
- Kubernetes tournament service;
- leaderboard/grading economy;
- new Week 16 checkpoint;
- fake sample-output numbers.

## Automation recommendation

The validation/receipt pattern is now scripted because this is the second serious course-specific Farkle build.

If DSCT or another third course needs the same underlying Farkle experiment execution/receipt machinery, do **not** copy `scripts/validate_week16_farkle.py` a third time. Promote the stable shared experiment/result/validation contract into the appropriate shared curriculum/tooling owner and let each course supply only its course-specific lens.

## Raw receipts

- `sidecar/runs/014_build_connector_receipt.md`
- future real run: `sidecar/runs/014_validation_<timestamp>.md`

## Closure

The missing CS2 Week 16 courseware has been built. The campaign is no longer a planning placeholder or a prompt-only artifact.

Current classification:

> **IMPLEMENTED WITH NAMED REAL-CHECKOUT VALIDATION YELLOW**

Promote to GREEN only after the one-command validator succeeds on a real checkout and its receipt is retained.
