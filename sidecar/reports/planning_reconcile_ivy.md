# CS2 planning reconciliation — Ivy

Date: 2026-09-07
Run: `ef331bdb0999ab80b072be211a8ed3c3`
Work file SHA-256: `f1f2d845c5a43e6a47e51ac66c28a19d3ccf379ddb841c97aee453d53d2e41de`

## Source verification

I freshly fetched `origin` before inspection. The verified `origin/main` tip
for this pass is `8075c7ecda3ec12ed8235a07b7b7a16c2f9d3568` (`Unlock Kelsey in
FA_2026`). Every Week 3–15 gate and rubric was read from that fetched ref;
the planning reconciliation below is based on those files, not on the stale
canonical checkout.

Weeks 1, 2, and 16 were not changed. No assignment gate or rubric file was
changed.

**Integration note (added by Ivy, not the Codex worker):** the worker's own
`planning/week-04.md` rewrite was correct on topic but has since been
dropped from this branch. A separate, already-accepted bite
(`ivy/cs2-week04-buildout-v2` @ `7c1a3c8`) rewrote the same file more fully
— full student path table, cross-reference tokens, AI Fluency section — and
both branches were based on `origin/main` independently, so merging both
unchanged would have produced a real conflict on this one file at
merge-to-main time. Reverted this branch's `planning/week-04.md` to
`origin/main`'s content (dropping this bite's own week-4 edit only) so
whichever of the two branches merges first, the other applies cleanly;
`ivy/cs2-week04-buildout-v2`'s version is the one that should win for
Week 4. Every other week (3, 5–15) and the two lesson-reference fixes below
are unaffected and remain this bite's own work.

## Before / after

| Week | Old `planning/` topic | Current gate/rubric topic | Result |
|---:|---|---|---|
| 3 | Cohesive Encapsulated Objects | Found Your World / Light World Seed (ungraded) | Rewritten |
| 4 | Collaborating Objects, Composition, and Invariants | Cohesive Object Boundary | Superseded — see note below |
| 5 | Earned Inheritance and Polymorphism | Collaborating Objects and Invariant | Rewritten |
| 6 | Contracts and Swappable Collaborators | Earned Substitution | Rewritten |
| 7 | Data Abstractions: List, Stack, Queue | Contract and Swap | Rewritten |
| 8 | Search, Order, and Maintenance Tradeoffs | World-Fit Data Abstraction | Rewritten |
| 9 | Compact GUI and Event Flow | Search/Order Tradeoff | Rewritten |
| 10 | Honest Data Visualization | Compact GUI over Tested Model | Rewritten |
| 11 | Data Storytelling / Flex Clinic | Honest Visualization from Project Data | Rewritten |
| 12 | Stabilize, Document, and Prepare Peer Review | Data Storytelling / Flex Clinic | Rewritten |
| 13 | Major Odyssey Culmination and Design Review | Stabilization and Peer-Review Preparation | Rewritten |
| 14 | Source Management, Collaboration, and Reproducibility | Culmination Design Review | Rewritten |
| 15 | Buffer: Asynchronous, Light, and Self-Contained | Professional Workflow Receipt | Rewritten |

Each planning file now states the corresponding gate's topic, evidence shape,
and week-specific narrative in the existing concise planning voice.

## Additional stale references

The live course docs, syllabus, resource map, course-design spine, and other
high-level CS2 references already matched the current Week 3–15 sequence.
Two small same-shaped stale references remained in lessons and were corrected:

1. `lessons/week-09-tkinter-model-view-lab.md` now maps composition,
   polymorphism, contract swap, data abstraction, search/order, and GUI work
   to Weeks 5–10 rather than Weeks 4–9.
2. `lessons/week-16-farkle-ml-experiment-bench.md` now identifies the
   swappable-collaborator idea as Week 7 rather than Week 6.

Historical sidecar reports and raw run records were left unchanged. No larger
separate concern was found in live source files.

## Validation

- `git diff --check` passes.
- Planning headers for Weeks 3–15 were cross-checked against the corresponding
  gate and rubric headers from freshly fetched `origin/main`.
- Changed paths are limited to the 13 planning files, the two stale lesson
  references above, and this report.
- The managed worktree was allocated from `origin/main` at
  `8075c7ecda3ec12ed8235a07b7b7a16c2f9d3568` using the run identity and exact
  work-file hash recorded above.
