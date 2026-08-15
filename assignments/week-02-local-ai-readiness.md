# Week 2 — Local AI Lab Readiness

## What this is

A thin CS2 pointer to the shared **Build and Verify Your Local AI Lab**
module, kept as a durable object for future Canvas/Savnac deployment. It does
not restate the shared directions. See the full crosswalk in
`planning/week-02-local-ai-lab-integration.md`.

## Canonical sources (do not duplicate)

- Shared instructional spine and readiness assignment/rubric:
  `local_ai_lab_setup/curriculum/shared/week2/` (start at `01_start_here.md`;
  assignment is `12_readiness_assignment.md`, rubric is
  `readiness_assignment_rubric.md`).
- CS2-specific bounded extension (repair `format_student_name`):
  `local_ai_lab_setup/curriculum/cs2/week2_extension.md`.
- Windows execution commands students actually run:
  `windows_classroom/docs/week2_student_guide.md`
  (`scripts\week2_classroom.ps1 Check` / `Baseline` / `Launch` / `Diff` /
  `Final` / `Reset -ConfirmReset`).

## Do

1. Follow `windows_classroom/docs/week2_student_guide.md` to run `Check`
   through `Final` in the supplied classroom environment.
2. Follow the shared readiness assignment
   (`local_ai_lab_setup/curriculum/shared/week2/12_readiness_assignment.md`)
   to generate and privacy-preview `local-ai-readiness.md`, and answer the
   three shared conceptual questions there.
3. Answer the CS2-specific reflection defined in
   `local_ai_lab_setup/curriculum/cs2/week2_extension.md` under
   `### Course-specific reflection` in the same file: identify the
   method-call defect, explain why the one-line diff (`.upper()` →
   `.title()`) fits the requested behavior, and state what the passing unit
   test does and does not establish.

## CS2-specific evidence/reflection expectation

Your reflection must use the actual evidence from your own run — the
`Baseline` failure, the `Diff` output, and the `Final` test result — not a
general description of how Aider or Ollama work. Generation is a proposal;
your acceptance decision has to rest on the baseline, the diff, the test, and
your own reading of the code, matching the AI-disclosure standard already in
force for all CS2 work (`docs/course-ethos.md`,
`assignments/A1-weekly-coding-practice.md`).

## Grading

This activity is part of Week 2's existing weekly-reinforcement grading
category (`assignments/A1-weekly-coding-practice.md`,
`docs/grading-model.md`); no new grading weight is introduced here. Exact
point allocation between this activity and the Week 2 Reasoning Odyssey gate is not
yet decided and is not asserted by this file.

## Status

This is a durable placeholder for a future Canvas/Savnac assignment object.
No Canvas/Savnac deployment has been performed as part of this stitch.
