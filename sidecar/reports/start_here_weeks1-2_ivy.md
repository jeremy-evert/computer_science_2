# CS2 Start Here rail + Weeks 1–2 overview pages — Ivy evidence

Date: 2026-09-08
Role: Ivy / Foreman Intern, for Anna's bite
`jobs/anna/bites/cs2_start_here_weeks1-4.md` (5-class layout campaign,
third bite — Commons and CS1 already deployed). No Canvas contact.

## Applied Anna's CS1 correction up front

CS1 shipped with bare relative hrefs (`href="week-04"`) that broke in
Canvas — assignments are ID-addressed, not slug-addressed, and relative
paths resolve against the page's own URL, not the course root. Every
`href` in both new pages below is an absolute
`https://swosu.instructure.com/courses/74031/...` URL — verified
programmatically (grepped every href in both files, confirmed each one
starts with that exact prefix).

## Week 2 — checked the source before assuming it needed building

Read `computer_science_2` `planning/week-02.md`,
`assignments/week-02-local-ai-readiness.md`, and the `lessons/week-02-*`
files fresh (fetched `origin/main` first — local was several commits
behind after today's earlier CS2 work merged). **CS2's Week 2 concept is
genuinely authored** — "Build and Verify Your Local AI Lab," the shared
local-AI bench, no Odyssey gate this week. Not a Jeremy-question gap;
built the real overview page from this source. (If I'd found nothing
authored, per the bite I'd have flagged it instead of inventing content —
didn't need to.)

## Pages built

- `sidecar/canvas_pages/week-01-overview.html` — CS2's shared orientation
  arc (same universal Week 1 as every course), linking the three
  orientation pages using the exact slugs Anna confirmed live on 74031
  specifically (`monday-survive-this-semester`,
  `wednesday-thrive-in-your-degree`, `friday-entering-your-career`).
- `sidecar/canvas_pages/week-02-overview.html` — the real Local AI Lab
  content from `planning/week-02.md`/`assignments/week-02-local-ai-readiness.md`.
  One link left as `{{ANNA: confirm...}}` rather than guessed: I don't
  have a live-verified Canvas slug/URL for the readiness page/assignment
  itself, and I'm not repeating CS1's mistake by guessing one.
- `sidecar/canvas_pages/start-here-week-rail-insert.html` — **the rail
  snippet only**, not a full reconstructed Start Here page body. See "What
  I didn't do" below for why.

## What I didn't do, and why

The bite says "insert the missing rail, don't rebuild the rest of it" —
but I was not given the live `start-here-this-week` body text the way
Anna gave me Commons' exact live body for that bite. Without it, I can't
produce a precise insertion diff or verify byte-identical preservation of
the parts I'm not supposed to touch, and after CS1's relative-href lesson
I'd rather ask than guess at content I can't see. **Delivered the
ready-to-paste rail snippet and exact placement instructions (right under
the header, before "This week" — same pattern as Commons and CS1) instead
of attempting a full-body reconstruction.** Flagging this to Anna
directly; if she can share the live body (like she did for Commons) I'll
do the precise insertion myself in a follow-up commit on this same
branch — otherwise she can paste the snippet in herself, which is a much
smaller/lower-risk edit than what Commons or CS1 needed.

## Rail

`course_foundry.week_rail.render_week_rail` reused unchanged (third
course in a row — the reuse keeps paying off). Weeks 3–17 use the exact
slugs Anna pre-pulled live; Weeks 1–2 point at the two new pages above.
Verified: no `<script>`/`<style>`/forbidden CSS property in the snippet
or either new page body.

## Not in scope for this bite (per Anna's bite)

- Cleaning up Weeks 5–17's auto-generated slugs — flagged by Anna already
  as a real-but-not-blocking follow-up, not touched here.
- Week 3's own overview-page content, and all of Week 4 — untouched;
  I never opened either page body, only referenced Week 3's current live
  slug in the rail.
- Module reorganization for Week 3's 20 items — Anna's own job per the
  bite; I don't have a specific item list to hand her since I didn't pull
  that module's contents (no Canvas access), unlike CS1 where her bite
  text already gave me the item list to relay.

## Update — Flo's three CS1-follow-up items, applied to CS2

### 1. Week 4 gate → graded discussion

No action needed from me — Anna's handling the Canvas discussion-topic
creation and old-assignment handling herself, same as CS1. I did not
touch CS2's Week 4 page/assignment (untouched per the original bite
scope too), and none of my new pages link to the old Week 4 gate
assignment as a submission target, so nothing here assumes the old link
is still where students submit.

### 2. Leak/reachability discipline — audited and fixed retroactively

**Caught a real violation in my own already-drafted pages before this
message arrived:** both `week-01-overview.html` and `week-02-overview.html`
had "(Source: `planning/week-0N.md`...)" repo-path phrasing in the
student-facing prose. Fixed both — removed the parenthetical citations
entirely rather than rewording around them. Re-grepped both files for
`github.com`, `planning/`, `lessons/`, `assignments/`, `docs/`: zero
matches now. Every `href` in all four page bodies (including the new
block map below) is either a `swosu.instructure.com` Canvas URL or one of
three well-established public documentation domains
(`docs.python.org`, `matplotlib.org`, `docs.github.com`) — verified
programmatically, not just by inspection.

### 3. CS 2 Planning Block Map — built, with one drift finding

`sidecar/canvas_pages/cs2-planning-block-map.html`: full Weeks 1–17
table (week overview link, technical focus, anchor question, optional
free public reference).

**Sourced from CS2's own `planning/week-0N.md` files — but caught a real
trap first.** `origin/main`'s `planning/week-03.md` through `week-15.md`
still carry the **stale pre-`b6fc6b1`-re-slide topics** (my own
`ivy/cs2-planning-reconcile` fix, already reviewed and accepted earlier
today, is not yet merged to `main`). Used the reconciled versions from
that branch instead of `origin/main` for weeks 3, 5–15; used `origin/main`
for weeks 1, 2, 4 (4's fix already merged), 16, and 17. Every topic label
and anchor question in the table traces to a real tie-in sentence from
the *correct* (reconciled) source, not the stale one.

**Second drift finding, flagged rather than silently worked around:**
`docs/curriculum/fall-2026-resource-map.md` — the natural source for the
"free reference" column — also appears to carry pre-re-slide week
numbers (its own week-9/10-11 grouping doesn't match the corrected
week-10/11 topics). I did not try to guess the correct shift arithmetic
under this bar's now-zero tolerance for a wrong public link. Instead,
assigned each week's reference by matching its own real (corrected) topic
directly to a well-known, stable public docs page — e.g. Week 6 "Earned
Substitution" (is-a / subtype swap) → `docs.python.org/3/library/abc.html`,
Week 10 "Compact GUI over Tested Model" → `docs.python.org/3/library/tkinter.html`
— rather than trusting the resource-map's week-number column at all. Left
several weeks' reference cell as "—" (no confident public-doc match)
rather than force one. **Flagging `fall-2026-resource-map.md` itself as a
third instance of the same `b6fc6b1` drift** for whoever eventually
reconciles it — not fixed here, out of this bite's scope.

## Spend split

Anthropic only — no Codex dispatch. Direct authoring, same reasoning as
Commons Part B and the whole CS1 bite: new-content assembly from already-
read source, not a task suited to a second agent's independent judgment.

IVY CS2 START HERE (PARTIAL — RAIL SNIPPET, NOT INSERTED) + BLOCK MAP
READY FOR ANNA
