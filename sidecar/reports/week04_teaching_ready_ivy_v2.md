# CS2 Week 4 teaching-ready buildout — Ivy v2

Before building anything, I ran `git fetch origin` in `computer_science_2` and
read the actual files from `origin/main`; the exact source checks confirmed
Week 4 is **Cohesive Object Boundary**, not Week 5's composition topic. The
rubric header I saw was `# Reasoning Odyssey gate rubric — Week 4 — Cohesive
Object Boundary (S01)`. The first refresh attempt exposed a local SSH config
permissions error, so I retried through the configured user SSH profile and
the fetch completed successfully. `origin/main` was `8075c7ecda3ec12ed8235a07b7b7a16c2f9d3568`.

## Built

- Added `lessons/week-04-cohesive-object-boundary.md` as a student-facing
  lesson covering the learning targets, Labor Day Monday bridge, Week 3 World
  Bible reopening, one-candidate boundary test, legitimate failed prediction,
  cohesive state/behavior reasoning, a focused `unittest` example, independent
  execution, World Bible evidence, and AI accountability.
- Rewrote `planning/week-04.md` to the settled Week 4 topic and student path.
- Did not modify `assignments/odyssey_gates/week-04.md` or
  `rubrics/odyssey_gates/week-04_rubric.md`.
- Did not copy or repurpose the bounced composition lesson or touch its branch.

## Pattern and cross-reference evidence

The planning page and new lesson use the established source-link token shape:
`{{link:week03_odyssey_gate}}`, `{{link:week04_lesson}}`,
`{{link:week04_odyssey_gate}}`, and `{{link:week04_odyssey_rubric}}`. These keys
match the prior CS2 Week 4 gate/lesson pattern, and the changed files contain
no bare local lesson paths. Source inspection across the current CS2 checkout
shows no CS2 live-link compiler/resolver; therefore these are correctly wired
source tokens, but live URL resolution is a separate course-foundry/compiler
follow-up and was not attempted or claimed here. No Canvas or live-course
action was performed.

## Validation

- `git fetch origin` via `git -c core.sshCommand='ssh -F /home/jevert/.ssh/config' fetch origin`: passed.
- Exact contract checks:
  - `git show origin/main:assignments/odyssey_gates/week-04.md | head -1` →
    `# Reasoning Odyssey Gate — Week 4 — Cohesive Object Boundary (S01)`
  - `git show origin/main:rubrics/odyssey_gates/week-04_rubric.md | head -1` →
    `# Reasoning Odyssey gate rubric — Week 4 — Cohesive Object Boundary (S01)`
  - Week 5 comparison confirmed its header is `Collaborating Objects and
    Invariant (S01/S08)`.
- `git diff --check`: passed.
- Existing suite: `python3 -m unittest discover -s tests -v` → **9 tests,
  9 passed**.
- `pytest`: unavailable in this environment (`pytest` was not installed/on
  PATH); no pytest validation was skipped silently.
- Settled Week 4 gate and rubric: unchanged relative to `origin/main`.
- Final intended change set: `planning/week-04.md` and
  `lessons/week-04-cohesive-object-boundary.md` only, plus this report.
