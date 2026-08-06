# Odyssey Gate — Week 6: Coding Odyssey Checkpoint 1 — robust, reusable, persistent

**Concept:** integration of exceptions, modules, and files (Chapters 10–12 in
the zyBooks numbering; Deitel, *Intro to Python for Computer Science and Data
Science*, exception, module/namespace, and file-processing topics). **This
week's gate is Checkpoint 1 itself** — see
`assignments/A2-coding-odyssey-project.md` and `planning/week-06.md`.
**Instruments:** Full Build + Debrief — see
`docs/curriculum/judgment_toolkit.md` §2/§4.

## The checkpoint (do this first)

Submit a small but complete working pass of your Odyssey world that connects
all three parts of this arc:

1. **Robust:** one user-facing action handles expected bad input or an invalid
   world rule without corrupting state or ending the program unexpectedly.
2. **Reusable:** related behavior lives in an imported local module with a
   clear boundary.
3. **Persistent:** the action saves meaningful state and a later run reloads
   it for a visible result.

Then **explain** in your own words how the exception path, module, and saved
data connect, and **demonstrate** the program with both an error-path trace
and a two-run persistence trace. This is an integration checkpoint, not a
request for a large project.

## Suggested textbook problem (optional scaffolding)

Use your Week 3 validation and Week 4 module as the core. Have one accepted
world action update state, save it through a context-managed text/CSV file,
then relaunch and display the reloaded state. Have one rejected action raise
and catch the custom exception before it changes saved data.

- **Frontier Settlement:** a ration request is validated in
  `settlement_tools`, saved to stores, and reloaded for the next distribution.
- **Investigation Bureau:** a case-priority update is validated in
  `case_tools`, saved to a case file, and reloaded into the next briefing.
- **Starship Log:** a fuel-consuming action is validated in `ship_tools`,
  saved to the log, and reloaded for pre-flight status.
- **Small Business:** a sale is validated in `inventory_tools`, saved to an
  inventory record, and reloaded before the next sale.

Do this version directly if it helps, then let it *be* your checkpoint
submission.

## Then: open continuation (full Build, holistic)

Polish only where it makes the integrated flow easier to run, read, or
explain. A small feature that genuinely connects all three concepts is
stronger than a large collection of unrelated commands.

## World Bible

Add a short Checkpoint 1 entry: what now works across runs, what failed while
connecting the three parts, and what you would change before adding the next
arc. This is the first Checkpoint Debrief and Judgment Log touchpoint.

## Looking ahead

Week 7 begins inheritance: the persistent world now needs objects with shared
state and specialized behavior.
