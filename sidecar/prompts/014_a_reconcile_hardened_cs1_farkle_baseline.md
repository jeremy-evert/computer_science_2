# Prompt 014A — Reconcile and freeze the hardened CS1 Farkle baseline

**Status:** READY  
**Parent:** `sidecar/prompts/014_build_cs2_week16_farkle_extension.md`

## Read first

- `sidecar/reports/014_week16_farkle_ml_current_state_report.md`
- `planning/week-16-farkle-ml-target-map.md`
- `planning/week-16-farkle-ml-implementation-plan.md`
- current CS1 Week 16 source
- CS1 `sidecar/prompts/100_harden_week16_farkle_ml_evidence.md`

## Work

1. Record current CS1 HEAD.
2. Reproduce the four known Prompt-100 evidence seams.
3. If still present, make the narrow CS1 repairs rather than importing known-bad semantics into CS2.
4. Update/add CS1 tests for the repaired contract.
5. Record the exact post-fix CS1 commit/provenance that CS2 will consume.
6. Do not redesign CS1 Week 16.

## Acceptance

- repeated comparison treats starting position fairly;
- Farkle rates use each player's own turns;
- printed learner preference matches actual greedy behavior;
- arbitrary positive `bank_at_N` human thresholds have a truthful supported CLI path;
- existing CS1 behavior/tests remain intact except for deliberate fixes;
- a short raw work receipt records changed files and test commands/results.

## Stop

Do not proceed to 014B until the baseline contract is either GREEN or a precise dependency is recorded.
