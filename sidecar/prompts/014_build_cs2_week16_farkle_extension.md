# Sidecar Prompt 014 - Build the full CS2 Week 16 Farkle + ML experiment bench

**Status:** READY AFTER CS1 WEEK 16 HARDENING LANDS  
**Scope:** CS2 Week 16 shared Farkle / Machine Learning experience  
**Owner:** Foreman  
**Mode:** inherit hardened CS1 truth -> preserve one Farkle contract -> build CS2-native experiment bench -> add cost/effectiveness evidence -> validate -> author student/instructor package -> report -> stop

## Mission

Build **Computer Science II Week 16 Farkle + Machine Learning** into a real, tested, polished applied experience at the same quality level as the CS1 Week 16 package, but unmistakably shaped by what CS2 students learned this semester.

This is not a thin placeholder anymore.

CS1 already provides the playful foundation: a real Farkle engine, deterministic seeds, human strategies, a transparent experience-table learner, simulation/comparison tooling, tests, a student lesson, an instructor guide, an evidence receipt, and a fallback demonstration path.

Computer Architecture now contributes a second important idea:

> **What does it cost a machine to make a better Farkle decision, and when is that extra cost actually worth paying?**

CS2 should combine those strengths with its own course question:

> **How do we inherit a trustworthy program, preserve its contracts, add richer interchangeable strategies and experiment infrastructure, and use honest evidence to decide whether the added complexity earned its keep?**

The desired student feeling is:

> I did not rebuild Farkle. I inherited a working system, understood its boundaries, swapped or composed strategies through a stable contract, ran controlled experiments, visualized the results honestly, and made a defensible software-design decision about complexity, cost, and effectiveness.

Week 16 remains playful application and synthesis. It is **not** Checkpoint 4, a second final project, a formal reinforcement-learning unit, or a hidden Computer Architecture course.

---

# Dependency: catch up completely with CS1 before building

Do not begin from memory or from the pre-hardening CS1 snapshot.

Before implementation, inspect the current `jeremy-evert/computer_science_1` repository and record its exact commit SHA.

Prompt 014 depends on the results of:

`computer_science_1/sidecar/prompts/100_harden_week16_farkle_ml_evidence.md`

If Prompt 100 has not landed, stop implementation and report the dependency rather than copying the known pre-hardening comparison semantics.

At minimum inspect the current CS1 versions of:

- `planning/week-16.md`
- `lessons/10-farkle-ml.md`
- `docs/curriculum/week-16-instructor-guide.md`
- `assignments/W16-farkle-ml-experiment-receipt.md`
- `docs/curriculum/cs2-farkle-ml-handoff.md`
- `reports/013_week16_farkle_ml_capstone.md`
- `lessons/code/farkle/engine.py`
- `lessons/code/farkle/strategies.py`
- `lessons/code/farkle/learner.py`
- `lessons/code/farkle/simulate.py`
- `lessons/code/farkle/cli.py`
- `tests/test_farkle_engine.py`
- `tests/test_farkle_learner.py`
- any new/changed Week 16 tests, fixtures, sample output, or CLI behavior produced by Prompt 100.

The CS2 package must inherit the corrected CS1 evidence contract, including any fixes for:

- first-player contamination in comparisons;
- player-specific Farkle-rate denominators;
- visible learner preference matching actual behavior;
- a truthful/easy student path for custom human threshold strategies;
- any additional Prompt-100 fixes that land after this prompt was authored.

**Do not reintroduce a bug because this prompt listed an older interface. Current hardened CS1 source wins.**

---

# Read the CS2 course before designing the extension

Read:

- `README.md`
- `ROADMAP.md`
- `planning/fall-2026-course-design.md`
- `planning/week-03.md` through `planning/week-14.md`
- `planning/week-16.md`
- `assignments/odyssey_gates/week-16.md`
- `rubrics/odyssey_gates/week-16_rubric.md`
- `docs/grading-model.md`
- relevant implemented lessons/tests for contracts, data abstractions, GUI/event flow, visualization/storytelling, review, and reproducibility.

The Week 16 experience should feel like a payoff for this actual CS2 course, especially:

