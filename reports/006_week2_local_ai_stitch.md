# Report 006 — Stitch the Local AI Week 2 Module into Computer Science II

Source prompt: `jeremy_task_tracking/codex_prompts/016_cs2_week2_local_ai_stitch.md`
(CS2 only; DSCT and Computer Architecture explicitly out of scope for this pass).

## Pre-mutation evidence table

| Question | Current evidence | Source |
|---|---|---|
| Is the local-AI module explicitly intended for CS2 Week 2? | Yes. `week2_module_manifest.yml` defines a `cs2` course module (`destination_title: "Savnac Computer Science 2 Week 2"`) with a full shared-spine + `cs2-week2-trace` extension sequence. `week2_module_plan.md` states the shared module "should fit both CS2 and DSCT." | `local_ai_lab_setup/curriculum/week2_module_manifest.yml`, `docs/week2_module_plan.md` |
| What shared student-facing artifacts already exist? | A 12-page shared spine (`01_start_here.md` … `12_readiness_assignment.md`) plus a shared rubric, covering PowerShell/Python/Git orientation, local-AI architecture, Ollama/models/hardware, Aider, localhost/APIs, the readiness checker, first interaction, troubleshooting, and the readiness assignment. | `local_ai_lab_setup/curriculum/shared/week2/*` |
| What CS2-specific extension already exists? | `curriculum/cs2/week2_extension.md`: a bounded Aider-assisted repair of `format_student_name` (all-uppercase → title case) with a known failing baseline, an exact requested change, `git diff` inspection, independent unit-test verification, and a course-specific reflection distinguishing generation from evidence of correctness. | `local_ai_lab_setup/curriculum/cs2/week2_extension.md` |
| What classroom execution commands are supported? | `scripts\week2_classroom.ps1` supports `Check`, `Baseline`, `Launch`, `Diff`, `Final`, `Reset -ConfirmReset`, confirmed both in docs and in the script's own `ValidateSet`/action switch. `Launch` invokes `scripts\student_agent.ps1`, which is pinned to Aider `0.86.2` against `ollama_chat/qwen3:8b` at loopback `127.0.0.1:11434` only. | `windows_classroom/docs/week2_student_guide.md`, `docs/week2_instructor_runbook.md`, `scripts/week2_classroom.ps1` |
| What does current CS2 Week 2 already teach? | Prior to this stitch, `planning/week-02.md` was entirely about exceptions (Chapter 10) and the Odyssey gate; it made no mention of the local-AI lab. `planning/fall-2026-course-design.md`'s Week 2–3 row was likewise exceptions-only. | `computer_science_2/planning/week-02.md` (pre-edit), `planning/fall-2026-course-design.md` (pre-edit) |
| What parts conflict, overlap, or complement each other? | No direct conflict. The exceptions/Odyssey spine and the local-AI lab are different kinds of Week 2 work (a chapter concept applied to a persistent project vs. a professional dev-environment/evidence-discipline exercise) and can coexist without a claimed day-level split. Both already share a "generation is not evidence of correctness" ethos: CS2's own `docs/course-ethos.md` and `assignments/A1-weekly-coding-practice.md` already require AI-assisted work to be inspected, tested, and disclosed, matching the local-AI module's baseline→diff→test→accept/reject loop almost exactly. | `local_ai_lab_setup/curriculum/cs2/week2_extension.md`; `computer_science_2/docs/course-ethos.md`; `assignments/A1-weekly-coding-practice.md` |
| What is still unresolved rather than safe to infer? | Exact Monday/Wednesday/Friday time allocation between exceptions and the local-AI lab (no source specifies one); Canvas/Savnac deployment of the CS2 module (not performed here); resolution of `[WINDOWS CAPTURE: ...]` media placeholders (owned by `local_ai_lab_setup`, untouched). | `local_ai_lab_setup/instructor/week2_placeholder_registry.md`; this report |

## Files changed

All changes are in `computer_science_2` only.

