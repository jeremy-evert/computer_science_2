# Report 007 — CS2 capability spine, CS1 handoff, and open-resource slurp

**Work order:** `jeremy_task_tracking/codex_prompts/019_cs2_capability_spine_handoff_and_open_resource_slurp.md` (Prompt 013 was read only as superseded provenance and was not run.)
**Scope:** research and decision support for Fall 2026 COMSC-1053 only; no course plan, assignment, rubric, Savnac, Canvas, or ZyBooks mutation.
**Access date:** 2026-08-12. **Official floor:** `course_metadata.yaml` catalog description. No separate verified CLO source was found in the active CS2 repository, so this report does not invent one.

## Executive finding

CS2 should make **eight** irreducible advances, led by object design rather than inheritance syntax: design encapsulated collaborating objects; select/use inheritance and polymorphism; express contracts with abstract classes/protocol-like interfaces; build a small event-driven GUI; choose and use list/stack/queue abstractions; reason about searching/sorting and cost; use recursion/linked structures only as a bounded supporting design lens; and deliver a tested, documented, reviewable project through professional workflow. The existing Week 3–13 map is a reasonable textbook survey, but it is invalid as the proposed course spine because it lacks the catalog-required GUI/event and abstract/interface treatment and does not explicitly teach classic list/stack/queue data abstraction.

The recommended package is **no single backbone**: course-owned Odyssey work supplies authentic practice; Python’s official documentation is the durable reference layer; Runestone *Problem Solving with Algorithms and Data Structures using Python* is the linked interactive data-structure/algorithm layer; the legally captured CS1 CS50P/GitHub corpus is reused only for prerequisite/reference and workflow; Docker documentation is a Week-14 link. This is a credible zero-cost path. ZyBooks remains an optional/control reference, not the organizing principle.

## A — Fixed semester frame and active-source conflicts

| Week | Jeremy-pinned role | Current active-course claim | Source file(s) | Conflict? | Follow-on reconciliation needed? |
|---|---|---|---|---|---|
| 1 | Universal Success Foundations; no technical CS2 spine | Universal kickoff; no chapter concept | `planning/week-01.md` | No material conflict | Confirm shared Monday/Wednesday/Friday bodies in shared repo only |
| 2 | Build/verify local AI lab; no equal traditional unit | Exceptions round 1 plus Odyssey gate and lab are both due | `planning/week-02.md`; `assignments/odyssey_gates/week-02.md` | **Yes** | Remove/relocate exceptions-first gate; preserve the shared lab’s baseline→bounded request→diff→independent test→reason→accept/reject shape |
| 3 | Begin a love and understanding of solid OOP | Exceptions round 2 | `planning/week-03.md` | **Yes** | Replace with object-design/encapsulation opening |
| 14 | Source management + containers using real project | Recursion/plotting checkpoint | `planning/week-14.md`; gate 14 | **Yes** | Author Git history/recovery, collaboration/review, reproducibility, and bounded container activity |
| 15 | Mexico; fully asynchronous and light | Integration/polish, MWF | `planning/week-15.md` | **Yes** | Make self-contained asynchronous cleanup/reflection only |
| 16 | Shared Farkle + ML consumes CS2 skills | Final integration/search-sort checkpoint | `planning/week-16.md`; gate 16 | **Yes** | Move major Odyssey construction to Week 13; integrate Farkle/ML |
| 17 | Reflection and closure | Final portfolio submission | `planning/week-17.md`; A2 | Partial | Retain project as evidence, remove technical-final pressure |

**Additional active drift:** A1/A2 and Reports 002–005 define the course from exceptions/modules/files → inheritance → recursion → plotting → search/sort and Deitel/ZyBooks. That map calls every genre to include a class hierarchy, recursion, plotting, and search/sort by Week 16–17. It does not earn all of those as catalog requirements, and it misses GUI/event/abstract/interface/list-stack-queue. Do not repair these files in this prompt.

## B — CS1 → CS2 handoff

The formal machine-readable handoff is [`007_cs1_to_cs2_handoff_matrix.csv`](007_cs1_to_cs2_handoff_matrix.csv) and [JSON](007_cs1_to_cs2_handoff_matrix.json). The reconciled CS1 source is Reports 011/012, not older maps.