- cohesive object boundaries;
- composition and earned inheritance;
- contracts and swappable collaborators;
- list/stack/queue abstractions when they naturally fit;
- search/order/maintenance tradeoffs;
- compact model/view event flow;
- honest data visualization and storytelling;
- testing, documentation, review, recoverable history, and reproducibility.

Do not force every semester topic into one lab. Use only the ones that fit the Farkle experiment honestly.

---

# Read the Architecture Week 16 design and steal the good parts carefully

Inspect the current:

`jeremy-evert/computer_architecture/sidecar/prompts/005_build_farkle_ml_architecture_capstone.md`

and current Architecture Week 16 planning before implementation.

Reuse its useful cost/effectiveness grammar without turning CS2 into an Architecture benchmark lab.

Preserve these distinctions:

## Effectiveness

- validated win rate / tournament outcome;
- average score/value where useful;
- stability across repeated deterministic seed bundles.

## Preparation cost

- training wall time;
- training effort/budget such as number of training turns;
- optional normalized compute cost when an instructor-controlled runner provides it.

## Operation cost

- decision or game runtime;
- games completed per fixed time window;
- amount of simulation/work performed per decision.

## Software complexity / maintenance cost

This is the specifically CS2 addition.

Students should also be able to reason about the engineering price paid for a strategy:

- more state/features;
- more collaborators/objects;
- more configuration;
- larger persisted model/table;
- more tests/contracts needed;
- more moving parts to understand and maintain.

Do **not** collapse all of these currencies into one fake universal score.

The closing judgment should ask what additional complexity or computation actually purchased.

---

# One canonical Farkle rules engine

CS2 does **not** need its own independent Farkle rules implementation.

Preserve one canonical hardened Farkle game contract derived from CS1.

Choose the least fragile mechanism available in the current repository ecosystem for CS2 to consume it. Options may include:

- a documented shared/import path supported by current course tooling;
- a small vendored snapshot with source SHA/provenance plus a cheap contract-drift test;
- another simple mechanism already used by the course repositories.

Do not create a new package registry, monorepo migration, submodule maze, generalized curriculum dependency service, or other infrastructure project merely to share Week 16 code.

The shared boundary must preserve:

- the documented Farkle rule variant;
- stable state representation at the boundary;
- `ROLL` / `BANK` semantics;
- deterministic seeds;
- corrected fair-comparison semantics;
- corrected result metrics;
- correctness tests;
- provenance/version evidence.

CS1 remains the source of truth for dice/scoring correctness. CS2 tests the **extension contract**, not every dice combination again.

---

# Build a real CS2 experiment bench

The authoring target should be a small, coherent, inspectable CS2 package rather than disconnected snippets.

A reasonable conceptual shape is:

```text
Shared Farkle engine / state / simulation contract
                    |
                    v
              Strategy contract
          /          |          \
 function adapter  learned    simulation
   heuristic        player       player
          \          |          /
             ExperimentConfig
                    |
              ExperimentRunner
                    |
               ExperimentResult
                    |
          CSV/JSON + honest chart
```

Exact class/module names are implementation decisions.

Use the simplest course-consistent mechanisms. `abc.ABC` / `@abstractmethod`, composition, dataclasses, or an optional `Protocol` may fit. Do not create decorative inheritance merely to check a Week-5 box.

The key lesson is:

> **The original strategy function was already a contract. CS2 makes that contract explicit enough to support interchangeable collaborators, richer configuration, repeatable experiments, and new strategy families without rewriting the game.**

---

# Fixed strategy families: make training cost and play cost visible

Provide a **small prescribed software menu** with stable behavior and correctness tests. Students should compare options, not invent incomparable game engines.

Aim for three conceptually distinct families if they can be implemented cleanly:

## A. Cheap human heuristic

Example: hardened CS1 threshold/composed human strategy.

- near-zero preparation cost;
- very cheap decisions;
- fully inspectable;
- useful baseline.

## B. Trained transparent learner

Start with the hardened CS1 experience-table learner.

Provide bounded training effort levels chosen after actual timing, such as quick / standard / deeper. Do not blindly freeze numbers until measured on the required CPU path.

Expose:

- training turns;
- training wall time;
- resulting table/model size;
- evaluation results;
- inference/play cost.

CS2 may add **one richer-state transparent variant** if it stays understandable. Strong candidate additions are one or two already-available features such as distance-to-target or opponent gap.

The comparison should make the tradeoff visible:

> richer state may make a better decision, but it also increases state space, evidence requirements, model size, and maintenance/testing surface.

Do not require formal Q-learning, Bellman equations, discount factors, neural networks, or calculus.

## C. Bounded simulation / Monte Carlo player

If it can be implemented cleanly with the standard library and a small contract, add a fixed simulation-based decision strategy at bounded effort levels.

This strategy exists because it tells a different cost story:

- little/no training preparation;
- potentially expensive work on every decision;
- an obvious knob such as number of rollouts;
- useful contrast with trained-cheap-inference and heuristic-cheap-everything approaches.

If Monte Carlo becomes too complicated for a humane Week 16 student-facing experience, keep it as instructor enrichment or omit it. Do not let one strategy family consume the entire build.

---

# The central CS2 experiment

The lab should make students compare **two fixed strategy/configuration choices** under a controlled workload and answer:

> **What additional software complexity or computation did this design purchase, and was that purchase worth it for the objective I chose?**

A student should normally choose two options from the provided menu, make a prediction, run a bounded experiment bundle, inspect the results, visualize one tradeoff honestly, and make a decision.

Useful objectives include:

- highest validated win rate;
- cheapest preparation that reaches a declared win-rate floor;
- most games completed in a fixed time;
- strongest effectiveness for a bounded training/runtime budget;
- simplest strategy that performs within a declared tolerance of a more complex one.

No single objective is universally "best."

---

# Make the CS2 semester reappear naturally

## Contracts and swappable collaborators

This is required flavor.

Students should see that heuristic, learned, and simulation strategies can satisfy one strategy contract and be swapped without changing the Farkle engine.

Include a real contract test.

## Composition versus inheritance

Use composition where it earns its keep, for example:

- a state-aware wrapper around an existing threshold strategy;
- a measured/timed wrapper around any strategy;
- a result recorder around an experiment runner.

If inheritance is used, make the substitution benefit real. Do not add an inheritance hierarchy for decoration.

## Data abstractions / queue

A small batch of experiment configurations naturally forms pending work.

If useful, model the experiment batch as a queue/deque so students can see a real FIFO work abstraction. This should support the experiment runner, not become a queue homework assignment.

If a queue adds no value, omit it and document why.

## Search, order, and maintenance tradeoffs

Results can be ordered by different objectives: win rate, runtime, training cost, complexity, or another declared metric.

Expose the fact that changing the ordering criterion changes the apparent "winner." Ask students to justify the ordering that answers their question.

No forced binary search or algorithms-theory detour.

## Model / view boundary

The **CLI is the required path**.

Optionally provide a tiny read-only Tkinter experiment/result viewer if it can reuse the course's Week-9 model/view pattern with very little additional code. It may select a saved result or trigger one bounded runner action through a callback.

The model/experiment code must remain independently testable without the GUI.

Do not make GUI work required for the Week 16 student.

## Honest visualization and storytelling

This is a strong CS2 requirement because Weeks 10–11 intentionally made visualization/storytelling a course priority.

Generate at least one course-owned chart from real experiment data using the existing small plotting path, preferably Matplotlib if that matches the course environment.

Good candidate plots include:

- training effort vs. win rate;
- training effort vs. model/table size;
- rollout effort vs. win rate and/or decisions per second;
- preparation cost vs. runtime cost;
- effectiveness vs. one declared cost currency.

The plot must:

- come from saved CSV/JSON experiment evidence;
- use honest axes/labels;
- identify seed bundle / sample size / configuration context;
- avoid implying a causal or universal claim beyond the experiment;
- support a plain-language takeaway;
- include one limitation or alternative interpretation.

Do not make students produce a dashboard.

## Professional workflow / reproducibility

Each experiment receipt should record enough provenance to reproduce or audit it, such as:

- CS1/shared engine source SHA or package provenance;
- CS2 source commit when practical;
- Python/runtime version;
- strategy/configuration names and parameters;
- deterministic seed bundle;
- training budget;
- evaluation game count;
- relevant execution context;
- result metrics;
- elapsed timing where used.

