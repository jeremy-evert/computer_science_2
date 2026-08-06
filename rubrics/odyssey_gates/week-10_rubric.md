# Odyssey Gate — Week 10 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, behavioral)

| Criterion | Pass condition |
|---|---|
| Base case | A clearly reachable case returns without another recursive call. |
| Reduction | The recursive call receives a smaller/simpler version of the problem. |
| Live depth | A normal demonstration makes at least two recursive calls before the base case. |

**All three present → pass.** This is a human/trace check; the important evidence is termination through a shrinking problem.

## Part 2 — Light Build (holistic)

Same three-band shape as Week 2 — see `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- A function that calls itself once and immediately stops on all normal inputs does not pass Live depth.
- A loop doing all meaningful work while a decorative recursive call occurs does not pass Reduction.