| CS1 capability | Evidence students are expected to have | CS2 treatment | New CS2 capability enabled | Evidence/source | Risk if assumption fails |
|---|---|---|---|---|---|
| Run/read/change Python; values/I/O; decisions/loops | Pinned C01–C04 | ASSUME; diagnostic through Week-3 studio | S01, S04, S05 | CS1 Report 011 | Trace/read diagnostic, never a full unit |
| Functions/decomposition; strings/lists/dicts | Pinned C05–C07; real Odyssey gates | ASSUME; QUICK REFRESH IN CONTEXT | S01, S05, S06, S08 | CS1 Report 011 | Refactor/data-state micro-clinic |
| Basic classes/objects, no inheritance | C08; Weeks 12–13 introductory OOP | QUICK REFRESH IN CONTEXT | S01 then S02 | CS1 Reports 011/012 | Object-model repair before inheritance, not syntax reteach |
| CSV/JSON/Markdown persistence | C09 and genre save/load | ASSUME | S08 | CS1 Report 011 | Refresh only when project format needs it |
| Testing/debugging; explanation | C10/C11 and Judgment Log | ASSUME/DIAGNOSTIC | S01, S06, S08 | CS1 Report 011 | Supplied failing test and existing explanation scaffold |
| Git/GitHub; AI accountability | C12/C13, CS1 Week 14 | QUICK REFRESH / ASSUME | S08 | CS1 Report 012 | Recovery diagnostic; explicitly repeat evidence habit |

## C — Proposed irreducible CS2 capability set

| ID | Capability and student evidence | Why CS2 | Official obligation | CS1 prerequisite | Natural Odyssey fit | Placement |
|---|---|---|---|---|---|---|
| S01 | Design encapsulated collaborating objects; state invariants, methods, composition, tests, and rationale | Goes beyond naming a beginner class | OOP thinking/design; program design; modularity; debugging/documentation | C05, C08, C10–11 | All: Settlement/Case/Ship/Business services collaborating | Weeks 3–4 + recurring |
| S02 | Choose inheritance only for a true subtype; override behavior and exercise polymorphism through a shared operation | New required OOP depth | inheritance, encapsulation, polymorphism | S01 | types of events, cases, crew roles, products/transactions | Weeks 5–6 |
| S03 | Define/test a contract with `abc.ABC`/abstract method and explain Python’s interface-equivalent protocol boundary | Explicitly named catalog concepts absent from CS1 | abstract classes; interfaces; modularity | S01–S02 | action/report/persistence interfaces in every world | Week 6 + recurring |
| S04 | Build a modest usable Tkinter view whose events invoke model operations; keep UI separate from domain logic | New interaction model | GUI; event-driven programming | S01, C03 | dashboard/command form for every world | Weeks 9–10 |
| S05 | Select and use list, stack, and queue abstractions; explain operations and representation boundaries | Catalog-specific data abstraction | list, stack, queue; design | C07 | roster, undo/history, work/event queue—natural across all worlds | Weeks 7–8 |
| S06 | Trace/select search/order operations and explain qualitative growth and data-maintenance tradeoffs | Builds upon collections and supports design judgment | program design, debugging/documentation (not separately catalog-named) | S05, C11 | find/sort roster, leads, log events, inventory | Week 8 + integrated |
| S07 | Use recursive or linked/nested representation only when it makes the model clearer; trace base/reduction/cost | Valuable design extension, **not an official hard floor** | Supports data abstraction/design | S05 | clue tree, nested order/category, system tree, connected map; may be genre-hostile for a flat world | Optional Week 11 clinic/enrichment |
| S08 | Deliver/review a tested documented Odyssey increment: bounded AI request, diff, independent tests, read/reason, accept/reject; use Git history and later containers to reproduce a runnable project | Turns skills into professional capability | design, modularity, debugging, documentation, source management in paired projects | C09–C13 | Genre-neutral, authentic project evidence | Every week; culminate Weeks 12–14 |

## D — Official catalog coverage audit

