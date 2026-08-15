# Reasoning Odyssey fabric reconciliation

## Outcome

CS2's durable student-facing name is now **Reasoning Odyssey**. The legacy
`assignments/coding-odyssey-project.md` path remains a compatibility pointer
only; it creates neither a second assignment nor a second gradebook path.
The four CS2-specific world options and the World Bible name are unchanged.

## Files changed

| Files | Why changed |
|---|---|
| `assignments/A2-coding-odyssey-project.md` | Renamed the project and its framing to Reasoning Odyssey while preserving its Week 2 kickoff, four-world menu, and growth path. Identified Weeks 12–13 as synthesis/stabilization rather than new-concept work. |
| `assignments/coding-odyssey-project.md` | Kept the legacy path as a compatibility pointer, but pointed it to the Reasoning Odyssey specification. |
| `assignments/A1-weekly-coding-practice.md`, `assignments/chapter-coding-practice.md`, `assignments/project-report-and-presentation.md`, `assignments/week-02-local-ai-readiness.md` | Replaced clear student-facing Coding/Odyssey doctrine references with Reasoning Odyssey; requirements and unresolved point-allocation language remain unchanged. |
| `assignments/odyssey_gates/week-02.md` through `week-14.md` (excluding nonexistent Week 15), and `week-16.md` | Renamed all 14 gate headers to Reasoning Odyssey. Week 2 remains optional/ungraded; Week 16 remains retired. Weeks 12–13 are explicitly named synthesis checkpoints and add reflection within the already-required World Bible entry. |
| `rubrics/odyssey_gates/week-02_rubric.md` through `week-14_rubric.md` (excluding nonexistent Week 15), and `week-16_rubric.md` | Renamed matching rubric headers and checkpoint references. Weeks 12–13 mirror the synthesis/no-new-concept/World-Bible-reflection framing without changing criteria or points. |
| `docs/course-ethos.md`, `docs/curriculum/judgment_toolkit.md`, `docs/grading-model.md` | Reconciled current doctrine and grading-model references to Reasoning Odyssey; no grading mechanics changed. |
| `planning/fall-2026-course-design.md`, `planning/week-02-local-ai-lab-integration.md` | Reconciled current Fall 2026 design/integration doctrine references to Reasoning Odyssey. |

## Gate and checkpoint verification

- CS2's own source places light, ungraded world seeding in **Week 2** and the
  first graded build in **Week 3**. A2 therefore remains the Week-2 home base;
  it was not moved to match CS1.
- The active required gate sequence is **Weeks 3–14**. Week 2 is optional
  setup, Week 15 has no gate file/required technical gate, and Week 16 is a
  retired wrapper for the shared Farkle/ML experience.
- CS2's consolidation span is **Weeks 12–13**: A2 and the grading model call
  it stabilization/culmination/design review. Both are now framed as synthesis
  checkpoints: no new technical concept, reflection embedded in the existing
  World Bible entry, and no additional required work stream.
- Each of the 14 existing week folders still has a gate guidance/task file and
  matching rubric. The source does **not** specify a per-gate submission path
  or point value. `docs/grading-model.md` explicitly leaves submission
  locations and checkpoint/review allocation for syllabus finalization.
  This is an existing source gap; no values or submission mechanism were
  invented. Week 2 is expressly ungraded and Week 16 is expressly retired.

## Coding Odyssey search ledger

The following clear current doctrine/student-facing hits were changed:

- `assignments/A1-weekly-coding-practice.md`
- `assignments/A2-coding-odyssey-project.md`
- `assignments/chapter-coding-practice.md`
- `assignments/coding-odyssey-project.md`
- `assignments/project-report-and-presentation.md`
- `docs/course-ethos.md`
- `docs/curriculum/judgment_toolkit.md`
- `docs/grading-model.md`
- `planning/fall-2026-course-design.md`
- `planning/week-02-local-ai-lab-integration.md`

The following hits were deliberately left unchanged:

- `docs/philosophy/teaching-patterns.md`: explicitly an archive-based snapshot,
  where Coding Odyssey is the historical name.
- `docs/reports/curriculum-history-synthesis.md`: explicitly reports archived
  course history, including the historical transition to Coding Odyssey.

Archived reports, historical planning data, and prompt/provenance files were
not changed.

## Grading safeguard

No category, grading weight, point value, or `course_metadata.yaml` grading
block was changed. No Canvas/Savnac system was accessed.

## Test result

`pytest -q tests` collected **0 tests** and exited with status **5** (`no tests
ran`). Therefore there are **0 passing** and **0 failing** tests; the suite is
not runnable because this repository currently has no test cases.
