# CS2 — August 31 lecture notes: find a useful boundary

## Big idea

“It runs” and “it runs usefully” are different claims. Your hardware is a
starting point, not your ceiling. Choose a model and a task that fit, then
verify the result instead of trusting a fluent answer.

## 7 things to remember

1. Local means the model runs on the box you are interacting with; remote
   means the model runs elsewhere and returns a result over a network.
2. A GPU has limited VRAM, and the display and other work already consume
   some of it.
3. A model’s size on disk is not the same as its working memory requirement.
4. GPU-only execution works only when everything fits; a CPU/GPU split can be
   useful, but may be slower.
5. Start with one small, bounded task. Read the diff and run an independent
   test.
6. “In God we trust; everything else we verify” is a workflow rule: the
   model’s claim about itself is not proof.
7. A World Bible is a fictional design seed. When a model treats it as a
   real engineering support ticket, that mismatch is evidence about the
   prompt and the model—not a reason to pretend the output is correct.

## Commands and code we used

These are the commands shown or directly discussed in class:

```text
ollama list
ollama run MODEL_NAME
nvidia-smi
clear
exit
```

The demonstrated model examples included `qwen3:1.7b`, `qwen3:14b`, and
Mistral. The class also discussed using Termux on a phone and reaching a
remote machine through WireGuard/SSH; no promise was made that a phone must
run a useful model locally.

## Vocabulary

- **CPU:** general-purpose processor.
- **GPU:** processor designed for parallel math.
- **VRAM:** memory local to the GPU; a practical model-size ceiling.
- **Local inference:** computation on the machine you are using.
- **Remote inference:** computation on another machine, reached over a
  network.
- **Model boundary:** the point where a model/task/context combination stops
  being useful.
- **World Bible v0.1:** premise, cast, one flow, questions, unknowns, and
  tentative object predictions for one fictional world.

## Common mistakes and what they mean

- **Choosing the largest model first:** size alone does not guarantee a good
  result. Use the smallest sufficient model for the bite.
- **Assuming GPU-only is always best:** if the model does not fit in VRAM,
  spilling work to the CPU may be necessary.
- **Pasting a huge prompt:** reduce the request to one bounded task and make
  the intended fictional context explicit.
- **Accepting the first answer:** compare the output with the prompt, inspect
  the change, and test independently.

## If you got lost

Return to this loop: state the goal → establish a baseline → make one small
request → inspect the diff/output → run independent proof → keep or revise.
For the world exercise, choose one of Frontier Settlement, Investigation
Bureau, Starship Log, or Small Business and write only a short v0.1 seed.

## Before next class

Complete the ungraded Week 3 World Bible v0.1: premise, 5–8 nouns, one real
flow, three software questions, 2–3 known unknowns, and 3–5 tentative object
predictions. Keep one concise entry and leave uncertainty visible.
