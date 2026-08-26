# CS2 durable engineering habits + starter reading list — report

Owner mission: `foreman_interface/jobs/tasks/cs2_durable_engineering_habits_and_reading_list_owner_20260825.md`, owner commit `72c434a5a00f27d842d6bb76ebecfced477b9a31`. Source-first, no Canvas mutation.

## Exact source HEAD inspected

`computer_science_2` at `26f3f9d` (the starter-reading-list commit, fast-forwarded from `8ca12af`) before this pass's edits.

## What already existed vs. what was missing

Inventory against the seven habit categories:

| Habit | Already present? | Where |
|---|---|---|
| Automated unit tests | **Implicit only.** Every gate said "test/trace" generically; nothing named `unittest` or asked for an assertion until Week 12's reading list. | rubrics' generic "Evidence" criterion |
| Focused trace/run evidence | Present throughout, every week | every gate's Required evidence |
| Logging | **Absent until Week 12**, and there only as an optional reinforcement link, never referenced in any gate's actual task text | reading list only, no gate text anywhere |
| Prompt/proposal provenance | **Present**, already well-formed | every rubric's "AI accountability" row: "proposal, diff, independent test, reading/reasoning, accept/reject decision" |
| Diff/review evidence | Present | same AI accountability language; Week 14's "review a bounded AI change from diff/tests/reasoning" |
| World Bible change/evidence/debt receipt | Present, consistently, every single week | the recurring "Keep one concise World Bible entry" line in every gate |
| Source history/recovery | Present at Week 14 specifically ("inspect history; recover/revert...") | week-14.md |

**Conclusion:** the owner's instinct was correct on testing and logging specifically (both real gaps, not imagined ones) and correct to assume the other five habits were largely already in place — no need to invent AI-accountability or World-Bible doctrine from scratch, only to relocate testing and logging earlier and make Week 14 read as synthesis rather than introduction.

## Where unit testing now begins and how it recurs

**Week 3** (`assignments/odyssey_gates/week-03.md`): now explicitly instructs `unittest` (or an already-covered equivalent) — construct the object, exercise one behavior, assert the result, run it independently, and say in the World Bible entry what the test proves and does not prove. This is the smallest useful automated-testing habit, matching the mission's own five-bullet shape.

Recurrence, each as a one-sentence continuation rather than a re-lecture:
- Week 4: "Continue the Week 3 `unittest` habit" for the invariant test.
- Week 5: "Continue the testing habit from Weeks 3-4" for subtype behavior.
- Week 6: "the same `unittest` habit from Weeks 3-5" for the contract test.
- Week 7: "continuing the habit from Weeks 3-6" for the LIFO/FIFO/list trace.
- Week 8: a test "is the strongest form of this trace, continuing the same testing habit."
- Week 12: explicitly reframed as deepening the existing habit, not introducing it.
- Week 14: explicitly named as one of the habits the repository already carries.

No week re-teaches `unittest` syntax after Week 3.

## Where logging now begins and why that week was chosen

**Week 4** (`assignments/odyssey_gates/week-04.md`). Reasoning: Week 4 is the first week with both a real collaboration (composition across ≥2 objects) and an enforced invariant — the first point in the semester where a program event (the invariant check) is genuinely worth a record, not a decorative add-on to a single isolated object (Week 3 has nothing yet worth logging). Framed as optional polish this week ("Logging is optional polish this week, not a separate requirement; the test remains the required evidence") to avoid inflating Week 4's evidence requirement. Week 5 offers one more optional recurrence ("A log line is welcome again here if it genuinely helps..."). Weeks 6-11 do not mention logging again — it was not force-fit into every week. Week 12 explicitly deepens ("improve tests, deepen any logging you have already been using") rather than introducing it, and Week 14's synthesis framing names it directly ("its occasional log lines").

Every logging mention explicitly distinguishes it from testing: a test checks a claim/expectation; a log records execution history/events for a human to read afterward. This distinction is stated directly in the Week 4 edit and restated in `docs/course-ethos.md`'s new doctrine section.

## Prompt provenance and durable receipts

No new mechanism was created. The existing AI-accountability rubric language ("proposal, diff, independent test, reading/reasoning, accept/reject decision") already implemented the doctrine correctly; Week 3's edit adds one explicit sentence making the provenance-vs-evidence distinction unmistakable to a first-time reader: *"if you used AI, keep the useful prompt/request itself as provenance; the test is still what proves the behavior, not the prompt."* The World Bible entry remains the single recurring receipt everywhere — no week gained a second report stream.