- **Modified** `planning/week-02.md` — added an explicit "Week 2 also carries... Build and Verify Your Local AI Lab" section: module purpose, CS2-depth tool roles, the readiness/evidence workflow, the CS2 bounded Aider extension, and an explicit statement that day-level allocation is unclaimed. The exceptions/Odyssey content is preserved unchanged; both deliverables are now listed under "Due this week."
- **Created** `planning/week-02-local-ai-lab-integration.md` — the durable table-first crosswalk required by the prompt: ownership statement (`local_ai_lab_setup` = instructional content, `windows_classroom` = execution harness, `computer_science_2` = when/why/CS2 connection) and a full student-path table (system model → `Check` → `Baseline` → `Launch` → `Diff` → `Final` → `Reset` → submission) with canonical source, student action, evidence produced, what it proves/does not prove, and CS2 connection for each step. Includes an explicit "how this coexists with exceptions/Odyssey" section and an "unresolved, not inferred" section.
- **Created** `assignments/week-02-local-ai-readiness.md` — a thin CS2 assignment wrapper. It does not restate shared directions; it points to the canonical readiness assignment/rubric, the CS2 extension, and the Windows student guide, then states the CS2-specific evidence/reflection expectation and notes that no new grading weight is introduced (existing weekly-reinforcement category applies) and that no Canvas/Savnac deployment has occurred.
- **Modified** `planning/fall-2026-course-design.md` — the Week 2–3 row in the semester spine table now names the local-AI lab readiness experience for Week 2, pointing to the new crosswalk, without altering the exceptions content, the two-week arc, or any weight/date.

`docs/curriculum/course-sequence.md` was inspected and left unmodified: it is a historical topic/chapter map with no per-week local-AI claim to contradict, so no reconciliation was needed there.

## Resulting Week 2 student path

1. Read the shared local-AI system-model pages (`local_ai_lab_setup/curriculum/shared/week2/01…08`).
2. Run `Check` (`windows_classroom/scripts/week2_classroom.ps1`) until `READY`.
3. Run `Baseline` — observe the known-failing `format_student_name` test.
4. Run `Launch`, enter the exact bounded Aider request from `curriculum/cs2/week2_extension.md`.
5. Run `Diff` — inspect the proposed one-line change to `student_code.py`.
6. Run `Final` — independently rerun the unit test.
7. Complete the shared readiness assignment (`12_readiness_assignment.md`) plus the CS2 course-specific reflection, and submit `local-ai-readiness.md`.
8. Separately and concurrently: complete the Week 2 Odyssey gate (exceptions) per `assignments/odyssey_gates/week-02.md`, unchanged.

## How local AI and the existing exceptions/Coding Odyssey spine coexist

They are treated as two separate, concurrently due Week 2 deliverables rather than merged or sequenced against each other. The exceptions gate remains the technical-concept application inside the student's persistent Odyssey world; the local-AI lab is the professional-environment/evidence-discipline exercise. No Monday/Wednesday/Friday split is asserted between them because no current source (CS2 planning, `local_ai_lab_setup`, or `windows_classroom`) specifies one. This is recorded explicitly as unresolved in both `planning/week-02.md` and the new crosswalk rather than invented.

## Canonical dependency paths

- `local_ai_lab_setup/curriculum/shared/week2/` (shared instructional spine, 12 pages + rubric)
- `local_ai_lab_setup/curriculum/cs2/week2_extension.md` (CS2 bounded extension)
- `local_ai_lab_setup/curriculum/week2_module_manifest.yml` (publishing manifest / module sequence)
- `local_ai_lab_setup/instructor/week2_teaching_notes.md`, `instructor/week2_placeholder_registry.md` (instructor-only; untouched)
- `windows_classroom/scripts/week2_classroom.ps1`, `scripts/student_agent.ps1` (execution harness)
- `windows_classroom/docs/week2_student_guide.md`, `docs/week2_instructor_runbook.md` (student/instructor command contract)

None of these files were modified. `local_ai_lab_setup` was fast-forward pulled (`6feb06f..88cdc35`) as part of Phase 0 reconciliation; its one pre-existing unrelated uncommitted local edit to `prompts/005_design_cs2_week2_savnac_transform.md` was left untouched, uncommitted, and unstashed, as instructed. `windows_classroom` was already clean and in sync with `origin/main`.

