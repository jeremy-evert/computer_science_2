# Week 16 instructor guide — Farkle + ML experiment bench

## Framing

This is a **payoff week**. Do not turn it into a surprise final project or a machine-learning theory unit.

The student-facing lesson is `lessons/week-16-farkle-ml-experiment-bench.md`.

The underlying implementation deliberately makes earlier CS2 ideas reappear in one inherited system:

- function contract -> explicit swappable strategy collaborator;
- composition around inherited behavior;
- reproducible experiment configuration/results;
- honest result ordering and visualization;
- test/review/provenance discipline.

Computer Architecture contributes the cost/effectiveness question, but CS2 adds the engineering cost of extra software structure.

## Before class

From a real checkout run:

```bash
python scripts/validate_week16_farkle.py
```

Do not demo live if the required tests are RED.

A matplotlib failure is a named plotting YELLOW, not a reason to distrust the Farkle engine or experiment evidence. Use the CSV/JSON directly if plotting is unavailable.

## Suggested 50-minute flow A — inherit, contract, predict

### 0–10 min — play/remember Farkle

Reuse the same simple bank/roll tension students can understand without ML vocabulary. If useful, physically roll dice for a few minutes.

### 10–20 min — inherited software

Show `vendor_cs1/PROVENANCE.md` and `contract.py`.

Ask:

> What did CS2 add without changing the Farkle rules?

Land on the idea that the CS1 function already had a behavioral contract; CS2 makes the boundary explicit enough to support multiple collaborators and experiment tooling.

### 20–30 min — three ways to buy a decision

Put these on the board:

- `bank_at_425`
- `learner:2000`
- `rollout:25`

Ask students where each pays its cost: before play, during play, or in software complexity.

### 30–40 min — predictions

Students choose two options and complete receipt sections 1–2 before running.

### 40–50 min — first controlled comparison

Run one example together. Call attention to balanced starts and saved evidence.

## Suggested 50-minute flow B — evidence, chart, judgment

### 0–15 min — run chosen experiments

Students run their two configurations using the same declared workload/seed context.

### 15–25 min — inspect saved receipts

Open JSON/CSV. Ask what fields exist because a future reviewer would need them.

### 25–35 min — honest plot

Choose one x-axis currency. Ask what different plot choices would answer different questions.

### 35–45 min — ship decision

Students finish the design judgment:

> What did the extra complexity/computation buy, and was it enough?

### 45–50 min — share contradictions

Invite two students who reached different decisions. Different objectives can legitimately produce different winners.

## Likely confusions

### "Which strategy is best?"

Ask: **best for what objective?** Raw win rate, preparation budget, runtime throughput, model size, and maintenance burden are different currencies.

### "Is the rollout strategy machine learning?"

No. It is simulation/search at decision time. That contrast is useful: a trained learner pays preparation cost; rollout pays operating cost.

### "Why not use a neural network?"

Because sophistication is not the learning target. The transparent strategies let students inspect what complexity bought.

### "Why is CS1 code inside CS2?"

The vendor directory is a deliberate standalone-course compromise with provenance and drift checks. CS1 remains canonical. A third repetition should trigger shared packaging/automation instead of another copy.

## Optional enrichment

If a verified instructor-controlled container/hardware/NRP runner exists later, run the **same saved configuration/artifact** there and add execution context to the receipt.

Do not require students to provision cloud accounts, use GPUs, or access Kubernetes.

## What not to do

- do not make students rewrite scoring;
- do not add Q-learning equations;
- do not require every strategy;
- do not turn plot cosmetics into the assignment;
- do not rank students by family hardware;
- do not create Checkpoint 4;
- do not silently install packages during class.

## Fallback

If the experiment runner is unavailable, use the latest real validation artifacts under `artifacts/week16_farkle/` and raw receipt under `sidecar/runs/`. Do **not** invent sample numbers. If no real validation artifact exists yet, treat Week 16 as not fully release-ready and run the validator on a known-good machine first.
