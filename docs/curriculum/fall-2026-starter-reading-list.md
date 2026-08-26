# Fall 2026 CS2 — good-enough starter reading list

**Status:** STARTER CANON — good enough to teach from now; improve later without reopening the course spine.

This file expands `docs/curriculum/fall-2026-resource-map.md` into a practical week-by-week starter shelf for the frozen Fall 2026 CS2 spine.

## Reading-list doctrine

- The **course-owned weekly page / gate is always the required source of truth** for what students must do.
- Each technical week gets one **START HERE** resource and at most a few optional reinforcements.
- Prefer official/open/no-cost sources: Python documentation, Runestone/PyDS3, Matplotlib, and GitHub Docs/Skills.
- Do not replace one commercial textbook with one giant free textbook requirement.
- A linked resource is there to clarify, demonstrate, or deepen the week's capability. It does not create a second homework stream.
- ZyBooks and Deitel remain optional historical/control references only.
- These links are intentionally a starter shelf. Better examples may replace them later if the capability spine remains unchanged.

---

## Week 3 — Cohesive encapsulated objects

**Course question:** What state and behavior genuinely belong together in one object?

### START HERE
- Python Tutorial — Classes: https://docs.python.org/3/tutorial/classes.html
  - Focus on class/instance objects, instance variables, and methods rather than reading every section.

### Reinforce if useful
- Python Tutorial — Classes, especially class vs. instance variables: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
- Course-owned Week 3 gate and four-world examples remain the primary applied material.

**Why this fits:** students need a clean language-level model of objects before judging whether their Week 2 predicted nouns deserve object boundaries.

---

## Week 4 — Composition, invariants, refactoring

**Course question:** What happens when one object cannot responsibly do the whole job alone?

### START HERE
- Python Tutorial — Classes: https://docs.python.org/3/tutorial/classes.html
  - Revisit object attributes and methods while reading the Week 4 course-owned collaborating-object example.

### Reinforce if useful
- Python Data Model overview: https://docs.python.org/3/reference/datamodel.html
  - Instructor-selected excerpts only; do not assign the entire reference chapter.
- Course-owned Week 4 composition/invariant examples are the primary teaching source.

**Why this fits:** official Python docs explain the mechanics; the course must teach the design judgment of composition and invariants.

---

## Week 5 — Earned inheritance and polymorphism

**Course question:** Is this truly an `is-a` relationship where substitution works, or should the design remain composition?

### START HERE
- Python Tutorial — Inheritance: https://docs.python.org/3/tutorial/classes.html#inheritance

### Reinforce if useful
- Python built-ins `isinstance()` / `issubclass()` are introduced in the same inheritance section.
- Re-read the Week 4 composition decision before choosing inheritance.

**Why this fits:** students see Python's actual inheritance behavior while the course supplies the stricter rule that inheritance must be earned by meaningful substitution.

---

## Week 6 — Contracts and swappable collaborators

**Course question:** Can different collaborators satisfy the same explicit contract and be swapped without breaking the client?

### START HERE
- Python `abc` — Abstract Base Classes: https://docs.python.org/3/library/abc.html
  - Focus on `ABC` and `@abstractmethod`.

### Reinforce if useful
- Python Tutorial — Inheritance: https://docs.python.org/3/tutorial/classes.html#inheritance
- `typing.Protocol` may be shown as an optional comparison, not the required path: https://docs.python.org/3/library/typing.html#typing.Protocol

**Why this fits:** Week 6's frozen contract explicitly centers `abc.ABC` / `@abstractmethod`, with Protocol only as optional comparison.

---

## Week 7 — List, stack, and queue abstractions

**Course question:** What operations does the problem need, and which abstraction makes those operations honest and predictable?

### START HERE
- Runestone PyDS3 — Basic Data Structures: https://runestone.academy/ns/books/published/pythonds3/BasicDS/toctree.html
  - Concentrate on stacks and queues.

### Reinforce if useful
- Runestone — Implementing a Stack in Python: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementingaStackinPython.html
- Python `collections.deque`: https://docs.python.org/3/library/collections.html#collections.deque

**Why this fits:** Runestone makes the ADT idea visible; Python's `deque` gives students a production-quality standard-library implementation to compare against hand-built structures.

---

## Week 8 — Search, order, and maintenance tradeoffs

**Course question:** What do we gain by keeping data ordered, and what does maintaining that order cost?

### START HERE
- Runestone PyDS3 — Searching and Sorting objectives / chapter: https://runestone.academy/ns/books/published/pythonds3/SortSearch/Objectives.html

