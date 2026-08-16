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

## Limitations and next action

The container cannot prove real course-3 enrollment or a real Marker/Coach
round trip. Foreman must run the bounded live adapter, preserve protected
receipts, and append the observed aggregate counts/timestamps/evidence to the
operational record before accepting Prompt 014. No next prompt was drafted or
executed.
