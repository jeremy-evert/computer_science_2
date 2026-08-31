# Week 2 opening — Your computer is more powerful than you think

## The reframe

Do not ask: **"Can my computer run AI?"** Ask: **"What AI can my computer run
well?"**

Every AI-assisted task in this course, and in your career after it, sits at
the intersection of five variables:

- **Hardware** — what you can run at all
- **Model** — what the loaded model is actually good at
- **Task size** — how much you asked for in one request
- **Context** — how much surrounding code or text the model has to hold
- **Verification** — how you will know whether the answer was right

A larger model does not rescue a task that is too big, too vague, or
unverified. The machine is powerful. **You are the multiplier.**

Slogan for the semester: **love AI more, trust AI less.**

## Hardware vocabulary, at a useful level

You do not need to become a hardware engineer. You need enough vocabulary to
reason about a decision.

- **CPU** — general-purpose processor. Always present. Fine for small models
  and for orchestrating tools like Aider.
- **RAM** — system memory. A model that will not fit in RAM cannot run on CPU
  alone.
- **GPU** — a processor built for the parallel math models need. Turns
  minutes of inference into seconds.
- **VRAM** — memory that lives on the GPU itself. This is usually the real
  ceiling on which model sizes are practical on a given machine, not the GPU's
  raw speed.
- **Quantization** — compressing a model's numbers (for example from 16-bit
  to 4-bit precision) so it fits in less VRAM, at a small and usually
  acceptable cost in answer quality. Quantization is why a model that looks
  too large on paper can still run well on modest hardware.

"It runs" and "it runs usefully" are different claims. Quantization, task
size, and context length all affect the second claim independently of the
first.

## Small models can be excellent at bounded work

A small local model asked to make one narrow, well-specified change to one
file — and checked against a real test — is a reliable tool. The same model
asked to "fix the whole project" with no test and no boundary is not a
reliable tool, regardless of its size. The goal is **the smallest sufficient
model for the bite**, not the largest model you can technically load.

A larger model does not fix an underspecified or oversized request. It just
produces a longer, more confident-sounding version of the same problem.

## Local versus remote inference

Both are legitimate architecture choices, not a hierarchy:

- **Local inference** — the model runs on your own machine. Private,
  works offline, bounded by your own hardware.
- **Remote inference** — your machine is a **cockpit**. It sends the request
  to a model running elsewhere (a lab machine, a server, a remote Linux
  environment) and receives the result over the network.

A tablet, an underpowered laptop, or another nontraditional device is not
disqualified from this course. It is a cockpit: it may run a small model
locally when that is practical, or connect to a remote Linux/model
environment when that is the stronger architecture for that device. This
course does not promise unsupported native Aider behavior on iPadOS or
similar platforms.

Your hardware determines your **starting point**, not your ceiling, as a
programmer.

## The Bite Ladder

A structured way to discover your own model/hardware/workflow boundary
instead of trusting a benchmark slogan:

1. Give the model one small, bounded task.
2. Inspect the diff. Read every changed line.
3. Run an independent test — not the model's own claim about itself.
4. If it held, take one rung up: a slightly larger task or more context.
5. If it broke, that is your current boundary. Back off a rung rather than
   blaming the model outright — the next request may simply need to be
   smaller or better specified.

## The course loop

Every AI-assisted change in this course follows the same loop:

```text
GOAL -> BASELINE -> AIDER -> DIFF -> PROOF -> COMMIT
```

State the goal. See the failing baseline. Let Aider propose a bounded change.
Read the diff. Run independent proof. Commit only what verified.

The shorthand for how trust gets built, one bite at a time:

```text
small model -> small bite -> inspect diff -> test -> trust earned
```

Model output is a proposal. The diff you actually read and the test you
actually ran are verified software-engineering evidence — a different, much
stronger claim than "the model said it worked."

## Where the technical setup lives

This page is the concept and confidence layer. The exact install/verify
steps — Ollama, the approved local model, Aider, and the readiness checker —
live in the shared Computing Commons Local AI road, not here, so the same
verified instructions serve every course. See the
[Week 2 walkthrough](week-02-hardware-confidence-walkthrough.md) for the
exact sequence and the Canvas link into that road.

## What this is not

This is not a hardware-engineering lecture, and it is not a conversion of CS2
into an AI course. Local AI here is an engineering instrument used to make
repository work, verification, and model boundaries visible — the same
discipline this course already asks of every other technique you use. The
Reasoning Odyssey / World Bible work that Week 2 also carries continues
alongside this opening, not instead of it.
