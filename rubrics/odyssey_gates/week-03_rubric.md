# Odyssey Gate — Week 3 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Named custom exception | A custom exception class exists and represents a real named world rule. |
| Validation raises it | A validation function explicitly raises that exception with a useful message when the rule is violated. |
| Safe recovery | A caller catches that exception; a demonstrated rejected action reports the failure and preserves the relevant pre-action state. |

**All three present → pass.** Any missing → not yet. Class definition,
`raise`, and a named handler are statically checkable; unchanged state needs
a brief run trace or focused human check.

## Part 2 — Light Build (holistic)

Same three-band shape as `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- Raising `ValueError` alone does not meet this CS2-depth gate; the custom
  class must be defined and used.
- A custom exception caught inside the same validation function without a
  caller-level recovery path does not demonstrate the intended boundary.
- “State unchanged” means validation occurs before the relevant mutation, or
  the work is reliably rolled back; printing an error after changing the
  value is not enough.
- The World Bible line is required but reviewed cumulatively at finals.
