# CS2 deterministic deployment manifest — required graded objects

**STATUS: DEPLOYED 2026-08-25 (final production closeout, owner commit `bc98456b798451c91b3c72f167dc78545e36c85b`).** All 14 rows below now exist live in Canvas — see `sidecar/reports/cs2_final_production_closeout.md` for exact assignment IDs, readback verification, and the grade-impact preview. `create_assignment` was re-tested at the start of that closeout pass and was no longer blocked (the block encountered in the earlier recovery/landing passes was session-specific, not permanent). This file is preserved as the original planning manifest / historical record of what was queued and why.

Campaign: Olivia's `owner_20260825_cs2_dsct_pure_course_recovery_map_april.md`. This is the exact, source-verified list of live Canvas objects that were needed to complete the pure-CS2 required grade.

Course: `74031`. Existing live assignment groups (verified live 2026-08-25, all currently empty except Assignments/Semester kickoff week — see `sidecar/reports/030_optional_commons_pivot_cs2_safe_execution.md`): `156885` Weekly reinforcement assignment (25% live, target 45%), `156886` Reasoning Odyssey checkpoints (15% live, target 30%), `156887` Final reflection paper (8% live, target 15%), `156890` Attendance & participation (5% live, target 8%), `156891` Course evaluation (2%, already correct). **Group weight changes are explicitly deferred** — not part of this manifest's authorization — until the objects below exist and a before/after grade-impact preview is computed.

Source verified against the actual `assignments/odyssey_gates/week-NN.md` + `rubrics/odyssey_gates/week-NN_rubric.md` files, not assumed from the grading-model doc — every points value below is read directly from the live rubric file's own `**Score: N points.**` line.

