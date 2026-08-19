# Prompt 022 — Flo production closeout for Computer Science II

**Status:** READY FOR FLO  
**Course:** COMSC-1053-1417 Computer Science II, Fall 2026  
**Role:** Flo, Lead Foreman  
**Human gate:** one production-write authorization after read-only preflight

## Mission

Take the source-backed, Savnac-accepted Computer Science II DesiredCourse through a bounded production Canvas closeout.

The intended human interaction is:

```text
Flo validation + preflight
    ↓
GREEN TO WRITE
    ↓
Jeremy: WRITE CS2
    ↓
Flo production reconcile + closeout
```

This prompt is the canonical burn. Do not resurrect the historical prompt chain.

## Runway contract

The launcher creates an **isolated production workspace** containing fresh origin clones of:

- `computer_science_2`
- `course_foundry`
- `harbor`
- `imprint`
- `local_ai_lab_setup`

Those clones are siblings under one campaign root. The ordinary checkouts elsewhere on Brandy may contain active work from CS1, Architecture, or other lanes. **Do not clean, stash, reset, modify, merge, or otherwise touch those ordinary checkouts.** Their dirt is not a CS2 blocker because this burn does not consume them.

Use the Python environment already placed first on `PATH` by the launcher. Source imports must come from the isolated campaign clones.

## Hard boundaries

- Own **Computer Science II only**.
- Computer Architecture is out of bounds.
- Computer Science 1 is out of bounds.
- Never invoke `sidecar/launch_flo.sh` from inside this already-launched job.
- Do not promote Luna/Course Foundry branches merely because they exist.
- Do not start a general Course Foundry cleanup campaign.
- Never echo, copy, or commit Canvas credentials.
- No production write is authorized before the human gate.
- Never widen the CS2 write to repair Week 1 shared-kickoff behavior.

## Accepted source contract

The CS2 compiler deliberately owns **Weeks 2 through 17**. Week 1 belongs to `semester_kickoff_week` and is read-only to this burn.

`scripts/cs2_production.py` pins the Savnac-accepted CS2 shape:

- 16 modules at positions 2 through 17
- 155 modeled objects
- 14 CS2 assignment groups
- assignment-group weights totaling 100%
- `prune_scope=none`

If current origin source no longer compiles to that shape, stop. That is real source/compiler drift.

## Phase A — prove the isolated runway

Work from current campaign Git, not old planning prose.

1. Confirm the current repository and all four sibling dependency clones are clean and record their exact HEAD SHAs.
2. Confirm the current repository remote is the canonical CS2 origin and that the sibling layout is the launcher-created campaign root.
3. Run the CS2 production-wrapper safety tests:

   ```bash
   python3 -m pytest -q tests/test_cs2_production.py
   ```

4. Run the **current existing** Course Foundry CS2 desired-course tests:

   ```bash
   cd ../course_foundry
   python3 -m pytest -q tests/test_cs2_desired_course.py
   cd ../computer_science_2
   ```

5. Do **not** attempt to run historical modules named `course_foundry.week1_validator`, `course_foundry.completeness_validator`, or `course_foundry.cross_repo_integrity`. They do not exist in current Course Foundry source and are superseded for this burn by the targeted tests above plus the production wrapper's pinned DesiredCourse shape check.
6. If either targeted test suite fails, repair a genuine CS2-owned defect only when safely in scope. If current origin dependencies are incompatible in a way CS2 cannot own, stop with one concise blocker report.

A dirty ordinary checkout outside the campaign root is **not** grounds to stop or alter it.

## Phase B — read-only production preflight

Use the existing production Canvas environment without printing secrets.

Run from the isolated CS2 repository:

```bash
python3 scripts/cs2_production.py preflight
```

This is the production authority boundary. Before it can emit `GREEN TO WRITE`, it must:

- require the production Canvas host marker;
- discover exactly one live Fall 2026 course matching `COMSC-1053-1417` and Computer Science II/2;
- bind a course-specific Canvas client to that exact course id;
- verify target identity again;
- require the isolated source-bearing repositories to be clean;
- compile exactly the accepted Weeks 2-17 shape;
- perform only an Imprint dry run with `force=False` and `prune_scope=none`;
- reject any proposed deletion;
- write `sidecar/runs/flo_cs2_preflight.json`;
- print an authorization token bound to target identity, source revisions, desired-plan digest, and the exact dry-run action log.

### Week 1

Week 1 remains read-only. The Savnac acceptance walk found a pre-existing shared-kickoff module-ordering defect. If production has the same defect, record it as an externally owned kickoff issue. Do not widen this CS2 reconcile to repair it.

### GREEN TO WRITE

If and only if the preflight succeeds, give Jeremy only this compact packet:

```text
GREEN TO WRITE
Target: <course id> <course name> <course code> <term>
Dry run: create=<n> update=<n> delete=0
Scope: CS2 Weeks 2-17, prune=none, Week 1 excluded
```

Keep the token in this Flo session. Jeremy does not relay it.

Then stop at the human gate.

## Human gate

A production write is authorized only by an explicit response from Jeremy in this same Flo session equivalent to:

```text
WRITE CS2
```

Silence, enthusiasm, status questions, or authorization from an older run do not count.

If source revisions, target identity, desired state, or dry-run actions change after preflight, the authorization is stale. Re-preflight and ask again.

## Phase C — production reconcile

After explicit authorization, use the token from the immediately preceding green preflight:

```bash
python3 scripts/cs2_production.py write --authorize "$TOKEN"
```

The wrapper must fresh-preflight before writing and reject a stale token. Live reconcile authority is limited to:

- the exact discovered and re-verified course id;
- Weeks 2-17 only;
- `force=False`;
- `prune_scope=none`;
- explicit production-write confirmation in Imprint.

Immediately afterward, the wrapper dry-runs the same plan again. Fixed-point DONE requires:

```text
create=0
update=0
delete=0
```

## Independent read-back

After a successful fixed point, independently inspect production read-only and verify at minimum:

- target remains Fall 2026 `COMSC-1053-1417` CS2;
- CS2-owned Week 2-17 modules exist and are published/coherent;
- CS2 assignment-group weights remain 100%;
- no duplicate CS2 assignment or page titles were introduced;
- Reasoning Odyssey checkpoint rubrics for Weeks 6, 9, and 14 are structurally present;
- no ZyBooks requirement was reintroduced;
- no backstage Four Living Worlds canon leaked into student-visible content.

Do not treat unrelated pre-existing production objects as drift to delete.

## Evidence

Write the successful closeout report to:

`sidecar/reports/023_flo_production_closeout.md`

If the **isolated** runway or production preflight still cannot reach GREEN TO WRITE, write:

`sidecar/reports/023_flo_preflight_blocked.md`

Include:

- exact CS2 and dependency SHAs from the campaign clones;
- targeted test results;
- target identity without credentials;
- preflight create/update/delete counts;
- whether Jeremy authorized the write and the exact authorization text, but not the token;
- live write counts;
- immediate closeout counts;
- independent read-back findings;
- any Week 1 external issue observed;
- exact files and commits produced.

Commit and push CS2-owned evidence from this isolated CS2 clone. Do not commit secrets.

## DONE conditions

DONE means all of these are true:

1. targeted current tests are green;
2. the production target is exact and unambiguous;
3. Jeremy explicitly authorized the live write after the fresh green preflight;
4. live reconcile succeeded with zero deletions;
5. immediate closeout is `create=0/update=0/delete=0`;
6. independent production read-back is coherent for Weeks 2-17;
7. Week 1 stayed outside CS2 write authority;
8. final report and receipts exist and CS2-owned durable evidence is pushed.

The production run should be boring. That is the feature.
