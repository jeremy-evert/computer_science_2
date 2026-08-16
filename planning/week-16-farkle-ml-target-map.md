# Week 16 Farkle + ML — Target Map

## North-star question

> **How do we inherit a trustworthy program, preserve its contracts, compare different ways of making a Farkle decision, and use honest evidence to decide whether added complexity and computation earned their keep?**

## Ownership map

### CS1 owns

- canonical Farkle rules;
- scoring behavior;
- core state dictionary;
- ROLL/BANK semantics;
- baseline human strategies;
- transparent experience-table learner;
- baseline simulation semantics;
- beginner-facing explanation of state/action/reward.

### CS2 owns

- explicit strategy contract/adapters;
- CS2 strategy composition and richer transparent configuration;
- experiment configuration/result objects;
- repeatable experiment runner;
- saved CSV/JSON evidence;
- honest visualization/storytelling path;
- comparison of software complexity, preparation cost, runtime cost, and effectiveness;
- CS2-specific tests, student lesson, instructor guide, receipt, and validation automation.

### Computer Architecture contributes

- the cost/effectiveness question;
- fixed strategy/effort comparisons;
- preparation versus operating cost;
- optional controlled hardware/container/NRP lanes;
- the rule that the required path stays CPU-only and accessible.

Architecture does **not** own the CS2 software-design judgment.

## Runtime/package map

```text
provenance-tracked CS1 Farkle baseline
            |
            v
      Strategy contract
      /      |       \
 heuristic  learned  bounded simulation
      \      |       /
       ExperimentConfig
              |
       ExperimentRunner
              |
       ExperimentResult
        /            \
      JSON           CSV
        \            /
         honest plot
              |
       student judgment
```

## Student flow

1. **Trust the baseline** — run a known-good fixed-seed CS1-compatible comparison.
2. **Find the contract** — identify what every strategy must accept/return.
3. **Choose two ways to buy a decision** — heuristic, trained transparent learner, or bounded simulation strategy/effort level.
4. **Predict** — playing strength, training/prep cost, runtime cost, maintenance complexity.
5. **Run** — execute one bounded deterministic experiment bundle.
6. **Save evidence** — JSON/CSV receipt, not terminal memory.
7. **Visualize** — one honest chart tied to a real question.
8. **Decide** — state which design should ship for the chosen objective and what evidence would change that decision.

## CS2 semester echoes

| Course idea | Week 16 use |
|---|---|
| Object boundaries | Experiment/config/result objects have narrow responsibilities |
| Composition | Wrappers and composed strategies add behavior without rewriting engine |
| Inheritance/polymorphism | Use only if substitution is genuinely useful |
| Contracts | All strategies satisfy one explicit decision contract |
| Queue abstraction | Optional pending experiment batch uses FIFO only if useful |
| Search/order tradeoffs | Rank results by different declared objectives |
| Model/view | CLI required; optional tiny result viewer only if nearly free |
| Visualization | Saved evidence -> labeled plot -> supported claim + limitation |
| Testing/review | Contract, reproducibility, invalid-action, compatibility tests |
| Reproducibility | seed bundle, source provenance, parameters, runtime context in receipts |

## Cost currencies

Keep separate:

### Effectiveness
- win rate;
- average score/value where useful;
- stability over deterministic seed bundles.

### Preparation
- training turns;
- training wall time;
- persisted model/table size.

### Operation
- elapsed evaluation time;
- games per second;
- bounded simulation effort per decision when applicable.

### Software engineering
- state/features added;
- configuration surface;
- collaborators/objects;
- tests/contracts required;
- persistence/maintenance burden.

Do not invent one universal score that pretends these are interchangeable.

## Required strategy families

1. **Cheap heuristic** — transparent, nearly free preparation and operation.
2. **Trained transparent learner** — preparation cost up front, inexpensive play; optionally one richer-state variant.
3. **Bounded simulation strategy** — little/no training, explicit runtime work knob; may be instructor enrichment if student complexity becomes too high.

## Required evidence contract

Every saved experiment result should include at least:

- schema version;
- upstream CS1 provenance;
- CS2 source/provenance when available;
- Python version;
- strategy/configuration names;
- seed bundle;
- training budget;
- evaluation games;
- elapsed preparation/evaluation time when measured;
- model/table size when applicable;
- win/effectiveness metrics;
- execution context label;
- notes/limitations field.

## Equity / scope boundary

Required path:

- ordinary CPU;
- no paid API;
- no GPU;
- no cloud account;
- no student Kubernetes access;
- bounded runtime.

Optional instructor enrichment may compare container/hardware/NRP lanes, but it cannot determine the grading ceiling.

## Done-state map

Week 16 is ready when the repository contains:

- real executable CS2 Farkle experiment code;
- real automated tests;
- a repeatable validation script;
- student lesson;
- instructor guide;
- short evidence receipt;
- saved sample/fallback evidence;
- plot path;
- current Week 16 planning/gate/rubric links;
- raw validation receipts from a real checkout;
- postmortem report.