Preserve test/diff/reasoning discipline.

Containers may be used only if the current verified `container_foundations` / classroom evidence supports a safe path by execution time. Containerized execution is an **optional reproducibility comparison**, not a Week 16 dependency.

Do not delay the CPU/native lab waiting for container perfection.

---

# Architecture-inspired execution/hardware scope

CS2 should benefit from the Architecture work without becoming a hardware tournament.

Required path:

- ordinary CPU;
- free/open tooling;
- bounded runtime;
- no GPU required;
- no paid cloud/API/AI required.

If instructor-controlled hardware lanes or runners exist by Week 16, the package may support an optional comparison on a controlled machine/container/cloud/NRP lane.

That enrichment may record:

- games/time;
- training time;
- runtime time;
- hardware/execution class;
- same artifact/configuration provenance.

Do not build the generalized Kubernetes tournament platform in this prompt.

If Architecture Prompt 005 later supplies a small stable tournament/runner contract, prefer **compatibility with that contract** over inventing a competing CS2 result schema. Reuse the useful shared receipt fields while preserving CS2-specific software-design evidence.

---

# Student-facing Week 16 flow

Author a polished student experience with approximately this cognitive shape:

## Part 1 - Remember the game, trust the baseline

Run the hardened CS1 baseline and inspect enough of its tests/results to know the inherited system is not magic.

## Part 2 - Find the contract

Identify what a Farkle strategy is allowed to know/do and how the engine depends on that promise.

Swap two existing strategies through the common interface.

## Part 3 - Compare different ways of buying a decision

Choose two provided strategies/configurations from the fixed menu.

Before running them, predict:

- which will play better;
- which will cost more to prepare;
- which will cost more per game/decision;
- which will be more complex to maintain/test.

## Part 4 - Run controlled evidence

Execute a bounded deterministic experiment bundle.

Save the result receipt rather than relying on terminal memory.

## Part 5 - Tell the data story

Generate/read one honest plot and state:

- the question;
- the supported takeaway;
- one limitation;
- the design decision it supports.

## Part 6 - Make the CS2 judgment

Answer in plain language:

- What contract stayed stable?
- What changed underneath/around it?
- What additional complexity or compute did the new strategy purchase?
- Was the observed effectiveness improvement large enough to justify that cost?
- Which design would you ship for the objective you chose?
- What test/evidence would make you change your mind?

Keep the receipt short enough that Week 16 still feels like a payoff week.

---

# Required implementation artifacts

Create a complete CS2 Week 16 package comparable in finish to CS1, including at minimum:

- a documented shared-CS1 consumption/provenance mechanism;
- CS2 experiment/strategy extension source;
- fixed strategy/configuration menu;
- experiment runner;
- machine-readable result receipt format (CSV and/or JSON);
- honest plot path from saved evidence;
- real automated tests;
- deterministic sample/fallback output checked into an appropriate course-owned location;
- a **student-facing Week 16 lesson**;
- a **CS2 Week 16 instructor guide** with classroom flow, likely confusions, recovery/fallback, and predicted surprises;
- a **short CS2 Week 16 evidence receipt**;
- updated `planning/week-16.md` pointing to the real package;
- minimal reconciliation of the retired Week 16 gate/rubric so they point to the applied evidence without resurrecting a checkpoint;
- durable build/validation report.

If a tiny optional GUI/result viewer materially improves the Week-9 callback/model-view echo without increasing student burden, include it. Otherwise explicitly decline it in the report.

---

# Testing requirements

Tests must be real and should protect the claims students are asked to trust.

At minimum validate:

1. shared/hardened CS1 engine contract compatibility;
2. existing function strategies work through the CS2 strategy boundary/adapter;
3. invalid strategy actions fail clearly;
4. deterministic experiment configs reproduce the same game outcomes/aggregate results where deterministic behavior is promised;
5. corrected fair-comparison semantics are preserved;
6. player-specific Farkle metrics remain correct;
7. learned strategy train/save/load/evaluate path works;
8. richer-state variant, if implemented, actually uses its added feature in a controlled test;
9. simulation/Monte-Carlo variant, if implemented, changes its work budget when the effort parameter changes;
10. machine-readable receipts round-trip or parse correctly;
11. visualization source data matches the saved experiment receipt;
12. optional model/view layer does not contain core game logic;
13. no test requires a magic exact stochastic win rate.

