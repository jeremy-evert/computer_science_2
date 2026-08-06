# Odyssey Gate — Week 5: The world remembers between visits

**Concept:** files — context-managed text or CSV input/output and persistence
across runs (Chapter 12 in the zyBooks numbering; Deitel, *Intro to Python
for Computer Science and Data Science*, text-file processing, `with`, and CSV
topics). **Arc:** 1 — Robust, Reusable, Persistent. **Instrument:** Quick
Check (pass/fail) — see `docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Make one meaningful piece of world state survive the program ending. Use
`with open(...)` (or a context-managed CSV operation) to save a record or
small collection, then on a **separate next run** load that same data and use
it in a visible world result. Include a short transcript or two-run demo that
makes the persistence clear.

## Quick Check (pass/fail)

- [ ] A context-managed file operation writes meaningful world state in a
      documented text or CSV format.
- [ ] A separate run reads the saved data and reconstructs enough state to
      use it, rather than only displaying the raw file.
- [ ] The demonstrated second run proves that a value from the first run
      survived (not merely a pre-seeded sample file).

All three present → pass. Missing any → not yet; resubmit, this is a gate,
not a one-shot.

## Suggested textbook problem (optional scaffolding)

The general problem: write one or more world records with `with open(...)`;
on the next run, read each record, split or use `csv.reader`, and produce a
status line computed from the loaded values. If using CSV, open with
`newline=''` and use the `csv` module rather than manually splitting quoted
fields.

- **Frontier Settlement:** save food stores and colonist count, then reload
  them to calculate rations per colonist.
- **Investigation Bureau:** save case IDs and priorities, then reload them to
  identify the next case to review.
- **Starship Log:** save fuel and hull readings, then reload them to print a
  pre-flight status.
- **Small Business:** save item names and quantities, then reload them to
  report available inventory.

Do this version directly if it helps, then let it *be* your gate submission —
you do not need a second, different one.

## Then: open continuation (light Build, holistic)

Add a second record type, a readable header, or a careful missing-file path if
it serves the world. Do not overwrite your only useful data accidentally:
choose file mode deliberately.

## World Bible

One line: what state now persists, what the second run recovered, and what
file/data-format debt remains.

## Looking ahead

Week 6 is Checkpoint 1: connect robust exceptions, your module boundary, and
persistent data in one working world pass.
