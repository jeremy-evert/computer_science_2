# CS2 production visual QA manifest — for Grace / Olivia visual acceptance

Companion to `jobs/tasks/cs2_grace_production_visual_acceptance.md` (owner commit `a4eee41d11b95c9a1fe95a8e065c740169845a69`). This manifest is the read-only visual-inspection route; Flo does not need to remain active while this runs.

**Course/commit being visually validated:** production Canvas `https://swosu.instructure.com/courses/74031`, against `computer_science_2` source at commit `7f4a5e8` (durable engineering habits) plus this closeout pass's live-only mutations (see `sidecar/reports/cs2_final_production_closeout.md` for the exact assignment IDs created).

**No-student-data capture boundary:** every recommended stop below is course structure, page content, or the instructor-facing assignment-group/weight view. Do **not** navigate to Grades, SpeedGrader, or any individual student submission — those are out of scope for this visual pass and are the one place real student work/identity is visible.

## Route (in order)

1. **Home/Modules full map** — `https://swosu.instructure.com/courses/74031/modules`. Expect: 5 Success-Foundations modules, then 16 weekly modules (Week 2 through Week 17) in calendar order, all published (green check), Weeks 3–14/16/17 each showing exactly one Page + one Assignment, Weeks 2 and 15 showing exactly one Page.
2. **Week 2 — Found Your World** — the Week 2 module's page. Expect: World Bible v0.1 structure (premise, cast, flow, questions, unknowns, object prediction), explicit "you are allowed to be wrong," no submission link (ungraded, correctly says "nothing to submit").
3. **Week 3 — Cohesive Object Boundary + its real assignment** — both the page and the linked Assignment. Expect: page states unittest starts here, assignment is 25 points in the Weekly reinforcement group with the same rubric table, page's "what do I turn in" line correctly says the assignment is live.
4. **Week 4 — collaborating objects/logging** — page + assignment. Expect: explicit "reopen the Week 3 object," logging introduced as optional polish, invariant-test language, 25 points.
5. **Week 6 checkpoint** — page + assignment. Expect: 40 points (larger than a normal gate), "first checkpoint," contract/swap task, correct group (Reasoning Odyssey checkpoints).
6. **Week 7/8 data-structure progression** — both pages + assignments. Expect: Week 7 introduces the structure, Week 8 explicitly reopens it ("do not build a new one").
7. **Week 9 GUI checkpoint** — page + assignment. Expect: 50 points, explicit dependency on the accumulated model, independent-testability language.
8. **Week 10/11 visualization-storytelling progression** — both pages + assignments. Expect: 25 points each, in the Weekly reinforcement group.
9. **Week 12/13 stabilization/culmination** — both pages + assignments. Expect: both titled "Synthesis Checkpoint" narratively but both 25 points in the *Weekly reinforcement* group, not the Checkpoints group (deliberate — narrative title, ordinary-gate tier).
10. **Week 14 workflow checkpoint** — page + assignment. Expect: 60 points, explicit "habits come together, not where they first appear" framing, correct group.
11. **Week 15 — asynchronous buffer** — page only. Expect: honestly says nothing is due, no assignment link at all.
12. **Week 16 — Farkle+ML receipt** — page + assignment. Expect: 0 points, omitted from final grade (confirm via the assignment's own detail page if visible, or trust the manifest/closeout report), explicitly not a fourth checkpoint.
13. **Week 17 — reflection** — page + assignment. Expect: 100 points in Final reflection paper group, five-prompt/four-category structure, no new technical work implied.
14. **Assignments/grade-group structural view** — `https://swosu.instructure.com/courses/74031/assignments` (list view, not SpeedGrader/Grades). Expect: assignment groups visible with weights Weekly reinforcement 45%, Reasoning Odyssey checkpoints 30%, Final reflection paper 15%, Attendance & participation 8%, Course evaluation 2%, Semester kickoff week 5% (unchanged, historical bonus), all previously-retired shared-strand/pathway groups showing 0% weight. **Do not open individual student rows.**

## Acceptance questions per stop

- Does the page visually match its described content (not garbled HTML, no stray markup, no broken table)?
- Is the six-question structure (learning / building / world connection / evidence / submission / carries-forward) visually scannable, not a wall of text?
- Does the rubric table render cleanly?
- Is it obvious to a first-time student what to do this week?
- For graded weeks: is the assignment visibly linked and does its point value match the page's stated rubric total?
- For Week 2/15: is it visually unambiguous that nothing is due?

## What this pass is not checking

Grading mechanics, actual submission flow, SpeedGrader, or any real student data — all explicitly out of scope for this visual-only, no-student-data pass.
