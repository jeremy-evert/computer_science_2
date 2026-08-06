# Odyssey Gate — Week 8 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, behavioral)

| Criterion | Pass condition |
|---|---|
| Subtype range | Two distinct subclasses share a meaningful base class. |
| Same message | Shared code calls the same meaningful method on both without type-based branching first. |
| Different effects | The run demonstrates different real behavior or state consequences. |

**All three present → pass.** A human should inspect the short run: this is polymorphism, not merely two classes that happen to have similarly named code.

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 — see `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- `if isinstance(...)` deciding which behavior to call does not pass Same message.
- Different printed names with no differing consequence do not pass Different effects.
- This exceeds a mere derived-class existence check: the common interface must run.

