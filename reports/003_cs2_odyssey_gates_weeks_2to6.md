# Prompt 003 — CS2 Odyssey gates, Weeks 2–6 report

## Built

Created paired assignment and rubric files for Weeks 2–6 under
`assignments/odyssey_gates/` and `rubrics/odyssey_gates/`.

| Week | Gate/checkpoint | CS2 depth beyond the CS1 baseline |
|---|---|---|
| 2 | Specific recovery for two expected exception types | Requires a bounded risky operation, two named handlers, and proof that the program continues after bad input. |
| 3 | Custom-exception validation boundary | Requires a custom exception, a function that raises it, caller-level recovery, and proof that rejected state was not mutated. |
| 4 | Real module boundary | Requires two related functions in a local imported module, qualified namespace use, and a working `__name__ == "__main__"` guard. |
| 5 | Persistent file state | Requires context-managed save plus a later separate run that reloads and uses state, not a same-run file print. |
| 6 | Checkpoint 1 integration | Requires one working flow in which validation/error handling, imported reusable code, and two-run persistence interact; assessed with the four Full Build axes. |

## Source and format grounding

Read in full before authoring: CS1 Week 2, 5, 6, 7, and 12 Odyssey-gate
assignments and rubrics, plus CS1's Week 6 checkpoint rubric and the CS2
`docs/curriculum/judgment_toolkit.md` §2. The Week 2–5 files retain the
Concept/Arc/Instrument header; gate; three-item pass/fail checklist;
genre-specific optional scaffold; open continuation; World Bible; and
Looking ahead shape.

Technical gates were grounded in the local Deitel PDF, *Intro to Python for
Computer Science and Data Science*: specific `try`/`except` handling and
small, meaningful try suites; explicit `raise`; custom exceptions; module
`__name__` and namespace behavior; context-managed text-file operations; and
CSV reading/writing. Per the stated standing convention, all student-facing
chapter labels use zyBooks Chapters 10, 11, and 12; no Deitel printed chapter
number is cited.

## Assumptions and open questions

The report from prompt 002 confirms CS1's exact four-genre menu as the CS2
default, but leaves new-CS2-world versus formal-CS1-world continuation for
Jeremy to decide. These gate files therefore refer neutrally to “your Odyssey
world”; their scaffolds use the four default genres without requiring a new
genre pick or founding charter.

Week 6 uses the prompt's explicit four-axis Full Build checkpoint shape
(Functions, Concept use, Explanation, Demonstrability). This matches the CS2
Judgment Toolkit §2, despite the older CS1 Week 6 exemplar using a two-axis,
25-point early-checkpoint variation.

Open question: before student release, resolve Odyssey continuity in
`assignments/A2-coding-odyssey-project.md`; no Week 2–6 gate wording needs
revision unless that choice adds a specific continuation-baseline artifact.
