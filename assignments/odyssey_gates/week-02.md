# Odyssey Gate — Week 2: The world survives a bad command

**Concept:** exceptions, Round 1 — a small `try` suite and specific exception
handlers (Chapter 10 in the zyBooks numbering; Deitel, *Intro to Python for
Computer Science and Data Science*, exception-handling topic). **Arc:** 1 —
Robust, Reusable, Persistent. **Instrument:** Quick Check (pass/fail) — see
`docs/curriculum/judgment_toolkit.md` §1.

## The gate (do this first)

Give your world one input-driven command that can fail in **two different,
expected ways**. Put only the conversion or operation that may fail in a
`try` suite, catch each expected exception by its specific type, and let the
program continue with a useful world-facing message. A good shape is a
numeric command that handles non-numeric input and a zero or out-of-range
value separately.

## Quick Check (pass/fail)

- [ ] A bounded `try` suite contains the operation that can actually raise an
      exception.
- [ ] At least two expected exception types are caught by specific handlers,
      not `except:` or one generic catch-all.
- [ ] A demonstrated bad input reaches a world-facing recovery message and
      the program continues to a usable next step.

All three present → pass. Missing any → not yet; resubmit, this is a gate,
not a one-shot.

## Suggested textbook problem (optional scaffolding)

The general problem: request a number for one world action; distinguish text
that cannot become an integer from a value that cannot safely perform the
action. The `try` body should stay small enough that each handler has a clear
meaning.

- **Frontier Settlement:** ask how many rations to distribute; distinguish
  `ValueError` from `ZeroDivisionError` when calculating a per-colonist share.
- **Investigation Bureau:** ask how many hours to allocate to a lead;
  distinguish invalid numeric input from division by zero when calculating a
  lead rate.
- **Starship Log:** ask for a jump divisor; distinguish invalid input from a
  zero divisor before reporting fuel-per-jump.
- **Small Business:** ask for a number of invoices; distinguish invalid input
  from a zero divisor before reporting average sale.

Do this version directly if it helps, then let it *be* your gate submission —
you do not need a second, different one.

## Then: open continuation (light Build, holistic)

Once the gate passes, add one or two more meaningful commands or recovery
paths. Keep failure messages useful to the person using the world; do not
turn every line into a `try` statement.

## World Bible

One line: what bad command your world now survives, what broke, and what
error path you still need to handle.

## Looking ahead

Week 3 moves the validation rule into reusable code: a function will reject
invalid world state by raising a named, custom exception.
