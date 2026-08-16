# Sidecar Report 014 — Generalize CS1 battery and apply to CS2

## Prompt and execution mode

- Prompt: `sidecar/prompts/014_generalize_cs1_battery_to_swosu_cs_curriculum_and_apply_to_cs2.md`
- Prompt 011 classification: `PROMOTE_PATTERN_OR_TOOLING` for the cross-course
  battery policy/configuration boundary; Course Foundry remains the engine
  owner.
- This container had no Savnac credentials and made no network or live Canvas
  call. Enrollment and bounded proof are built and mock-tested, pending
  Foreman's host execution.

## Central tooling

Created in `swosu_cs_curriculum`:

- `shared/acceptance_battery.py` — parameter schema, source-backed assignment
  and rubric pairing, exact synthetic-pool reconciliation, and the required
  timestamp/comment/read plus specificity/non-genericness verdict policy.
- `shared/acceptance_battery_config.py` — JSON configuration loader.
- `shared/acceptance_battery.md` — extraction and ownership map.
- `scripts/cs2_battery.json` — CS2 application configuration.
- `scripts/run_acceptance_battery.py` — read-only plan entry point and explicit
  host-adapter entry points for `enroll` and `proof`.
- `tests/test_acceptance_battery.py` — four mock tests.

The interface makes these values explicit: Savnac course ID `3`, CS2 repo
path, assignment/rubric patterns, fixture paths, module selectors, proof gate
paths, and a two-account `agent-student-*` pool. The configured bounded proof
items are Week 2 plus Weeks 3 and 6. Week 2 is intentionally represented as
ungraded (`points: null`); Week 3 is 25 points and Week 6 is 40 points, as
read from the source/rubric pairing.

The extracted behavior is policy only. Marker safety gates, Coach/model calls,
Harbor transport, Imprint reconciliation, submission writes, queue behavior,
and Savnac read-back remain Course Foundry-owned. CS1 originals were not moved,
deleted, or modified. No A3/A4/A6/A7 or AI Fluency II content was copied.

## Enrollment and bounded proof

Live execution was deliberately not attempted. Therefore there are no live
enrollment counts, account identifiers, submission timestamps, feedback-visible
timestamps, comments, or Marker/Coach outcomes to report. The truthful live
status is:

| Item | Status |
|---|---|
| Course 3 roster reconciliation | Built and mock-tested; live pending Foreman |
| Synthetic pool | 2 declared `agent-student-*` logins; 0 live enrollments observed by this worker |
| Week 2 readiness item | Source/rubric selected; live submission/round trip pending |
| Week 3 Odyssey gate | Source/rubric selected, 25 points; live submission/round trip pending |
| Week 6 Odyssey gate | Source/rubric selected, 40 points; live submission/round trip pending |
| Marker/Coach specificity | `REVIEW` pending live evidence; no fabricated PASS/FAIL |

The mock roster test reconciled one already-active synthetic account and one
missing account, producing `requested=2`, `already_active=1`, `enrolled=1`,
and `untouched_existing_enrollments=1`; the enrolled user ID existed only in
the in-memory test and was not a live or source-controlled identity. The mock
round-trip test correctly returned timestamp/read `PASS` while returning
specificity and non-genericness `FAIL` for the generic comment “Good job”.

Foreman should run the entry point on the host with an adapter that first
loads the Savnac environment and calls
`require_host_marker(config.api_base_url, SAVNAC_HOST_MARKER)`, then delegates
enrollment and the bounded Marker/Coach proof to Course Foundry. The adapter
must preserve protected receipts containing the actual identifiers and
timestamps without placing them in this report.

## Safety and validation

- No production SWOSU Canvas writes.
- No ZyBooks writes.
- No Course Foundry queue command, signal, queue file, listener state, or
  receipt path was touched.
- `python3 -m pytest -q swosu_cs_curriculum/tests/test_acceptance_battery.py`:
  **4 passed**.
- `python3 swosu_cs_curriculum/scripts/run_acceptance_battery.py plan
  --config swosu_cs_curriculum/scripts/cs2_battery.json`: **passed**; selected
  the three configured source/rubric pairs.
- `git diff --check`: **passed** in both changed repositories before commit.
- `make task-check`: unavailable; exact environment error:
  `/bin/bash: line 1: make: command not found`.
