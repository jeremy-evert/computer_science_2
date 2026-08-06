# Odyssey Gate — Week 10: The world solves a smaller version (Recursion, Part 1)

**Concept:** recursive functions: base case, recursive case, and tracing calls (Deitel, §§11.2–11.5). **Arc:** 3 — Worlds That Think About Their State. **Instrument:** Quick Check (pass/fail) — see `docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Add one small recursive world operation. It must have an explicit base case and a recursive case that reduces the problem. Show a trace or output proving that one normal input makes at least two recursive calls before the base case.

## Quick Check (pass/fail)

- [ ] The function has a base case that returns a result without another recursive call.
- [ ] Its recursive case calls the same function on a genuinely smaller/simpler world problem.
- [ ] A demonstrated non-base input descends through at least two recursive calls and reaches the base case.

## Suggested textbook problem (optional scaffolding)

The general problem: recursively total or describe a nested/ordered slice of world data, keeping each call's remaining work visible.

- **Frontier Settlement:** recursively total food across a sequence of days.
- **Investigation Bureau:** recursively walk a chain of linked clues.
- **Starship Log:** recursively count unresolved alerts in a nested subsystem list.
- **Small Business:** recursively total a run of transaction amounts.

Do this version directly if it helps, then let it *be* your gate submission.

## Then: open continuation (light Build, holistic)

Keep the trace while developing. It is evidence that the problem shrinks, not a loop disguised as recursion.

## World Bible

One line: base case, shrinking step, what broke.

## Looking ahead

Week 11 asks whether recursion is actually the better design for one real world problem.
