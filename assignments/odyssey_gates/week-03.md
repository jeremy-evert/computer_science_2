# Odyssey Gate — Week 3: The world enforces one rule

**Concept:** exceptions, Round 2 — raising an exception, a custom exception
class, and robust validation (Chapter 10 in the zyBooks numbering; Deitel,
*Intro to Python for Computer Science and Data Science*, explicitly raising
exceptions and custom-exception topics). **Arc:** 1 — Robust, Reusable,
Persistent. **Instrument:** Quick Check (pass/fail) — see
`docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Give your world one rule that cannot be represented by Python's ordinary
type conversion alone — for example, a negative inventory transfer, an
impossible case priority, or an unavailable crew action. Define a custom
exception class for that rule. A validation function must raise it with a
useful message; a caller must catch it, explain the failed action, and leave
the world's valid state unchanged.

## Quick Check (pass/fail)

- [ ] A custom exception class is defined and is used for one named world
      rule (not merely declared).
- [ ] A validation function raises that exception on invalid input or state,
      with a message that identifies the problem.
- [ ] A caller catches the custom exception; a demonstrated rejected action
      leaves the relevant state unchanged and the program can continue.

All three present → pass. Missing any → not yet; resubmit, this is a gate,
not a one-shot.

## Suggested textbook problem (optional scaffolding)

The general problem: define `class InvalidWorldAction(Exception): pass` (or a
more specific name), then write `validate_...()` that raises it before an
invalid state change. Catch it at the command boundary and show both the
message and unchanged state.

- **Frontier Settlement:** reject a food distribution larger than current
  stores with `InsufficientRationsError`.
- **Investigation Bureau:** reject a case priority outside 1–5 with
  `InvalidPriorityError`.
- **Starship Log:** reject a jump that requires more fuel than remains with
  `InsufficientFuelError`.
- **Small Business:** reject a sale quantity larger than inventory with
  `OutOfStockError`.

Do this version directly if it helps, then let it *be* your gate submission —
you do not need a second, different one.

## Then: open continuation (light Build, holistic)

Add another rule only if it clarifies the world. The aim is a clear boundary
between validation, the attempted change, and the command that reports the
problem — not an elaborate exception hierarchy.

## World Bible

One line: what rule the world now protects, what rejected action you tested,
and what validation debt remains.

## Looking ahead

Week 4 packages related validation and world behavior in an imported module
so the main program has a clear boundary too.
