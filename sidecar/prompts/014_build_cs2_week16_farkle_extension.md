# Sidecar Prompt 014 - Build the CS2 Week 16 Farkle extension without forking the game

**Status:** READY AFTER CS1 WEEK 16 HARDENING LANDS  
**Scope:** CS2 Week 16 shared Farkle / ML experience only  
**Owner:** Foreman  
**Mode:** inspect upstream CS1 package -> preserve contract -> add a thin CS2 extension layer -> test -> author light student experience -> reconcile Week 16 wrapper -> report -> stop

## Mission

CS2 does **not** need its own Farkle engine.

CS1 already owns a real, tested Farkle engine, strategies, transparent learner, simulation code, CLI, student lesson, instructor guide, and evidence receipt. CS1 also has a bounded hardening prompt for Week 16 evidence quality. Treat that hardened CS1 package as the upstream shared computational artifact.

The legitimate CS2 question is:

> **How do we extend a working program without breaking the contract that already makes it trustworthy?**

Use Farkle as a playful final application of CS2 ideas already taught during the semester: boundaries, contracts, composition, data abstractions, testing, configuration, reproducibility, and professional workflow.

Do **not** turn Week 16 into a new final project, a formal reinforcement-learning unit, an Architecture benchmark tournament, or a rewrite of CS1.

The desired student feeling is:

> I inherited a working system. I understood its contract, changed one bounded design layer, proved I did not break the shared behavior, and used evidence to explain whether my design was actually better for the goal I chose.

---

## Dependency / starting condition

Before implementation, inspect the current CS1 Week 16 source, including any changes produced by:

`computer_science_1/sidecar/prompts/100_harden_week16_farkle_ml_evidence.md`

Do not copy a known-buggy pre-hardening snapshot if Prompt 100 has already landed.

Read at minimum from CS1:

- `planning/week-16.md`
- `lessons/10-farkle-ml.md`
- `docs/curriculum/week-16-instructor-guide.md`
- `assignments/W16-farkle-ml-experiment-receipt.md`
- `docs/curriculum/cs2-farkle-ml-handoff.md`
- `lessons/code/farkle/engine.py`
- `lessons/code/farkle/strategies.py`
- `lessons/code/farkle/learner.py`
- `lessons/code/farkle/simulate.py`
- `lessons/code/farkle/cli.py`
- `tests/test_farkle_engine.py`
- `tests/test_farkle_learner.py`

Then read current CS2 source:

- `README.md`
- `ROADMAP.md`
- `planning/week-16.md`
- `assignments/odyssey_gates/week-16.md`
- `rubrics/odyssey_gates/week-16_rubric.md`
- `docs/grading-model.md`
- the current Week 14 material far enough to avoid accidentally creating a second final technical checkpoint

---

# Governing design choice

## Preserve one canonical Farkle rules engine

Do not create an independent CS2 copy of the Farkle rules and scoring logic and then let it drift.

Choose the smallest maintainable way for CS2 to consume the shared CS1 artifact in the current repository ecosystem. Possible mechanisms include a clearly documented imported/shared source path, a small vendored snapshot with provenance and an explicit refresh test, or another simple mechanism supported by the existing course tooling.

The exact mechanism is an implementation decision, but the contract is not:

- one documented Farkle rule variant;
- one stable state dictionary shape at the shared boundary;
- `ROLL` / `BANK` behavior preserved;
- deterministic seeds preserved;
- shared comparison semantics preserved;
- upstream correctness tests remain authoritative for the engine;
- CS2 tests focus on the extension boundary rather than re-proving every dice rule.

If the repo ecosystem has no clean way to consume shared Python source without creating brittle path magic, document the tradeoff and choose the least fragile bounded option. Do not create a new shared infrastructure project just to solve Week 16.

---

# The CS2 extension: composition over reinvention

Build a thin, inspectable CS2 layer around the shared strategy contract.

The preferred design is a small **strategy object / adapter / composition layer** that can wrap the existing function strategies rather than replacing them.

A reasonable shape might expose concepts such as:

```text
Strategy contract
  decide(state) -> "roll" | "bank"

FunctionStrategyAdapter
  wraps an existing CS1 strategy function

ComposedStrategy
  chooses between two existing strategies using a bounded policy

ExperimentConfig
  records seed / games / strategy names / relevant parameters

ExperimentResult
  records the reproducible comparison receipt
```

Do not force these exact class names or an inheritance hierarchy if composition, a Protocol, a dataclass, or another simpler design fits the current CS2 teaching sequence better.

The point is not "classes are better than functions." The point is:

> A working function interface is already a contract. CS2 should show how to preserve that contract while adding structure around it.

