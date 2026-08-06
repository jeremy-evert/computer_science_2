# Odyssey Gate — Week 6 rubric: Checkpoint 1 (four-axis Full Build)

Matches `docs/curriculum/judgment_toolkit.md` §2/§4. This is a checkpoint,
not a Quick Check: assess the working integrated build on the four Full Build
axes rather than averaging Week 2–5 gate checklists.

| Axis | Strong | Solid | Not yet |
|---|---|---|---|
| Functions | The project runs end to end; an accepted action, a rejected action, and a relaunch/reload all work as claimed. | Main flow runs, but one secondary/error/reload path needs a small correction. | The integrated project cannot be run or its claimed flow is substantially missing. |
| Concept use | Exceptions protect a real mutation, an imported module owns coherent related behavior, and saved state is reloaded in a later run. | All three concepts appear and mostly connect, but one is thin or only partly integrated. | One or more required concepts is absent, cosmetic, or disconnected from the working flow. |
| Explanation | Clearly explains the data/control path across validation, module call, save, and reload, including one real problem encountered. | Explains what changed and names the pieces, though one connection or failure analysis is vague. | Explanation is absent, generic, or inconsistent with the submitted program. |
| Demonstrability | Another person can follow concise run steps plus error-path and two-run persistence evidence without guessing setup. | Evidence is present but setup, trace, or file location needs clarification. | No usable run instructions/evidence, or the claimed persistence/error behavior cannot be checked. |

## Grading notes

- “Integrated” means the rejected action does not corrupt the data that is
  subsequently saved or reloaded; three isolated demos do not meet the
  checkpoint's purpose.
- The local module must be genuinely imported by the working entry point, not
  merely included in the repository.
- A pre-seeded file is useful setup but does not replace evidence that a first
  run saved data later used by a second run.
- Scope is deliberately low-stakes. Do not reward size over a clear,
  working, explainable three-concept connection.
- The World Bible/Checkpoint Debrief entry is required evidence for
  explanation, but is not an additional separately scored gate.
