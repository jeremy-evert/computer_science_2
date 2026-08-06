# Coding Odyssey / Choose Your Own Adventure

## Purpose

One persistent, student-chosen project runs the semester and applies each week's concepts as taught. It is CS2's technical spine: the chapter concept is applied inside the student's own world rather than through a separate standalone problem set. This keeps CS1's proven structure while raising the work to exceptions, modules/files, inheritance, recursion, plotting, and algorithmic judgment.

**This is the weekly coding practice assignment.** Each gate below also fulfills `assignments/A1-weekly-coding-practice.md` for that week — they are not two separate submissions.

## Continuity decision — resolved 2026-08-06

**Jeremy's call: fresh world, same four genres.** Every CS2 student starts
a new Odyssey world in Week 2, at CS2's greater rigor from day one — they
do not formally continue whatever world (if any) they built in CS1. This
also keeps CS2 self-contained for any student who didn't take CS1 here.

## Do

1. **Week 2:** pick one of the four genres below and write a one-paragraph
   founding charter — what the world is, who is in it, and what is at
   stake. This starts the World Bible and is the first Judgment Log
   checkpoint.
2. **Gate weeks (2–5, 7–8, 10–13):** pass that week's small Quick Check gate first, then extend the world with anything covered so far. Each specific requirement belongs in `assignments/odyssey_gates/week-NN.md` (rubric: `rubrics/odyssey_gates/week-NN_rubric.md`). Each may include an optional **suggested textbook problem** as private scaffolding, not a second assignment.
3. **Checkpoints (Weeks 6, 9, 14, 16):** submit a working version, explain in your own words what changed, and demonstrate it. See the table below; full criteria belong in the checkpoint's gate/rubric files.
4. **Week 17 (finals):** submit the final portfolio version — playable or usable, clear enough for someone else to try — with a final reflection.
5. Keep the World Bible current every week. It is graded evidence, not optional bookkeeping.

## The genre menu — pick once, Week 2, keep all semester

- **The Frontier Settlement** — manage colonists, resources, events.
- **The Investigation Bureau** — a detective case-file engine.
- **The Starship Log** — crew and exploration management.
- **The Small Business** — inventory, customers, transactions.

Bounded on purpose — four options, not open worldbuilding — so genre-based peer grouping and grading stay tractable. Whichever genre a student picks must support by the Week 16–17 capstone: persistent saved data, robust error handling, reusable modules, at least one class hierarchy, recursive reasoning or feature, a numeric/data visualization feature, and a searching/sorting decision. These requirements are the confirmed CS2 progression (`docs/curriculum/course-sequence.md`; Deitel, *Intro to Python for Computer Science and Data Science*).

## The four checkpoints

| Checkpoint | Week | What it is |
|---|---|---|
| 1 | 6 | Exceptions + modules + files integration — a working, explainable pass that connects robust handling, reusable code, and persistence. |
| 2 | 9 | Inheritance checkpoint — a meaningful base/derived-class design, explained and demonstrated after two weeks of development. |
| 3 | 14 | Recursion + plotting checkpoint — demonstrate recursive reasoning and a clear data visualization, with a Full Trail Debrief. |
| 4 | 16 | Searching/sorting plus full integration — final creative-project pass, capstone Decide/Compare, and final-reflection kickoff. |

The final Coding Odyssey portfolio submission is due Week 17 (finals week).

## Weekly gates

Starting Week 2, most weeks add a small pass/fail Quick Check tied to that week's new concept — the smallest proof that the concept was actually used, not a full spec. If a gate takes more than a couple of sentences to state, it is overbuilt; that is true of the *assignment*, not just the code. Detailed gate files and their rubrics are authored separately.

## The World Bible

Keep a living document — a miniature project roadmap:

- Founding charter (from Week 2's fresh-world charter).
- Current state of the world.
- One line per week: what gate was passed and what broke.
- A running “known debt” list.

This is normal project record-keeping, not extra work. It is reviewed as the **Judgment Log** at Week 2, mid-semester through each Debrief, and Week 17 as a whole. See `docs/curriculum/judgment_toolkit.md` §5.

## Decide/Compare moments

Twice a semester, commit to a real design choice in writing *before* comparing it against a real alternative, then defend it:

- **Week 13** — a searching/sorting or algorithmic-efficiency choice for the world.
- **Week 16** — a capstone-scale choice for the whole project.

Full instrument definition: `docs/curriculum/judgment_toolkit.md` §3; each week's specifics belong in that gate file.

## Grading

Each gate and checkpoint is graded from its paired files — `assignments/odyssey_gates/week-NN.md` and `rubrics/odyssey_gates/week-NN_rubric.md` — using the five instruments (Quick Check, Build, Decide/Compare, Debrief, Judgment Log) defined in `docs/curriculum/judgment_toolkit.md`. Grade-category weights are in `docs/grading-model.md`.

## Design history

Kept for provenance; none of this is needed to complete the assignment.

- CS2 historically used CYOAG/Coding Odyssey projects, often alongside chapter practice, and valued creativity, clarity, effort, playability, and presentation (`docs/reports/curriculum-history-synthesis.md`).
- The 2024–25 archive adds driver/navigator pair programming with AI as a collaborator and “Coding Quest” duplicate practice. Those are depth and collaboration references here, not verbatim imports.
- **2026-08-06:** Jeremy directed CS2 to reuse CS1's persistent-project, weekly-gate, four-checkpoint, judgment-toolkit structure at greater depth, with a fresh Odyssey world (same four genres) rather than continuing each student's CS1 world.