Also add one cheap upstream-contract drift check so a future CS1 public-boundary change makes CS2 fail loudly instead of silently lying.

---

# Validation / authoring quality bar

The authoring work may be substantial so the student experience can remain simple.

Before calling this implemented:

- run the full relevant test suite;
- execute every student command exactly as written from a clean-ish supported CPU environment;
- time the quick/standard/deeper training and any simulation effort levels;
- choose bounded defaults from observed runtime rather than guessing;
- execute at least two seed bundles so the sample story is not one lucky run;
- generate the chart from actual saved evidence;
- verify the fallback/sample files match current code;
- run a fresh student-path dry run without relying on author knowledge;
- confirm no required dependency violates the free path;
- run `git diff --check` or equivalent hygiene;
- verify Week 16 remains small in student burden even if the supplied bench is sophisticated.

A surprising result is not a failure. Preserve it if correct and make the lesson reason about it.

---

# Explicit non-goals

Do not add:

- a second independent Farkle scoring engine;
- a new Odyssey Checkpoint 4;
- a giant final project;
- formal Q-learning/SARSA/Bellman-equation mathematics;
- neural networks or LLM training;
- scikit-learn merely because it exists;
- a large model/dataset download;
- a required GPU;
- paid AI/API/cloud access;
- a generalized Kubernetes submission service;
- a semester-long live tournament platform;
- a database-backed experiment-tracking product;
- a large GUI application;
- artificial stacks/queues/trees/inheritance added only to reference earlier weeks;
- production Canvas/Savnac writes.

Use the smallest mechanism that makes the CS2 concept visible and testable.

---

# Grading / scope guardrail

Current CS2 source says Weeks 15–17 have no invented technical gate. Preserve that.

Week 16 is shared applied participation/evidence, not a new Reasoning Odyssey checkpoint.

Do not invent a new numeric weight. If exact mapping remains operationally open, name the open item rather than making policy here.

Students are not graded on owning expensive hardware or achieving the highest raw win rate.

A student on the free CPU path must be able to reach the same grading ceiling by making a strong evidence-backed design judgment.

---

# Required report

Write:

`sidecar/reports/014_build_cs2_week16_farkle_extension.md`

Include:

- exact hardened CS1 commit consumed;
- Prompt-100 status and fixes inherited;
- shared-source/provenance mechanism chosen;
- exact strategy families implemented;
- training/simulation effort levels and measured CPU runtimes;
- CS2 contract/object/composition design;
- which CS2 semester concepts were naturally reused and which were deliberately omitted;
- Architecture cost/effectiveness fields reused;
- result receipt schema;
- visualization implemented and what claim it supports;
- test commands/results;
- fresh student-path dry-run commands/results;
- sample evidence across at least two seed bundles;
- optional container/hardware/GUI enrichment status;
- student runtime/friction;
- files created/changed;
- explicit confirmation that no second engine, Checkpoint 4, formal ML unit, required GPU, or tournament-platform project was created;
- final commit SHA(s);
- any genuine remaining yellow.

---

# Done when

CS2 Week 16 is no longer a reservation wrapper.

It is a **real, tested, humane Farkle + ML experiment bench** that is at least as polished as CS1's Week 16 package while being clearly more mature in the ways appropriate to CS2:

- the game contract is inherited rather than rewritten;
- collaborators are interchangeable through an explicit boundary;
- richer strategies/configurations are comparable;
- preparation, runtime, effectiveness, and software complexity are visible as different costs;
- saved experiment data becomes an honest visualization/story;
- tests and provenance make the evidence trustworthy;
- students make a design decision instead of merely admiring a model.

The final student judgment should sound like:

> **For the objective I chose, I would ship this strategy/configuration because the additional effectiveness did or did not justify its training, runtime, and software-complexity costs, and this evidence is why I believe that.**

Then stop.