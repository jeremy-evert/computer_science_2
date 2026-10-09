# CS2 Week 4 teaching-ready pass — Ivy

Date: 2026-09-07
Branch: `ivy/cs2-week04-buildout` (source worktree branch
`ivy/cs2-week04-buildout-source`, to be published to the authorized ref)
Work file: `foreman_interface/jobs/tasks/ivy_cs2_week04_buildout.md`

## Source truth inspected

- Canonical `computer_science_2` was clean on local `main` at `7311efe` but
  diverged from fetched `origin/main` (`main` was 1 ahead/154 behind). The
  managed source worktree was therefore allocated explicitly from local
  `main`; the canonical checkout was not changed.
- Read the Week 4 plan, gate, and rubric; the Week 2 and Week 3 plan/gate
  pattern; `lessons/classes-and-oop.md`; the CS2 course compiler; and the
  durable-engineering-habits record at `7f4a5e8`.
- The settled Week 4 contract is composition, one invariant, focused
  evidence, plain-language rationale, and AI proposal/diff/test/read/
  accept-or-reject evidence when AI is used. No Week 4 plan change authorizes
  a new AI Fluency pairing; this pass keeps only the existing Decompose the
  Task connection.

## What was built

- `lessons/week-04-composition-and-invariants.md`: a student-facing entry
  with learning targets, the Labor Day bridge, Wednesday refactor path,
  worked `Order`/`Inventory` composition example, invariant test, Friday
  verification/decision card, AI accountability, and submission handoff.
- `planning/week-04.md`: expanded the stub into the Week 4 overview with
  Wednesday/Friday student evidence path and tokenized links to lesson, gate,
  and rubric.
- `assignments/odyssey_gates/week-04.md`: preserved the settled gate while
  adding the 25-point submission contract, lesson/rubric token links, and an
  explicit Week 3 object handoff.

No other week, grading weight, course, Canvas surface, production deploy
path, or `course_foundry/production_deploy.py` entry was touched.

## Cross-reference proof and YELLOW

Source scan found seven well-formed `{{link:key}}` references across the
three Week 4 student-facing files. They use the established token syntax and
never contain a hand-authored repository or Canvas path. The current shared
CS2 compiler does not yet invoke a CS2 link resolver (its live resolver is
CS1-specific and only maps the existing Week 2 slide key). Therefore these
tokens are source-wired but cannot be claimed as live URL-resolved in this
source-only run. **YELLOW:** a separate shared `course_foundry` resolver
follow-up is needed before any deployment; no deployment was attempted.

## Rubric and points before/after

- Week 4 rubric SHA-256 before and after: `619c27ab0094d9a51b66b410d48c44b1364325691b1fb836bc5ef392701f98fd`
  (byte-identical; no rubric text or criterion changed).
- The existing compiler declaration remains 25 points with criteria 8/7/6/4
  (total 25). The assignment now states that same 25-point contract; no
  grading weight changed.

## Focused validation

- `git diff --check`: PASS.
- Token-shape scan: PASS; 7 tokens, all closed, all in markdown links, no
  bare path links introduced.
- Rubric byte comparison: PASS; unchanged SHA-256 above.
- `pytest tests/test_cs2_desired_course.py`: not runnable because this host's
  Python environment has no `pytest` (`No module named pytest`).
- Direct CS2 compiler import: not runnable because the host environment has
  no `pydantic` (`ModuleNotFoundError`). This is an environment limitation,
  not treated as a source test pass.

## Handoff

The source package is ready for Anna review, with the resolver limitation
explicitly carried as YELLOW. Commit `bfd217c` was pushed to
`origin/ivy/cs2-week04-buildout` as a new normal branch ref; no merge or
promotion was performed.

IVY CS2 W4 READY FOR ANNA
