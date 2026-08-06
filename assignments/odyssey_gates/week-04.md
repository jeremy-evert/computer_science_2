# Odyssey Gate — Week 4: The world has a tool chest

**Concept:** modules — a deliberate module boundary, imports, module
namespaces, and `__name__ == "__main__"` (Chapter 11 in the zyBooks
numbering; Deitel, *Intro to Python for Computer Science and Data Science*,
module and namespace topics). **Arc:** 1 — Robust, Reusable, Persistent.
**Instrument:** Quick Check (pass/fail) — see
`docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Move one coherent piece of your world into its own module: related validation,
formatting, or state-operation functions belong together. The module must
export **at least two functions** that the main program imports and uses
through the module namespace. Include a small direct-run demonstration behind
`if __name__ == "__main__":` so importing the module does not run that demo.

## Quick Check (pass/fail)

- [ ] A separate project module defines at least two related, usable
      functions.
- [ ] The main program imports that module and calls both functions through
      the module namespace (for example, `world_tools.validate_move(...)`).
- [ ] A direct-run block exists; importing the module does not trigger its
      demonstration or other unintended output.

All three present → pass. Missing any → not yet; resubmit, this is a gate,
not a one-shot.

## Suggested textbook problem (optional scaffolding)

The general problem: make a `world_tools.py` module with one validation
function and one formatting/status function. In `main.py`, use
`import world_tools`; run the world through `main.py`, then separately run
`world_tools.py` to show its guarded demo.

- **Frontier Settlement:** `settlement_tools.py` validates a ration request
  and formats a food-status line.
- **Investigation Bureau:** `case_tools.py` validates case priority and
  formats a case-status line.
- **Starship Log:** `ship_tools.py` validates a fuel request and formats a
  system-status line.
- **Small Business:** `inventory_tools.py` validates a sale and formats an
  inventory-status line.

Do this version directly if it helps, then let it *be* your gate submission —
you do not need a second, different one.

## Then: open continuation (light Build, holistic)

Keep module boundaries meaningful. Move related behavior when it reduces
confusion, but do not split every tiny function into its own file.

## World Bible

One line: what the new module owns, what import or namespace problem broke,
and what still belongs in the main program.

## Looking ahead

Week 5 gives the world memory: meaningful state will be written to a file and
loaded again on a later run.
