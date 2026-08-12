# Week 2 — Local AI Lab Integration Crosswalk

## Purpose

This file makes explicit how CS2's Week 2 ("Build and Verify Your Local AI
Lab", `planning/week-02.md`) connects to the shared **Build and
Verify Your Local AI Lab** module. It exists so a future instructor, Canvas
builder, or agent does not have to reconstruct the relationship between three
repositories from memory.

Do not duplicate the shared instructional content here. This is a map, not a
copy.

## Ownership

- **`local_ai_lab_setup`** owns the shared student-facing instructional
  content, the CS2 extension text, the readiness assignment, and the rubric.
  It is the canonical instructional source for this module.
- **`windows_classroom`** owns the tested Windows execution harness — the
  actual `Check` / `Baseline` / `Launch` / `Diff` / `Final` / `Reset` command
  surface students run, the diagnostic codes, and the pre-provisioning
  contract.
- **`computer_science_2`** (this repository) owns *when and why* the activity
  appears in CS2, and how it connects to CS2's outcomes and the Coding
  Odyssey. It does not own or re-author the shared lesson content or the
  execution harness.

Neither shared repository is modified by this stitch. Both remain read-only
inputs from CS2's perspective.

## Student path crosswalk

| CS2 purpose | Canonical source | Student action | Evidence produced | What it proves / does not prove | CS2 connection |
|---|---|---|---|---|---|
| Understand the local-AI system model (PowerShell, Python, Git, Ollama, Aider, `localhost`, the approved model) | `local_ai_lab_setup/curriculum/shared/week2/01_start_here.md` through `05_local_ai_architecture.md`, `06_ollama_models_and_hardware.md`, `07_aider_as_a_client.md`, `08_localhost_apis_and_local_vs_cloud.md` | Read the shared pages; trace the request/response diagram | A working mental model; no artifact submitted | Explains the system; proves nothing about the student's own machine yet | Establishes vocabulary CS2 reuses for the bounded Aider exercise below |
| Confirm the classroom machine is ready | `windows_classroom/scripts/week2_classroom.ps1` via `docs/week2_student_guide.md` | Run `Check` | `READY` (exit 0) or `NOT READY` (exit 2) plus a stable `W2-<AREA>-001` diagnostic | `READY` proves tool/API/model/inference checks each passed *at that moment*; it does not prove code correctness or answer quality | Gatekeeper before the CS2 bounded exercise begins |
| See the known-failing starting point | `windows_classroom/scripts/week2_classroom.ps1 Baseline`; exercise defined via `local_ai_lab_setup/curriculum/cs2/week2_extension.md` | Run `Baseline` | A failing unit test (title-case assertion fails against all-uppercase output) | Establishes the pre-change state; proves the defect is real and reproducible | Baseline anchor for the CS2 extension's diff/test reasoning |
| Request one bounded AI-assisted change | `windows_classroom/scripts/student_agent.ps1` via `Launch`; exact request text in `local_ai_lab_setup/curriculum/cs2/week2_extension.md` | Run `Launch`, enter the exact supplied Aider request (`format_student_name` → title case, `student_code.py` only) | An Aider-proposed change to `student_code.py` | Proves a request was sent and a change was proposed; does not prove the change is correct | This is the CS2-specific extension of the shared module (`cs2-week2-trace` in `curriculum/week2_module_manifest.yml`) |
| Inspect exactly what changed | `windows_classroom/scripts/week2_classroom.ps1 Diff` | Run `Diff` | A `git diff` limited to `student_code.py` (expected: `.upper()` → `.title()`) | Proves what changed and where; does not by itself prove behavior is correct | Direct application of CS2's course-wide AI-disclosure rule: every AI-assisted line must be inspected (`docs/course-ethos.md`) |
| Independently verify the change | `windows_classroom/scripts/week2_classroom.ps1 Final` | Run `Final` | A passing (or still-failing) run of the supplied unittest suite | A pass proves the tested behavior now matches the tested expectation; it does not prove untested behavior is correct or that the AI "understood" the task | Same evidence discipline CS2 already requires for AI-assisted work generally |
| Recover to the disposable starting state if needed | `windows_classroom/scripts/week2_classroom.ps1 Reset -ConfirmReset` | Run `Reset -ConfirmReset` | A dated backup under `classroom\backups`, then a reset exercise tree | Confirms the exercise is disposable and safely repeatable | Not itself submitted; supports retry without risk |
| Submit readiness evidence and reflection | `local_ai_lab_setup/curriculum/shared/week2/12_readiness_assignment.md` and `readiness_assignment_rubric.md`, plus the CS2 reflection prompt in `curriculum/cs2/week2_extension.md` | Preview and submit `local-ai-readiness.md` in Canvas (future deployment) | The generated readiness report, three shared conceptual answers, and the CS2 course-specific reflection (method-call defect, why the one-line diff fits, what the passing test does/does not establish) | Establishes the full evidence chain the student can defend | Recorded in CS2 via `assignments/week-02-local-ai-readiness.md` |

## How this fits the Coding Odyssey

The local-AI readiness artifact is the sole required technical experience in
Week 2. `assignments/odyssey_gates/week-02.md` permits only an ungraded,
light world seed. It is not an exceptions gate and does not compete with the
shared module. Graded Odyssey construction begins Week 3.

## What is intentionally not copied here

- The full shared Week 2 instructional spine (`local_ai_lab_setup/curriculum/shared/week2/*`) stays in `local_ai_lab_setup`.
- The Windows execution harness, diagnostic codes, and pre-provisioning steps stay in `windows_classroom`.
- Media/screenshot placeholders (`[WINDOWS CAPTURE: ...]`) remain unresolved in `local_ai_lab_setup/instructor/week2_placeholder_registry.md`; CS2 does not track or duplicate that registry.

## Unresolved, not inferred

- Exact Monday/Wednesday/Friday time allocation between exceptions and the local-AI lab.
- Canvas/Savnac deployment of this module for CS2 (not performed by this stitch; see `reports/006_week2_local_ai_stitch.md`).
- Final resolution of the `[WINDOWS CAPTURE: ...]` media placeholders, owned by `local_ai_lab_setup`.
