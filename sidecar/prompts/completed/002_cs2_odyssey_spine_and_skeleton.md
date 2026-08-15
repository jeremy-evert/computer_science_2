# Prompt 002 — CS2 Coding Odyssey spine: skeleton documents

**Status: decided by Jeremy 2026-08-06. Ready to execute.**

## Context

CS1 (`/mnt/brandy_nvme/jevert/git/computer_science_1`) already proved a
course structure that works: one persistent per-student Coding Odyssey
project as the spine, weekly gates tied to a textbook chapter, four
checkpoints, a five-instrument "judgment toolkit" (Quick Check / Build /
Decide-Compare / Debrief / Judgment Log), and five shared cross-course
strands (Monday Moment, Wacky Wednesday, Fun Friday, Paired Programming,
Show and Tell) that are IDENTICAL across CS1/CS2/DSCT and are NOT part of
this task — do not touch or recreate them here.

Jeremy's explicit call, 2026-08-06: CS2 should reuse this same structure
almost exactly ("if CS2 looks a lot like CS1, that is okay"), applied to
the *next* stretch of the Deitel textbook (*Intro to Python for Computer
Science and Data Science*, already in `curriculum_rag_supporter/books/`) at
greater depth, using the CS2 Canvas archive's own historical durable
sequence (already synthesized in this repo:
`docs/curriculum/course-sequence.md`, `docs/curriculum/unit-notes.md`,
`docs/reports/curriculum-history-synthesis.md`) plus the old zyBooks
assignment signals (driver/navigator pair programming with AI as a
collaborator, "Coding Quest" duplicate practice, three-problems+mini-report
depth) as texture/depth references, not verbatim imports.

## The confirmed chapter/week mapping — do not redesign this, only build it

CS1 covers Deitel chapters ~1-9 (variables, branching x2, loops, functions,
strings, lists/dicts, classes x2). CS2 continues into chapters 10-16:

| Weeks | Topic (Deitel ch.) | Depth note |
|---|---|---|
| 2-3 | Exceptions (10) | two weeks — a harder topic gets two rounds, same pattern CS1 used for classes |
| 4 | Modules (11) | |
| 5 | Files (12) | |
| **6 (checkpoint 1)** | Exceptions+Modules+Files integration | |
| 7-8 | Inheritance (13) | two weeks, mirrors CS1's "classes Round 1/2" |
| **9 (checkpoint 2)** | Inheritance checkpoint | |
| 10-11 | Recursion (14) | two weeks — historically the hardest topic per the archive synthesis |
| 12 | Plotting/data exploration (15) | |
| 13 | Searching, sorting, Big-O (16) | |
| **14 (checkpoint 3)** | Recursion+Plotting checkpoint | |
| **16 (checkpoint 4)** | Searching/sorting + full integration checkpoint | |
| 17 (finals) | Final portfolio, same project continued/leveled-up | |

**Use week NUMBERS, not calendar dates — CS2's real Fall 2026 meeting
schedule (days/times/room) is not yet known to this prompt.** Leave a
`[[DATE: week N — TBD, confirm against real CS2 section schedule]]`
placeholder anywhere CS1's own template has a real date. Do not invent
dates. Do not assume CS2 meets the same days/times as CS1 (MWF) — it may
not.

## Task — build these skeleton/spine documents only

Mirror each CS1 source file's *structure and shape* exactly, adapted to
CS2's chapter mapping above. Read every CS1 file listed below in full
before writing its CS2 counterpart — do not guess the shape from this
prompt's summary alone.

1. **`docs/grading-model.md`** — mirror
   `/mnt/brandy_nvme/jevert/git/computer_science_1/docs/grading-model.md`'s
   exact category structure and weights (Monday Moment 6%, Wacky Wednesday
   6%, Fun Friday 6%, Paired-programming 5%, Friday feedback 5%, Weekly
   reinforcement 25%, Odyssey checkpoints 15%, Final reflection 10%,
   Attendance 20%, Course evaluation 2%) — same categories, same weights,
   CS2-specific description text where the category ties to CS2's own
   Weekly reinforcement/checkpoint content.
