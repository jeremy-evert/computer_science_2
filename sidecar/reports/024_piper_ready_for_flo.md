# Report 024 — Piper handoff: CS2 ready for Flo

**Date:** 2026-08-19  
**Verdict:** READY FOR FLO  
**Scope:** Computer Science II only

## Current truth

Current `main` before this report was `cef7c8229bce79986ece3abfe79d05ef94f3a764` (`Add one-command CS2 Flo launcher`).

The newest repository evidence supersedes old planning prose:

- Prompt 021 / commit `8f7b498d9738dac9fe4ef9b99549692c17c7ba7a` rendered and accepted the complete honest Fall 2026 semester in Savnac.
- Week 1 is real and live but is owned by the separate `semester_kickoff_week` pipeline, not the CS2 DesiredCourse builder.
- The CS2 builder owns Weeks 2-17 and its Savnac-accepted shape is 16 modules, 155 modeled objects, 14 CS2 assignment groups, total group weight 100%, with `prune_scope=none`.
- Savnac read-back in Report 021 found 20 total published modules, 121 assignments with zero duplicate names, 69 pages with zero duplicate titles, 15 assignment groups totaling 100%, all three checkpoint rubrics present, zero ZyBooks references, and no backstage Four Living Worlds canon leak.
- The one known Savnac defect is Week 1 Wednesday/Friday/A07 module ordering after Week 17. It predates the CS2 reconcile and belongs to the shared kickoff pipeline. It is not authority for widening the CS2 write.
- No production SWOSU Canvas write is recorded by the Savnac acceptance work.

## Student-facing source

No RED student-facing source gap remains in the source-backed semester compile. Weeks 1-17 genuinely exist under the ownership split above.

Honest unresolved policy/design items that are not blockers to rendering remain disclosed rather than invented, including late/drop mechanics. They are not prerequisites for Flo production closeout.

## Production machinery now present

Piper's production-preparation chain on `main` is:

1. `scripts/cs2_production.py` — guarded production preflight/write wrapper.
2. `tests/test_cs2_production.py` — target-selection, diff-token, porcelain-path, and Savnac-shape guard tests.
3. `sidecar/prompts/022_flo_production_closeout.md` — one canonical Flo burn.
4. `sidecar/launch_flo.sh` — one-command launcher with main-branch, clean-tracked-worktree, fast-forward, recursion, CLI, and single-Foreman lock guards.

The production wrapper deliberately:

- requires the production Canvas host marker;
- discovers exactly one Fall 2026 `COMSC-1053-1417` Computer Science II target;
- verifies target identity again with a course-specific allowlisted client;
- requires clean source-bearing repositories;
- pins the DesiredCourse to the accepted Weeks 2-17 shape;
- dry-runs with `force=False`, `prune_scope=none`, and no live-write confirmation;
- rejects proposed deletions;
- binds a short authorization token to target identity, source revisions, desired-plan digest, and the exact dry-run action log;
- fresh-preflights before any write and rejects a stale token;
- writes live only after the explicit human gate;
- immediately dry-runs again and requires a `create=0/update=0/delete=0` fixed point;
- writes durable preflight and closeout receipts under `sidecar/runs/`.

## Flo burn

Canonical burn: `sidecar/prompts/022_flo_production_closeout.md`.

Human interaction is intentionally collapsed to:

```text
./sidecar/launch_flo.sh
    ↓
Flo read-only validation + production preflight
    ↓
GREEN TO WRITE
    ↓
Jeremy: WRITE CS2
    ↓
Flo production reconcile + fixed-point + read-back + closeout report
```

Flo must rerun the current validators/tests in Phase A before emitting `GREEN TO WRITE`. This handoff does not substitute historical green evidence for that fresh production runway check.

## Human gates

There is exactly one production-write gate.

After a fresh successful preflight, Jeremy must explicitly authorize the write in the same Flo session with text equivalent to:

```text
WRITE CS2
```

Silence, prior authorization, or a status request is not authorization. If target/source/dry-run state changes, Flo must re-preflight and the prior authorization becomes stale.

## Authority boundaries

- Computer Architecture: out of bounds.
- Computer Science 1: out of bounds.
- Week 1 shared kickoff: read-only to this CS2 production burn.
- Luna/Course Foundry unpromoted work: not a prerequisite unless fresh CS2 evidence proves a concrete blocker.
- No general Course Foundry cleanup.
- No production deletion campaign; `prune_scope=none` is deliberate.

## DONE conditions

Flo's job is DONE only when:

1. current validators/tests are green;
2. production target selection is exact and unambiguous;
3. Jeremy explicitly authorizes the live write after the fresh green preflight;
4. live reconcile succeeds with zero deletions;
5. immediate closeout dry-run is a no-op (`0/0/0` create/update/delete);
6. independent production read-back is coherent for CS2 Weeks 2-17;
7. Week 1 remains outside CS2 write authority;
8. final report/evidence are committed without secrets.

## Launch

```bash
./sidecar/launch_flo.sh
```

No further Piper source/tooling work is currently justified before Flo. The next useful information comes from the fresh read-only production preflight.