# Sidecar Report 010 — CS1 parity and CS2 grading parity

**Prompt:** `sidecar/prompts/010_steal_from_cs1_until_proven_wrong.md`
**Branch:** `golem/cs2-010-grading-parity`
**Implementation commit:** `f855dfb10efd7ff0e9b6bf253071e36c6d16711e`

## Summary

The CS2 source repository now has the high-value structural surface that CS1
had solved: root navigation and naming guidance, a living roadmap, a repo
ownership map, presentation-source organization, orientation templates, and
course-native A3/A4/A6/A7 artifacts. The Week 3–14 Odyssey evidence now has
explicit points, submission shape, category, and CS2-specific rubric scoring.
The grading model reproduces the directed 100% category split while keeping
Weeks 6/9/14 visibly larger checkpoints and not inventing technical gates for
Weeks 15–17.

## CS1 inventory and parity table

The inventory examined current CS1 root files (`NAMING.md`, `ROADMAP.md`,
`START_HERE.md`, `README.md`), `docs/repo-map.md`, `docs/course-ethos.md`,
`docs/grading-model.md`, `assignments/`, `rubrics/odyssey_gates/`,
`templates/T4-module-overview.md`, `templates/T5-start-here.md`,
`presentations/beamer/README.md`, current planning/lesson organization, and
the Monday Moment/shared-source pointers. The four requested CS1 assignment
files were read in full before their CS2 counterparts were written.

| Meaningful CS1 item or pattern | Classification | CS2 result / reason |
|---|---|---|
| Root README/course map | COPY_ADAPT | Updated CS2 README with its own Odyssey spine and boundaries |
| `NAMING.md` | COPY_ADAPT | Added CS2 naming contract |
| `ROADMAP.md` | COPY_ADAPT | Added CS2 status/open-work roadmap |
| `START_HERE.md` | COPY_ADAPT | Added CS2 reading order and ownership boundaries |
| `docs/repo-map.md` | COPY_ADAPT | Added CS2 cross-repository ownership map |
| Beamer presentation README/source convention | COPY_ADAPT | Added CS2 presentation source README; later decks remain deliberate work |
| T4 module overview template | COPY_ADAPT | Added CS2 template with CS2 weekly rhythm |
| T5 start-here template | COPY_ADAPT | Added CS2 orientation template and assignment map |
| A3 paired-programming report | COPY_ADAPT | Added CS2-native object/design/test contribution report |
| A4 Show-and-Tell reflection | COPY_ADAPT | Added CS2-native 10-point four-question journal |
| A6 professional pathway artifacts | COPY_ADAPT | Added CS2 Week 14/15 artifact and reasoning requirements |
| A7 Friday feedback report | COPY_ADAPT | Added CS2-native feedback evidence report |
| Named A1/A2/A5 assignment structure | ALREADY_EQUIVALENT | CS2 already had the relevant templates; no duplicate renamed copies |
| Weekly planning/lesson/module organization | ALREADY_EQUIVALENT | Existing CS2 `planning/`, `lessons/`, and week files already provide it |
| Odyssey gate/rubric paired packaging | ALREADY_EQUIVALENT | Existing CS2 gate and rubric directories retained and strengthened |
| Course metadata | ALREADY_EQUIVALENT | Existing CS2 `course_metadata.yaml` is the authoritative CS2 record |
| Course ethos and curriculum sequence | ALREADY_EQUIVALENT | Existing CS2 documents already express the CS2 capability progression |
| Monday Moment local pointer/template | ALREADY_EQUIVALENT | Existing CS2 pointer/template retained; its ownership wording remains shared-source work |
| Historical archive organization | ALREADY_EQUIVALENT | CS2 already has its own archive snapshots; no archive cloning was useful |
| Week 1 kickoff bodies | SHARED_UPSTREAM | Remain in `semester_kickoff_week` |
| Week 2 local-AI lab bodies | SHARED_UPSTREAM | Remain in `local_ai_lab_setup`/`windows_classroom`; CS2 keeps a wrapper |
| Monday Moment lesson bodies | SHARED_UPSTREAM | Continue to use `ai_fluency/ai_i`; no AI Fluency II created |
| Professional Minds readings/slides/rubrics | SHARED_UPSTREAM | Continue to use `professional_minds`; no local strand duplication |
| CS1 beginner technical lesson sequence | CS1_ONLY | CS2's object/data/GUI/visualization progression is genuinely different |
| CS1 course code, section, catalog facts, and dates | CS1_ONLY | CS2 retains its own COMSC-1053 metadata and calendar |
| CS1-specific assignment examples and beginner-world prompts | CS1_ONLY | Would misrepresent CS2 technical evidence |
| CS1-specific Farkle/ML and intro-course handoffs | CS1_ONLY | CS2 uses its shared applied Week 16 reservation and own spine |
| CS1 archive snapshots and historical external links | STALE_OR_BAD | Provenance is course-specific and bulk copying would add noise/risk |
| CS1 compiled deck intermediates | STALE_OR_BAD | Build artifacts are not a reusable source convention; CS2 README explicitly excludes them |
| Exact CS1 Canvas/Savnac object IDs and due-date map | UNCLEAR | Deployment/import ownership and live mapping remain outside this source-only pass |

**Counts:** `COPY_ADAPT` 13; `ALREADY_EQUIVALENT` 7; `SHARED_UPSTREAM` 4;
`CS1_ONLY` 4; `STALE_OR_BAD` 2; `UNCLEAR` 1. Total: 31 inventory rows.

## Grading-parity implementation

`docs/grading-model.md` now contains this exact 100% table:

| Category | Weight |
|---|---:|
| Semester kickoff week | 5% |
| Monday Moment quiz | 5% |
| Wacky Wednesday reflection | 5% |
| Fun Friday reflection | 5% |
| Paired-programming report (A3) | 5% |
| Friday feedback report (A7) | 5% |
| Show-and-Tell reflection (A4) | 5% |
| Weekly reinforcement assignment | 25% |
| Reasoning Odyssey checkpoints (Weeks 6/9/14) | 15% |
| Final reflection paper (A5) | 8% |
| Professional pathway — Week 14 update (A6) | 5% |
| Professional pathway — Week 15 submission (A6) | 5% |
| Attendance & participation | 5% |
| Course evaluation | 2% |
| **Total** | **100%** |

Weeks 3–5, 7–8, and 10–13 are weekly reinforcement gates at 25 points
each. Week 6 is a 40-point checkpoint, Week 9 a 50-point checkpoint, and
Week 14 a 60-point checkpoint; all three remain in the 15% checkpoint group.
The point sizes express the larger evidence packages and do not add weight
beyond the table. Every gate uses text explanation plus code/evidence (or a
repository link) and a matching CS2 rubric. Week 2 remains optional setup;
Weeks 15–17 receive no fabricated technical gate.

## A3/A4/A6/A7 source determination

- **A3:** original CS1 course-local prose, not a shared-repository wrapper.
  Created a CS2 version centered on object design, tests, traces, contribution
  evidence, and AI accountability.
- **A4:** original CS1 course-local prose, not a shared-repository wrapper.
  Created the same four-question/10-point shape with CS2-native evidence
  examples and distinctness from A7 and Professional Minds reflections.
- **A6:** original course-local assessment policy with a pointer to shared
  Week-1 baseline artifacts, not a thin wrapper. Created a CS2 version for the
  Week-14 update and asynchronous Week-15 completion; did not duplicate the
  shared baseline handouts.
- **A7:** original CS1 course-local prose, not a shared-repository wrapper.
  Created a CS2 version grading the specificity and reasoning of feedback on
  CS2 demonstrations.

The local Monday Moment README/template were not replaced with course-local
lesson bodies. CS2 continues to reference the existing AI Fluency I source;
AI Fluency II remains Spring 2027 future work and is out of scope.

## Deliberate non-copies and promotion candidates

I did not copy CS1's beginner lesson prose, course-specific dates/IDs,
historical archives, compiled intermediates, or exact Canvas object map. I
also did not copy Professional Minds or AI Fluency bodies, because their
repositories are the shared upstream owners. The reusable candidates for
later central promotion are the naming contract, orientation-template shape,
weekly evidence/point declaration pattern, and the distinction between
recurring reports and technical Odyssey checkpoints.

## Candidate Jeremy question

The model uses mixed point totals (40/50/60) inside the 15% checkpoint group
so the larger Weeks 6/9/14 evidence packages can be explicit without changing
the category split. Before deployment, Foreman should confirm that the
operational importer/Canvas group behavior handles that mapping as intended.
If it does not, that would materially change how grade dependence is
distributed among those three checkpoints and should be routed as a Jeremy
question. No question-tracking repository was changed here.

## Validation

- `git diff --check` — passed before the implementation commit.
- Weight-table arithmetic — verified to sum to 100%.
- Gate declaration scan — verified explicit grading declarations for every
  Week 3–14 file.
- CS1 residue scan — no accidental CS1 course code/name/date or assignment
  residue in newly adapted CS2 files; the intentional shared-boundary and
  historical references are documented above.
- `make task-check` — unavailable: `/bin/bash: line 1: make: command not found`.
- `make check` — unavailable: `/bin/bash: line 1: make: command not found`.
- No Python test suite exists in this content repository; no test suite was
  invented or reported green.
- No Canvas, Savnac, ZyBooks, `course_foundry`, or production-system writes
  were performed.

## Foreman verification (2026-08-15/16)

Independently reviewed the full diff (37 files, `NAMING.md`/`README.md`/
`ROADMAP.md`/`START_HERE.md`/`docs/repo-map.md`/templates, the grading model,
all 12 Week 3–14 gate+rubric point declarations, and A3/A4/A6/A7). No CS1
course-code/name/date residue found in course content (only in this report's
own analysis prose, as expected). Confirmed via `git status` in
`computer_science_1`, `professional_minds`, `ai_fluency`, `swosu_cs_curriculum`,
`jeremy_task_tracking`, and `course_foundry` that this dispatch wrote only
inside `computer_science_2/` and left `course_foundry`'s live overnight
zero-submission drain untouched.

**Candidate Jeremy question resolved by direct live precedent, not escalated:**
checked Savnac course 1 (CS1) live via `GET /api/v1/courses/1/assignment_groups`
— CS1's own "Coding Odyssey checkpoints" group is already deployed at
`group_weight=15.0` today, proving Canvas/Savnac's weighted-group mechanism
already handles a group whose member objects carry different point totals
(standard Canvas behavior: a weighted group's contribution to the final grade
is fixed at its `group_weight`; individual assignment points only set
relative weight *within* the group). CS2's proposed 40/50/60-point Weeks
6/9/14 checkpoints inside its own 15% group will behave identically once
deployed the same way. No implementation or policy risk found; no
`jeremy_task_tracking/questions/` entry needed for this item.

**Verdict: ACCEPT.** Merging `golem/cs2-010-grading-parity` to `main` and
moving `sidecar/prompts/010_steal_from_cs1_until_proven_wrong.md` to
`sidecar/prompts/completed/`.

## Traceability and handoff

The implementation is committed as `f855dfb10efd7ff0e9b6bf253071e36c6d16711e`.
This report is the requested source-repository receipt and is committed
separately after the implementation. `AGENTS.md` was not created or updated.
The next action is Foreman review of this report, the parity diff, and the
checkpoint-group mapping; no next prompt was executed or drafted here.
