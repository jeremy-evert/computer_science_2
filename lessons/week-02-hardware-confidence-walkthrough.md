# Week 2 walkthrough — How to get started

This is the **how**, not the **why** — see
[Hardware Confidence + Small Models](week-02-hardware-confidence.md) for the
concepts this walkthrough assumes. It does not repeat installation steps
that Computing Commons already owns as the shared, verified route; it points
to that road instead of forking a second copy of it.

## The sequence

1. **Inventory what you have.** CPU, RAM, GPU/VRAM if present, and whether
   the machine is a managed lab machine or your own device. You do not need
   exact numbers — you need enough to reason about scale.
2. **Choose your path.** Managed CS lab machine, your own machine, or a
   cockpit device connecting to a remote environment. All three are
   legitimate; pick the one that matches what you inventoried.
3. **Reach the canonical Local AI setup/verification road.** Go to
   **Computing Commons → `02 — Week 2: Build and Verify Local AI`**. That
   module is the shared, verified sequence for installing and confirming
   Ollama, the approved model, and Aider — the same instructions every
   Fall 2026 course uses, kept in one place so they stay correct.
4. **Prove a model can answer** — locally through Ollama, or through the
   approved remote/cockpit architecture if that is your path. This is the
   `BASELINE` step: confirm the tool actually responds before asking it to
   do anything useful.
5. **Run one tiny bounded Aider task.** Use the Commons "Aider Work First"
   guide's safe loop (`computing_commons/curriculum/week2/aider-work-first.md`,
   linked from the Canvas Week 2 module): one sentence, one bounded change,
   nothing else touched.
6. **Inspect the diff.** Read every line Aider changed before you judge
   anything. This is not optional and it is not something you delegate back
   to the model.
7. **Run independent proof.** Run the supplied test yourself. A model
   claiming success is not evidence; a test you ran and read is.
8. **Record what worked and where your confidence dropped.** One or two
   honest sentences. This is the raw material for the Bite Ladder: where did
   the boundary actually sit for your hardware, your model, and your task?

## Next step

Once you have completed the loop once, continue into the Computing Commons
**Aider Days** road for the next bounded exercise, and keep the World Bible
work for this week moving in parallel — this walkthrough is the on-ramp, not
a detour from it.
