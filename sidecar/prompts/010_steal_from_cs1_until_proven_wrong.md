# Sidecar Prompt 010 — Steal from CS1 until proven wrong

**Status:** OPEN
**Owner:** Foreman
**Mode:** compare, dispatch, adapt, verify

## Problem

Computer Science I has been developed farther and has accumulated useful course structure, documents, patterns, assets, and delivery machinery. Computer Science II should not independently rediscover things CS1 has already solved.

Default rule:

> **If CS1 has it, CS2 probably wants an equivalent.**

That is a presumption, not a command to clone blindly. The burden is on the worker to explain why a useful CS1 artifact or pattern should **not** have a CS2 counterpart.

## Mission

Foreman should dispatch a worker/golem to perform a deliberate CS1 → CS2 parity and scavenging pass.

Inspect the current repositories, not memory:

- `../computer_science_1/`
- this `computer_science_2/` repository

If checked out elsewhere, locate the current repos first.

The worker should inventory the **current useful surface of CS1** and compare it against CS2. Steal aggressively where the thing is genuinely useful, then adapt it so it belongs to CS2.

## What counts as worth stealing

Look beyond lesson text. Compare the useful project/course surface, including where present:

- root orientation files;
- naming conventions;
- start-here/navigation documents;
- roadmaps;
- course metadata patterns;
- assignment structure;
- lesson/module packaging;
- presentations/slides source organization;
- rubrics and assessment packaging;
- planning structure;
- reusable templates;
- validation/tests/scripts;
- student-facing navigation;
- deployment/export/import machinery;
- shared-source references;
- repository conventions that make the course easier to understand or operate.

Do **not** recursively ingest archives or sidecar/process history merely to make the inventory bigger. Inspect those only when a specific useful artifact requires provenance.

## Parity rule

For each meaningful CS1 artifact or pattern, classify it as one of:

- `COPY_ADAPT` — CS2 should have an equivalent; create/adapt it.
- `ALREADY_EQUIVALENT` — CS2 already solves the same problem adequately.
- `SHARED_UPSTREAM` — this should not be duplicated locally; CS2 should consume/reference the shared source.
- `CS1_ONLY` — genuinely specific to CS1; do not copy, and explain why.
- `STALE_OR_BAD` — present in CS1 but not worth reproducing; explain why.
- `UNCLEAR` — needs Foreman/Jeremy decision; do not guess.

The important bias is intentional: **do not classify something `CS1_ONLY` merely because the content is currently written for CS1.** Ask whether CS2 needs the same *kind of thing* with CS2 content.

## Known comparison clues

Do not treat this list as exhaustive, but current GitHub inventory shows CS1 has structural artifacts such as:

- `NAMING.md`
- `ROADMAP.md`
- `START_HERE.md`
- `presentations/`

CS2 currently does not visibly have direct equivalents for all of those. Inspect them before deciding whether and how CS2 should gain equivalents.

## Scope discipline

This prompt is about reusing solved patterns, not redesigning CS2 from CS1.

Preserve CS2-specific truth, especially:

- CS2's own capability progression;
- Reasoning Odyssey as the current technical spine;
- current no-required-textbook decision;
- shared ownership of Week 1 / Week 2 / other explicitly shared material;
- current grading and deployment uncertainties rather than inventing answers.

Never overwrite a stronger CS2 design merely to make the repositories symmetrical.

## Sharpened sub-charter: Week 3–14 Odyssey gate grading parity (added 2026-08-15, Jeremy's live directive)

The live finding to resolve is specific: CS2's Week 3–14 Odyssey gate
assignments currently compile as `grading=not_graded, points=None` (verified
against current source with `course_foundry.cs2_dry_run`). CS1's equivalent
weekly gate is a real graded object: the CS1 grading model makes the weekly
reinforcement assignment 25% of the course grade, with points attached and a
rubric-backed submission shape. This is a real CS2 grading/deployment gap, not
merely a documentation difference.

