# Prompt 004 — CS2 Coding Odyssey gates + rubrics: Weeks 7-17

**Status: decided by Jeremy 2026-08-06. Ready to execute. Runs in parallel
with prompt 002 (skeleton) and prompt 003 (weeks 2-6) — this prompt only
touches weeks 7-17 files, the other two touch disjoint file sets.**

## Context

Same background as `prompts/002_cs2_odyssey_spine_and_skeleton.md` and
`prompts/003_cs2_odyssey_gates_weeks_2to6.md` — read both files' Context
sections first, not repeated in full here. Read these CS1 source files in
full before writing anything (the exact shapes to mirror):

- `computer_science_1/assignments/odyssey_gates/week-05.md` +
  `rubrics/odyssey_gates/week-05_rubric.md` (plain gate shape)
- `computer_science_1/assignments/odyssey_gates/week-09.md` +
  its rubric, and `week-14.md`/`week-16.md` + rubrics (checkpoint shape —
  four-axis Build rubric)
- `computer_science_1/assignments/A5-final-reflection.md` (Week 17 finals
  shape)
- `computer_science_1/docs/curriculum/judgment_toolkit.md` (all five
  instruments — Decide/Compare and Debrief in particular are used at
  weeks 10-11 and checkpoint closes, read §3/§4)

## The confirmed chapter mapping for weeks 7-17 — do not redesign, only build

| Week | Topic (Deitel ch.) | Note |
|---|---|---|
| 7 | Inheritance (13), Round 1 | base/derived classes, `super()`, overriding methods |
| 8 | Inheritance (13), Round 2 | polymorphism, multiple derived classes interacting — mirrors CS1's "classes Round 2" (`week-13.md`) making world objects interact |
| **9** | **Checkpoint 2** | Inheritance checkpoint — four-axis Build rubric, same shape as `computer_science_1/rubrics/odyssey_gates/week-09_rubric.md` |
| 10 | Recursion (14), part 1 | base case + recursive case, tracing |
| 11 | Recursion (14), part 2 | a real recursive decomposition of a world problem — this is also a **Decide/Compare** instrument point per `judgment_toolkit.md` §3 (a real design choice between a recursive and iterative solution, defended) |
| 12 | Plotting/data exploration (15) | simple visualization of world-state data over the semester (e.g. a plot of the World Bible's own accumulated stats) |
| 13 | Searching, sorting, Big-O (16) | tracing, comparison, Big-O intuition applied to the student's own world data |
| **14** | **Checkpoint 3** | Recursion+Plotting integration — four-axis Build rubric, mirrors `week-14_rubric.md` |
| **16** | **Checkpoint 4** | Searching/sorting + full-semester integration — four-axis Build rubric, mirrors `week-16_rubric.md`, this is also a capstone **Decide/Compare** point per `judgment_toolkit.md` §3 |
| 17 (finals) | Final portfolio | mirror `computer_science_1/assignments/A5-final-reflection.md` and `computer_science_1/planning/week-17-finals.md`; the Debrief instrument (§4) closes here — CS2's version should ask students to reflect across the *whole* semester (CS1 concepts they're assuming as background, plus CS2's own chapters 10-16) |

Week 15 is a buffer/async week in CS1 (no gate) — mirror that unless
prompt 002's report (if it exists yet) says otherwise; note the assumption
if it doesn't exist yet, same as prompt 003.

**Same Odyssey world/genre menu as CS1's four genres** (Frontier Settlement,
Investigation Bureau, Starship Log, Small Business) unless prompt 002's
report flags otherwise — check `reports/002_cs2_odyssey_spine_and_skeleton.md`
if it exists; if not yet, default to CS1's four genres and note the
assumption.

## Task

For weeks 7, 8, 10, 11, 12, 13: write
`assignments/odyssey_gates/week-0N.md` (or `week-NN.md` for 10-13) and
matching rubric files, same plain-gate format as prompt 003's weeks.
Ground each in the relevant Deitel chapter (13-16) content
(`curriculum_rag_supporter/books/Intro to Python for Computer Science and
Data Science...pdf`).

For weeks 9, 14, 16: write the checkpoint-shaped gate + rubric (four-axis
Build rubric per `judgment_toolkit.md` §2), matching CS1's checkpoint
files' structure exactly.

For week 17: write the CS2 equivalent of `A5-final-reflection.md` (if
prompt 002 hasn't created it yet, create it here instead and note that in
your report so nothing gets silently overwritten) and
`planning/week-17-finals.md`.

Depth requirement, same framing as prompt 003: CS2's gates should ask for
more than the minimum-viable version of the equivalent CS1 concept —
e.g. inheritance week 8 should require actual polymorphic behavior (calling
the same method name on different subclasses and getting different real
behavior), not just a derived class that exists; recursion should require a
real recursive case with more than one level of actual recursion in a live
trace, not a disguised loop.

## Explicitly out of scope

- Weeks 1-6 — prompt 003 covers those. Do not create or edit anything
  under those week numbers.
- Skeleton documents — prompt 002 owns those; if you need
  `docs/curriculum/judgment_toolkit.md` and it doesn't exist yet in this
  repo, read CS1's copy directly instead of creating your own competing
  version.
- Shared-strand content — not this repo's job.
- Any live Canvas/Savnac push.

## Requirements

- Read the named CS1 source files in full before writing CS2 counterparts.
- Ground technical content in the Deitel PDF, cite what's drawn from where
  grounding matters.
- If a genuine ambiguity surfaces, stop and report it rather than guessing.
- Do not commit — leave edited files for review.

## Report Requirement

Write `reports/004_cs2_odyssey_gates_weeks_7to17.md`: what was built per
week, how depth exceeds CS1's equivalent baseline, any assumptions made in
parallel with 002/003, and open questions.
