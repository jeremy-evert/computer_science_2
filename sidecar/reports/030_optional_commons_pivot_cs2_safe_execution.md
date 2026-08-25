# Report 030 — CS2 Optional Computing Commons Pivot: Safe First Execution Slice

Campaign: `fall-2026-four-course-cleanup-chain-gun-20260824-v2`. Prompt: `sidecar/prompts/030_optional_commons_pivot_cs2_safe_execution.md` (staged and pushed by Jeremy, commit `77c6df7`). Owner decision: `swosu_cs_curriculum/decisions/029_fall_2026_optional_computing_commons_pivot.md`. Inventory authority: `swosu_cs_curriculum/reports/029_four_course_optional_commons_pivot_inventory.md`, §§15–16.

## 1. Source HEADs / references

- `swosu_cs_curriculum` Decision 029 and Report 029 §§15–16 (live-Canvas follow-up, 2026-08-25T00:43Z) read in full before execution.
- `computer_science_2` main was at `f507659` locally; Jeremy's Prompt 030 commit (`77c6df7`) had landed on `origin/main` first — rebased cleanly onto it before this pass (no conflicting work).

## 2. Source files changed and why

- `docs/grading-model.md` — added a "New required grading model" section (45% weekly gates / 30% checkpoints / 15% final reflection / 8% attendance / 2% course eval = 100%, Week 1 Kickoff preserved as historical bonus outside the 100%); the prior full-cadence table is kept underneath as an explicitly-labeled superseded/historical section, not deleted (provenance preserved).
- `docs/syllabus.md` — the student-facing grading table updated to the same new required model, with an explanatory note that pair programming/Show & Tell continue in class with no separate assignment.
- `assignments/A3-pair-programming.md`, `A4-show-and-tell-reflection.md`, `A7-friday-feedback-report.md`, `A6-professional-pathway-artifacts.md` — each marked with a `RETIRED (Prompt 030...)` provenance note at the top of the file rather than deleted or moved (this repo's `archive/` directory is for past-semester snapshots, not a "retired current content" bucket, so an in-place marker was the correct convention here, not a move).
- `docs/repo-map.md` — reviewed; its Monday Moment/Professional Minds rows are provenance pointers ("shared across Fall 2026 host courses"), not "required" claims, so left unchanged — no contradictory required-language found there.

## 3. Before/after required grading model

Before (source-described, never fully deployed live — see §5): Semester Kickoff 5% + Monday Moment 5% + Wacky Wednesday 5% + Fun Friday 5% + A3 5% + A7 5% + A4 5% + Weekly reinforcement 25% + Checkpoints 15% + A5 8% + A6×2 10% + Attendance 5% + Course eval 2% = 100%.

After (target, recorded in source only — not yet live): Weekly reinforcement/Odyssey gates 45% + Checkpoints 30% + Final reflection 15% + Attendance 8% + Course eval 2% = 100%. Week 1 Kickoff preserved as bonus, outside the 100%.

## 4. Retired/legacy source artifacts and preserved provenance

A3, A4, A7, A6 assignment files marked retired in place (see §2); their full original content is preserved unchanged below the marker. The original grading-model.md table is preserved as a labeled "Superseded" section rather than deleted.

## 5. Live Canvas preflight table (read-only, immediately before considering mutation)

Course allowlist restricted to `{74031, 24298}` for this entire pass, verified via `read_canvas_config().allowed_course_ids` before any call.

`list_assignment_groups(74031)`, cross-checked against a fresh `list_assignments(74031)` (14 live assignments, confirming Report 029 §15's finding still holds):

| Group ID | Name | Weight | Live assignment count | Disposition |
|---|---|---:|---:|---|
| 151255 | Assignments (Roll Call Attendance) | 0% | 1 | Course-core — do not touch |
| 156878 | Semester kickoff week | 5% | 13 | Real submissions — do not touch |
| 156879 | Monday Moment quiz | 5% | 0 | **Candidate — empty, matches prompt's named list** |
| 156880 | Wacky Wednesday reflection | 5% | 0 | **Candidate — empty** |
| 156881 | Fun Friday reflection | 5% | 0 | **Candidate — empty** |
| 156882 | Paired-programming report | 5% | 0 | **Candidate — empty** |
| 156883 | Friday feedback report | 5% | 0 | **Candidate — empty** |
| 156884 | Show-and-Tell reflection | 5% | 0 | **Candidate — empty** |
| 156888 | Professional pathway — Week 14 update | 5% | 0 | **Candidate — empty** |
| 156889 | Professional pathway — Week 15 submission | 5% | 0 | **Candidate — empty** |
| 156885 | Weekly reinforcement assignment | 25% | 0 | Course-core future home — do not touch |
| 156886 | Reasoning Odyssey checkpoints | 15% | 0 | Course-core future home — do not touch |
| 156887 | Final reflection paper | 8% | 0 | Course-core future home — do not touch |
| 156890 | Attendance & participation | 5% | 0 | Course-core future home — do not touch |
| 156891 | Course evaluation | 2% | 0 | Course-core future home — do not touch |

All 8 named candidate groups are confirmed live-empty, matching the prompt's expectation exactly.

## 6. Exact live mutations performed: NONE

**No live Canvas mutation was performed this pass.** `harbor.api` has `list_assignment_groups`/`create_assignment_group`/`update_assignment_group` but **no `delete_assignment_group` function** — a real tooling gap, not a stale one (confirmed by reading the module directly). Adding it (a thin `client.delete(f"/api/v1/courses/{course_id}/assignment_groups/{group_id}")` wrapper, the same pattern as the existing `delete_assignment`/`delete_module`) was attempted through the normal reviewed Harbor path and was **blocked by this session's own safety classifier** on the edit itself, before any Canvas call was made.

Per this campaign's explicit doctrine ("Do not weaken or bypass a safety classifier") and per this prompt's own stated fallback ("If the approved production tooling cannot retire only verified-empty groups safely, leave Canvas unchanged and record the smallest tooling gap. Source cleanup should still proceed if safe"), no workaround was attempted. Live Canvas 74031 is byte-for-byte unchanged by this pass.

## 7. Post-write readback

N/A for live Canvas — no mutation occurred. Source-file edits were reviewed by re-reading the diff before commit.

## 8. Blocked tooling seam

`harbor.api.delete_assignment_group(client, course_id, group_id)` does not exist. Unlike the Architecture campaign's earlier (later-resolved) `delete_assignment` gap, this one remains open. A future pass with a human present to authorize/perform the Harbor edit (or working through whatever review path the classifier expects) should add it — same transport-only shape as `delete_module`, no course-specific policy, tests mock Canvas.

## 9. Remaining work before pure CS2 technical content is fully deployed

1. Add `harbor.api.delete_assignment_group` (blocked this pass, see §8).
2. Once available: live-retire the 8 confirmed-empty candidate groups in 74031, with immediate readback proving Semester Kickoff, Roll Call Attendance, and all course-core groups are unchanged.
3. Build the actual required CS2 weekly technical objects (Odyssey gates/checkpoints/final reflection) into the still-empty course-core groups — this is new content authorship, not cleanup, and is out of this campaign's scope.
4. A live assignment-group weight migration to the new 45/30/15/8/2 split, gated behind a before/after grade-impact preview (same invariant as Architecture's deferred renormalization) — not authorized in this slice regardless of tooling.

## 10. Final verdict

`CS2 OPTIONAL COMMONS PIVOT SLICE PARTIAL — SOURCE CLEAN / LIVE MUTATION SAFELY DEFERRED`

Source cleanup (grading model, syllabus, retired-assignment provenance markers) is complete, committed, and pushed. Live Canvas is unchanged — the 8 empty legacy assignment groups remain, correctly identified and safe to retire once the harbor tooling gap is closed, but not touched this pass since the required tooling addition was blocked by the environment's own safety classifier rather than worked around. Week 1 Semester Kickoff, Roll Call Attendance, and all course-core groups were read but not touched.