## Validation performed

1. Confirmed all four repositories (`jeremy_task_tracking`, `computer_science_2`, `local_ai_lab_setup`, `windows_classroom`) were clean or safely fast-forwardable via `git status --short --branch` and `git fetch`/`git pull --ff-only` before any edit (Phase 0).
2. Read `AGENTS.md`/`README.md` guidance in each repository.
3. Read every file listed in the prompt's Phase 1 minimum-inspection list, plus `student_agent.ps1`/`week2_classroom.ps1` directly to confirm the exact supported action names (`Check`, `Baseline`, `Launch`, `Diff`, `Final`, `Reset` with `-ConfirmReset`) rather than trusting the prompt's summary.
4. Verified every file path referenced in the new/edited CS2 files actually exists on disk (script-checked; see command list below), including cross-repo references into `local_ai_lab_setup` and `windows_classroom`.
5. Confirmed the CS2 extension's exercise contract (bounded request text, expected `.upper()` → `.title()` diff, independent unit-test verification) matches what is described in the new crosswalk and assignment wrapper.
6. Confirmed no student-facing direction added by this stitch asks for admin rights, cloud credentials, model downloads, SSH keys, or broad machine repair — all new CS2 text points to the existing `windows_classroom` guide, which already excludes those.
7. Confirmed local-vs-cloud language in the new CS2 text does not assert absolute privacy (it explicitly says "never treated as correct merely because it ran" and reuses the loopback-only framing already established upstream).
8. Confirmed no new due dates or grading weights were invented; the new assignment wrapper explicitly states it introduces no new grading weight and folds into the existing weekly-reinforcement category.
9. Confirmed no content blob was copied wholesale — the new crosswalk and wrapper reference and summarize, they do not reproduce, the shared spine or CS2 extension text.
10. Ran `git status --short --branch` and `git diff --cached --stat` / `git diff --cached --check` in `computer_science_2` before committing; confirmed only the four intended files changed and no whitespace errors were introduced.
11. Confirmed via `git status --short` in `local_ai_lab_setup`, `windows_classroom`, and `jeremy_task_tracking` that no files in those repositories were modified by this task.

Validation command used for path existence (all passed):

```
for p in <every relative/absolute path referenced above>; do [ -f "$p" ] || echo MISSING; done
# output: ALL REFERENCED PATHS EXIST
```

The Windows classroom wrapper itself was not executed; this is Linux (Brandy), and the prompt explicitly calls for static inspection rather than a Linux run standing in for Windows lab verification.

## Future Canvas/Savnac deployment implications (not performed)

This stitch is source-curriculum only. No Canvas/Savnac page, module, or assignment object was created or modified. Future deployment would need: (1) a dry-run Imprint transformation of the CS2 module sequence already defined in `week2_module_manifest.yml`, consistent with that manifest's own `publishing_notes`; (2) resolution of the `[WINDOWS CAPTURE: ...]` media placeholders in `local_ai_lab_setup/instructor/week2_placeholder_registry.md`; (3) a decision on whether `assignments/week-02-local-ai-readiness.md` becomes the literal Canvas assignment shell or is superseded by a generated one; (4) confirmation of the actual Week 2 day-level schedule before any Canvas "Week at a Glance" page asserts one.

## Unresolved decisions/placeholders requiring Jeremy

1. Monday/Wednesday/Friday time allocation between the exceptions spine and the local-AI lab within Week 2 (explicitly left unclaimed by this stitch).
2. Whether/when to run the analogous DSCT stitch (explicitly deferred per the prompt).
3. Whether `assignments/week-02-local-ai-readiness.md` or a different existing file should become the eventual Canvas assignment object once deployment begins.
4. Resolution of `local_ai_lab_setup`'s `[WINDOWS CAPTURE: ...]` media placeholders — owned upstream, tracked upstream, not duplicated into CS2.

No blocking source defect was found in `windows_classroom` or `local_ai_lab_setup` during this pass; no changes were made to either repository.

## Commit SHA

`62bf345` on `computer_science_2` `main` — "Stitch Build and Verify Your Local AI Lab into CS2 Week 2" (includes this report file).