| Official requirement | Exact source | IDs | Proposed weeks | Existing coverage | Gap/conflict | Confidence |
|---|---|---|---|---|---|---|
| Inheritance, encapsulation, polymorphism | `course_metadata.yaml: official.catalog_description` | S01–S02 | 3–6 | Inheritance W7–9; polymorphism gate evidence in Report 004 | Encapsulation/design ramp is missing; late ordering conflicts Week 3 | High |
| Abstract classes; interfaces | same | S03 | 6 | No active Week 3–13 plan/gate treatment found | **Missing hard outcome** | High |
| GUI and event-driven programming | same | S04 | 9–10 | No active Week 3–13 plan/gate treatment found | **Missing hard outcome** | High |
| List, stack, queue data abstraction | same | S05 | 7–8 | Collections/search/sort only; no classic stack/queue commitment | **Missing hard outcome** | High |
| OOP thinking/design; program design; modularity | same | S01, S03, S08 | 3–13 | Modules W4 and inheritance exist | Topic-first rather than design-first | High |
| Debugging; documentation | same | S01, S08 | recurring | Existing Odyssey evidence/process exists | Make explicit design/test/documentation evidence | High |
| Source management in paired projects | same | S08 | 14 bridge, recurring before it | Week 2 diff and inherited CS1-style evidence; no pinned Week-14 plan | **Conflict with pinned Week 14** | High |

No verified official CLO added recursion, linked structures, search/sort, plotting, or Big-O. They remain pedagogical choices, not claimed official outcomes.

## E — Coding Odyssey fit and practice sufficiency

| ID | Frontier / Investigation / Starship / Small Business | Existing evidence | Repetition missing? | Required standalone practice | Optional/bonus | Genre concern |
|---|---|---|---|---|---|---|
| S01 | Settlement/Case/Ship/Business objects collaborating | World Bible and builds already exist | Design critique | 0 | object-model sketch/review | None |
| S02–S03 | event/case/crew/product subtypes; Action/Report contract | inherited W7–9 hierarchy gates | polymorphic call and contract test | 0 | small hierarchy trace | Avoid invented hierarchies |
| S04 | dashboard/form, event log, ship controls, inventory UI | none | GUI-event trace | 0 | Tkinter callback micro-lab | Keep interface modest; all worlds fit |
| S05 | roster/undo/work queue respectively | none | operation trace | 0 | visual stack/queue trace | Stack/queue should solve a real flow |
| S06 | lookup/order real world data | W13 existing | qualitative cost explanation | 0 | trace comparison | Binary search artificial if data is not maintained sorted |
| S07 | route/clue/system/category tree | W10–11 forces recursion | none when no natural nesting | 0 | optional recursion trace | **Genre-hostile when world is flat** |
| S08 | same project repo across all worlds | A1/A2 process and Week-2 lab | pair/review/container evidence | 0 | optional repair kata | None |

The Odyssey remains sufficient required programming practice when each gate carries a specific evidence pattern and timely feedback. It does **not** justify a second weekly problem-set treadmill.

## F — Existing course / ZyBooks alignment

| ID | Current week/topic | Current Odyssey/ZyBooks alignment | Catalog fit | Candidate | Why |
|---|---|---|---|---|---|
| S01 | none before inheritance | classes treated only as CS1 diagnostic in Report 005 | partial | Move to Weeks 3–4 | Needed conceptual ramp |
| S02 | W7–9 inheritance | Chapters 13 / hierarchy checkpoint (reports/plans) | yes | Move/compress | Put after object design; preserve only meaningful hierarchy |
| S03 | none | none | no | Add | Hard catalog gap |
| S04 | none | none | no | Add | Hard catalog gap |
| S05 | W13 search/sort uses collections | ZyBooks chapter 16 route | partial | Replace/expand | Stack/queue absent |
| S06 | W13 | real-data gate | supportive only | Keep compressed | Valuable but not a standalone hard floor |
| S07 | W10–11 recursion | two forced gates and W14 checkpoint | not required | Demote enrichment | Does not fit every genre |
| S08 | W2 and inherited checkpoints | local-AI stitch; A1 process | partial | Integrate; W14 upgrade | Pinned Week 14 requires containers/source management |

## G/H — Public resource scorecard and strategies

Full scores: [`007_cs2_resource_coverage_matrix.csv`](007_cs2_resource_coverage_matrix.csv) and [JSON](007_cs2_resource_coverage_matrix.json). Scores use 0 absent, 1 weak mention, 2 teachable/incomplete, 3 strong second-course treatment. Python documentation’s license explicitly allows documentation reproduction/derivatives under PSF License v2; its examples are also 0BSD. Runestone’s PyDS3 exposes direct basic-data-structure and tree/algorithm sections with interactive exercises, but this pass did not establish a corpus-preservation right, so it is link-only. GitHub Docs/Skills are reused from CS1’s captured CC BY/MIT evidence. Docker’s current official conceptual page is a direct no-account reference, but the documentation reuse basis was not established, so it is link-only.

