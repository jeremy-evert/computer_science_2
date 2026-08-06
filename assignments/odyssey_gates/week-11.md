# Odyssey Gate — Week 11: Choose the right repetition (Recursion, Part 2)

**Concept:** recursive decomposition versus iteration (Deitel, §11.5, “Recursion vs. Iteration”). **Arc:** 3 — Worlds That Think About Their State. **Instrument:** Quick Check + Decide/Compare #1 — see `docs/curriculum/judgment_toolkit.md` §1/§3.

## The gate (do this first)

Choose one genuine world problem that can be solved recursively and implement its recursive decomposition. The recursive case must do meaningful work on a smaller subproblem; a normal trace must reach more than one recursive level.

## Quick Check (pass/fail)

- [ ] The recursive function solves a real world problem, not an isolated factorial-style demo.
- [ ] Each recursive case makes progress toward a base case and the live run reaches at least two levels.
- [ ] The result is used by the world (a decision, report, state update, or visible outcome).

## Decide/Compare #1 (mandatory)

Before comparing, commit in writing: should this feature use recursion or iteration? Then compare the real alternative for *this* world: clarity of the decomposition, termination/traceability, and any cost or awkwardness. State whether the comparison confirmed or changed your call.

## Suggested textbook problem (optional scaffolding)

- **Frontier Settlement:** recursively inspect connected land parcels for available routes.
- **Investigation Bureau:** recursively follow a clue tree until a terminal lead.
- **Starship Log:** recursively inspect a nested system/component tree.
- **Small Business:** recursively total a nested category/order structure.

## Then: open continuation (light Build, holistic)

Improve the base case or input validation after you have a working trace; do not turn this into a hidden loop.

## World Bible

Log the recursive design choice, alternative, and what the comparison changed.

## Looking ahead

Week 12 turns accumulated world data into a view a human can read quickly.
