# Prompt 030 — CS2 Optional Computing Commons Pivot: Safe First Execution Slice

Date: 2026-08-24
Owner decision: `jeremy-evert/swosu_cs_curriculum/decisions/029_fall_2026_optional_computing_commons_pivot.md`
Inventory authority: `jeremy-evert/swosu_cs_curriculum/reports/029_four_course_optional_commons_pivot_inventory.md`, including the live Canvas follow-up in §§15–16.

## Outcome

Make `computer_science_2` the first clean execution slice of the Fall 2026 optional-Commons pivot.

CS2 should become a straight-ahead Computer Science II course. Shared enrichment and accelerators remain available through optional Computing Commons, but they are not required CS2 coursework. Pair programming and Show & Tell remain available as in-class teaching practices with no assignment, reflection, receipt, online mirror, or points.

This slice is intentionally conservative in live Canvas because current production state is unusually favorable: the shared-strand/paperwork assignment groups exist but are empty, and the unwanted assignment objects were never built.

## Read first

- this repository's `AGENTS.md`, `README.md`, `docs/repo-map.md`, `docs/grading-model.md`, and current Fall 2026 planning/course-map sources;
- Decision 029 in `swosu_cs_curriculum`;
- Report 029 in `swosu_cs_curriculum`, especially §§15–16;
- the current live CS2 Canvas state through the existing approved Harbor read path immediately before any mutation.

Do not rely on the older source-only inference where Report 029's live follow-up supersedes it.

## Binding owner decisions

### Computing Commons is optional

Do not require CS2 students to complete AI Fluency/Monday Moments, Professional Minds, Success Foundations, professional-pathway/career artifacts, Local AI Lab, shared Farkle + ML, or generic accelerators merely because those resources exist.

Students may use optional Commons resources. Jeremy may naturally discuss or demonstrate them in class. No Commons completion receipt or home-course bonus-submission mechanism is authorized.

### Pair programming / Show & Tell

Pair programming and Show & Tell are in-class practices only.

Do not retain or build A3 Pair Programming Report, A4 Show-and-Tell Reflection, A7 Friday Feedback Report, or online equivalents as required CS2 assignments.

### Week 1 earned work

The live Semester Kickoff group contains real submissions. Preserve it exactly in Canvas. Do not delete, regrade, move, zero, or otherwise mutate any existing Week 1 assignment or submission in this slice.

Treat Week 1 kickoff credit as historical bonus relative to the new required-course design. This prompt does **not** authorize a live weighting change that could alter current student grades.

### Local AI Lab

Live evidence shows no Local AI Lab assignment object exists in CS2 Canvas. The experience is already effectively Commons-only in production. Do not invent, move, or delete a CS2 Local AI assignment. Update source/planning so future CS2 builds do not create one as a required assignment.

## New required CS2 grading doctrine

The future required CS2 grade should be entirely native to the course's existing disciplinary spine. Record this target model in source documentation:

| Required CS2 category | Target weight |
|---|---:|
| Weekly CS2 reinforcement / Reasoning Odyssey gates | 45% |
| Reasoning Odyssey checkpoints | 30% |
| Final reflection | 15% |
| Attendance & participation | 8% |
| Course evaluation | 2% |
| **Required-course total** | **100%** |

Week 1 Semester Kickoff credit already earned/submitted is outside that required 100% as preserved historical bonus. Do **not** change live Canvas weights in this slice merely to implement this future target. Live weight migration belongs in a later bounded deployment step after the required core assignment objects are ready and an impact preview proves no student loses credit.

Rationale: this keeps 90% of the required grade on CS2 technical work/evidence, preserves a small participation/evaluation component, and replaces the mash-in categories with the course material that was already available rather than inventing filler.

## Source-repository cleanup

Update the current CS2 source of truth so it no longer tells future builders to recreate the superseded structure.

At minimum reconcile:

- `docs/grading-model.md`;
- Fall 2026 course-design/course-map/schedule documents that explicitly require the removed strands;
- `docs/repo-map.md` or equivalent ownership guidance if it still describes shared strands as required;
- student-facing assignment indexes or navigation that make A3/A4/A7, A6 professional pathway, Monday Moment, Wacky Wednesday, Fun Friday, Local AI setup, or Farkle/ML required CS2 work.

Preserve useful historical artifacts when provenance matters, but remove them from the active required path. Prefer marking/moving to an explicit retired/legacy or sidecar location over destroying evidence if repository conventions support that. Do not delete canonical content owned by another repository.

Keep the actual CS2 disciplinary spine intact: weekly technical work, Reasoning Odyssey gates/checkpoints, final reflection, ordinary attendance/participation, and course evaluation.

