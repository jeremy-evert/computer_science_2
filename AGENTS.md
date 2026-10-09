# AGENTS.md

## Shared Rules

Read and follow the top-level shared instructions: `../AGENTS.md`. Those apply
here unless this file is stricter.

## Repository Purpose

Source material for CS2 (COMSC-1053). Content here becomes student-facing Canvas material.

## Repository-Specific Rules

### Done means tracked and pushed (Jeremy, 2026-10-09)

Git is Jeremy's safety belt. **Anything an agent does is not done until it is
committed and pushed. If it is not in `origin`, it did not happen.**

- Commit and push each completed unit of work immediately (a TDD cycle step, a
  file, a fix). Do not batch, and do not leave work "for later".
- Chat is not a record. Explanations, decisions, and teaching points that
  matter must be written into a file in the repo (e.g. a `NOTES.md` next to
  the work) and pushed, so the next agent and the instructor can find them.
- A red or in-progress state is fine to commit. Say so in the commit message.
  Uncommitted work is the only unacceptable state.
- Never commit secrets, student data, or databases (`*.db`, `*.sqlite*` are
  ignored on purpose). Track the schema and notes, not the data.
- Before ending a turn, run `git status` and confirm the tree is clean and
  `origin/main` matches. Report what was pushed, or say plainly what was not.

### Student work is a shared learning resource (Jeremy, 2026-09-24)

Every student deliverable in this course is authored as a **graded discussion**
where students see each other's work, so student work becomes a resource for
other students. A private assignment or text-entry gate is allowed only for a
real privacy reason (or a documented safety/format reason) recorded in the
week's source. Student-facing text should say that peers will see the work.
Never reveal student names or personal details when quoting work elsewhere.
Full rule: `../jeremy_task_tracking/COURSE_DESIGN_RULES.md`.