| Week | Source | Canvas title | Group (target) | Points | Submission type | Rubric source | Class |
|---|---|---|---|---:|---|---|---|
| 2 | `assignments/odyssey_gates/week-02.md` | Reasoning Odyssey Gate — Week 2 — Light World Seed | n/a — **optional_no_gate, do not deploy as graded** | 0 | — | — | optional/ungraded |
| 3 | `assignments/odyssey_gates/week-03.md` | Reasoning Odyssey Gate — Week 3 — Cohesive Object Boundary (S01) | 156885 Weekly reinforcement | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-03_rubric.md` | gate |
| 4 | `assignments/odyssey_gates/week-04.md` | Reasoning Odyssey Gate — Week 4 — Collaborating Objects and Invariant (S01/S08) | 156885 | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-04_rubric.md` | gate |
| 5 | `assignments/odyssey_gates/week-05.md` | Reasoning Odyssey Gate — Week 5 — Earned Substitution (S02) | 156885 | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-05_rubric.md` | gate |
| 6 | `assignments/odyssey_gates/week-06.md` | Reasoning Odyssey Gate — Week 6 — Contract and Swap (S03/S08) | 156886 Reasoning Odyssey checkpoints | 40 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-06_rubric.md` | **checkpoint** (largest-tier, cross-referenced by weeks 12/13 as one of "the larger Weeks 6/9/14 checkpoints") |
| 7 | `assignments/odyssey_gates/week-07.md` | Reasoning Odyssey Gate — Week 7 — World-Fit Data Abstraction (S05) | 156885 | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-07_rubric.md` | gate |
| 8 | `assignments/odyssey_gates/week-08.md` | Reasoning Odyssey Gate — Week 8 — Search/Order Tradeoff (S05/S06) | 156885 | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-08_rubric.md` | gate |
| 9 | `assignments/odyssey_gates/week-09.md` | Reasoning Odyssey Gate — Week 9 — Compact GUI over Tested Model (S04) | 156886 | 50 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-09_rubric.md` | **checkpoint** |
| 10 | `assignments/odyssey_gates/week-10.md` | Reasoning Odyssey Gate — Week 10 — Honest Visualization from Project Data (S09/S06/S08) | 156885 | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-10_rubric.md` | gate |
| 11 | `assignments/odyssey_gates/week-11.md` | Reasoning Odyssey Gate — Week 11 — Data Storytelling / Flex Clinic (S09 + S07) | 156885 | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-11_rubric.md` | gate |
| 12 | `assignments/odyssey_gates/week-12.md` | Reasoning Odyssey Synthesis Checkpoint — Week 12 — Stabilization and Peer-Review Preparation (S08) | 156885 | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-12_rubric.md` | gate (titled "Synthesis Checkpoint" narratively; 25 pts, same tier as an ordinary gate — do not deploy into the 156886 checkpoints group) |
| 13 | `assignments/odyssey_gates/week-13.md` | Reasoning Odyssey Synthesis Checkpoint — Week 13 — Culmination Design Review (S01–S08) | 156885 | 25 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-13_rubric.md` | gate (same note as Week 12) |
| 14 | `assignments/odyssey_gates/week-14.md` | Reasoning Odyssey Gate — Week 14 — Professional Workflow Receipt (S08) | 156886 | 60 | online_text_entry + upload/repo link | `rubrics/odyssey_gates/week-14_rubric.md` | **checkpoint** |
| 15 | — | — | n/a | — | — | — | no gate exists or is planned (asynchronous buffer week, matches DSCT's Week 15) |
| 16 | `assignments/W16-farkle-ml-design-receipt.md`, `lessons/week-16-farkle-ml-experiment-bench.md` | Week 16 — Farkle + Machine Learning Evidence Receipt | n/a — ungraded/participation, shared-strand, not a Decision-029-retired object | 0 | online_text_entry + upload/repo link | none dedicated; the receipt template itself is the structure | **CORRECTED 2026-08-25 (semester-landing pass): this row was previously and wrongly marked "already live" — live `list_assignments(74031)` confirms no Farkle/W16 object exists in Canvas at all. Queued for deployment like every other row.** |
| 17 | `assignments/A5-final-reflection.md` | A5 — Final Reflection and Closure | 156887 Final reflection paper | TBD at deployment (weight-group controlled, not a fixed point target in source) | online_text_entry + upload | none dedicated found; uses the 5-prompt selection rubric in the assignment body itself | final |

Also required, not authored as odyssey-gate content (course-core, unrelated to Decision 029): Attendance & participation (156890, instructor-entered, no student submission object) and Course evaluation (156891, typically an institutional external-tool/LTI object, not authored in this repo).

## Totals check

Weekly reinforcement group (target 45%): 9 gates × 25 pts (weeks 3,4,5,7,8,10,11,12,13) = 225 raw points, group-weighted to 45% regardless of raw total.
Checkpoints group (target 30%): 40 + 50 + 60 = 150 raw points (weeks 6, 9, 14), group-weighted to 30%.
Final reflection (target 15%): 1 object (week 17 / A5).
Attendance (8%) + Course evaluation (2%) are non-authored administrative categories.

## Not part of this manifest (explicitly retired, do not deploy)

A3 (Paired Programming Report), A4 (Show and Tell Reflection), A7 (Friday Feedback Report), A6 (Professional Pathway) — retired per Decision 029, marked in place in their own source files (`assignments/A3-pair-programming.md` etc.), not part of the required grade. Monday Moment / Professional Minds objects — optional Computing Commons enrichment, no CS2-side Canvas object should be created for them.

## Deployment notes for the later mechanical pass

- Every gate/checkpoint row's `submission_types` should be `["online_text_entry", "online_upload"]` per this repo's existing convention (confirmed in every `assignments/odyssey_gates/week-NN.md`'s own "Grading" line).
- Due dates are not source-pinned in this repo (no explicit calendar date found in the gate files) — the later deployment pass should derive them from the live course calendar / syllabus schedule, not invent one here.
- Do not change the 5 existing group weights until every row above is deployed and a grade-impact preview is computed (Week 1 Kickoff credit must be provably preserved).
