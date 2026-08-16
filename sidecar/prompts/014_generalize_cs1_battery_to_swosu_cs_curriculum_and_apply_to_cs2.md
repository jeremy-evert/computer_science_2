# Sidecar Prompt 014 — Generalize the CS1 acceptance battery to SWOSU CS Curriculum and apply it to CS2

**Status:** OPEN  
**Owner:** Foreman  
**Mode:** inspect → parameterize → bounded Savnac proof → read back → verify  
**Related:** Prompt 011 (promotion charter); Prompt 010 (CS1 → CS2 parity); Prompt 013 (Savnac imprint/read-back)

## Problem

Course Foundry contains a useful CS1 acceptance/quality battery, but the
current scripts and zero-submission helpers encode CS1 assumptions in places
that should become reusable across SWOSU computing courses. The battery should
be composed and identified centrally without moving Course Foundry's Harbor,
Imprint, Marker, Coach, or Canvas-facing engine ownership into the curriculum
repository.

This is the first concrete application of the already-authorized promotion
charter in CS2 sidecar Prompt 011. Do not duplicate Prompt 011's charter;
apply its ownership and proof rules here.

## Mission

Take the genuinely reusable portions of the inventoried Course Foundry CS1
battery and adapt them into course-parameterized shared tooling in
`swosu_cs_curriculum`. The shared layer should make at least these values
explicit parameters rather than CS1 constants:

- course identity / Savnac course ID (CS2 is course 3 for this proof);
- course repository path;
- gate and assignment path/name patterns and any fixture-to-source mapping;
- student profile pool and the `agent-student-*` enrollment naming pattern;
- any course-specific module/layout selectors needed by a battery component.

`course_foundry` keeps owning the underlying Harbor/Imprint engine,
Savnac/Canvas-facing plumbing, and model-feedback pipeline. The shared
curriculum repository owns cross-course battery composition, parameter schemas,
course identity, and reusable acceptance policy. Do not create a parallel
deployment or feedback engine.

The parameterization must preserve the useful acceptance behavior, including
the CS1 pattern of checking real assignment/rubric material, safety-gated
Marker/Coach output, escalation behavior, Savnac layout/navigation
expectations, and the bounded zero-submission round trip. Remove hardcoded CS1
course IDs, paths, assignment labels, and lesson maps from the shared-facing
interface; retain course-specific fixtures as explicit data rather than hidden
branches.

When adding CS2 course-local wrappers for A3/A4/A6/A7 or the weekly
Wacky Wednesday/Fun Friday/Monday Moment machinery, first verify ownership.
If CS1's file is a thin wrapper into `professional_minds` or `ai_fluency`, use
the same thin-wrapper/reference pattern and the same shared source for CS2;
do not copy the pedagogical prose. CS2's Fall 2026 Monday Moment / AI-fluency
touchpoints remain on the existing shared AI Fluency I content already used by
CS1. Do not build AI Fluency II: it is Spring 2027 future work and out of scope
for this launch pass.

## Read first

Read current versions of:

- `computer_science_2/sidecar/prompts/010_steal_from_cs1_until_proven_wrong.md`,
  including its landed Odyssey-gate grading-parity sub-charter; this prompt
  depends on that work and must not duplicate it;
- `computer_science_2/sidecar/prompts/011_promote_reusable_stolen_goods_to_swosu_cs_curriculum.md`;
- `computer_science_2/sidecar/prompts/013_imprint_cs2_to_savnac_and_read_back.md`;
- CS2's Week 2 readiness assignment and 1–2 graded Week 3–14 gate sources and
  rubrics, after Prompt 010's grading work has landed;
- the Course Foundry scripts inventoried for the CS1 battery:
  `cs1_marker_battery.py`, `cs1_coach_quality_battery.py`,
  `cs1_rubric_quality_battery.py`, `cs1_escalation_ladder_battery.py`,
  `cs1_savnac_layout_and_navigation.py`,
  `scripts/zero_submission_experiment.py`,
  `scripts/run_zero_submission_queue.py`, and
  `scripts/list_zero_submission_candidates.py` when present;
- the relevant CS1 zero-submission campaign report pattern, not every report;
- `swosu_cs_curriculum/README.md`, `swosu_cs_curriculum/AGENTS.md`, and its
  current `shared/`, `courses/`, and `scripts/` layout;
- the shared `professional_minds` and `ai_fluency` source locations needed to
  distinguish wrappers from original course-local content.

Do not assume a new central location is needed if an adequate canonical
artifact already exists. Do not move or delete the CS1 originals in this
pass. Adapt-and-parameterize first, prove the CS2 application, and only then
consider retiring or thin-wrapping CS1-specific scripts as a separately
approved cleanup prompt. That cleanup is explicitly out of scope here.

## Required execution

### 1. Build the shared parameter boundary