Do not reshuffle the calendar just to replace removed prelude/reflection blocks. Reclaimed time belongs to the daily CS2 experience.

## Live Canvas mutation authority: narrow and evidence-gated

Target only production CS2 Canvas course `74031` on `swosu.instructure.com` through the existing approved Harbor/Course Foundry/Savnac boundary already used by this environment.

Immediately before mutation, re-read assignment groups and assignments live.

This prompt authorizes deletion/retirement of an assignment group **only when all of the following are true at mutation time**:

1. it is one of the superseded shared/paperwork categories named below;
2. the group contains zero assignment objects;
3. therefore it contains zero submissions and zero grades;
4. it is not Semester Kickoff, the default group holding Roll Call Attendance, or a CS2 course-core group;
5. a dry-run/preview identifies the exact Canvas group ID and live name before mutation.

Candidate empty groups to retire if their live state still matches Report 029:

- Monday Moment quiz;
- Wacky Wednesday reflection;
- Fun Friday reflection;
- Paired-programming report;
- Friday feedback report;
- Show-and-Tell reflection;
- Professional pathway — Week 14;
- Professional pathway — Week 15.

Do not delete or modify empty course-core groups such as Weekly reinforcement, Reasoning Odyssey checkpoints, Final reflection, Attendance, or Course evaluation; those are future homes for the pure CS2 design.

### Absolutely not authorized in this slice

- deleting or editing any Canvas assignment object;
- deleting or editing Semester Kickoff;
- changing an existing score, grade, submission, comment, rubric assessment, or due date;
- moving Roll Call Attendance;
- changing assignment-group weights in production;
- publishing new required assignments;
- changing enrollments;
- creating a Commons completion mechanism;
- touching CS1, DSCT, Architecture, or Computing Commons production Canvas;
- weakening Harbor/Savnac/Course Foundry target guards.

If the approved production tooling cannot retire only verified-empty groups safely, leave Canvas unchanged and record the smallest tooling gap. Source cleanup should still proceed if safe.

## Verification

After source edits:

- search active CS2 student-facing/planning sources for contradictory required references to the removed strands;
- verify the new required grading model totals exactly 100%;
- verify Week 1 is explicitly preserved as historical bonus rather than silently folded into the required 100%;
- verify Pair Programming/Show & Tell remain teaching practices, not assignments;
- verify Local AI and Farkle/ML are optional Commons destinations, not required CS2 obligations;
- run repository tests/builds/lint/render checks that are relevant to touched files.

After any live Canvas empty-group retirement:

- read course 74031 back through Harbor;
- verify every retired group is absent;
- verify Semester Kickoff and all of its assignment IDs remain unchanged;
- verify Roll Call Attendance remains unchanged;
- verify no assignment object was deleted or modified;
- verify submission and grade counts for all pre-existing assignments are unchanged;
- verify course-core empty groups remain available;
- capture a sanitized receipt containing IDs/names/counts only, no student PII.

## Durable report

Write:

`sidecar/reports/030_optional_commons_pivot_cs2_safe_execution.md`

Include:

1. source HEADs and Decision/Report 029 references;
2. source files changed and why;
3. before/after required grading model;
4. retired/legacy source artifacts and preserved provenance;
5. live Canvas preflight table of candidate group IDs/names/assignment counts;
6. exact live mutations performed, if any;
7. post-write readback showing no assignment/submission/grade change;
8. any blocked tooling seam;
9. remaining work needed before the pure CS2 technical content is fully deployed;
10. final verdict.

Commit and push all accepted repository changes according to repository rules. Record only a thin pointer in JTT if Jeremy-facing state changes.

## Chain-gun behavior

This is an execution slice, not a new owner-design workshop. Own routine reconnaissance, source reconciliation, tooling diagnosis, preview, verification, repair, and retry. Do not return to Jeremy for choices already resolved by Decision 029 or this prompt.

Stop only for a genuine human gate, an unexpected non-empty migration-candidate group, any evidence that a proposed mutation could affect earned student work, an unsafe/diverged repository state that cannot be reconciled without risking pre-existing work, or missing credential/production authority.

## Final verdict / sentinel

End the durable report with exactly one of:

- `CS2 OPTIONAL COMMONS PIVOT SLICE COMPLETE — SOURCE CLEAN / SAFE EMPTY-GROUP RETIREMENT VERIFIED`
- `CS2 OPTIONAL COMMONS PIVOT SLICE PARTIAL — SOURCE CLEAN / LIVE MUTATION SAFELY DEFERRED`
- `CS2 OPTIONAL COMMONS PIVOT BLOCKED — HUMAN GATE REQUIRED`

When the first or second verdict is durably committed and pushed, reply exactly:

`CS2 OPTIONAL COMMONS PIVOT SLICE COMPLETE.`
