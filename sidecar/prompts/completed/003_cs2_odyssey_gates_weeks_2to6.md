# Prompt 003 — CS2 Coding Odyssey gates + rubrics: Weeks 2-6

**Status: decided by Jeremy 2026-08-06. Ready to execute. Runs in parallel
with prompt 002 (skeleton) and prompt 004 (weeks 7-17) — this prompt only
touches weeks 2-6 files, the other two touch disjoint file sets.**

## Context

Same background as `prompts/002_cs2_odyssey_spine_and_skeleton.md` — read
that file's Context section first, it is not repeated in full here. CS1
(`/mnt/brandy_nvme/jevert/git/computer_science_1`) proved a per-week
"Odyssey Gate" format: a short, mechanically-checkable Quick Check tied to
one concept, plus an optional suggested-textbook-problem scaffold per genre,
plus a matching rubric file with a pass/fail Quick Check table and a
"grading notes" section. Read these two CS1 files in full before writing
anything — they are the exact shape to mirror:

- `computer_science_1/assignments/odyssey_gates/week-05.md`
- `computer_science_1/rubrics/odyssey_gates/week-05_rubric.md`

Also skim 2-3 more CS1 week files (`week-02.md`, `week-07.md`,
`week-12.md` and their rubrics) to see how the format flexes for different
concept types (a first-checkpoint week, a functions week, a classes week).

## Chapter-numbering convention (resolves a real conflict found 2026-08-06)

The chapter numbers in this prompt (10 Exceptions, 11 Modules, 12 Files,
13 Inheritance, 14 Recursion, 15 Plotting, 16 Searching/Sorting) are
**zyBooks' *Programming in Python 3* chapter numbers** (confirmed directly
against `curriculum_rag_supporter/books/Programming in Python 3 with
zyLabs _ zyBooks.pdf`'s own table of contents — exact match), which is the
department-standard numbering other CS1 faculty already use and what CS1's
own week files already cite. **They do NOT match the Deitel PDF's own
printed chapter numbers** (Deitel's ch.9 is "Files and Exceptions"
combined, ch.10 is OOP, ch.11 is "Recursion, Searching, and Sorting"
combined — a different, incompatible scheme). Jeremy's resolution
(2026-08-06): cite "Chapter N" using the zyBooks numbering throughout —
that's the standing convention, not a per-file judgment call. Use the
Deitel PDF as source material for topical content/depth/examples, cited by
topic, not by its own chapter number. If a document needs a citation
sentence, phrase it like CS1's own files do (e.g. "chapter 10's exceptions
concept") — do not add a Deitel chapter number anywhere.

## The confirmed chapter mapping for weeks 2-6 — do not redesign, only build

| Week | Topic (Deitel ch.) | Note |
|---|---|---|
| 2 | Exceptions (10), part 1 | try/except, catching specific exception types |
| 3 | Exceptions (10), part 2 | raising exceptions, custom exception classes, robust input validation |
| 4 | Modules (11) | writing/importing a module, `__name__ == "__main__"`, namespacing |
| 5 | Files (12) | reading/writing text and/or CSV, persistence across runs |
| **6** | **Checkpoint 1** | Exceptions+Modules+Files integration — same four-axis "Build" checkpoint rubric shape as `computer_science_1/rubrics/odyssey_gates/week-06_rubric.md` (read it), not a plain gate |

**Same Odyssey world/genre menu as CS1's four genres** (Frontier Settlement,
Investigation Bureau, Starship Log, Small Business) unless prompt 002's
report flags a genuine reason CS2 needs its own menu — check
`reports/002_cs2_odyssey_spine_and_skeleton.md` if it exists yet; if it
doesn't exist yet (parallel execution), use CS1's exact four genres as the
default and note the assumption in your own report.

## Task

For each of weeks 2, 3, 4, 5: write
`assignments/odyssey_gates/week-0N.md` and
`rubrics/odyssey_gates/week-0N_rubric.md`, matching CS1's week-05 format
exactly (Concept/Arc/Instrument header, "The gate" section, Quick Check
checklist, optional suggested-textbook-problem per genre, "open
continuation" section, World Bible one-liner, "Looking ahead" pointer to
the next week). Ground each gate's concept in the Deitel chapter 10/11/12
content (`curriculum_rag_supporter/books/Intro to Python for Computer
Science and Data Science...pdf`) — the gate should test something real
about exceptions/modules/files, not a generic restatement.

For week 6: write `assignments/odyssey_gates/week-06.md` and
`rubrics/odyssey_gates/week-06_rubric.md` as **Checkpoint 1**, matching
`computer_science_1/assignments/odyssey_gates/week-06.md` and its rubric's
checkpoint shape (the four-axis Build rubric referenced in
`docs/curriculum/judgment_toolkit.md` §2 — read that section, in
`computer_science_1/docs/curriculum/judgment_toolkit.md` if the CS2 copy
doesn't exist yet from prompt 002) — integration across exceptions,
modules, and files, not a single new concept.

Depth requirement per Jeremy's "same areas, greater depth" framing:
CS2's gates should ask for more — e.g. a custom exception class, not just a
caught built-in one; a module with more than one function; file
persistence that survives and is reloaded on the next run — rather than the
minimum-viable version CS1 asked for at the equivalent concept depth.

## Explicitly out of scope

- Weeks 1, 7-17 — prompt 004 or prompt 002 cover those. Do not create or
  edit anything under those week numbers.
- Skeleton documents (`docs/grading-model.md`, `docs/course-ethos.md`,
  `docs/curriculum/judgment_toolkit.md`, `assignments/A1`/`A2`/`A5`,
  `planning/week-NN.md`) — prompt 002 owns those.
- Shared-strand content (Monday Moment, Wacky Wednesday, Fun Friday,
  Paired Programming, Show and Tell) — not this repo's job.
- Any live Canvas/Savnac push.

## Requirements

- Read the named CS1 source files in full before writing CS2 counterparts.
- Ground technical content in the Deitel PDF, cite what's drawn from where
  a claim needs grounding (matching CS1's own judgment_toolkit.md
  citation bar).
- If a genuine ambiguity surfaces, stop and report it rather than guessing.
- Do not commit — leave edited files for review.

## Report Requirement

Write `reports/003_cs2_odyssey_gates_weeks_2to6.md`: what was built per
week, how each gate's depth exceeds CS1's equivalent-concept baseline, any
assumptions made about the genre menu (since this runs in parallel with
002), and any open questions.
