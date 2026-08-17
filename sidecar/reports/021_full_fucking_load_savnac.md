# Report 021: Full Fucking Load — Render and Accept the Complete CS2 Semester in Savnac

**Prompt:** `../prompts/021_full_fucking_load_savnac.md`
**Closes:** Prompt 013's acceptance debt (see `013_imprint_cs2_to_savnac_and_read_back.md`, moved to `sidecar/prompts/completed/`).

## Commits inspected

| Repo | Commit | 
|---|---|
| `computer_science_2` | `8debc538ed3ac7b58672dd62eae32380b6b9049` |
| `course_foundry` | `11a2a2c742b0b1a4f33494c04c2cb0a9f964b981` |
| `imprint` | `ef17850f905f20962674a2f5b52b06679e7d9c7` |
| `harbor` | `5d69e3ede4b6f1ab4cb32cf003faea79f7df8cc0` |

## Course Foundry / Imprint paths used

- `course_foundry.savnac_deploy` -- the unified, Savnac-gated `dry-run`/`push`
  CLI already covering cs1/cs2/dsct/architecture. No new deployment stack
  written.
- `course_foundry.cs2_desired_course.cs2_savnac_desired_course` -- CS2's
  existing compiler, unchanged.
- `imprint.reconcile.push_course` -- existing reconcile/prune engine.
- `imprint.config.require_host_marker` -- the Savnac-vs-production host
  guard; enforced on every call in this session via `SAVNAC_HOST_MARKER =
  "192.168.122.172"`.

Credentials sourced from `~/.config/canvas/savnac.env` (Savnac-specific;
never `~/.config/canvas/canvas.env`, which defaults to production
`https://swosu.instructure.com`). No credential value was echoed, logged, or
committed at any point.

## Savnac course identity

`course_id=3`, name `"Computer Science 2 (CS2)"`, `workflow_state=available`.
Confirmed as the correct, pre-existing target -- not created fresh.
Enrollments: 1 teacher (Jeremy/`jevert`), 2 synthetic student test accounts
(`Agent Student 1`, `Agent Student 2`), both `active`. No real students
enrolled.

## Preflight state (before this session's write)

A `dry-run --course cs2` against the live course, before any mutation,
returned:

```
Dry-run plan: course=3 label='CS2'; 155 objects, 16 modules, 14 grading groups
Reconcile summary: create=0, update=1, skip=168, delete=0
```

This means the great majority of the full Weeks 2-17 semester was **already
live in Savnac course 3** from earlier work -- this session's job was
substantially acceptance/verification/closure, not a first-time bulk
imprint, though the full compile-and-verify cycle Prompt 021 specifies was
run in full regardless of that head start.

## Compile coverage by week

| Week | Coverage | Status |
|---|---|---|
| 1 | Owned by `semester_kickoff_week`, not by CS2's builder. Already live (3 sub-modules: Monday/Wednesday/Friday + A07 Advisor). | GREEN (pre-existing, out of this builder's scope by design) |
| 2 | Shared local AI lab manifest, thin CS2 extension page, readiness-check assignment. | GREEN |
| 3-14 | Full Odyssey gates (25 pts weekly, 40/50/60 pts checkpoints at 6/9/14), Monday Moment, Wed/Fri Professional Minds readings+slides, A3/A4/A7 recurring artifacts, attendance/course-eval (week 3 only). | GREEN |
| 15 | Overview page + A6 Professional Pathway (Week 15 submission). No gate -- source declares none. | GREEN (honest, not a gap) |
| 16 | Overview page only. No gate object -- Odyssey gate status is `retired`; canonical Farkle/ML body intentionally not invented as a gate. | GREEN (honest, not a gap) |
| 17 | Overview page + A5 Final Reflection and Closure. | GREEN |

No week is RED. No week required fabricating an unresolved value to render.

## YELLOW ledger (honest, disclosed, not fabricated around)

1. **Odyssey gate due dates.** Present and computed (`_gate_due_at`) for
   Weeks 3-14's gate assignments in this build (e.g. Week 6 gate due
   `2026-09-28`, Week 9 `2026-10-19`, Week 14 `2026-11-23`) -- verified live
   in the read-back. `docs/grading-model.md`'s own text still calls late/drop
   mechanics a "deployment question" not settled by source; this build does
   not invent late penalties or drop-lowest behavior, matching that.
