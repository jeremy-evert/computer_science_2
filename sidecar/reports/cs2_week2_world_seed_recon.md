# CS2 Week 2 World Seed reconnaissance and four-world continuity — report

Owner mission: `foreman_interface/jobs/tasks/cs2_week2_world_seed_recon_owner_20260825.md`, owner commit `e0cb31d7f1bf2150b827894be0ecc7ed152c666c`. Read-only reconnaissance and design synthesis, no Canvas mutation.

## 1. Exact source HEAD inspected

`computer_science_2` at commit `d49519b` (main, pushed). This includes two prior commits from this same session that already implement most of this mission's owner hypothesis: `7fcb853` (Week 2 "Found Your World"/World Bible v0.1 rewrite plus Week 3/4 backward-reference edits) and `d49519b` (live Canvas preview-page reconciliation for the same three weeks).

**Important framing note, stated plainly per the mission's own instruction not to defend a draft idea uncritically:** this mission's "Purpose" section describes Week 2 as still being the old thin "choose a genre, jot a few nouns if helpful" page. That description is now stale — a materially similar hypothesis was independently approved by Jeremy directly in this session and already shipped to both source and live Canvas before this mission was executed. This report treats the mission as what it functionally is now: **an audit of the already-shipped design against a deeper, more rigorous spec**, not pre-authoring reconnaissance for an unbuilt idea. Every gap between what shipped and what this mission asks for is called out explicitly below, and no Canvas mutation was performed in producing this report.

## 2. Week 3 contract — exact text and what Week 2 must supply

`assignments/odyssey_gates/week-03.md` (current, post-`7fcb853`): 25 points, Weekly reinforcement group (45% target weight). Required evidence, verbatim structure: reopen Week 2 World Bible v0.1 → pick one predicted object → build one cohesive world object with meaningful state/behavior → focused test/trace → boundary rationale → AI evidence trail when used → one World Bible entry (what changed/evidence/debt). Rubric (`rubrics/odyssey_gates/week-03_rubric.md`): World fit/build 8, Evidence 7, Reasoning 6, AI accountability 4.

**What it implicitly assumes exists:** a world (genre choice) and at least a rough sense of "things" in that world worth turning into an object — otherwise "pick one candidate" has nothing to pick from. Before this session's edit, the live Week 2 supplied neither concretely; a student could arrive at Week 3 having written nothing more than a genre name.

## 3. Week 4 contract — exact text and what Week 3 must supply

`assignments/odyssey_gates/week-04.md` (current, post-`7fcb853`): 25 points, same group. Required evidence: reopen the Week 3 object → ask what it needs to collaborate with and why → refactor a real flow into collaborating objects using composition → protect one invariant with test/trace → explain why composition beats an unnecessary hierarchy → World Bible entry. Rubric: Composition fit 8, Invariant test/trace 7, Rationale/World Bible 6, AI accountability 4.