| Strategy | Sources | Strong-core count | Clear holes | Cost/friction | Rights/capture | Decision |
|---|---|---:|---|---|---|---|
| **Zero-cost selected bundle** | course/Odyssey + Python docs + Runestone + reused CS1 corpus + Docker link | 8/8 with course-owned practice | GUI practice is course-owned; Runestone rights need confirmation for capture | $0; optional accounts only | PSF captured; CS1 reused; others links | **Select** |
| Lean/hybrid | selected bundle + ZyBooks assigned only to granular optional sections | 8/8 | same structural gaps unless course-owned material supplies them | possible paid access | ZyBooks restricted | Viable comparison, not default |
| ZyBooks-heavy control | inherited Chapters 10–16 plus gates | 4/8 clear/partial | GUI/event, abstract/interface, stack/queue and pinned weeks | paid/authenticated | restricted/private corpus | Reject as spine |

## I — Capture/slurp receipt

| Source | Reused CS1 | Attempted | Captured | Metadata-only | Skipped | Failed | New bytes | Manifest |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| CS50P; GitHub Docs/Skills | 15 existing bodies / 4 resource families | 0 | 0 | 0 | 0 | 0 | 0 | CS1 corpus references |
| Python official docs | 0 | 4 | 4 | 0 | 0 | 0 | 962,612 | `/mnt/brandy_nvme/jevert/durable/cs2_open_resources/manifest.jsonl` |
| Runestone PyDS3; Docker Docs; ZyBooks | 0 | 0 body captures | 0 | 3 | 0 | 0 | 0 | links/metadata only |

The intentionally small new durable corpus contains `abc`, `tkinter`, `queue`, and the license page. It covers S02–S05 and has four distinct capability sections. No third-party body was put in Git or duplicated from CS1.

## J/K — Holes and zero-cost package

| ID | Starting coverage | Exact missing piece | Severity | Candidate | Recommendation |
|---|---|---|---|---|---|
| S04 | Official Tkinter reference is strong but not instructional practice | accessible, bounded GUI/event practice | medium | course-owned two-callback micro-lab | Author it in follow-on; do not slurp another textbook |
| S05/S06 | Runestone strongest practice, capture rights unclear | class-ready optional exercise reuse | low | Runestone direct links | Link students; confirm rights only if reuse/capture is later desired |
| S08 | Docker page is conceptual | tiny reproducible-container exercise aligned to Windows lab constraints | medium | Docker Docs + instructor-owned Dockerfile | Author Week-14 activity after machine constraints are confirmed |
| S07 | no need for universal coverage | genre-fit recursive/linked task | low | optional Runestone section | Keep enrichment; instructor-owned alternative only when authentic |

| ID | Primary | Supplemental/practice | Account/license | Why sufficient |
|---|---|---|---|---|
| S01–S03 | Python `abc` docs; course studio | reused CS50P OOP reference | none; PSF / CC BY-NC-SA | Course owns design evidence; docs give exact language reference |
| S04 | Python Tkinter docs | course micro-lab/Odyssey UI | none; PSF | Catalog outcome plus authentic UI feature |
| S05–S06 | Runestone PyDS3 direct sections | Python `queue`; Odyssey traces | no account to read; link-only | Best focused interactive data/algorithm layer |
| S07 | Optional Runestone trees/recursion | Odyssey only when natural | link-only | Does not become universal requirement |
| S08 | reused GitHub Docs/Skills; Docker Docs | Week-2 local-AI workflow | optional GitHub; linked | Real project/repo is the evidence |

## L — Provisional Weeks 3–13 technical spine

