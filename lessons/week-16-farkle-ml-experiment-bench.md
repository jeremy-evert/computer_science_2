# Week 16 — Farkle + ML: what did the extra complexity buy?

## The point of this week

You already know how to build software. This week you inherit software that already works and ask a more professional question:

> **If two designs can make the same kind of Farkle decision, what does the more complicated one actually buy us?**

You are not rebuilding Farkle and you are not starting a new machine-learning unit.

The shared Farkle rules, scoring engine, basic strategies, transparent learner, and bounded rollout machinery come from the canonical `Farkle_and_Machine_Learning` package synchronized into `lessons/code/farkle_ml/`. CS2 adds the course-facing experiment configuration/results, saved evidence, visualization, and engineering judgment about software complexity and maintenance.

## Your experiment has four currencies

Do not mash them into one magic score.

### Effectiveness

How well did it play?

- win rate against the same baseline;
- average score and Farkle rate when useful;
- whether the story survives a different deterministic seed bundle.

### Preparation cost

What did you pay before playing?

- training turns;
- training wall time;
- model/table size.

### Operating cost

What did you pay while playing?

- evaluation time;
- games per second;
- number of simulated next rolls per decision for a rollout strategy.

### Software cost

What did the design add that somebody now has to understand, test, and maintain?

- more state or configuration;
- more collaborators/objects;
- persisted learned data;
- more tests or failure modes.

A design can win one currency and lose another.

---

## Part 1 — See the inherited contract

From the repository root, inspect:

- `lessons/code/farkle_week16/contract.py`
- `lessons/code/farkle_ml/_SHARED_PROVENANCE.json`
- `lessons/code/farkle_ml/contract.py`

The important contract is tiny:

```text
state -> strategy -> "roll" or "bank"
```

The CS2 `contract.py` path is intentionally a thin facade over the canonical shared contract. That gives this course a stable place to discuss the abstraction without creating another implementation to maintain.

The Farkle engine does not need to know whether the decision came from:

- one human-written threshold;
- a table trained from experience;
- a bounded simulation.

That is the Week 7 idea of a swappable collaborator showing up in a real inherited system.

Run the menu:

```bash
PYTHONPATH=lessons/code python3 -m farkle_week16.cli menu
```

On Windows PowerShell, `python` may be your launcher instead of `python3`.

---

## Part 2 — Pick two ways to buy a decision

The supported strategy specifications are intentionally small.

### Human threshold

```text
bank_at_425
```

Almost no preparation. Almost no decision cost. Extremely easy to explain and maintain.

### Transparent trained learner

```text
learner:2000
learner:20000
```

The number is training turns. More training means more preparation work before the strategy plays.

### Bounded rollout strategy

```text
rollout:25
rollout:100
```

The number is sampled possible next rolls **at each decision**. It pays little up front and spends work while playing.

The rollout player is deliberately modest. It does not search the whole future game. It asks one transparent question: if I roll once more and then bank, does the sampled average look better than banking now?

### Before running anything

Choose **two** options and write a prediction:

1. Which will have the higher win rate against the fixed `bank_at_425` baseline?
2. Which will cost more to prepare?
3. Which will cost more while games are running?
4. Which will be harder to maintain/test?

You are allowed to be wrong. A prediction gives the evidence something to argue with.

---

## Part 3 — Run controlled evidence

Example:

```bash
PYTHONPATH=lessons/code python3 -m farkle_week16.cli compare \
  --strategy-a learner:2000 \
  --strategy-b bank_at_425 \
  --games 1000 \
  --seed 6262 \
  --out artifacts/week16_farkle/my_learner.json
```

Then compare another strategy using the **same game count and seed**.

The simulator alternates who starts each game. With an even game count, both strategies start exactly the same number of games. Farkle rate is calculated over each strategy's own turns.

Those details matter because "evidence" that quietly gives one strategy first move more often is not the comparison we think we ran.

---

## Part 4 — Run the fixed class suite when useful

The instructor may ask you to run or inspect the standard suite:

```bash
PYTHONPATH=lessons/code python3 -m farkle_week16.cli suite \
  --games 500 \
  --seed 6262 \
  --out-dir artifacts/week16_farkle/suite
```

This writes individual JSON receipts and one `suite_results.csv`.

Notice the design decision: **the terminal output is not the evidence of record. The saved result is.**

That is the same professional-workflow habit you have practiced all semester.

---

## Part 5 — Tell one honest data story

Choose the cost currency that answers your question.

For example, plot preparation time versus win rate:

```bash
PYTHONPATH=lessons/code python3 -m farkle_week16.plot_results \
  artifacts/week16_farkle/suite/suite_results.csv \
  artifacts/week16_farkle/suite/prep-vs-win.png \
  --x preparation_seconds_a
```

Other available x-axes include:

- `seconds_per_game`
- `model_size_bytes_a`
- `training_turns_a`

Then state four things:

1. **Question:** what were you trying to learn from the chart?
2. **Takeaway:** what does the plotted evidence support?
3. **Limitation:** what does it *not* establish?
4. **Decision:** what would you ship for the objective you chose?

A chart that makes a weak strategy look strong by changing the question after seeing the data is not a better chart. It is a different question.

---

## Part 6 — The CS2 judgment

Finish the short receipt in:

`assignments/W16-farkle-ml-design-receipt.md`

Your conclusion should be specific enough to disagree with:

> **For this workload, under this objective, I would choose ___ because the additional effectiveness did/did not justify the additional preparation, runtime, and software complexity. My evidence is ___.**

Then name one test or new piece of evidence that could make you change your mind.

## What you are NOT required to do

- rebuild the Farkle engine;
- implement Q-learning or derive an RL equation;
- use a GPU;
- use cloud/NRP compute;
- build a GUI;
- test every strategy;
- win a leaderboard;
- write a giant report.

This is the payoff week. The machine does enough work that you can spend your attention on **contracts, evidence, tradeoffs, and judgment**.
