# Odyssey Gate — Week 2 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Bounded risky operation | A `try` suite encloses the conversion or operation that can raise, rather than an unrelated large block. |
| Specific recovery paths | At least two expected exception types have named `except` handlers; a bare `except:` does not count. |
| Continues after bad input | A demonstrated invalid-input path prints a useful world message and reaches a usable next command or retry. |

**All three present → pass.** Any missing → not yet. Static review can detect
the `try`/`except` structure and named types; the continued, usable recovery
path needs a short behavioral trace.

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 in the CS1 model:

| Band | What it looks like |
|---|---|
| Strong | Recovery paths feel like real parts of this world and make more than the gate's minimum usable. |
| Solid | Gate passed, with a real continuation beyond the minimum. |
| Minimal | Gate passed, little to no continuation. |

## Grading notes

- Do not award “specific recovery paths” for `except Exception` or bare
  `except:` when the program can name the expected types.
- The two cases must be meaningfully different; duplicate messages for two
  handlers without a distinct recovery explanation are not enough.
- The World Bible line is required but reviewed cumulatively at the final
  Judgment Log checkpoint, not scored separately here.
- Light Build is graded separately and holistically, not as partial credit on
  the gate.
