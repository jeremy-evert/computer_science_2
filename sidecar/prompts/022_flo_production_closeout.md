# Prompt 022 — Flo production closeout for Computer Science II

**Status:** READY FOR FLO  
**Course:** COMSC-1053-1417 Computer Science II, Fall 2026  
**Role:** Flo, Lead Foreman  
**Human gate:** one production-write authorization after read-only preflight

## Mission

Take the already source-backed and Savnac-accepted Computer Science II DesiredCourse from a clean repository state to a bounded production Canvas closeout.

The desired human experience is:

```text
Flo preflight
    ↓
GREEN TO WRITE
    ↓
Jeremy: WRITE CS2
    ↓
Flo production closeout
```

Do not turn this into a chain of historical prompts. This prompt is the canonical burn for the current CS2 production closeout.

## Hard boundaries

- You own **Computer Science II only**.
- **Do not work on Computer Architecture.** It is another Foreman's lane.
- **Do not work on Computer Science 1.** It is another worker's lane.
- You are already launched. **Never invoke `sidecar/launch_flo.sh` from inside this job.**
- Do not make promotion of a Luna/Course Foundry branch a prerequisite. Use current evidence. If a current dependency is genuinely insufficient, prove the exact CS2 blocker before touching shared tooling.
- Do not start a general Course Foundry cleanup campaign.
- Never stash, reset, clean, delete, or overwrite unknown human work to make a checkout look clean.
- Never echo, copy, or commit Canvas credentials.
- No production write is authorized until the human gate below is satisfied.

## Current accepted contract

The current CS2 compiler deliberately owns **Weeks 2 through 17**. Week 1 is excluded from the CS2 DesiredCourse because the shared `semester_kickoff_week` pipeline owns it.

The Savnac-accepted CS2-owned DesiredCourse shape is pinned by `scripts/cs2_production.py`:

- 16 modules, positions 2 through 17
- 155 modeled objects
- 14 CS2 assignment groups
- assignment-group weights sum to 100%
- `prune_scope=none`

If the compiler no longer produces that shape, stop. That is source/compiler drift requiring review, not permission to silently widen the write.

## Phase A — prove the runway

Work from current Git and current source, not old planning prose.

1. Confirm this repository is on the intended current commit and inspect any pre-existing worktree dirt. Preserve unknown work.
2. Confirm these sibling repositories exist and are clean before production work:
   - `course_foundry`
   - `harbor`
   - `imprint`
   - `local_ai_lab_setup`
3. Run the current CS2 production-wrapper tests:

   ```bash
   python3 -m pytest -q tests/test_cs2_production.py
   ```

4. Run the current source validators using the working Course Foundry environment:

   ```bash
   python3 -m course_foundry.week1_validator --repo "$CS2_ROOT"
   python3 -m course_foundry.completeness_validator --repo "$CS2_ROOT" --expected-weeks 17
   python3 -m course_foundry.cross_repo_integrity
   ```

5. Run the relevant Course Foundry CS2 desired-course tests if the current environment exposes them. Prefer targeted tests over an unrelated full-repository campaign.
6. Do not promote or merge any branch merely because it exists. Current clean dependencies that satisfy the tests are enough.

If a validator fails, repair a real CS2-owned source/tooling defect when safely in scope, commit it, rerun validation, and restart the production preflight from fresh source truth. If the defect belongs to another active lane or requires a human policy decision, stop with one concise blocker report.

## Phase B — read-only production preflight

Use the existing production Canvas environment. Do not print secrets.

Run:

```bash
python3 scripts/cs2_production.py preflight
```

This command is the production authority boundary. Before it can emit `GREEN TO WRITE`, it must:

- require the production Canvas host marker;
- discover exactly one live Fall 2026 course matching `COMSC-1053-1417` and Computer Science II/2;
- bind a course-specific Canvas client to that exact course id;
- verify the live target identity again;
- require all source-bearing repositories to be clean;
- compile exactly the Savnac-accepted Weeks 2-17 shape;
- perform only an Imprint dry-run with `prune_scope=none`;
- reject any proposed deletion;
- write `sidecar/runs/flo_cs2_preflight.json`;
- print a short authorization token bound to the exact target, source revisions, desired-plan digest, and full dry-run action log.

