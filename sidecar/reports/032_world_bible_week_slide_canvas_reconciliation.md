# CS2 World Bible week-slide — Canvas reconciliation

Owner decision (2026-08-26, verbatim): "the canvas page is more ephemeral
and the GitHub stuff is our source of Truth and so if you shifted the
source of truth and did the mechanical changes, then go ahead and do the
updates on canvas and make everything line up."

Follow-on to `sidecar/reports/031_world_bible_week_slide.md`, which shifted
the Reasoning Odyssey chain one week later in source but explicitly did not
touch Canvas. That report flagged that the *old* week numbers were already
live (a separate 2026-08-25 deployment pass, commit `bc98456b`). This pass
reconciles live Canvas (course_id `74031`) to match the new source.

## Safety check before touching anything

Read every live submission on the 12 affected assignments first
(`GET .../submissions`). All 9 enrolled students showed zero real activity
(no `submitted_at`, no comments) on any of the 12 — only empty Test-Student
placeholders. Nothing was renamed out from under real student work.

## What changed on live Canvas

**12 assignments renamed** (title bumped by exactly one week, matching the
new source `assignments/odyssey_gates/week-NN.md` titles verbatim):

| ID | Old title | New title |
|---|---|---|
| 914175 | Week 3 — Cohesive Object Boundary (S01) | Week 4 — Cohesive Object Boundary (S01) |
| 914176 | Week 4 — Collaborating Objects and Invariant (S01/S08) | Week 5 — Collaborating Objects and Invariant (S01/S08) |
| 914177 | Week 5 — Earned Substitution (S02) | Week 6 — Earned Substitution (S02) |
| 914178 | Week 6 — Contract and Swap (S03/S08) | Week 7 — Contract and Swap (S03/S08) |
| 914179 | Week 7 — World-Fit Data Abstraction (S05) | Week 8 — World-Fit Data Abstraction (S05) |
| 914180 | Week 8 — Search/Order Tradeoff (S05/S06) | Week 9 — Search/Order Tradeoff (S05/S06) |
| 914181 | Week 9 — Compact GUI over Tested Model (S04) | Week 10 — Compact GUI over Tested Model (S04) |
| 914182 | Week 10 — Honest Visualization from Project Data (S09/S06/S08) | Week 11 — Honest Visualization from Project Data (S09/S06/S08) |
| 914183 | Week 11 — Data Storytelling / Flex Clinic (S09 + S07) | Week 12 — Data Storytelling / Flex Clinic (S09 + S07) |
| 914184 | Synthesis Checkpoint — Week 12 — Stabilization and Peer-Review Preparation (S08) | Synthesis Checkpoint — Week 13 — ... |
| 914185 | Synthesis Checkpoint — Week 13 — Culmination Design Review (S01-S08) | Synthesis Checkpoint — Week 14 — ... |
| 914186 | Week 14 — Professional Workflow Receipt (S08) | Week 15 — Professional Workflow Receipt (S08) |

**Description text**: 7 of the 12 live descriptions contained an internal
"Week N" back-reference (e.g. "Reopen your Week 2 World Bible v0.1",
"the same system you have been building since Week 3") — these are hand-
authored sentences in the live HTML, not a verbatim copy of the source
markdown, so rather than regenerate each description from scratch (real
risk of silently drifting from carefully-worded live content), every
`Week \d+` mention was bumped by exactly one via targeted substitution and
spot-verified against the new source's own cross-references (week-05.md
"Week 4", week-06.md "Week 5"/"Week 3", week-08.md "Week 3", week-09.md
"Week 8" — all confirmed matching the uniform +1 shift before applying).
5 of the 12 had no week-number mention in their description and were left
content-unchanged (title only).

**12 modules renamed** to match (`218888`-`218899`, old Week 3-14 →
new Week 4-15), same title strings as the assignments above minus the
"(S01)" etc. suffixes, matching the existing "CS2 Week N — Title" module
naming convention already in use.

## Explicitly NOT touched — two real judgment calls, not mechanical

1. **Module `218887`, "CS2 Week 2 — Found Your World (World Bible v0.1)"**
   already exists live at position 6, meaning the World Bible intro *is*
   already present on live Canvas under the old Week 2 slot — contradicting
   report 031's belief that "no Canvas mutation performed" applied to the
   whole feature. Jeremy was explicit: "we will work on introducing the
   four worlds and the world Bibles to the computer science 2 class next
   week" — renaming this module to Week 3 would be activating/repositioning
   the World Bible intro itself, which is exactly what was ruled out of
   scope for this pass. Left untouched. **Needs Jeremy's decision**: what
   this module actually contains right now (an active assignment students
   can see today, or an unpublished shell?) and when to move it to Week 3.

2. **Module `218900`, "CS2 Week 15 — Asynchronous Buffer"** collides with
   the just-renamed `218899` ("CS2 Week 15 — Professional Workflow Receipt
   (Checkpoint 3)") — both now claim Week 15. Per source report 031, Week
   15's buffer status was deliberately spent to absorb the slide; the buffer
   module needs to be retired/merged/renamed, not just relabeled, which is
   a structural change beyond a title fix. Left untouched pending Jeremy's
   call on whether to delete this module, repurpose it, or fold its
   content elsewhere.

No other module reordering or item movement was performed — every other
module kept its existing item membership and position.

## Verification

All 12 assignments and all 12 modules re-read via `GET` after the writes
and confirmed to show the new titles exactly as intended above.

## Verdict

`CS2 CANVAS RECONCILED TO NEW SOURCE NUMBERING FOR WEEKS 4-15 — WEEK 2/3
WORLD BIBLE ACTIVATION AND WEEK 15 BUFFER COLLISION LEFT FOR OWNER DECISION`
