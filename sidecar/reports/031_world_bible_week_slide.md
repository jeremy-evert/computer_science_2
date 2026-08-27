# CS2 World Bible week-slide — report

Owner decision (2026-08-26, verbatim): "I think the right move to do would
be to slip everything one week back and if we have to we take a week of
activity off the entire schedule as opposed to just cramming everything in
their tighter." Follow-on: dogfood this in CS2 only — do not extend World
Bible to CS1/DSCT/Architecture this pass.

## What moved

The Reasoning Odyssey chain (World Bible intro/test/collaborate, and
everything after it) slides one week later:

- World Bible intro ("Found Your World") — Week 2 → **Week 3**.
- Test predicted object — Week 3 → **Week 4**.
- Collaborate/refactor — Week 4 → **Week 5**.
- Every remaining active week (old Weeks 5–14) slides the same one week,
  landing at **Weeks 6–15**.
- **Week 15** (previously an explicit no-required-content buffer, titled
  "Buffer: Asynchronous, Light, Self-Contained") absorbs the last slid week
  (old Week 14 — Professional Workflow Receipt / Checkpoint 3) cleanly.
  Nothing was cut; the buffer is what got spent, per the owner's own
  fallback instruction.
- **Week 2** keeps its existing Local AI Lab readiness content untouched —
  that activity never moved and the World Bible seed no longer shares the
  week with it.
- **Weeks 16 (Farkle/ML) and 17 (finals)** are untouched — fixed calendar
  positions, not part of the slide.

The three larger checkpoints (Contract/Swap, Compact GUI, Workflow Receipt)
move from old Weeks 6/9/14 to **Weeks 7/10/15**.

## Files changed

- `assignments/odyssey_gates/week-02.md` through `week-14.md` → shifted to
  `week-03.md` through `week-15.md` (13-file content shift via `git mv` in
  reverse order, each file's internal "Week N" title and prose
  cross-references bumped in place — not just the filename).
- `rubrics/odyssey_gates/week-02_rubric.md` through `week-14_rubric.md` →
  same shift, `week-03_rubric.md` through `week-15_rubric.md`, including
  the repeated boilerplate footer ("Week 02 is ungraded setup...") and the
  "larger Weeks 6/9/14 checkpoints" cross-reference in the two
  synthesis-checkpoint rubrics (now "Weeks 7/10/15").
- `assignments/A2-coding-odyssey-project.md` — intro paragraph and the
  full "Growth path" week-range table bumped.
- `assignments/A1-weekly-coding-practice.md`, `docs/curriculum/judgment_toolkit.md`,
  `docs/course-ethos.md`, `docs/syllabus.md` (including its full Week 1–17
  course-schedule table), `docs/curriculum/fall-2026-starter-reading-list.md`
  (full week-by-week reading shelf, all 12 section headers plus internal
  cross-references), `planning/fall-2026-course-design.md` (full semester
  spine table plus prose), `planning/week-02-local-ai-lab-integration.md`,
  `presentations/beamer/orientation/welcome-to-the-odyssey.tex` (student
  orientation deck — checkpoint list, weekly-gate range, "pick your world"
  line), `README.md`, `ROADMAP.md`, `NAMING.md`, `templates/T5-start-here.md`
  — all had "Week N" cross-references to this content that needed the same
  bump; found by a full-repo grep for Reasoning-Odyssey/World-Bible-adjacent
  files followed by targeted week-number checks, not just the files the
  read-only recon pass had already flagged.

Every stale "Week 15 is asynchronous/light/buffer" claim was removed or
corrected (`docs/course-ethos.md`, `docs/syllabus.md`'s schedule table,
`assignments/A1-weekly-coding-practice.md`, `planning/fall-2026-course-design.md`'s
spine table) since Week 15 no longer is a buffer — it now holds real,
graded checkpoint content.

## Firewall preserved

No `sidecar/worlds/` internal lore (character names, world-internal detail)
was added anywhere during this pass — this was a pure renumbering and
cross-reference pass, not new content authoring.

## Explicitly NOT touched

- `assignments/week-02-local-ai-readiness.md` — the separate Week 2 Local
  AI Lab gate, unrelated to World Bible, confirmed untouched (`git status`
  shows no change to this file).
- `docs/syllabus.md` line "Professional-pathway updates in Weeks 14–15" —
  references A6, which was already retired in Decision 029
  (2026-08-25, `sidecar/reports/030_optional_commons_pivot_cs2_safe_execution.md`)
  before this pass. Left alone: fixing a reference to already-retired
  content is a separate cleanup, out of this directive's scope.
- `sidecar/prompts/` and `sidecar/reports/` (except this new report) —
  these are append-only process history per this repo's own convention
  (`NAMING.md`: "completed prompts move only after Foreman accepts the
  work"). Editing historical week numbers there would falsify the record
  of what was actually built when.
- CS1, DSCT, Architecture — untouched, per explicit owner instruction to
  dogfood in CS2 only this pass.

## Important finding — flag for the owner, not fixed here

**The old week numbers are already live on real Canvas**, not just staged
in source. `sidecar/reports/cs2_pure_course_deployment_manifest.md` and
`sidecar/reports/cs2_final_production_closeout.md` show a separate,
already-executed deployment pass (2026-08-25, commit `bc98456b`) put all
14 Reasoning Odyssey gates live under their **old** week numbers and
titles (e.g. Canvas assignment group `156885`/`156886`, "Week 3 —
Cohesive Object Boundary" etc.). This pass only touched source — no Canvas
call was made, per the directive's explicit source-only boundary — so
**Canvas currently shows the old week numbers while the source repository
now shows the new ones.** A follow-up deployment pass (rename the live
Canvas assignment titles/positions, and decide what happens to
already-existing student submissions on the old-numbered objects, if any
exist yet this early in the semester) is needed before the live course
matches this source update. This is a real gap the read-only recon pass
did not know about (it was told nothing was deployed) and is squarely the
owner's call on timing/risk, not something to auto-fix in this pass.

## Verdict

`CS2 WORLD BIBLE WEEK-SLIDE COMPLETE IN SOURCE — CS2 ONLY, CANVAS NOT YET RECONCILED`