### Week 1 during preflight

Week 1 is **read-only to this CS2 burn**. Do not add it to the CS2 DesiredCourse and do not use course-wide prune.

The final Savnac walk found a pre-existing shared-kickoff module-position defect. If a read-only production inspection proves the same defect exists there, record it as an externally owned kickoff issue. Do not widen the CS2 write to repair it.

### GREEN TO WRITE message

If and only if the preflight succeeds, report to Jeremy only the compact decision packet:

```text
GREEN TO WRITE
Target: <course id> <course name> <course code> <term>
Dry run: create=<n> update=<n> delete=0
Scope: CS2 Weeks 2-17, prune=none, Week 1 excluded
```

Keep the token in the Foreman session. Jeremy should not have to relay it.

Then stop at the human gate.

## Human gate

A production write is authorized only by an explicit response from Jeremy in this same Foreman session equivalent to:

```text
WRITE CS2
```

Silence, enthusiasm, a request for status, or permission from an older run is not authorization.

If source revisions, target identity, desired state, or dry-run actions change after the preflight, the old authorization is stale. Re-preflight and ask again with the new compact packet.

## Phase C — production reconcile and closeout

After explicit `WRITE CS2` authorization, use the token from the immediately preceding green preflight:

```bash
python3 scripts/cs2_production.py write --authorize "$TOKEN"
```

The wrapper itself must fresh-preflight before writing and reject a stale token. The live reconcile must use:

- the exact auto-discovered/verified course id;
- Weeks 2-17 only;
- `force=False`;
- `prune_scope=none`;
- explicit production-write confirmation in Imprint.

Immediately after the write, the wrapper must dry-run the same desired plan again. DONE requires:

```text
create=0
update=0
delete=0
```

The wrapper writes `sidecar/runs/flo_cs2_closeout.json` whether the closeout converges or the write lands but fails the fixed-point check.

## Independent read-back

After a successful fixed point, perform a read-only production walk sufficient to catch the failures a write response cannot prove. At minimum verify:

- target identity is still `COMSC-1053-1417` Fall 2026 CS2;
- the CS2-owned Week 2-17 modules exist and are published/coherent;
- CS2 assignment-group weights remain 100%;
- there are no duplicate CS2 assignment/page titles introduced by this reconcile;
- the Reasoning Odyssey checkpoint rubrics for Weeks 6, 9, and 14 are structurally present;
- no ZyBooks requirement was reintroduced;
- no backstage Four Living Worlds canon leaked into student-visible content.

Do not treat unrelated pre-existing production objects outside the CS2 modeled scope as drift to delete. `prune_scope=none` is deliberate.

## Closeout evidence

Write the final durable report to:

`sidecar/reports/023_flo_production_closeout.md`

If preflight cannot reach GREEN TO WRITE, write instead:

`sidecar/reports/023_flo_preflight_blocked.md`

The report must include:

- exact CS2/source dependency commit SHAs used;
- target id/name/course code/term, without credentials;
- validator/test results;
- preflight create/update/delete counts;
- whether Jeremy authorized the write and the exact human authorization text, but **not** the token if there is no reason to preserve it;
- live write counts;
- immediate closeout dry-run counts;
- independent read-back findings;
- any Week 1 external issue observed;
- exact files/commits produced.

Commit CS2-owned source/evidence changes with a clear message. Do not commit secrets or generated credential material.

## DONE conditions

This burn is DONE only when all of the following are true:

1. source validators/tests used for the burn are green;
2. production target selection is exact and unambiguous;
3. the human explicitly authorized the live write after the fresh green preflight;
4. the live reconcile succeeded with zero deletions;
5. the immediate closeout dry-run is a fixed point: create=0, update=0, delete=0;
6. independent read-back is coherent for the CS2-owned scope;
7. Week 1 remained outside CS2 write authority;
8. the final report and evidence receipts exist and are committed where appropriate.

The point of this prompt is not heroics. The point is for the production run to be boring.