| Week | Technical purpose | IDs | Odyssey evidence | Sources | AI/tool habit | Standalone |
|---|---|---|---|---|---|---|
| 3 | Model a real world with cohesive encapsulated objects and explain boundaries | S01 | object map + tested behavior | CS1 OOP refresh; Python docs | inspect a small diff | 0 |
| 4 | Refactor collaborating objects/composition; protect invariants and document decisions | S01, S08 | design revision + test | course studio/Python docs | test before/after request | 0 |
| 5 | Use inheritance only where substitution is real; verify polymorphic behavior | S02 | mixed subtype behavior | Python docs | compare proposed hierarchy with composition | 0 |
| 6 | Define an abstract contract/interface boundary and use it to swap a collaborator | S03, S08 | contract test + checkpoint | Python `abc` | read/reason about contract | 0 |
| 7 | Make data representation a design choice: list, stack, queue | S05 | operation trace in real world flow | Runestone/Python queue | test edge operations | 0 |
| 8 | Search/order real state and explain cost/maintenance tradeoff | S05, S06 | trace + choice | Runestone | verify claim from trace | 0 |
| 9 | Separate model from view and construct a modest usable GUI | S04 | view renders model state | Tkinter docs/course lab | inspect UI change | 0 |
| 10 | Handle events as controlled changes to model state and test callbacks | S04, S08 | two events + test/evidence | Tkinter docs | independent run/test | 0 |
| 11 | Make a bounded design extension; recursion/linked/nested structure only when authentic | S07, S01 | optional authentic feature or design refinement | Runestone | justify acceptance/rejection | 0 |
| 12 | Stabilize, document, and prepare the major Odyssey slice for peer review | S08 | runnable feature, test, docs | course/GitHub Docs | review diff and evidence | 0 |
| 13 | Culminate major creative construction with a design review and recovery-ready evidence | S01–S08 | demo, rationale, test, clean history | selected bundle | AI-aware peer review | 0 |

## M — Week 14 bridge: source management + containers

| Capability | CS1 baseline | CS2 upgrade | Real evidence | Candidate activity | Official obligation | Resource | Question |
|---|---|---|---|---|---|---|---|
| History/recovery | commits/GitHub basics | read history, recover a change, branch/merge or equivalent | real Odyssey repository | recreate/resolve a small reviewed change | source management; paired projects | reused GitHub Docs/Skills | pair workflow/tool constraints |
| AI-aware review | Week-2/CS1 evidence habit | peer reviews a bounded proposal from diff/tests/reasoning | project PR/branch or local patch | accept/reject review receipt | debugging/documentation | reused GitHub Docs | local collaboration setup |
| Reproducible runtime | no CS1 container requirement | distinguish source, dependency environment, image/container and run project | real small Odyssey entry point | author/run a minimal Dockerfile; explain result | modularity/design (professional extension) | Docker Docs | classroom Docker availability—verify before authoring |

## N — What not to pull / teach standalone

- Do not mirror a second broad textbook, Runestone body, Docker Docs body, or restricted ZyBooks content.
- Do not reteach CS1 fundamentals, files, exceptions, modules, or beginner classes as full units; use diagnostics/refresh in authentic work.
- Do not force a hierarchy, recursion, plot, or search/sort into every genre. Plotting is especially not catalog-required; recursion/linked structures are enrichment unless they earn a concrete design role.
- Do not make Big-O, containers, or ML a detached theory/certification unit.
- Do not create a second required weekly problem set; optional micro-practice is sufficient.

## O — Decisions and next bounded prompts

1. **Best next prompt:** CS2 pre-Savnac source reconciliation—apply the pinned Week 1/2/14–17 decisions and this Weeks 3–13 spine to planning, A1/A2, gates, and rubrics; preserve traceability and do no deployment.
2. Upgrade the CS2 Week-2 Friday extension only if its current one-line formatting repair cannot support a real evidence conversation.
3. Author Weeks 3–13 gates/rubrics from S01–S08, including a small course-owned Tkinter event lab.
4. Author Week 14 source-management/containers work after classroom capability confirmation.
5. Integrate the shared Week-16 Farkle/ML experience, then deploy/accept-test Savnac.

## Validation and limitations

Read the required CS2, reconciled CS1, shared Week-2, and durable-corpus sources; inspected all active CS2 planning weeks and gates; used current primary documentation for Python, GitHub, and Docker. The durable ZyBooks private manifest was used only for section/title inventory—no body is reproduced. A current verified CLO source beyond catalog text was not located, and Runestone/Docker capture rights were deliberately not assumed. `git diff --check`, JSON parsing, JSONL parsing, and CSV parsing passed. `make -C computer_science_2 task-check` returned `make: *** No rule to make target 'task-check'.  Stop.` (exit 2); `make -C computer_science_2 check` returned `make: *** No rule to make target 'check'.  Stop.` (exit 2).