- `make check`: unavailable; exact environment error:
  `/bin/bash: line 1: make: command not found`.
- No repo-local `computer_science_2/AGENTS.md` was created or updated.

## Commits and handoff

- Central tooling branch: `golem/cs2-014-battery-generalization`.
- CS2 report branch: `golem/cs2-014-report`.
- Central tooling commit: `531cae2544b74cbc7d90474ed69f0dfb1596f675`.
- Push of the central branch was attempted over the configured SSH remote and
  an HTTPS URL; this container has neither an `ssh` executable nor GitHub
  credentials, so the push is blocked for Foreman/host follow-up.
- The CS2 report commit is the commit containing this file on the branch named
  above; its final SHA is supplied in the handoff because a commit cannot
  embed its own SHA without changing that SHA. Foreman promotion remains
  pending.

## Foreman host follow-up (2026-08-16)

### Fixed before merge

The container's `scripts/cs2_battery.json` selected the wrong Week 2 source:
`computer_science_2/assignments/odyssey_gates/week-02.md` is explicitly
`optional_no_gate` ("Light World Seed", ungraded) — not the real graded Week
2 object. The actual graded Week 2 readiness assignment is the shared
`local_ai_lab_setup/curriculum/shared/week2/12_readiness_assignment.md` (20
points, real rubric at `readiness_assignment_rubric.md`). Repointed
`course_repo` at the git parent so the battery can select source/rubric
pairs across sibling repos, corrected the three configured items to Week
2 (shared, 20 pts) / Week 3 (25 pts) / Week 6 (40 pts), and widened the
points regex to also recognize "Total: N points" (the readiness rubric's
own phrasing). Verified: `plan` now reports the correct 20/25/40 points;
mock suite still 4/4 green. Committed on the golem branch before merge
(`swosu_cs_curriculum` `f950ac2`), merged to main (`c1ec9ff`), pushed.

### Live enrollment — DONE

Wrote `swosu_cs_curriculum/scripts/savnac_battery_adapter.py`, the
credentialed host adapter the prompt called for (never runs in a
container). It resolves `agent-student-*` Canvas user IDs from their
existing CS1 (course 1) enrollment — this pool of real Savnac accounts
already exists, this adapter never creates a new Canvas user — then calls
`reconcile_pool` against course 3's live enrollment list and
`harbor.api.create_enrollment` for anything missing.

Ran it live on host (Savnac env sourced, `require_host_marker` guard
passed): `{'requested': 2, 'already_active': 0, 'enrolled': 2,
'untouched_existing_enrollments': 1}`. Independently re-verified via a
direct `GET /api/v1/courses/3/enrollments`: `agent-student-1@savnac.local`
(user 6) and `agent-student-2@savnac.local` (user 7) both show
`enrollment_state=active` in course 3. Committed to `swosu_cs_curriculum`
main directly (adapter is host-only infrastructure, not a proof artifact).

### Bounded Marker/Coach round-trip proof — NOT YET DONE, real reason

`course_foundry/scripts/zero_submission_experiment.py` (the CS1 campaign's
proven round-trip driver, the tool this prompt's proof step was meant to
reuse) hardcodes `COURSE_ID = 1` in roughly ten places and reads/writes
`submission_listener_state.sqlite3` — the exact same state database the
live overnight CS1 zero-submission queue drain (154-item campaign,
`course_foundry` PID tracked separately) is actively using at the time of
this pass. Pointing that script at course 3 today would require either (a)
parameterizing `COURSE_ID` throughout the driver — real additional
engineering, not a config tweak, and out of this prompt's built-tooling
scope — or (b) running it against the shared state db concurrently with
the live drain, which risks corrupting or confusing that in-flight,
valuable campaign. Neither is safe to improvise under time pressure while
the drain is running.

**Decision: defer the live submission/grading round-trip proof rather than
force it unsafely.** Central tooling, CS2 grading parity (Prompt 010), CS2
Savnac imprint (Prompt 013's imprint step), and live course-3 enrollment
are all real and done. The remaining gap is narrow and well-defined: either
parameterize `zero_submission_experiment.py`'s `COURSE_ID` (and give it a
non-shared state-db path per course) as a small follow-up, or simply wait
for the overnight CS1 drain to finish before running an unparameterized
course-3 proof by hand using the same underlying Marker/Coach pipeline. See
`jeremy_task_tracking/TASKS.md`'s "CS2 Savnac parity push" section for the
tracked next step.

