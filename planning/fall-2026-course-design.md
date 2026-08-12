# COMSC-1053 Fall 2026 course design

## Purpose and outcomes

Computer Science II is the post-COMSC-1033 depth course: students arrive able to write small Python programs with functions, collections, and introductory classes, then learn to make programs robust, reusable, persistent, extensible, explainable, and algorithmically defensible. The durable course rhythm is the Coding Odyssey: a persistent project with weekly gates, four checkpoints, pair-work, feedback/debriefs, and a final portfolio. Required outcomes are exception-aware design; modules and files; deliberate inheritance; traced recursion; data visualization; and justified search/sort choices. Students must test, document, and explain their own code. AI may be used as a reasoning/debugging companion only when its contribution is disclosed, inspected, tested, and revised by the student; it cannot replace the demonstration or debrief.

## Semester spine and module blueprint

Every Canvas/Savnac module has: **Week at a Glance** (purpose, objectives, path, due items), instructor slides/live examples, selected zyBooks links, Odyssey gate/checkpoint and rubric, and a visible acceptance-test path (overview → reading/activity → submission/evidence). Publish only source-backed dates; Week 17 deadline remains a schedule confirmation.

| Week | Learning purpose and selected zyBooks | Student activity / evidence | Module readiness |
|---|---|---|---|
| 1 | Kickoff; diagnose COMSC-1033 carryover. Optional Ch. 9 classes review. | Environment/repository check; Odyssey choice. | Shared kickoff materials and diagnostic visible. |
| 2–3 | Exceptions (required Ch. 10 non-lab sections). Week 2 also carries the shared Build and Verify Your Local AI Lab readiness experience (`planning/week-02-local-ai-lab-integration.md`); canonical content stays in `local_ai_lab_setup`/`windows_classroom`. | Build and test recoverable error paths; Gates 2–3. Week 2: local-AI readiness check plus a bounded Aider-assisted repair, verified by independent diff/test review. | Exception examples, links, gate rubric. Local-AI lab crosswalk and readiness pointer published. |
| 4 | Modules (required Ch. 11). | Extract a coherent module; Gate 4. | Import/reuse activity and rubric. |
| 5 | Files (required Ch. 12). | Persist meaningful program state; Gate 5. | File/data activity and rubric. |
| 6 | Integrate robustness, reuse, persistence. | Checkpoint 1 and debrief. | Checkpoint brief/rubric published. |
| 7–8 | Inheritance (required Ch. 13). | Model and test a hierarchy; Gates 7–8. | Live modeling, links, rubrics. |
| 9 | Consolidate inheritance. | Checkpoint 2 demonstration/debrief. | Checkpoint path visible. |
| 10–11 | Recursion (required Ch. 14). | Trace, test, and justify base cases; Gates 10–11. | Tracing activity and evidence rubric. |
| 12 | Plotting/data exploration (required Ch. 15). | Plot project data and interpret it; Gate 12. | Data/plot activity and rubric. |
| 13 | Search, sort, qualitative efficiency (required Ch. 16). | Decide/Compare #1 plus Gate 13. | Trace/compare activity and rubric. |
| 14 | Consolidate recursion + plotting. | Checkpoint 3 and Full Trail Debrief. | Checkpoint path visible. |
| 15 | Integration/polish; no new chapter. | Resolve project debt; update World Bible. | Feedback and polish checklist. |
| 16 | Full integration. | Checkpoint 4, capstone Decide/Compare, final reflection start. | Runnable portfolio expectation/rubric. |
| 17 | Final portfolio and reflection. | Demonstration, Judgment Log, reflection. | Finals visibility after actual deadline confirmation. |

## Section menu and non-zyBooks work

`zybooks-section-decisions.csv` assigns all 466 discovered sections once. The 44 KEEP sections are the non-lab instructional sections in chapters 10–16. Labs in those chapters, class refresher chapters 9/26, aligned additional labs (27–30), and AI chapter 32 are OPTIONAL (100) for diagnosis, extra practice, or enrichment. The remaining 322 are UNUSED in the normal path because they repeat CS1 or are bank/extra content. This protects the course from becoming a second introduction to Python.

ZyBooks alone does not supply the Odyssey's sustained design, pair programming/code review, version-control practice, instructor feedback, live debugging, project demonstrations, or evidence-based AI provenance. Those remain instructor-created/course-owned work.

## Open decisions and vendor question

- Jeremy must choose whether Odyssey is a new CS2 world or a formal continuation of the CS1 world; existing A2 preserves both paths.
- Confirm the actual final-portfolio deadline and any shared-strand artifacts against the real section schedule.
- Ask zyBooks: “For COMSC-1053, what is the student subscription price for a configuration limited to the required chapters 10–16, compared with the current configuration?” No price reduction is assumed.