2. **Week 1 module ordering.** Pre-existing, not introduced by this
   session's write (`prune_scope=none` never touches Week 1, which
   `cs2_desired_course.py` intentionally excludes -- "semester_kickoff_week
   owns it"). Read-back shows Canvas module *position* values placing
   Monday's kickoff module first (position 1, correct) but Wednesday/Friday/
   A07-Advisor sub-modules at positions 18-20 -- *after* Week 17 -- rather
   than immediately following Monday. A student navigating module-by-module
   would hit Week 17's closure before ever reaching Week 1's
   Wednesday/Friday content. This is owned by the separate
   `semester_kickoff_week` deployment pipeline, not CS2's builder; fixing it
   here would mean building a second deployment stack into another
   pipeline's scope, which Prompt 021 explicitly prohibits. Recorded here as
   a real defect for whoever owns that pipeline's next pass, not hidden.
3. **`course_foundry/scripts/cs2_course_map.py`'s docstring is now stale.**
   It claims (as of a 2026-08-09 check) that "Weeks 2-17 have NO live
   per-week Canvas modules ... yet." That is no longer true as of this
   session. This is a different, smaller tool (the Week-at-a-Glance widget
   pusher), out of Prompt 021's scope to fix, but worth flagging so its next
   run doesn't quietly assume stale state.

## Imprint into Savnac -- objects created/updated/left untouched

Live push (`push --course cs2 --confirm-live --prune-scope none`):

```
Live push plan: course=3 label='CS2'; 155 objects, 16 modules, 14 grading groups
Reconcile summary: create=0, update=1, skip=168, delete=0
Detail: Reconciled CS2: 0 created, 1 updated, 168 unchanged, 0 deleted.
Assignment-group self-check: 100% across 15 groups (100%).
```

The single update: `Week 16: Shared Farkle + Machine Learning Applied Fun` ->
`CS2 Week 16 Overview` page body, refreshed to match today's Farkle/ML
package landing in `planning/week-16.md`. Sixteen module-metadata
"refreshes" also logged (unconditional, not counted in the tally -- no
content change).

**`prune_scope=course` was evaluated in dry-run only and deliberately not
used for the live push** -- it proposed 20 deletions, all of which turned
out to be Week 1's entire shared-kickoff module set (Monday/Wednesday/
Friday sub-modules + A07 Advisor), because CS2's builder doesn't model Week
1 at all. That is real, wanted, correctly-owned content this specific
builder simply doesn't claim -- not drift. Using `prune_scope=course` here
would have deleted all of Week 1. This was caught before any write; `none`
was used for the actual push. Recorded here explicitly per Prompt 021's
"do not delete unrelated or instructor-created material" instruction.

## Whole-course read-back

- **Course identity:** confirmed (`id=3`, `Computer Science 2 (CS2)`,
  `available`).
- **Instructor enrollment:** confirmed (Jeremy, `TeacherEnrollment`,
  active).
- **Modules:** 20 total, all `published=True`. Week 1 (3 sub-modules) +
  Week 2 + Weeks 3-17 (15 modules) = 20, exactly matching source
  ownership boundaries.
- **Assignments:** 121 total. Zero duplicate names.
- **Pages:** 69 total. Zero duplicate titles.
- **Rubrics:** spot-checked all three checkpoints -- Week 6 (40 pts, 4
  rubric criteria), Week 9 (50 pts, 4 criteria), Week 14 (60 pts, 4
  criteria) -- all present and attached to the correct assignment.
- **Assignment groups:** 15 groups, weights sum to exactly 100%.
- **ZyBooks:** zero references found across all 121 assignment
  names/descriptions and all 69 page titles. No stale required-ZyBooks
  doctrine returned.
- **Backstage Four Living Worlds canon:** zero leaks. Scanned every
  assignment name/description for the specific internal-canon terms
  (character names, world/institution names, "Four Living Worlds",
  "continuity ledger"). The only hits were the ordinary phrase "World
  Bible" -- which is the *student's own* World Bible from
  `assignments/A2-coding-odyssey-project.md`, a legitimate public term the
  gate rubrics are supposed to use, not the internal canon this session was
  built to keep hidden (see `sidecar/worlds/README.md`'s explicit
  distinction between the two).

