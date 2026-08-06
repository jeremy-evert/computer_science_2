# Odyssey Gate — Week 4 rubric: Quick Check (pass/fail) + light Build

Matches `docs/curriculum/judgment_toolkit.md` §1/§2.

## Part 1 — Quick Check (pass/fail, mechanical-checkable)

| Criterion | Pass condition |
|---|---|
| Coherent module | A separate local module defines at least two related functions that do real world work. |
| Qualified imported use | The main program imports the module and calls both functions via its namespace. |
| Guarded direct run | `if __name__ == "__main__":` protects a direct-run demonstration; import does not run it. |

**All three present → pass.** Any missing → not yet. File/module structure,
function definitions, qualified calls, and the guard are statically
checkable; run the main program once to confirm the import path works.

## Part 2 — Light Build (holistic)

Same three-band shape as `rubrics/odyssey_gates/week-02_rubric.md`.

## Grading notes

- `from module import *` does not meet the qualified-use requirement: this
  gate explicitly tests namespace awareness.
- Two unrelated utility functions placed in a file do not make a meaningful
  module boundary; a brief human read decides coherence.
- A guard with only `pass` is insufficient: it must protect a small,
  runnable direct-run demonstration.
- The World Bible line is required but reviewed cumulatively at finals.
