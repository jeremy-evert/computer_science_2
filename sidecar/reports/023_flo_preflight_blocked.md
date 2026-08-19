# Report 023 — Flo CS2 preflight blocked

**Status:** BLOCKED before GREEN TO WRITE
**Course:** COMSC-1053-1417 Computer Science II, Fall 2026
**Prompt executed:** `sidecar/prompts/022_flo_production_closeout.md`
**Human gate reached:** No. No production write was attempted or authorized. No Canvas credentials were read, echoed, or committed.

## Summary

This run used a fresh isolated campaign workspace (`20260819T141517Z-2586746`). Unlike the prior blocked run recorded in this same file, all five runway clones are clean and Phase A's own targeted test suites pass. The burn still cannot reach `GREEN TO WRITE`, for two distinct reasons discovered in sequence:

1. **CS2-owned defect** — `scripts/cs2_production.py`'s `_contract()` reads `course_metadata.yaml` expecting a schema (`course.title`, `course.course_code`, `course.section`, `term.name`, `instructor.name`) that the current `course_metadata.yaml` does not have. Preflight fails immediately with `STOP: 'title'` before any Canvas contact. This is untested: `tests/test_cs2_production.py` hand-builds an in-memory contract dict and never round-trips the real YAML file through `_contract()`, so this drift was never caught by the targeted suite.
2. **Runway-completeness gap, not CS2-owned** — even past that, the shared `course_foundry` desired-course compiler (`cs2_savnac_desired_course` → `_monday_moment_object`) requires Monday Moment content from a sibling `ai_fluency` repository (`course_foundry/course_foundry/savnac_deploy.py`'s `SourcePaths.defaults()` hardcodes `ai_root = git_parent / "ai_fluency"`). The launcher's runway contract for this campaign only provisions five sibling clones — `computer_science_2`, `course_foundry`, `harbor`, `imprint`, `local_ai_lab_setup` — and does not include `ai_fluency`. Confirmed by running `course_foundry`'s own targeted test suite (`tests/test_cs2_desired_course.py`), which fails with `FileNotFoundError` for `ai_fluency/ai_i/monday_moments/week_03_plan_the_work/student_activity.md` under the campaign root. An ordinary (non-isolated) `ai_fluency` checkout exists elsewhere on Brandy, but per the hard boundary against consuming source outside the isolated campaign clones, it was not touched or referenced.

Neither issue was repaired in-place this run: (1) touches the production-authority target-identity binding path, and picking the "correct" fix (patch the code's expected schema vs. add a title/section/term/instructor.name block to the metadata file) is a judgment call outside this run's authority; (2) is not CS2's to fix — it requires either the launcher including `ai_fluency` in the runway contract, or a decision from Jeremy about how the CS2 compiler should be sourced.

## Exact commit SHAs used

| Repo | HEAD |
|---|---|
| computer_science_2 | `71f0bdcf23277c42088c57e462d9dd80759ad1f2` |
| course_foundry | `969b50aa7f07dedb96049103f52b8bcc9fa0ac5c` |
| harbor | `91c1e400ce21b89f96b2697e9d1ae9d716694442` |
| imprint | `7745fe1c1819a2c39c1b3ef488cde450a3ba8cf0` |
| local_ai_lab_setup | `b2b2ec1afcea98c59a5ab3818cd361a29eb0f99c` |

All five clones were confirmed clean (`git status --porcelain=v1 -uall` empty) before any other step.

## Target

Not reached. `_contract()` fails locally before any Canvas discovery or binding is attempted; no course was ever identified, no client was ever bound.

## Validator / test results

- `python3 -m pytest -q tests/test_cs2_production.py` (this repo) — **4 passed**.
- `python3 -m pytest -q tests/test_cs2_desired_course.py` (course_foundry, targeted per Phase A step 4) — **1 passed, 3 failed**, all three failures on the identical `FileNotFoundError` for missing `ai_fluency/ai_i/monday_moments/week_03_plan_the_work/student_activity.md` (see blocker detail below).
- The three historical validators named in the prompt (`course_foundry.week1_validator`, `course_foundry.completeness_validator`, `course_foundry.cross_repo_integrity`) were correctly **not** invoked, per Phase A step 5.
- `python3 scripts/cs2_production.py preflight` was run (read-only) and halted immediately:

  ```text
  STOP: 'title'
  ```

  This is a `KeyError` inside `_contract()` (`scripts/cs2_production.py:87-96`) reading `course_metadata.yaml`, which currently has `course.name`/`course.code`/`course.section_number`/`course.instructor` (a plain string) and no top-level `term` mapping — not the `course.title`/`course.course_code`/`course.section`/`term.name`/`instructor.name` shape `_contract()` expects. No production host was contacted, no course was discovered/bound, no token was issued.

## Blocker detail

**Blocker 1 (CS2-owned, in `computer_science_2`):** `course_metadata.yaml`'s own header states it was authored for the shared `course_foundry.course_information_page` generator (prompt 045), not for `scripts/cs2_production.py`'s `_contract()`. The two CS2-owned consumers of this file now expect incompatible schemas. Fixing this requires a decision about which shape is authoritative (extend the YAML with the fields `_contract()` wants, or update `_contract()` to read the current YAML shape) — a target-identity-binding code path, which this run treated as too sensitive to patch unilaterally without sign-off.

**Blocker 2 (not CS2-owned):** `course_foundry`'s `SourcePaths.defaults()` (`course_foundry/course_foundry/savnac_deploy.py:55-67`) expects a much larger sibling-repo set under `git_parent` than this campaign's runway contract provisions, including `ai_fluency`, which the CS2 builder path (`_build_cs2` → `cs2_savnac_desired_course` → `_monday_moment_object`) actually dereferences for weeks 3–14 Monday Moment content. This campaign's isolated runway does not include an `ai_fluency` clone. This is a runway-contract gap, not a CS2 source defect, and per the hard boundaries this run did not reach into the ordinary (non-isolated) `ai_fluency` checkout elsewhere on Brandy to work around it.

## Preflight create/update/delete counts

Not produced — preflight halted on the `_contract()` KeyError before reaching any compile or diff step.

## Human authorization

Not requested. Not given. No `WRITE CS2` gate was reached.

## Live write counts

None. No write was attempted.

## Closeout dry-run counts

Not applicable — no write occurred.

## Independent read-back

Not performed — no production reconcile occurred, so there is nothing new to verify against production.

## Week 1

Week 1 remained entirely outside CS2 write authority. No CS2-owned action touched Week 1 or `semester_kickoff_week`. No live read of production occurred this run, so no fresh observation of the previously reported shared-kickoff module-ordering defect was made.

## Recommended next step

Both items need a human decision, not further autonomous action from this seat:

1. Decide the authoritative schema for `course_metadata.yaml` vs. `scripts/cs2_production.py`'s `_contract()`, and fix the mismatched side. Consider adding a test that round-trips the real file through `_contract()` so this class of drift is caught going forward.
2. Decide how the CS2 desired-course compiler should source Monday Moment content: either add `ai_fluency` to this campaign's launcher-provisioned runway contract, or change `course_foundry`'s CS2 builder to not require it outside the isolated clone set.

Once both are resolved, re-run this same prompt from fresh source truth; do not resume from this report's state.

## Files/commits produced by this run

- `sidecar/reports/023_flo_preflight_blocked.md` (this file, overwriting the prior run's now-superseded blocker report)
- No other files were created, modified, staged, or committed. `sidecar/runs/flo_cs2_preflight.json` was not written because preflight halted before reaching that step.