Create or update the smallest appropriate shared-tooling surface in
`swosu_cs_curriculum`, following its repository conventions. Provide a clear
configuration/interface for course ID, repo path, gate/assignment patterns,
fixtures, module/layout selectors, and synthetic-student pool. Keep the
Course Foundry implementation as the engine dependency; do not fork it.

Document which behavior was extracted from each CS1 battery and which parts
remain Course Foundry-specific. Include a short ownership map showing why
each changed file belongs in the central curriculum repository.

### 2. Enroll the bounded synthetic pool

Using the existing Savnac-supported enrollment/account path, enroll a small
`agent-student-*` synthetic-student pool in Savnac course 3. Reconcile the
existing roster first; do not create duplicate accounts or silently replace
real people. Record account identifiers only in protected execution receipts,
not in source-controlled prompt/report prose or logs that expose credentials.

### 3. Run a small CS2 proof

This is a bounded proof, not a campaign. After Prompt 010's grading-parity
sub-charter has landed and the selected gates compile as real graded objects,
run:

1. the real CS2 Week 2 readiness assignment (20 points, real rubric); and
2. one or two of the now-graded Week 3–14 Odyssey gates, selected to exercise
   the CS2-specific gate/rubric shape.

Use the parameterized battery and the enrolled synthetic pool. Do not run the
full CS1 campaign, the overnight queue, or an unbounded all-course sweep.

### 4. Prove feedback round-trip quality

For each bounded proof item, preserve real evidence of the Marker/Coach
round-trip: submission timestamp, feedback-visible timestamp, comment content,
and the resulting read. Apply the same evidentiary standard demonstrated by
the CS1 zero-submission campaign reports: explicitly assess whether feedback
is specific to the submission and non-generic, and record a `PASS`/`FAIL` (or
an explicit `REVIEW` when evidence is insufficient) for each dimension.
Include enough source-term or criterion-linked evidence that an independent
reviewer can distinguish a real round trip from a fabricated success claim.

## Safety boundaries

- Savnac writes and the bounded synthetic-student enrollment/proof are in
  scope.
- Production SWOSU Canvas writes are explicitly out of scope.
- ZyBooks writes are explicitly out of scope.
- Do not read, echo, commit, or place credentials in source, reports, or
  receipts.
- Do not touch, stop, restart, reconfigure, drain, or inspect-mutatively the
  live `course_foundry` overnight queue process; do not write, edit, move, or
  delete its files. Read-only source inspection needed for parameterization is
  allowed.
- Do not fabricate grading data, feedback, timestamps, enrollment evidence,
  or gate readiness. If a prerequisite is not real, stop the affected proof
  and report the concrete blocker.
- Do not move/delete CS1 battery originals in this pass.
- Do not build AI Fluency II or otherwise expand this Fall 2026 proof into
  Spring 2027 strand work.

## Required report

Write:

`computer_science_2/sidecar/reports/014_generalize_cs1_battery_and_apply_to_cs2.md`

The report must include:

- Prompt 011 ownership classification and the central paths created/updated;
- the CS1 battery components inspected and the reusable behavior extracted;
- parameter/interface details and the Course Foundry ownership boundary;
- confirmation that CS1 originals were left in place;
- CS2 course 3 roster reconciliation and synthetic pool identity pattern;
- the exact bounded proof items and their source/rubric/points evidence;
- Marker/Coach timestamps, comment-content evidence, and specificity/
  non-genericness PASS/FAIL/REVIEW results;
- Savnac-only proof and explicit confirmation of no production Canvas/ZyBooks
  writes;
- validation, limitations, unresolved questions, receipt paths, and commit
  SHA(s) for every repository changed.

## Foreman acceptance

The worker does not self-certify completion. Foreman independently verifies:

1. the shared tooling is genuinely parameterized and does not hide CS1-only
   course IDs, paths, names, or lesson mappings;
2. `course_foundry` still owns the engine and Canvas-facing plumbing;
3. CS1 originals were not moved or deleted;
4. the CS2 course-3 pool and bounded proof are real and reproducible;
5. Week 2 and the selected post-010 gates are real source-backed graded
   objects with matching rubrics/points;
6. Marker/Coach evidence contains real timestamps and submission-specific,
   non-generic feedback findings;
7. no production Canvas/ZyBooks, credential, or live overnight-drain action
   occurred; and
8. the report and diffs support the ownership classification.

Only after that independent verification may Foreman move this prompt to:

`sidecar/prompts/completed/014_generalize_cs1_battery_and_apply_to_cs2.md`

## Done when

The reusable CS1 acceptance behavior has a documented, course-parameterized
home in `swosu_cs_curriculum`, the original CS1 scripts remain intact, and a
small real CS2 Savnac proof demonstrates assignment/rubric selection plus a
timestamped, submission-specific Marker/Coach round trip for Week 2 and 1–2
post-010 graded Odyssey gates, with Foreman acceptance still pending.