## Professor-walk findings

Walking the module sequence as Jeremy would see it in Canvas's module list:
each week's title states its Odyssey capability focus (e.g. "Week 6:
Contracts and Swappable Collaborators (S03/S08)"), gates/checkpoints sit in
the correct weeks per `docs/grading-model.md`, assignments/rubrics are
inspectable without opening GitHub alongside Canvas, and the checkpoint
weeks are visibly larger (40/50/60 pts, more rubric criteria) than the
surrounding 25-point weekly gates. The one real defect: Week 1's
Wednesday/Friday sub-modules sort to the end of the module list (see YELLOW
2 above) -- a professor scanning top-to-bottom would see it, even if it
doesn't block using the course.

## Student-walk findings

Sampled: course landing -> Week 1 (Monday module reachable first, as
intended) -> Week 2 (13 items, readiness-check assignment present) -> Week
3 (13 items, ordinary Odyssey week) -> Week 6 (checkpoint, visibly larger)
-> Week 9 (GUI/data-storytelling territory, checkpoint) -> Week 14
(professional-workflow checkpoint) -> Week 15 (async, 2 items, no gate) ->
Week 16 (Farkle/ML, 1 item, no gate) -> Week 17 (closure, 2 items). No dead
ends, no broken navigation *within* Weeks 1-17 in sequence order; the only
navigation issue is the Week 1 Wed/Fri tail-sort already recorded. No
student-visible instructor-only material found. No accidental reliance on
hidden lore -- confirmed by the same backstage-canon scan above.

## Duplicate/drift/idempotence evidence

Two consecutive `dry-run --course cs2` runs immediately after the live push
both returned:

```
Reconcile summary: create=0, update=0, skip=169, delete=0
```

A genuine, twice-confirmed idempotent fixed point. No known non-idempotent
object class was encountered in this session.

## Unresolved LMS-policy questions (not fabricated around)

- Late/drop mechanics for the weighted assignment groups -- still an open
  "deployment question" per `docs/grading-model.md`'s own text, unchanged
  by this session.
- The Week 1 module-ordering defect (YELLOW 2) -- belongs to the
  `semester_kickoff_week` pipeline, not this prompt.

## Runtime checks still deferred for later weeks

Per Prompt 021's explicit "what this prompt deliberately does not require"
list: the Week 14 container runtime was not verified this session (not due
for months), and no weekly lecture slide deck completeness was checked
(separate, ongoing work under Prompts 015-020).

## Prompt 013 reconciliation outcome

Closed with evidence. See `013_imprint_cs2_to_savnac_and_read_back.md`,
moved to `sidecar/prompts/completed/`. Prompt 013's originally-requested
minimum slice (Course Information + Weeks 1-3) is a strict subset of what
this session verified live in Savnac.

## Explicit confirmation

**No production SWOSU Canvas write occurred.** Every write and read this
session targeted `http://192.168.122.172:3000` (the Savnac host), enforced
by `imprint.config.require_host_marker` on every call; the default
production base URL (`https://swosu.instructure.com`) was never reached.
No ZyBooks write occurred. No credential value was read aloud, logged, or
committed.

## Final acceptance verdict

**ACCEPTED.** The complete honest, source-backed Fall 2026 CS2 semester
(Weeks 1-17, with Week 1 owned by a separate pipeline and confirmed present)
is live and inspectable in Savnac course 3. Coverage is GREEN for every
week; three YELLOWs are disclosed above, none fabricated around. The
rendered course was read back independently (not trusted from the write
response), walked as a professor and as a student, and shown to converge to
a true no-op on immediate re-run. Prompt 013's acceptance debt is closed.
Production SWOSU Canvas was never touched and remains a separate,
explicitly unauthorized boundary for a future session.

**What exactly was in CS2 when we declared Savnac ready (2026-08-17):** 20
modules, 121 assignments, 69 pages, 15 assignment groups at exactly 100%
weight, three checkpoints (Weeks 6/9/14) with 4-criterion rubrics each,
zero ZyBooks references, zero backstage-canon leaks, one disclosed
navigation defect owned by another pipeline.
