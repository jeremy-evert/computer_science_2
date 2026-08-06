# Odyssey Gate — Week 7 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, human-checkable)

| Criterion | Pass condition |
|---|---|
| Real hierarchy | The base/subclass pair is a defensible is-a relationship in this world. |
| Shared setup | The subclass uses `super().__init__` for inherited state, then adds/refines its own state. |
| Real override | The same method name has specialized behavior, demonstrated in a run. |

**All three present → pass.** This needs a brief human read: syntactically valid inheritance can still model the wrong relationship.

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 — see `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- Copying the base initializer into the subclass does not pass shared setup.
- A changed `__repr__` alone is insufficient unless it reflects a real specialized behavior in the demonstrated world.
- The World Bible line is required but reviewed cumulatively at finals.

