# COMSC-1053 — Grading Model (Fall 2026 source model)

**Status update (Prompt 030, 2026-08-25 — Decision 029 optional-Commons pivot):** the shared/paperwork categories below (Monday Moment quiz, Wacky Wednesday, Fun Friday, Paired-programming report/A3, Friday feedback report/A7, Show-and-Tell reflection/A4, Professional Pathway/A6) are **retired from the required CS2 grade**, per `swosu_cs_curriculum/decisions/029_fall_2026_optional_computing_commons_pivot.md`. Pair programming and Show & Tell remain in-class teaching practices only — no assignment, reflection, receipt, or online mirror. AI Fluency/Monday Moment and Professional Minds content remains available to students only through optional Computing Commons (course `24298`), not as required CS2 coursework. See "New required grading model" below for the current target. The original full-cadence model is preserved further down this file as historical/superseded context, not as the active design.

## New required grading model (current target, Prompt 030)

| Required CS2 category | Weight |
|---|---:|
| Weekly CS2 reinforcement / Reasoning Odyssey gates | 45% |
| Reasoning Odyssey checkpoints | 30% |
| Final reflection | 15% |
| Attendance & participation | 8% |
| Course evaluation | 2% |
| **Required-course total** | **100%** |

Week 1 Semester Kickoff credit already earned/submitted by enrolled students is preserved but sits **outside** this required 100% as historical bonus credit — it is not clawed back, regraded, or folded into the new split. No live Canvas weight change has been made to implement this target yet; live weight migration is a later, separately gated deployment step requiring a before/after impact preview that proves no enrolled student loses credit (see `sidecar/reports/030_optional_commons_pivot_cs2_safe_execution.md`).

This keeps 90% of the required grade on native CS2 technical work/evidence (weekly gates + checkpoints), preserves a small participation/evaluation component, and replaces the retired mash-in categories with the course's own material rather than inventing filler to hit a target count.

## Superseded: original full-cadence model (historical, not the active design)

This was the CS2 source model prior to the Decision 029 pivot. It adopted the established weekly cadence and category split shared across all four courses. Preserved here for provenance; do not build from this table going forward.

| Category | Weight | Canvas/Savnac object shape | Graded weeks |
|---|---:|---|---|
| Semester kickoff week | 5% | Shared kickoff assignment group / exit-ticket objects | Week 1 |
| Monday Moment quiz | 5% | Short quiz or text-entry object using shared AI Fluency I content | Weekly touchpoint, excluding shared setup exceptions |
| Wacky Wednesday reflection | 5% | Professional Minds reflection object | Weekly Professional Minds weeks |
| Fun Friday reflection | 5% | Professional Minds reflection object | Weekly Professional Minds weeks |
| Paired-programming report (A3) | 5% | Individual text-entry/upload report with rubric | Weekly paired-work weeks |
| Friday feedback report (A7) | 5% | Individual text-entry/upload report with rubric | Weekly Show-and-Tell weeks |
| Show-and-Tell reflection (A4) | 5% | Individual 10-point journal/text-entry object with rubric | Weekly Show-and-Tell weeks |
| Weekly reinforcement assignment | 25% | Odyssey gate objects, 25 points each, with gate rubric | Weeks 3–5, 7–8, 10–13 |
| Reasoning Odyssey checkpoints | 15% | Larger Odyssey checkpoint objects with checkpoint rubrics | Weeks 6, 9, 14 |
| Final reflection paper (A5) | 8% | Final text-entry/upload reflection object | Week 17 finals period |
| Professional pathway — Week 14 update (A6) | 5% | Update/changelog upload with rubric | Week 14 |
| Professional pathway — Week 15 submission (A6) | 5% | Portfolio package upload with rubric | Week 15, asynchronous |
| Attendance & participation | 5% | Instructor-entered attendance/participation group | Course cadence |
| Course evaluation | 2% | End-of-term completion object | End of term |
| **Total** | **100%** | | |

The percentages above were intentionally explicit: no category was silently omitted or folded into another. This table is retained for historical reference only — the "New required grading model" section above is the current target.

## Odyssey gate grading shape

Every active Week 3–14 Odyssey file names its submission shape, points, and
category. A weekly gate is a small, gradable evidence package rather than a
second problem-set track:

- **Weekly gates:** Weeks 3–5, 7–8, and 10–13 are 25 points each in the
  Weekly reinforcement assignment group. Submit a text explanation plus
  runnable code, test/trace, diff, or other evidence named by that week's
  technical brief. The matching rubric uses four CS2-native dimensions:
  world-fit technical change, evidence of behavior, plain-language reasoning,
  and AI accountability when AI was used.
- **Larger checkpoints:** Week 6 (40 points, baby-project contract and swap),
  Week 9 (50 points, GUI/model or data-story synthesis), and Week 14 (60
  points, professional workflow receipt and full trail debrief) belong to the
  Reasoning Odyssey checkpoints group. Their points are not additional
  percentage weight beyond the 15% row; the group controls the course weight.
  Their larger evidence packages are deliberately distinct from a weekly
  gate.
- **No fabricated gates:** Week 2 is optional setup; Week 15 has no technical
  gate; Week 16 is a shared Farkle/ML applied experience with no CS2 Odyssey
  gate; Week 17 is reflection and closure. Existing Week 16 reservation text
  stays retired/ungraded.

### Weekly gate evidence pattern

The student submits the week's actual technical work, not an unrelated essay:

1. the world-fit implementation or design change;
2. a focused run, test, trace, visualization, GUI/model demonstration, or
   recovery receipt appropriate to that week;
3. a short explanation of the design choice and trade-off; and
4. the World Bible entry plus AI proposal/diff/test/read/reason/accept-or-
   reject evidence when AI helped.

The rubric criteria are adapted per week. For example, Week 9 requires a
meaningful callback and independently tested model behavior, Week 10 requires
a real data question and defensible visualization, and Week 14 requires
history/recovery/collaboration evidence. No gate rewards a GUI, hierarchy,
recursion, container, or algorithm merely for existing when that week's
content does not call for it.

## Shared-strand boundaries

Monday Moment objects use the existing shared AI Fluency I content in
`../ai_fluency/ai_i/`; this course does not create an AI Fluency II strand.
Professional Minds reflection objects point to content owned in
`../professional_minds/`. Week 1 and Week 2 use their shared owners as
described in `docs/repo-map.md`.

## Deliberate limits and candidate question

This source model makes a deliberate points choice for the three checkpoint
objects (40/50/60) so their evidence packages are larger while the group
weight remains 15%. Canvas group weighting, late/drop rules, and whether the
course's operational importer accepts mixed point values inside a weighted
group must be confirmed before deployment. If that implementation detail
materially changes how students' grades depend on Week 6, Week 9, or Week 14,
it is a candidate Jeremy question for Foreman to route; this pass does not
write that question-tracking entry or silently alter the 100% split.