2. **`docs/course-ethos.md`** (new file, CS1 has one at
   `computer_science_1/docs/course-ethos.md`) — same voice/purpose, adapted
   to CS2's "greater depth, same spine" framing Jeremy gave directly.
3. **`docs/curriculum/judgment_toolkit.md`** — mirror
   `computer_science_1/docs/curriculum/judgment_toolkit.md`'s five
   instruments exactly (do not redesign the pedagogy — this is a proven,
   RAG-grounded design). Adapt only the concrete examples to CS2-level
   topics (exceptions, inheritance, recursion, etc. instead of loops,
   branching, classes).
4. **`assignments/A1-weekly-coding-practice.md`** and
   **`assignments/A2-coding-odyssey-project.md`** — mirror CS1's same-named
   files at `computer_science_1/assignments/A1-weekly-coding-practice.md`
   and `A2-coding-odyssey-project.md`. A2 in particular needs the genre
   menu section preserved (same four genres, or confirm via
   `computer_science_1/assignments/A2-coding-odyssey-project.md`'s "genre
   menu" section whether CS2 continues the *same* per-student world from
   CS1 or starts a new one at greater rigor — if genuinely ambiguous, flag
   it explicitly in your report rather than guessing).
5. **`assignments/A5-final-reflection.md`** — mirror
   `computer_science_1/assignments/A5-final-reflection.md`.
6. **`planning/week-NN.md`** skeleton files for weeks 1-17 (new
   `planning/` directory, mirroring `computer_science_1/planning/week-NN.md`'s
   shape) — Weekly Focus / gate-or-checkpoint tie-in / Due-this-week
   sections per the table above, dates left as `[[DATE: TBD]]`
   placeholders. Week 1 should note it's the universal cross-course Week 1
   (same as CS1 — don't reinvent it, just reference
   `semester_kickoff_week`).

## Explicitly out of scope — other prompts cover these, do not touch

- `assignments/odyssey_gates/week-NN.md` and their rubrics — a separate
  prompt (003) covers weeks 2-6, another (004) covers weeks 7-17. Do not
  create or edit anything under `assignments/odyssey_gates/` or
  `rubrics/odyssey_gates/`.
- Monday Moment / Wacky Wednesday / Fun Friday / Paired Programming / Show
  and Tell content — identical across CS1/CS2/DSCT, already exists
  elsewhere, not this repo's job to rebuild.
- Anything in `archive/`, `career-artifact-sequence.md`,
  `chapter-coding-practice.md`, `coding-odyssey-project.md` (the old
  pre-pivot placeholder files) — leave those alone; they're historical
  synthesis inputs, not being deleted or edited by this prompt.
- Any live Canvas/Savnac push — this prompt only writes local files.

## Requirements

- Read every CS1 source file named above in full before writing its CS2
  counterpart.
- Ground CS2-specific content (topic descriptions, examples) in the
  Deitel PDF (`curriculum_rag_supporter/books/Intro to Python for Computer
  Science and Data Science...pdf`) and this repo's own archive synthesis
  (`docs/curriculum/`, `docs/reports/`) — cite what you drew from where a
  claim needs grounding, same bar CS1's own judgment_toolkit.md holds.
- Do not invent calendar dates. Do not touch shared-strand content.
- If a genuine ambiguity surfaces (e.g., new vs. continued Odyssey world;
  whether CS2's own historical career-artifact-sequence should map onto
  anything), stop and report it explicitly rather than guessing.
- Do not commit. Leave the working tree as edited files only — Jeremy's
  session will review and commit.

## Report Requirement

Write `reports/002_cs2_odyssey_spine_and_skeleton.md`: what was built, what
was mirrored verbatim vs. adapted, every real ambiguity or open question
found, and confirmation every listed CS1 source file was actually read
(not assumed) before its CS2 counterpart was written.
