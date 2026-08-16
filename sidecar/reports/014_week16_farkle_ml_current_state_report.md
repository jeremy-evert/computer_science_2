# 014 Current-State Report — CS2 Week 16 Farkle + ML

**Date:** 2026-08-16  
**Scope:** `jeremy-evert/computer_science_2` Week 16 and upstream CS1 Farkle dependencies  
**Status:** PRE-BUILD REPORT

## Executive finding

CS2 Week 16 is not implementation-complete.

The course has a clear Week 16 reservation in:

- `planning/week-16.md`
- `assignments/odyssey_gates/week-16.md`
- `rubrics/odyssey_gates/week-16_rubric.md`

but it does not yet have a CS2-native executable Farkle/ML lab, tests, student lesson, instructor guide, experiment receipt, plotting path, sample output, or validation runner.

The `tests/` directory contains only `.gitkeep` at inspection time.

This is a real implementation gap, not a reason to redesign the semester.

## Upstream CS1 state

CS1 is the strongest existing Farkle implementation and should remain the source of truth for the game rules and baseline learning experience.

Observed CS1 assets include:

- `lessons/code/farkle/engine.py`
- `lessons/code/farkle/strategies.py`
- `lessons/code/farkle/learner.py`
- `lessons/code/farkle/simulate.py`
- `lessons/code/farkle/cli.py`
- `tests/test_farkle_engine.py`
- `tests/test_farkle_learner.py`
- `lessons/10-farkle-ml.md`
- `docs/curriculum/week-16-instructor-guide.md`
- `assignments/W16-farkle-ml-experiment-receipt.md`
- `reports/013_week16_farkle_ml_capstone.md`
- `docs/curriculum/cs2-farkle-ml-handoff.md`

At inspection time CS1 HEAD is `c350d3d96f93b011d4efd9a2802f226020389bf0`.

That commit adds `sidecar/prompts/100_harden_week16_farkle_ml_evidence.md`; the hardening work itself has **not yet landed**. Therefore CS2 must not freeze a pre-hardening copy as authoritative without first reconciling the known evidence seams.

Known Prompt-100 seams:

1. strategy A always starts, which can contaminate win-rate evidence;
2. Farkle rates use total game turns rather than each player's own turns;
3. displayed learner preference can disagree with actual greedy choice under sparse evidence;
4. student prose implies arbitrary human thresholds while the CLI exposes only fixed named strategies.

## Existing CS2 strengths to reuse

CS2 already has the right semester grammar for a strong Week 16 payoff:

- Week 3: cohesive object boundaries;
- Week 4: composition, invariants, refactoring;
- Week 5: earned inheritance / polymorphism;
- Week 6: contracts and swappable collaborators;
- Week 7: list/stack/queue abstractions;
- Week 8: search/order/maintenance tradeoffs;
- Week 9: compact model/view event flow;
- Weeks 10–11: honest visualization and data storytelling;
- Weeks 12–14: testing, review, source management, reproducibility, AI accountability.

Existing implemented micro-labs include at least:

- `lessons/week-09-tkinter-model-view-lab.md`
- `lessons/week-10-data-storytelling-micro-lab.md`
- `lessons/week-10-data-storytelling-micro-lab.py`

Week 16 should reuse their habits, not invent a parallel CS2 identity.

## Architecture work worth importing

Computer Architecture Prompt 005 contributes a useful cross-course experiment grammar:

- hold the Farkle problem/rules fixed;
- compare fixed software strategies or effort levels;
- distinguish effectiveness, preparation cost, and operating cost;
- ask when extra computation actually earns its keep;
- preserve CPU/free-tooling as the required path;
- treat hardware/container/cloud/NRP lanes as optional instructor enrichment;
- do not build the grand tournament platform as a Week 16 prerequisite.

CS2 should add one currency Architecture does not own: **software complexity and maintenance cost**.

## Gap classification

### RED — missing implementation

- no CS2 Farkle experiment package;
- no CS2 Farkle tests;
- no Week 16 student lesson;
- no Week 16 instructor guide;
- no CS2 experiment receipt;
- no saved machine-readable experiment schema;
- no Week 16 plot path;
- no repeatable validation script;
- no raw run receipt convention;
- no post-build report.

### YELLOW — upstream dependency

CS1 Prompt 100 must be reconciled before CS2 declares its vendored/shared baseline trustworthy.

### GREEN — course decisions already settled

- Week 16 is shared Farkle + ML application/fun;
- no Checkpoint 4;
- no formal reinforcement-learning prerequisite;
- no paid AI requirement;
- no required GPU/cloud path;
- Weeks 15–17 do not gain a surprise technical final.

## Recommendation

Build the missing CS2 package now.

Do not wait for a new grand shared infrastructure project. Use a small provenance-tracked upstream snapshot/adapter, real CS2 contracts and experiment objects, honest saved evidence and plotting, a compact student experience, automated tests, and a scriptable validation path.

The build should be substantial for the authoring system and deliberately light for the student.