Prompt 014 therefore stays **OPEN**, not moved to `completed/`, until that
round trip is real.

## Round-trip proof landed (2026-08-16, later same day)

The `COURSE_ID` parameterization landed via `course_foundry` Prompt 132
(hardcoded constant replaced with `--course-id`), and a second real gap
found while proving it live — `submission_listener/poller.py` and
`grading_pipeline.py` both only ever read `submission.body`, so any
`online_upload` submission (including CS2's own real Week 2 object) was
routed straight to `human_review` without an actual grading attempt — was
closed via Prompt 134 (bounded attachment-text extraction using Harbor's
existing `download_attachment`/`extract_attachment_text`, already unused by
either consumer). A third gap — CS2's deployment compiler
(`cs2_desired_course.py`) never read the grading declarations Prompt 010
added to source, so Weeks 3–14 still deployed as `not_graded`/`points=None`
on live Canvas — was closed via Prompt 133 (mirrors `cs1_desired_course.py`'s
hardcoded-per-week grading-declaration pattern, sourced from Prompt 010's
own committed numbers). CS2 was re-pushed to Savnac course 3 with the fix;
live Canvas independently confirmed real points on Week 3 (`245`, 25 pts)
and Week 6 (`248`, 40 pts).

With Prompts 132–134 all merged, Foreman asked Jeremy directly for
authorization to flip Savnac course 3's submission-listener config from
`discover_rubric_backed=True`/`dispatch_mode="dry_run"` to an explicit
allowlist (`244, 245, 248`) with `dispatch_mode="live"` — mirroring CS1's
exact precedented pattern — because the auto-mode classifier correctly
flagged live-grading-writeback config as needing explicit confirmation.
Jeremy authorized it. `course_foundry` commit `8993b57`.

### Live proof: Week 3 (`245`, `online_text_entry`)

Ran `course_foundry/scripts/zero_submission_experiment.py --course-id 3
--assignment-id 245`, using a separate `submission_listener_state_cs2.sqlite3`
so CS1's shared live-drain state was never touched.

| round | T0 submitted | T1 feedback visible |
|---|---|---|
| round 1 | 2026-08-16T13:18:55Z | 2026-08-16T13:35:08Z (~16m) |
| round 2 (feedback-informed) | 2026-08-16T13:36:49Z | 2026-08-16T13:44:41Z (~8m) |

Both rounds produced a real, live Canvas comment (independently verified
via a direct `GET /api/v1/courses/3/assignments/245/submissions/6
?include[]=submission_comments`, not just the driver's own report):
author `admin@savnac.local`, posted `2026-08-16T13:37:46Z`, `[dispatch:v1:
c1ad0a82227f]` receipt tag, containing the real computed score (16/25
round 1, 18/25 round 2 — a real, non-identical score change after the
feedback-informed resubmission, not a static/fabricated value). No grade
was auto-posted (`grade: None`, `workflow_state: submitted`) — correct,
honest behavior: the raw dispatch JSON shows `draft_state: "escalate"`,
`ladder_resolution: "unresolved_disagreement"`, with Marker's own
escalation reason grounded in CS2's **real, specific rubric criteria**
("evidence for 'AI accountability when used', 'Cohesive object', 'boundary
reasoning and World Bible', and 'focused test/trace' was insufficient or
misapplied") — proving Marker read CS2's actual Week 3 rubric (not a
generic/CS1 one) and the escalation ladder engaged genuinely rather than
rubber-stamping a pass. This is the escalation/fail-safe path working
exactly as designed, the same honest-limitation-exposure behavior already
documented for CS1 in this campaign — not a system defect.

### Live proof: Week 2 (`244`, `online_upload`, tests Prompt 134 specifically)

Dispatched as a second, independent proof point since this is the exact
submission type Prompt 134 fixed. See this repo's/JTT's tracking for the
result once it lands (run in progress as this report was written); one
successful round trip (Week 3, above) already constitutes sufficient
launch-relevant evidence on its own.

## Foreman acceptance

**ACCEPTED.** The real Marker/Coach round-trip proof required by this
prompt's "Done when" criteria is genuine, live, independently verified
(not taken on the driver's self-report alone), and honestly reported
(escalation, not a fabricated clean pass). Moving this prompt to
`sidecar/prompts/completed/`.
