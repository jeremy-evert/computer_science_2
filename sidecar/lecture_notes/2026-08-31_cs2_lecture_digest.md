# CS2 lecture digest — August 31, 2026

**Course:** Computer Science II (COMSC-1053-1417)
**Date:** August 31, 2026
**Evidence:** fresh local Whisper/CTranslate2 medium.en VTT from the protected
MP4; Teams VTT used only as a cross-check.
**Purpose:** de-identified instructor digest, not a transcript.

## Teaching goals

- Distinguish “runs” from “runs usefully.”
- Explain local versus remote inference and the role of CPU, GPU, RAM, and
  VRAM.
- Practice the smallest-sufficient-model / smallest-sufficient-task mindset.
- Establish verification as a required engineering step.
- Introduce the four fictional worlds and the World Bible v0.1 seed.

## What was actually taught

The instructor opened with the reframe “What AI can my computer run well?”
and used the contrast between a technically runnable system and a useful
workflow. Local was defined as computation on the box being used; remote was
defined as computation elsewhere returned over a network. The room’s 8 GB
GPUs were discussed as shared hardware whose display and recording duties
consume capacity.

The class examined Ollama model inventory and runs, including a small
`qwen3:1.7b`, larger Qwen examples, and Mistral. The instructor compared a
model’s disk size with its working size, used `nvidia-smi`, and explained why
an oversized model spills work between GPU and CPU. A live readout showed a
10 GB working model using roughly 37% CPU / 63% GPU, followed later by an
80% GPU / 20% CPU versus 63% GPU / 37% CPU comparison. The practical analogy
was a model that is too large for an 8-sized bucket.

The workflow lesson was: give a model one small task, inspect the diff, run
an independent test, and climb the task/context ladder only when evidence
holds. The instructor used an `add` function and 4 + 4 as the simplest
acceptable-result test, emphasizing that an answer of 7 stops the process.

The instructor then demonstrated a World Bible prompt using **Starship Log**
(one of four choices: Frontier Settlement, Investigation Bureau, Starship
Log, Small Business). The small model misread the fictional setting prompt
as a real engineering support ticket, discussing sensor calibration and
oscilloscope-style troubleshooting. This was explicitly treated as a
teaching moment and evidence of a context/model mismatch. The instructor
retried with a mixed model and compared model sizes.

Finally, the class discussed phone workflows: Termux can provide a terminal,
but a slow phone plus a tiny local model may be less useful than using the
phone as a client for a remote server. WireGuard and SSH were named as one
remote-access architecture, and Microsoft Copilot was mentioned as another
remote service available on a phone.

## Commands and examples demonstrated

```text
ollama list
ollama run MODEL_NAME
nvidia-smi
clear
exit
```

Other demonstrated material: a minimal `add(4, 4)` verification example;
Ollama model inventory; a Starship Log World Bible prompt; and a model
comparison using the same prompt. No student names or student work are
included here.

## Timestamp table (approximate)

| Time | Teaching moment / evidence |
|---|---|
| 09:15 | Reframe: “What AI can my computer run well?” |
| 09:57 | “It runs” versus “it runs usefully.” |
| 11:05 | Physical GPU touchpoint and local definition. |
| 17:10–17:55 | One small task; diff; independent test; `add(4, 4)`. |
| 32:20 | `ollama list` and choosing a model. |
| 34:19 | Four world choices; Starship Log selected. |
| 35:10–36:05 | Small model misreads fictional prompt as engineering ticket; correction. |
| 37:27–38:55 | Mixed model and 1.4 GB versus 9.3 GB comparison. |
| 39:23–41:18 | 8 GB VRAM, 10 GB working model, CPU/GPU allocation. |
| 42:11–45:05 | 20/80 and 63/37 splits; fit and fan behavior. |
| 46:00–48:45 | Termux, WireGuard/SSH, and remote phone access. |

## Corrections and unfinished threads

**LECTURE SAID:** A model’s disk footprint and operating footprint are
different; a 10 GB working model cannot fit entirely in an 8 GB GPU.
**FOLLOW-UP NOTE:** Read the live memory and utilization evidence, not just
the model name or download size.

**LECTURE SAID:** The Starship Log prompt was a World Bible prompt.
**FOLLOW-UP NOTE:** Make the fictional/design intent explicit and treat a
real-world troubleshooting answer as a mismatch to investigate.

The instructor left the broader question of how much productive friction to
introduce as an ongoing teaching-design question. The phone-local versus
phone-remote tradeoff was discussed but not benchmarked in this class.

## Assignment / next step

Complete the ungraded Week 3 World Bible v0.1: premise, 5–8 nouns, one real
flow, three software questions, 2–3 known unknowns, and 3–5 tentative object
predictions. The seed is allowed to be wrong and will be revisited later.
