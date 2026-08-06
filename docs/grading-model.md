# COMSC 1053 — Grading Model (DRAFT PROPOSAL)

**Status: decided by Jeremy, 2026-08-06.** CS2 retains CS1's no-traditional-
tests model: points attach to weekly artifacts, the final is a reflection,
and the Coding Odyssey is the technical spine. Percentages below are the
confirmed CS1 structure, carried into CS2 unchanged.

**Reconciled 2026-08-06:** the “weekly reinforcement assignment” and
“Coding Odyssey checkpoints” are two grains of the *same* CS2 project, not
separate assignments. Every technical week applies its Deitel concept in the
student's Odyssey world; the weekly gate or checkpoint is the reinforcement
assignment. See `assignments/A1-weekly-coding-practice.md` and
`docs/curriculum/judgment_toolkit.md`.

> **Final:** the final is a **reflection paper**, based on
> `assignments/A5-final-reflection.md`. Confirm university finals policy at
> syllabus finalization.

## Proposed weights

| Category | Weight | Cadence | Notes |
|---|---:|---|---|
| Monday Moment quiz | 6% | weekly | Short; checks the AI-fluency principle of the week |
| Wacky Wednesday reflection | 6% | weekly | Tie-in to the week |
| Fun Friday reflection | 6% | weekly | Tie-in to the week |
| Paired-programming report | 5% | weekly | Student's own contribution, honestly assessed |
| Friday feedback report | 5% | weekly | Quality of feedback the student gave |
| Weekly reinforcement assignment | 25% | weekly | Two axes: result 15% + process 10%. Result = that week's CS2 Coding Odyssey gate + Light Build continuation (Weeks 2–5, 7–8, 10–13). |
| Coding Odyssey checkpoints | 15% | 4 checkpoints (Wk 6/9/14/16) | Periodic grading pass on the same project — full four-axis Build rubric, not the weekly gate's pass/fail. The checkpoints integrate exceptions/modules/files; inheritance; recursion/plotting; and searching/sorting plus the full project. |
| Final reflection paper | 10% | finals week | Template basis: `assignments/A5-final-reflection.md`; confirm finals policy |
| Attendance & participation | 20% | daily | Historical policy; confirm language at syllabus finalization |
| Course evaluation | 2% | end of term | Carried from current model |
| **Total** | **100%** | | |

Weekly categories inherit the standing two-week late window, subject to
syllabus finalization; decide any drop-lowest rule then.

## The two-axis rubric for the weekly reinforcement assignment

**Axis 1 — the working result (15 points of the 25).** For gate weeks, this
is that week's Odyssey Quick Check (pass/fail floor) plus the Light Build
continuation band, mapped onto the historical effort-based ladder: gate not
yet passed sits around 25% of the axis; gate passed with minimal continuation
50–75%; gate passed with a solid-to-strong continuation 100%. For checkpoint
weeks, the four-axis Full Build rubric (`docs/curriculum/judgment_toolkit.md`
§2) stands in for this axis directly.

**Axis 2 — process (10 points of the 25).** Knowledge management and
resource tracking are part of the ethos. Four dimensions, graded from what
the student submits:

| Dimension | What earns points | Evidence submitted |
|---|---|---|
| **Rhetoric** | Interrogated the question — restated it, challenged an assumption, or justified taking it as written — rather than silently answering it | 2–3 sentences at the top of the submission |
| **Planning** | A plan existed before code and the submission notes where reality diverged from it | Outline, pseudocode, flowchart, or steps |
| **Resource budgeting** | Tracks every service/model/tier used, limits hit, and why that tool fit; different models fit different work. **Graded on tracking and reasoning, never on money spent** | Tool-and-limits ledger |
| **Knowledge management** | Prompts and chats are tracked well enough to find and reuse next week | Prompt/chat log attached or linked |

Scoring per dimension: 0 (absent) / 1 (present) / 2 (present and thoughtful),
× 4 dimensions = 8, plus 2 points for an organized, reusable package = 10.

## What this replaces

The prior working model's broad homework/practice/project bucket is split
into named categories. The technical content remains one persistent project:
at greater depth, students use robust error handling, reusable modules and
persistent files, inheritance, recursion, plots, and algorithmic choices in
their own world. This application follows the confirmed CS2 course map
(`docs/curriculum/course-sequence.md`; Deitel, *Intro to Python for Computer
Science and Data Science*, exceptions through searching/sorting topics).

## Pair-work grading rule

Pairs may share one repository. Each student documents their own
contributions, and the pair's git log must show a lines-of-code split no more
lopsided than 80/20. The paired-programming report is where each student
narrates their side. Driver/navigator work and AI as a collaborator are
historical CS2 texture, not a substitute for explainable individual work
(`docs/reports/curriculum-history-synthesis.md`).

## Open decisions

- [ ] Confirm university finals policy accepts a reflection paper.
- [ ] Confirm or adjust the carried-forward percentages at syllabus finalization.
- [ ] Decide the drop-lowest policy per weekly category.
- [ ] Decide Canvas submission locations.
- [ ] Decide how automated feedback informs, without replacing, professor scoring.