### Reinforce if useful
- Python Sorting HOWTO: https://docs.python.org/3/howto/sorting.html
- Python `bisect` — maintaining sorted lists: https://docs.python.org/3/library/bisect.html

**Why this fits:** Week 8 is not an algorithm-recitation contest; students need enough search/order mechanics to justify a real choice in their world's state.

---

## Week 9 — Compact GUI and event path

**Course question:** Can a small view trigger meaningful behavior while the model remains independently testable?

### START HERE
- Python `tkinter` documentation: https://docs.python.org/3/library/tkinter.html

### Reinforce if useful
- TkDocs Tutorial: https://tkdocs.com/tutorial/
  - Use as a friendly supplemental walkthrough; Python's official docs remain the canonical language/library reference.

**Why this fits:** students need the event-loop/callback mental model, not a semester-long GUI framework detour.

---

## Week 10 — Honest data visualization

**Course question:** What question are we asking, and what visual representation answers it without misleading the reader?

### START HERE
- Matplotlib Quick Start: https://matplotlib.org/stable/users/explain/quick_start.html

### Reinforce if useful
- Matplotlib Plot Types: https://matplotlib.org/stable/plot_types/index.html
- Python `csv` module for plain-Python data input: https://docs.python.org/3/library/csv.html

**Why this fits:** Week 10 needs enough plotting fluency to choose and defend a chart, while keeping the emphasis on question, evidence, labels, scale, and limitations rather than library trivia.

---

## Week 11 — Data storytelling / Flex Clinic

**Course question:** What claim does the evidence support, what does it not support, and what decision follows?

### START HERE
- Matplotlib Quick Start, revisited with emphasis on labels, titles, axes, legends, and annotation: https://matplotlib.org/stable/users/explain/quick_start.html

### Reinforce if useful
- Matplotlib text and annotations: https://matplotlib.org/stable/users/explain/text/annotations.html
- Week 10's actual chart and project data are more important than new reading this week.

**Why this fits:** this week is about evidence-backed explanation and limitations, not accumulating more plotting APIs.

---

## Week 12 — Stabilize and prepare peer review

**Course question:** What evidence would convince another programmer that this slice works and is understandable?

### START HERE
- Python `unittest` documentation: https://docs.python.org/3/library/unittest.html
  - Focus on test cases, specific assertions, and independent repeatability.

### Reinforce if useful
- Python logging basic tutorial: https://docs.python.org/3/howto/logging.html
- Existing project tests, README, and runnable evidence are primary.

**Why this fits:** stabilization is evidence work. Students should improve the project's ability to prove behavior rather than add ornamental features.

---

## Week 13 — Major construction culmination

**Course question:** Can the project demonstrate meaningful completion while remaining testable, explainable, and recoverable?

### START HERE
- No new external chapter required. Reuse the most relevant prior official reference for the student's actual design problem.

### Reinforce if useful
- Python `unittest`: https://docs.python.org/3/library/unittest.html
- Python Tutorial — Classes: https://docs.python.org/3/tutorial/classes.html
- The student's own accumulated World Bible, tests, traces, and design evidence are the central reading this week.

**Why this fits:** Week 13 is synthesis. Adding a new content unit would compete with the work students need to finish and defend.

---

## Week 14 — Source management and bounded reproducibility

**Course question:** Can another person inspect, recover, review, and reproduce the important parts of this work?

### START HERE
- GitHub Skills — Introduction to GitHub: https://skills.github.com/
  - Instructor selects the relevant short skill path rather than assigning the entire catalog.

### Reinforce if useful
- GitHub Docs — Get started using Git: https://docs.github.com/en/get-started/using-git
- GitHub Docs — Pull requests: https://docs.github.com/en/pull-requests
- Docker Docs — Get Started: https://docs.docker.com/get-started/ — **link/reference only unless classroom runtime has been independently verified**.

**Why this fits:** Week 14 assesses real repository evidence, recovery, collaboration, review, and bounded reproducibility. Containers remain subordinate to verified classroom reality.

---

## Weeks 15–17 — closure

- **Week 15:** no new required reading; asynchronous buffer/catch-up.
- **Week 16:** use the course-owned/shared Farkle + ML wrapper and evidence instructions; do not bolt on a new textbook chapter.
- **Week 17:** no technical reading requirement; reflection uses the student's repository and semester evidence.

---

## Instructor maintenance rule

A future improvement pass may replace or add a resource when it does at least one of these better:

1. explains the week's capability more clearly;
2. provides a better inspectable example;
3. reduces reading burden while preserving understanding;
4. is more accessible, current, or classroom-friendly;
5. better supports the Reasoning Odyssey evidence for that week.

Do **not** reopen the frozen Week 3–14 capability spine merely because a better reading is discovered.