## Reading-list changes

`docs/curriculum/fall-2026-starter-reading-list.md`:
- **Week 3**: added Python `unittest` documentation to START HERE, explicitly labeled "Moved here from Week 12."
- **Week 4**: added Python `logging` HOWTO to "Reinforce if useful," explicitly labeled "Moved earlier from Week 12," framed as optional.
- **Week 12**: reframed from "START HERE: unittest docs" (as if introducing it) to "the student's own accumulated tests/logs/World Bible... not new reading," with `unittest`/`logging` docs demoted to "revisited" reinforcements.
- Weeks 5-11 were **not** touched — testing/logging references were deliberately not added mechanically to every week, per the mission's own "carry forward only where it adds value" instruction; the existing gate text's one-sentence habit-continuation references (in the gate files, not the reading list) are enough.
- The "1 primary + 1-2 reinforcements" pattern, official/open/no-cost preference, and START-HERE structure were all preserved. No paid dependency was added.

## Files changed

`assignments/odyssey_gates/week-03.md`, `week-04.md`, `week-05.md`, `week-06.md`, `week-07.md`, `week-08.md`, `week-12.md`, `week-14.md`; `docs/course-ethos.md`; `docs/curriculum/fall-2026-starter-reading-list.md`. Ten files, all small, targeted edits — no file was rewritten wholesale.

## Weeks 9-14 — edits made or deliberately not made

Audited every week's current gate text against the mission's Phase 5 checklist before touching anything:

- **Week 9**: already says "Show that the model behavior can be tested or traced without trusting the GUI alone" — independently testable model already required. **No edit.**
- **Weeks 10-11**: already require "retain runnable code/data or a reproducible trace" (10) and "name a limitation, uncertainty, or alternative interpretation" (11). **No edit.**
- **Week 12**: edited — added "deepen any logging" to the existing tests/docs list, and one framing sentence naming this as applying Weeks 3-8 habits rather than new material.
- **Week 13**: already requires "important tests... and clean enough history for recovery/review." **No edit** — adding a logging mention here would be the kind of mechanical every-week insertion the mission explicitly warns against, and the existing language already satisfies the audit question (inspectable history and evidence).
- **Week 14**: edited — one framing sentence naming the repository's tests, log lines, prompts, and World Bible as things "you have been building since Week 3," making the synthesis explicit rather than implicit.

## Validation results (Phase 7 checklist)

1. Week 3 clearly starts automated unit-testing practice — **pass**.
2. Logging appears before Week 12 at an authentic point (Week 4) — **pass**.
3. Tests and logs are explicitly distinguished, both in Week 4's gate text and in the new course-ethos doctrine — **pass**.
4. AI prompt provenance is optional when AI is used and never substitutes for independent evidence — **pass**, unchanged existing doctrine plus one clarifying sentence.
5. World Bible remains the sole recurring receipt; no second report stream was created anywhere — **pass**.
6. Week 14 reads as synthesis, not a surprise workflow unit — **pass**, explicit framing sentence added.
7. The starter reading list has a useful no-cost/open starting point for every Week 3-14 core topic, and now supports early tests/logging — **pass**.
8. No core week/topic was moved, replaced, or redesigned — **pass**; every edit added evidentiary/habit detail to an already-frozen topic, none changed what a week is about.
9. No Canvas mutation occurred — **pass**; this entire mission was source-only, confirmed by reviewing every tool call made during execution.

## Genuine remaining owner question

None found that source precedent cannot settle. One judgment call worth naming explicitly rather than leaving implicit: Week 4 was chosen over Week 5 as logging's first authentic home because Week 4 is the first week with both collaboration *and* an enforced invariant simultaneously; Week 5 (substitution/polymorphism) has collaboration but no invariant-check moment as natural to log. This is a defensible reading of "objects collaborate or behavior/state transitions become easier to inspect," not a coin flip, but it is a judgment call rather than something the source dictated outright — flagged for visibility, not because it needs to be revisited.

## Verdict

`CS2 DURABLE ENGINEERING HABITS LANDED — UNIT TESTING BEGINS WEEK 3, LOGGING BEGINS WEEK 4, BOTH RECUR AS ONE-SENTENCE CONTINUATIONS THROUGH WEEK 14, NO NEW ASSIGNMENTS CREATED, FROZEN SPINE UNTOUCHED, NO CANVAS MUTATION`
