# The judgment-building toolkit — Build / Decide-Compare / Debrief / Quick Check / Judgment Log

**Why this exists.** CS2 uses the proven Coding Odyssey spine: one persistent per-student project, weekly gates, and four checkpoints. The same five instruments build judgment directly rather than grading it as a side rubric. At CS2 depth, students judge robust error paths, module and file boundaries, inheritance versus alternatives, recursive designs, data displays, and algorithmic trade-offs. This is an adaptation of CS1's RAG-grounded design, not a new pedagogy.

**Grounding.** The instrument design follows Wiggins & McTighe, *Understanding by Design* (2005), and *How Learning Works* (2010), as in the CS1 source design. Its CS2 topic placements follow the confirmed course map in `docs/curriculum/course-sequence.md`, the historical synthesis in `docs/reports/curriculum-history-synthesis.md`, and Deitel, *Intro to Python for Computer Science and Data Science* (exceptions, inheritance, recursion, plotting, and searching/sorting topics). The archive shows formative, effort-based, demonstrative grading as the durable local norm (`docs/philosophy/teaching-patterns.md`).

**Where each instrument sits, at a glance:**

| Instrument | Grain | Frequency | Ties to |
|---|---|---|---|
| Quick Check | one gate, one concept | ~weekly | the weekly technical topic |
| Build | one checkpoint or continuation | ~weekly (light) + 4 checkpoints (full) | `assignments/A2-coding-odyssey-project.md` |
| Decide/Compare | one real choice, defended | 2 points (Wk 13, Wk 16 capstone) | searching/sorting choice; capstone |
| Debrief | reflective, cyclical | 4 arc closes + finals | Checkpoints 1–4, Week 17 |
| Judgment Log | cumulative, living | 3 checkpoints (Wk 2 / mid / Wk 17) | the World Bible |

---

## 1. Quick Check — the weekly gate

**Grain:** the smallest thing that proves this week's concept was actually used. Not a spec, not a full assessment — a gate.

**Why this shape.** Wiggins & McTighe describe effective formative checkpoints as **specific** and **relevant** (pp. 59–60, 68), rather than a scaled-down version of the whole unit assessment. A gate longer than 2–3 sentences has stopped being a gate and started being a spec.

**Format:** one criterion, pass/fail (or complete/incomplete). No partial credit; nuance belongs in Build. Each Quick Check states:

1. The one concept being gated — for example, “a `try`/`except` path that handles invalid input without ending the program,” “an overridden method that changes inherited behavior,” or “a recursive function with a base case and progress step.”
2. Where the evidence appears — in this week's world code, not a separate exercise file.
3. The pass/fail line: does it exist and run, yes or no.

**Grading path — mechanical vs. human, decide per gate.** Imports, a context-managed file operation, or a recursive base case may be mechanically checkable. Whether an inheritance hierarchy fits the student's world, a plot communicates its data, or an algorithm choice makes sense needs a human or frontier-agent read. Author each decision per gate; do not set a global rule.

---

## 2. Build — construction evidence

**Grain:** did the student actually build or extend the world with this week's or checkpoint's concept, correctly, and does it run.

**Two grains of Build, graded differently:**

- **Light Build (weekly creative continuation).** Holistic, not the full rubric — did the student do something real with the week's open extension time.
- **Full Build (the 4 checkpoints + Week 17 final).** Submit a working version, explain what changed, and demonstrate it; the rubric formalizes that established shape.

**Full Build rubric axes:**

| Axis | What it checks | Note |
|---|---|---|
| Functions | Does it run; does it do what the student claims | Not “is it impressive” — does the claimed behavior happen |
| Concept use | Does this arc's target concept genuinely appear, rather than cosmetically | Quick Checks are the evidence trail |
| Explanation | Can the student say, in their own words, what changed and why | Matches checkpoint mechanics |
| Demonstrability | Could another person run or follow it | Matches playability and clarity as recurring values |

Checkpoint 1 (Wk 6) integrates exceptions, modules, and files and rehearses the full submit/explain/demonstrate cycle. Checkpoint 2 (Wk 9) deepens the inheritance design; Checkpoint 3 (Wk 14) brings recursion and plotting into one review; Checkpoint 4 (Wk 16) evaluates searching/sorting plus full integration. These placements follow the confirmed map, including two-week rounds for inheritance and recursion because recursion is historically the hardest topic (`docs/reports/curriculum-history-synthesis.md`).

---

## 3. Decide/Compare — judgment under real trade-offs

**Grain:** commit to a choice *before* comparing it against alternatives, then defend it against a genuine trade-off — not a retroactive rationalization.

**Two placements, both tied to real content:**

1. **Week 13 (Searching, sorting, Big-O).** Pick an approach for a concrete lookup or ordering need, commit, then compare it with a real alternative: for example, linear search versus binary search given the sorted-data precondition, or a simple sort versus a different workflow. The defense must name cost, preconditions, and fit for the world.
2. **Week 16 capstone**, alongside Checkpoint 4 — the same move at the scale of the whole world.

**Grading:** does the comparison name a real trade-off (not just restate the chosen option's benefits), and does the final choice follow from it rather than precede it cosmetically?

---

## 4. Debrief — the reflective cycle

**Grain:** structured reflection on what was planned, what happened, what broke, and what would be done differently.

**Why this shape.** *How Learning Works* describes a metacognitive cycle: assess the task, evaluate knowledge and gaps, plan, monitor progress, and reflect (pp. 217–220). Students need that practice modeled explicitly (pp. 237, 245). Debrief is that practice, not a bonus paragraph.

**Placement — the 4 checkpoints plus Week 17, not new dates:**

- **Checkpoint 1 (Wk 6):** what failed or became clearer while connecting exception handling, reusable code, and persistent data?
- **Checkpoint 2 (Wk 9):** standard Debrief on the inheritance design: what behavior belongs in the base class, what belongs in a subclass, and what would composition have changed?
- **Checkpoint 3 (Wk 14): Full Trail Debrief, mandatory.** Recursion is the historically hardest topic; use its trace and the plot/data work to name exactly what broke, why, and how the design would change from scratch.
- **Checkpoint 4 (Wk 16) + Week 17 final:** capstone Debrief, paired with show-and-tell and the final reflection.

---

## 5. Judgment Log — the cumulative record

**Grain:** not a new document — this *is* the World Bible, viewed as a running judgment record rather than a project journal. It shows both what exists (Build evidence) and how the student decided to get there.

**Minimum contents:** founding charter (Week 2's fresh-world charter), current state, one line per week on what gate was passed and what broke, and a running “known debt” list.

**Three graded checkpoints, not a running grade:**

1. **Week 2** — charter exists and is committed.
2. **Mid-semester** — implicitly checked at each Debrief; no separate grade.
3. **Week 17 final** — reviewed with the final Debrief and show-and-tell.

---

## Open, not decided here

- **Which gates route through Marker versus human Quick Check:** a per-week authoring decision.
- **Point values within the five instruments:** the grade-category weights are set in `docs/grading-model.md`; detailed gate rubrics remain separate prompt work.