Prefer composition over decorative inheritance.

---

# One bounded richer-decision experiment

CS1 deliberately keeps its learner state tiny: turn-score bucket + dice remaining.

CS2 should add **one** bounded opportunity to reason about a richer decision without turning Week 16 into an ML course.

Preferred options, in order:

1. **Composed human strategy:** combine existing strategies based on already-present state such as distance to target or opponent gap.
2. **Richer transparent learner state:** add exactly one already-available state feature such as distance-to-target or opponent gap and compare it with the smaller CS1 state.
3. **Experiment/configuration design:** compare the same strategy under several reproducible configurations and reason about stability / evidence quality.

Choose the smallest option that best reinforces the CS2 course as actually taught.

If implementing the richer learner would require formal RL theory, large dependencies, or a substantial new framework, do **not** implement it. Use the composed-strategy path instead.

---

# Required student experience

Keep the student burden small enough for Week 16.

A good experience should require students to:

1. run the shared CS1 baseline so they know the inherited system works;
2. identify the existing strategy boundary/contract;
3. inspect the small CS2 extension layer;
4. make or configure one bounded extension using composition or a richer state decision;
5. run shared correctness/compatibility tests plus CS2 extension tests;
6. compare baseline vs. extension over deterministic repeated games;
7. answer:
   - What contract did you preserve?
   - What changed?
   - What evidence says it helped, hurt, or merely behaved differently?
   - What complexity did the new design buy, and was it worth it?

Students should not be asked to rebuild Farkle, implement full Q-learning, derive Bellman equations, or write a new simulation framework.

---

# Testing requirements

The CS2 extension must have real tests.

At minimum validate:

- existing CS1 strategy functions still work through the CS2 boundary/adapter;
- invalid actions are rejected or surfaced cleanly;
- deterministic configurations reproduce the same result;
- composed/richer strategies can complete full games;
- the chosen extension actually changes behavior in at least one controlled state;
- comparison evidence uses the hardened upstream semantics rather than reintroducing first-player or metric bugs;
- no test requires a magic exact stochastic win rate.

If a shared-source mechanism is used, add one cheap drift/compatibility check so CS2 fails loudly if the upstream public contract changes underneath it.

---

# What to author in CS2

Create only what CS2 legitimately owns. Likely artifacts:

- a small CS2 extension/adapter package or module;
- CS2-specific tests;
- a short Week 16 student guide or extension page;
- a short CS2 evidence receipt;
- instructor notes explaining the CS1 baseline -> CS2 extension progression;
- an updated `planning/week-16.md` pointing to the real implementation;
- minimal reconciliation of the retired Week 16 gate/rubric so they point at participation/evidence without becoming a technical checkpoint;
- a durable report.

Do not duplicate the full CS1 lesson merely to make CS2 self-contained.

---

# Explicit non-goals

Do not add:

- a second Farkle rules engine;
- a formal Q-learning / SARSA / Bellman-equation unit;
- scikit-learn merely because CS2 can tolerate dependencies;
- neural networks;
- Kubernetes / NRP tournament infrastructure;
- CPU-vs-GPU benchmarking;
- cloud deployment;
- hardware-cost accounting;
- leaderboards;
- a new Odyssey checkpoint;
- a large GUI project;
- a database-backed experiment tracker;
- property-testing infrastructure unless it is already available and adds obvious value;
- production Canvas/Savnac writes.

Interesting future directions belong in a handoff note, not in Week 16.

---

# Grading / scope guardrail

Current CS2 source says Weeks 15-17 have no invented technical gate. Preserve that.

Week 16 remains shared-strand participation/evidence, not Checkpoint 4.

Do not invent a new numeric weight. If the current grading model lacks a settled mapping for the light Week 16 artifact, name that as an operational open item rather than deciding it here.

---

# Required report

Write:

`sidecar/reports/014_build_cs2_week16_farkle_extension.md`

Include:

- exact upstream CS1 commit / state consumed;
- whether CS1 Prompt 100 had landed;
- shared-source mechanism chosen and why;
- contract preserved;
- CS2 extension chosen;
- tests executed and results;
- baseline vs. extension sample evidence;
- student runtime/friction;
- files created/changed;
- explicit confirmation that no second engine, new checkpoint, formal ML unit, or Architecture tournament platform was created;
- final commit SHA(s);
- any genuine remaining yellow.

---

# Done when

CS2 Week 16 is no longer merely a reservation wrapper.

It should be a small, tested, real experience that demonstrates:

> **A CS2 student can inherit a trustworthy program, preserve its contract, extend one design layer, and use evidence to decide whether the added complexity earned its keep.**

Then stop.
