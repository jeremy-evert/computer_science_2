# Computer Science II Sidecar

This directory is the project-local workbench for Jeremy, ChatGPT, the Foreman, golems, and other agents working **about** Computer Science II.

The repository outside `sidecar/` is the course itself: current course content, scripts, configuration, decisions, planning, tests, and other hard-nosed project truth. It should describe Computer Science II without narrating the agent/human process that produced it.

The sidecar preserves the self-aware work history: prompts, reports, questions, run evidence, investigations, abandoned ideas, and the reasoning trail that may matter later.

## Context rule

Do not recursively read the entire sidecar by default. Read the current prompt and only the sidecar history needed for the job. When working on the course itself, prefer current project truth outside `sidecar/`; consult sidecar history when the task actually requires archaeology.

## Current shape

- `prompts/` — open project-local work orders and investigations.
- `prompts/completed/` — prompts that have been completed; done prompts remain durable prompts.
- `reports/` — results, conclusions, postmortems, and evidence summaries from sidecar work.
- `questions/` — unresolved ambiguities or decisions that need explicit resolution.
- `runs/` — raw or bulky execution evidence that should not clutter current course truth.

A sidecar artifact is not authoritative merely because it exists. When a sidecar investigation establishes durable current truth, promote that truth into the appropriate project file outside `sidecar/` and keep the sidecar record as provenance.
