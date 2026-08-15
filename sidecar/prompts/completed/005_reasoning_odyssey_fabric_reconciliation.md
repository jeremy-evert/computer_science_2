# Prompt 005 — Reconcile CS2 source to the Reasoning Odyssey doctrine (Prompt 126 slice 2 of 4)

## Status

READY. Second course-specific slice of
`jeremy_task_tracking/prompts/126_cross_course_reasoning_odyssey_fabric.md`,
mirroring the accepted CS1 slice
(`computer_science_1/reports/015_reasoning_odyssey_fabric_reconciliation.md`,
`computer_science_1/prompts/015_reasoning_odyssey_fabric_reconciliation.md`)
— read that CS1 report first for the shape of an accepted leaf.

Precedent this must follow exactly:
`jeremy_task_tracking/questions/answered_questions/003_cs1_a2_reasoning_odyssey_project_never_built.md`
(CS1-specific in its wording but the *doctrine* generalizes — the name is
Reasoning Odyssey, checkpoints are synthesis weeks, no second gradebook, no
unpaid required work).

## Why

CS2 already has the real machinery: `assignments/A2-coding-odyssey-project.md`,
a legacy pointer file `assignments/coding-odyssey-project.md`, and 14 weekly
files in `assignments/odyssey_gates/` + matching `rubrics/odyssey_gates/`.
It still uses "Coding Odyssey" naming throughout (18 files hit). Reconcile it
to Reasoning Odyssey exactly the way CS1 was reconciled — same doctrine,
CS2's own weekly content and world options untouched.

## Scope — this leaf only

1. Read `assignments/A2-coding-odyssey-project.md` in full and reconcile its
   title/language to Reasoning Odyssey framing. Keep it as the Week-2 (or
   CS2's actual kickoff week — confirm which week from the file itself, do
   not assume it matches CS1's week number) kickoff/home base. CS2's four
   world options (Frontier Settlement, Investigation Bureau, Starship Log,
   Small Business) are course-specific content — do not alter them.
2. Update `assignments/coding-odyssey-project.md` (the legacy compatibility
   pointer) to point at/reference the Reasoning Odyssey naming too, keeping
   its role as a compatibility pointer.
3. Read all 14 files in `assignments/odyssey_gates/` and their matching
   rubrics in `rubrics/odyssey_gates/`. For each week, verify guidance +
   assignment task + rubric + submission path + points already exist. Where
   "Coding Odyssey" language survives and should read "Reasoning Odyssey",
   fix it. Do not invent or remove weeks.
4. Identify CS2's own checkpoint/synthesis weeks (read the grading model /
   A2 file to find them — do not assume they are Weeks 6/9/14 like CS1;
   confirm from CS2's actual source) and, if they exist, reframe them as
   synthesis checkpoints the same way CS1's were (add a reflect step,
   "no new technical concept" framing) while preserving their point values.
   If CS2 has no such checkpoint weeks defined, do not invent any — say so
   in the report instead.
5. Grep the rest of the repo (`lessons/`, `docs/`, `planning/`, other
   `assignments/`) for "Coding Odyssey" and reconcile only clear
   student-facing/doctrine references. Leave historical/provenance/
   instructor-only planning docs alone unless doctrine clearly calls for the
   change. If unsure, list the hit in the report rather than guessing.
6. Do **not** touch CS2's grading model / weights, do not create a new
   assignment category, do not touch Canvas/Savnac directly (source only),
   do not touch any other course repo.

## Do not

- Do not build a new Odyssey homework track alongside the real weekly gates.
- Do not rename "World Bible" (if CS2 uses that term) or any of CS2's
  course-specific world/genre content.
- Do not change point values or grading weights.
- Do not touch `course_metadata.yaml`'s grading block.
- Do not touch any other repo.

## Deliverable

Write `reports/005_reasoning_odyssey_fabric_reconciliation.md` in this repo
listing: every file changed and why, every "Coding Odyssey" hit found and
whether changed or deliberately left (with reason), confirmation of CS2's
actual checkpoint weeks and whether they were reframed, and confirmation
that grading weights were not touched. Flag any tension or gap explicitly
rather than guessing a resolution — CS1's leaf found and reported one
(Weeks 15/16 ungraded exceptions); CS2 may or may not have an equivalent.
