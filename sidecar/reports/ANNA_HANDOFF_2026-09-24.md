# Anna handoff — CS2 weeks 7-17 overview fix, 2026-09-24 (session paused for April restart)

Work file: `foreman_interface/jobs/tasks/anna_cs2_weeks7_17_overview_off_by_one_fix_2026-09-24.md`
(+ ADDENDUM: Friday 11:59pm due dates, all 4 courses).
Branch: `anna/cs2-weeks7-17-overview-fix` (not merged to main).

## What's actually live right now (verified by direct read, 2026-09-24)

The real bug was narrower than the work file assumed, and narrower than my
own first-pass investigation fork found. Two independent off-by-one bugs
existed and mostly cancelled out:
1. Each week-N module's "Overview" item linked to page-slug (N-1).
2. Each page-slug N's own body actually held week (N+1)'s real content, for
   N=7..14 (verified by reading every body against `planning/week-NN.md`,
   not assumed from the slug name).

Net effect: **weeks 8-15 were already showing correct content live** before
any of my changes (the two bugs cancelled out) — do not "fix" their links
without re-verifying, the naive fix would have broken them. Only weeks 5,
6, 7 were actually broken, and are now fixed and verified live:
- Week 5 module -> `cs2-week-05-overview-5` (correct content).
- Week 6 module -> `cs2-week-06-overview-5` (the 2026-09-21/22 hand-fixed
  body is now finally actually linked in — it never was before).
- Week 7 module -> new page `cs2-week-07-overview-6`, authored fresh from
  `planning/week-07.md` + `assignments/odyssey_gates/week-07.md` (the real
  Week 7 content had been overwritten by the Week 6 hand-fix and no longer
  existed anywhere live).
- Course front-page "week rail" nav (separate static component, same class
  of bug, no cancellation) repointed for weeks 7-15 to the slugs that
  actually hold each week's real content; week 15's rail chip now points at
  the graded Checkpoint 3 content instead of the separate "Buffer" page.

Verified live via direct GET after the write (module items + front-page
rail all match the corrected map). See
`sidecar/reports/fix_weeks5_7_overview_and_rail_run_2026-09-24.md` for the
run log and `backup_2026-09-24_pre_overview_fix.json` for the full pre-fix
snapshot (front page, all 14 overview pages, all module items 218888-218902).

**Known API gotcha, worth keeping**: `harbor`'s `update_module_item` PUT
with a changed `page_url` returns 200 but silently does not change
anything (confirmed 2026-09-24). The working pattern, used successfully, is
delete the old module item and create a new one at the same position —
see `scripts/fix_cs2_module_overview_items_2026-09-24.py`. This should
probably become a harbor-level note/fix later; not touched this session.

## What's NOT done — remains open

1. **Weeks 8-15 cosmetic mismatch.** Content is correct but the page's own
   `title` and each module item's display title still say the wrong week
   number (e.g. a page titled "CS2 Week 07 — Overview" is actually serving
   Week 8). Rails explicitly ask to check "module item titles/links" —
   this is the one piece of that not yet done. Lower risk (metadata only,
   not body/link), but not started.
2. **Due-date ADDENDUM, not started at all** (Friday 11:59pm Central,
   CS2 first then CS1/DSCT/Architecture). My investigation fork already
   pulled the data read-only — see
   `sidecar/reports/weeks7_17_overview_diff_and_duedate_audit_2026-09-24.md`
   Part B for the derived per-week Friday dates and flagged HUMAN_GATEs
   (CS2 weeks 15 [Thanksgiving] and 17 [finals] need a real date decision,
   not the +7-day pattern; DSCT needs its own calendar re-derivation, not
   done). No due_at was written anywhere. `course_foundry`'s own automated
   weekly-rollover dry-run (see below) independently flags the CS2 Week 7
   gate as missing a due date, corroborating this.
3. `scripts/fix_weeks5_17_overview_linkage_and_due_dates.py` is my
   investigation fork's **first draft**, built on the wrong assumption
   (that only linkage was broken, bodies were fine). It's inert (empty
   mapping tables, refuses to run) but **superseded — do not fill in or
   run it**; the two scripts dated 2026-09-24 (`fix_weeks5_7_overview_and_rail`
   and `fix_cs2_module_overview_items`) are the ones that actually ran and
   are correct.
4. **Part C (non-discussion assignment audit)** — Jeremy's new standing
   rule (`jeremy_task_tracking/COURSE_DESIGN_RULES.md`, "student work is a
   shared learning resource") asked, read-only, for a list of every future
   assignment across all 4 courses not yet a graded discussion. Raw data
   already gathered opportunistically, unverified submission counts — see
   audit report Part C. No conversions done or planned; audit-only per
   Jeremy's explicit instruction.
5. Report table (acceptance-test format: per-week live-before/correct/
   action/readback) not yet assembled into the work file's requested shape
   — the run log has the raw data, just not written up as that table.

## Also found, not mine, not acted on

`course_foundry/sidecar/reports/auto_weekly_rollover_runs/` has two fresh
dry-run JSON files (2026-09-24T20:21Z, `apply: false` throughout) from what
looks like a separate automated weekly-rollover process, showing CS2/DSCT/
Commons about to roll from Week 6 to Week 7, and independently flagging the
CS2 Week 7 gate as missing a due date. CS1 and Architecture's rail-update
step reports "skipped — ambiguous/stale Week 6 page title" — likely the
same class of title-mismatch bug as item 1 above, in those courses. Left
untouched (not something I started or understand the ownership of); worth
someone checking whether `apply: true` is expected soon given "Week 7 opens
soon."

## Blocker

None for resuming later — this session's harness blocked further live
Canvas writes for the remainder of the task (auto-mode classifier), which
is why the due-date and title-cleanup work wasn't attempted after this
point. Nothing is left half-written live; every write that happened has
been read back and verified.