**What Week 4 needs from Week 3:** exactly one real object with a defensible boundary (Week 4's own pre-existing verb, "refactor," only makes sense against something that already exists). Students need **at least two collaborating objects by end of Week 4** — the one from Week 3 plus at least one new collaborator introduced this week. The invariant/state relationship must span the collaboration (e.g., inventory count vs. an order that must never ship unpaid — matches `capability_map.md` row 3-4 across all four worlds). **What Week 2 seed choices make this natural:** a cast of 5-8 nouns wide enough that at least two of them plausibly interact (a settler and a supply cache; a case and a piece of evidence; a ship and a subsystem; an order and an inventory item) — the shipped Week 2 cast-of-things step already produces this by construction. No world in the palette creates an awkward Week 4 relationship — see §6.

## 4. Weeks 3–14 World Bible continuity table

| Week | Disciplinary concept | What changes in the student's system | Evidence produced | World Bible entry | Natural or decorative? |
|---|---|---|---|---|---|
| 3 | Cohesive object boundary (S01) | First real object exists | Object + test/trace + boundary rationale | what changed/evidence/debt | **Natural, explicit** (this session's edit: reopens Week 2 predictions directly) |
| 4 | Collaborating objects + invariant (S01/S08) | Object refactored to collaborate with ≥1 more object | Refactor + invariant test/trace + rationale | same | **Natural, explicit** (this session's edit: reopens the Week 3 object directly) |
| 5 | Earned substitution (S02) | Student evaluates whether a true is-a relationship exists among world nouns; adds a subtype or documents why composition wins | Substitution demo or composition rationale + WB entry | same | Natural in principle (every world has a credible type family per `capability_map.md` row 5 — Claim/Case/Sensor/Product types) but **not yet made explicit in the gate text** — no line says "reopen your Week 4 objects and ask if one deserves a subtype." Real, small continuity gap; not part of this mission's authorized edit scope (Weeks 3-4 only). |
| 6 | Contract and swap, checkpoint (S03/S08, 40 pts) | Defines a collaborator contract, swaps two conforming implementations | Contract test + explanation + WB entry | same | Builds on Week 4's collaboration concept but likewise not explicitly backward-referenced in gate text. |
| 7 | World-fit data abstraction (S05) | Student identifies a real list/stack/queue flow in their world | Structure + operation trace + rationale | same | Free-standing by design (new capability), still expected to reuse the same world/system — not explicitly stated but implicit throughout ("world-fit," not a toy structure). |
| 8 | Search/order tradeoff (S05/S06) | Traces a lookup/ordering operation "over real world state" | Trace + tradeoff explanation | same | Gate text itself says "real world state" — implicit continuity, still not an explicit backward reference. |
| 9 | Compact GUI, checkpoint (S04, 50 pts) | Builds a Tkinter view over "real model state" | View + callback + independent model test | same | **Strong explicit continuity** — the gate cannot be completed without the student's own accumulated model. |
| 10 | Honest visualization (S09/S06/S08) | Visualizes "real selected-world or project data" | Chart + rationale + pitfall + reproducible evidence | same | **Strong explicit continuity** — same reasoning as Week 9. |
| 11 | Storytelling/flex (S09+S07) | Tells an evidence-backed story from "project/world data," or reinforces prior design/data/GUI/testing work if not yet data-rich | Story/claim + limitation + decision | same | **Strong explicit continuity**, with a built-in fallback that itself reuses prior weeks' artifacts. |
| 12 | Synthesis checkpoint — stabilization (S08, 25 pts) | Freezes a substantial slice of the accumulated system for review | Tests, docs, debt record | same, reflecting on accumulated evidence | **Maximal continuity by construction** — the whole system to date is the subject. |
| 13 | Synthesis checkpoint — culmination (S01–S08, 25 pts) | Major creative construction substantially complete | Runnable slice, tests, design rationale, recoverable history | same | **Maximal continuity.** |
| 14 | Workflow receipt, checkpoint (S08, 60 pts) | Uses "the real Reasoning Odyssey repository" for history/recovery/collaboration/AI-review evidence | Change/test/recovery evidence | same | **Explicit, unambiguous continuity** — the gate names the student's own repository directly. |

**Net finding:** the back half of the semester (Weeks 9–14) already has strong, explicit textual continuity — those gates cannot be completed without the student's own accumulated world/system. The front half (Weeks 5–8) has *plausible, intended* continuity that is currently implicit rather than stated. This mission's authorized scope was Weeks 3–4 only, and that pair is now the strongest link in the chain. Weeks 5–8 are the next natural (optional, small) candidates for the same one-paragraph backward-reference treatment in a future bounded pass — not recommended now, per "do not redesign every week."

**Weak world fits found:** none. Every capability row in `sidecar/worlds/capability_map.md` has a credible, differentiated scenario for all four worlds. Recursion and file/data persistence — both named in this mission's stress-test list — are simply **not part of the Fall 2026 CS2 spine at all** (confirmed against `planning/fall-2026-course-design.md`'s semester spine table and `A2-coding-odyssey-project.md`'s growth path; no week teaches either concept this term), so "world fit" for those two is not applicable rather than failing.

## 5. Existing CS1/CS2 sources worth reusing

- **`assignments/A2-coding-odyssey-project.md`** — the one and only canonical World Bible contract in CS2 (or CS1 — see below). Defines the four world names, the "pick one, not a CS1 continuation" framing, the growth path table, and the World Bible definition ("charter, current state, one line per week... a project receipt, not duplicate homework"). Authoritative; this session's edits extended it, did not contradict it.
- **`sidecar/worlds/` (README.md, `frontier_settlement.md`, `investigation_bureau.md`, `starship_log.md`, `small_business.md`, `capability_map.md`, `continuity_ledger.md`)** — a complete internal-only "Four Living Worlds Bible" already built (Prompt 017) with per-world cast/artifact-language/problem-generator sections that map closely to this mission's own per-world noun tables. **Explicitly marked "Never hand a student this directory"** — reusable as authoring inspiration only, never linked or copied verbatim into student-facing material. This firewall was preserved throughout the already-shipped work and must stay preserved in any future pass.
- **`sidecar/prompts/018_the_four_calls_world_selection_experience.md`** + **`sidecar/worlds/four_calls/`** — a fully scripted video world-selection experience (one persona call per world) and a specified (not yet implemented) single-select world-choice capture mechanism. **Not recorded, not deployed.** Useful future asset, irrelevant to a text-only Week 2 page today.
- **`sidecar/worlds/transfer_portal/README.md`** (Prompt 020) — the resolved world-switching policy ("students may switch worlds... nobody restarts, work carries forward"). Already reflected in the shipped Week 2 page's "the door stays unlocked" section.
- **CS1 (`computer_science_1`)** — searched exhaustively for "World Bible," "four world," or any of the four world names. **Zero hits.** CS1 has no equivalent doctrine at all; nothing in it needs to be, or can be, adapted. The mission's premise that CS1 might contain stronger source material does not hold — the strongest existing material is entirely CS2-native (`sidecar/worlds/`, built specifically for CS2's Reasoning Odyssey).

## 6. Four-world stress test

Checked against `capability_map.md`'s full Week 3–14 row set (the authoritative cross-world capability mapping) plus the concept list in this mission:

| Concept | Present in CS2 Fall 2026? | All four worlds fit? |
|---|---|---|
| Cohesive object boundaries (Wk 3) | yes | yes — every world's premise names at least one natural single-entity boundary |
| Collaborating objects / invariants (Wk 4) | yes | yes — every world has a natural must-never-violate rule (negative inventory, double-claimed evidence, contradicted sensor readings, over-allocated water rights) |
| Inheritance/substitution (Wk 5) | yes | yes — every world has a plausible type family (Claim/Case/Sensor/Product types) |
| Contracts/interfaces (Wk 6) | yes | yes — every world has a format-mismatch scenario (merging ledgers, mismatched agency reports, incompatible subsystem eras, new supplier data format) |
| Collections/data structures (Wk 7-8) | yes | yes — every world has a natural queue/priority/search scenario |
| Recursion | **not in the Fall 2026 spine** | n/a |
| GUI/model-view (Wk 9) | yes | yes — every world has a plausible dashboard/console/register screen |
| File/data persistence | **not in the Fall 2026 spine** | n/a |
| Data visualization/storytelling (Wk 10-11) | yes | yes — every world has an honest-chart scenario |
| Testing/debugging | implicit throughout every gate ("test/trace" required every week) | yes |
| Recovery/version-control/professional workflow (Wk 14) | yes | yes — every world has a "reconcile two conflicting records" scenario already seeded in `capability_map.md` |

No weak fit found anywhere. No world requires a "no action, concept stands alone" carve-out beyond the two concepts (recursion, persistence) that are simply outside this term's scope entirely.

## 7. Verdict on each owner-hypothesis field (KEEP / MODIFY / DROP)

| Field | Verdict | Notes |
|---|---|---|
| 1. World premise (2-3 sentences) | **KEEP** | Shipped as-is in `week-02.md`. |
| 2. Cast of 5-8 things | **KEEP** | Shipped. Directly feeds Week 4's collaboration requirement (§3). |
| 3. One end-to-end flow | **KEEP** | Shipped. |
| 4. Three software questions | **KEEP** | Shipped. Cheap, motivates behavior/collaboration framing early. |
| 5. Known unknowns | **KEEP** | Shipped. Mirrors the internal continuity-ledger's own "canon that only exists in someone's head is the failure mode" spirit — legitimate thematic echo, cheap to write. |
| 6. Object predictions (3-5 nouns) | **KEEP** | Shipped. This is the field Week 3 actually tests — load-bearing, not decorative. |
| 7. One sentence of confidence/uncertainty | **NOT YET SHIPPED — recommend adding, folded into field 6 rather than as a separate numbered step.** | Genuinely cheap (one sentence) and sharpens the Week 3 hook ("you flagged X as your shakiest guess — was it?"), but adding it as its own numbered step would push the artifact past the "5-8 fields, 20-30 minutes" target. Appending it to the existing object-prediction step preserves both. |

No field warrants DROP. All seven earn their keep against the "every field must help later CS2 reasoning" design principle — including the un-shipped field 7, once folded in cheaply rather than added as new bureaucracy.

## 8. Recommended Week 2 student experience

The shipped version already matches this closely; the one recommended change is folding in field 7. Otherwise: keep it to thinking, not code (already true); keep the four worlds as the only bounded choices, no fifth/custom option (matches `A2-coding-odyssey-project.md`'s exact "pick one world—[four names]" phrasing — the source does not currently authorize a student-proposed equivalent world, so this is a real existing constraint, not an invented one); keep it ungraded (matches Jeremy's own explicit prior instruction not to touch `docs/grading-model.md` for this — Week 2 does not need a new gradebook object, and the course's existing Attendance & Participation category already covers general engagement without a submission-shaped object).

## 9. Recommended student-facing wording outline (not final prose)

1. Frame: "This week is thinking, not code. World Bible v0.1 is what Week 3 tests."
2. Choose your world (four names, one-line premise each, no harder/easier door, not required to continue CS1 work).
3. World premise (2-3 sentences).
4. Cast of things (5-8 nouns, explicitly not-classes-yet).
5. One real flow (worked example from one world, not the student's own — avoid anchoring).
6. Three software questions.
7. Known unknowns (2-3, with one worked example).
8. Object prediction (3-5 nouns) **+ one added sentence: which prediction feels strongest, and which feels most likely to change once Week 3 introduces cohesion/responsibility.**
9. "You are allowed to be wrong" — explicit permission, tied directly to what Week 3 will do with the prediction.
10. "The door stays unlocked" — one sentence, world-switching is available without losing earned work.

This matches the already-shipped page's actual structure with the single field-7 addition folded into step 8.

## 10. Exact source files that would need changing in a later implementation pass

- **`assignments/odyssey_gates/week-02.md`** — append one sentence to the "Object prediction" step for field 7. Smallest possible diff.
- No other file requires a change to satisfy this mission. `week-03.md`/`week-04.md` already carry the backward-reference language this mission asks for. `A2-coding-odyssey-project.md` already names World Bible v0.1. `docs/grading-model.md` intentionally untouched, per standing owner instruction.
- **Optional, not required, future-bounded pass:** `week-05.md` through `week-08.md` could each receive the same one-paragraph backward-reference treatment already proven on Weeks 3-4 (§4's "natural but not yet explicit" finding) — explicitly not authorized or recommended in this pass.

## 11. Genuine owner questions (cannot be resolved from source precedent)

1. **Field 7 folding vs. separate step:** this report recommends folding the confidence/uncertainty sentence into the existing object-prediction step rather than adding a 7th numbered field. If Jeremy wants it as its own distinct step instead (e.g., because it reads better standalone), that's a real stylistic call, not something source precedent settles.
2. **Weeks 5-8 backward-reference expansion:** is proving the chain across Weeks 3-4 sufficient for now (as the prior owner instruction explicitly said), or should the next bounded slice extend the same explicit-continuity treatment to Weeks 5-8, where this report found the connection is real but currently implicit? Both are legitimate; this is a sequencing preference, not a design gap.
3. **World Bible's storage location:** `A2-coding-odyssey-project.md` defines what the World Bible contains but not its exact medium (a file in the student's own repo vs. a running Canvas text-entry log vs. something else). Given every gate's submission type already includes "repository link," a `WORLD_BIBLE.md` in the student's own project repo is the most source-consistent default — but this has never been made explicit anywhere and is worth a one-line confirmation before Weeks 5+ start referencing "the existing World Bible entry" more heavily (as Weeks 12-13 already do).

## 12. Final verdict

**READY TO AUTHOR** (for the single remaining recommended change — field 7 — which is a one-sentence addition to an already-shipped file) — **and READY, ALREADY SHIPPED** for everything else this mission asked to evaluate. No blocking issue found anywhere in the four-world palette, the Week 3-14 continuity path, or the existing source base. The three open items in §11 are preference questions for Jeremy, not defects requiring resolution before proceeding.