The implementing worker must adapt CS1's proven *weekly-gate grading shape* to
CS2's own gate content and week structure. Preserve the useful shape—explicit
points possible, an appropriate submission type, and rubric criteria that make
the required evidence gradable—but write CS2-native criteria for CS2's
object-oriented, GUI, data-visualization, collaboration, and other actual
technical work. Do not copy CS1's exact gate numbers or week mapping blindly:
CS2 has GUI/data-visualization weeks without a direct CS1 counterpart, and
Weeks 15–17 currently have no gate. Preserve the distinction between weekly
gates and the larger Reasoning Odyssey checkpoints at Weeks 6/9/14.

At the same time, Jeremy's default for the surrounding course design is
deliberate CS1 parity, not reinvention. Reproduce CS1's weekly cadence and
grading categories/percentages nearly verbatim as the starting point for
CS2: Semester kickoff 5%; Monday Moment quiz 5%; Wacky Wednesday reflection
5%; Fun Friday reflection 5%; paired-programming report A3 5%; Friday
feedback report A7 5%; Show-and-Tell reflection A4 5%; weekly reinforcement
assignment 25%; Reasoning Odyssey checkpoints (Weeks 6/9/14) 15%; final
reflection paper A5 8%; professional-pathway Week 14 and Week 15 updates A6
5% + 5%; attendance and participation 5%; and course evaluation 2%. Do not
silently omit or reweight one of these categories. If CS2's weeks or calendar
require a narrow deviation, document that deviation and its consequence.
The gate's points and rubric details must still be CS2-native rather than an
unexplained wholesale import of CS1's numeric object map.

The worker must produce a coherent, explicit CS2 weights table in
`computer_science_2/docs/grading-model.md`, including how each category maps
to Canvas/Savnac objects and which CS2 weeks are graded. If the resulting
total or split materially changes what students' grades depend on, flag that
for Foreman/Jeremy sign-off instead of silently resolving it. Foreman will
route a genuine ambiguity through `jeremy_task_tracking/questions/`; this
worker must not write there.

For A3, A4, A6, and A7, inspect the corresponding CS1 files before creating
CS2 equivalents. If the pedagogical source is actually in the shared
`professional_minds` or `ai_fluency` repository and the course-local CS1 file
is a wrapper/reference, make the CS2 file the same kind of thin wrapper into
that same shared source. Do not duplicate shared strand prose merely because
CS1 has a local filename. Likewise, CS2's Monday Moment / AI-fluency
touchpoints must continue using the existing shared AI Fluency I content used
by CS1. AI Fluency II is Spring 2027 future work and is explicitly out of
scope for this Fall 2026 CS2 launch pass; do not build it now.

All constraints in this prompt remain in force for this sub-charter:
Savnac-only work where deployment is explicitly authorized, no fabrication,
no production Canvas or ZyBooks writes, no credential handling, and no
writing to Foreman's question-tracking surface.

## Worker proof

The worker must report:

1. the CS1 inventory examined;
2. a parity table with every meaningful item classified;
3. each CS2 artifact created or adapted;
4. each CS1 item deliberately not copied and why;
5. any reusable cross-course item flagged for central promotion;
6. validation performed;
7. commit SHA(s).

Run at minimum:

- `git diff --check`;
- repository-specific validation already available;
- checks for accidental CS1 course codes, assignment names, dates, grading rules, or other residue in newly adapted CS2 files.

Do not write to Canvas, Savnac, or production student systems.

## Required report

Write:

`sidecar/reports/010_steal_from_cs1_until_proven_wrong.md`

## Foreman acceptance

The worker does not close this prompt.

Foreman reviews the parity table, diff, and proof. Foreman should be suspicious of unexplained gaps: when CS1 has a useful thing and CS2 does not, "we did not copy it" is not enough; the report needs a reason.

After Foreman accepts the work, move this prompt to:

`sidecar/prompts/completed/010_steal_from_cs1_until_proven_wrong.md`

## Done when

Foreman can explain, for the useful current surface of CS1, either **where the CS2 equivalent is** or **why CS2 intentionally does not need one**, and the high-value reusable pieces have actually been adapted rather than merely listed.
