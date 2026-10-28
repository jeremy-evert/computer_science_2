# CS2 student-facing page source (pages only)

Source of truth for what CS2 (Canvas course 74031) shows on its front page and
week Overview pages. Canvas is rendered FROM these files; do not hand-edit Canvas.
No student data belongs here. File links carry no `verifier=` tokens (they are
capabilities); the renderer restores the live ones at write time.

- `manifest.json`: course id/section lock, `rail_slugs` (fills weeks the Canvas modules
  cannot name; module truth wins), page list.
- `start-here-this-week.html`: the Start Here frame. Tokens: `{{WEEK}} {{WEEK_RAIL}}
  {{THIS_WEEK}} {{DUE_BANNER}} {{GO_HERE_FIRST}} {{QUICK_ANSWERS}} {{EXTRA_LINKS}}`.
- `start-here/week-NN/<part>.html`: hand-written text for that week only (part =
  `this_week due_banner go_here_first quick_answers extra_links`). Missing file ->
  generated from Canvas truth (module, gate `due_at`); `extra_links` -> nothing. So
  Week 12 never inherits Week 11's text, and Week 11's hand edits are never lost.
- `cs2-week-NN-overview-*.html`: each published week Overview body, verbatim (file name
  = Canvas page url).

To change a page: edit here, commit, push to `main`, then Flo/Anna renders it
(`course_foundry/scripts/repair_start_here.py --course cs2 --from-repo --apply`; the
Saturday rollover does the same from `origin/main`). Read-only drift check, Thursday and
before Saturday: `course_foundry/scripts/page_drift_check.py --course cs2`.
Bootstrapped 2026-10-28 from the live pages by `scripts/export_pages_to_repo.py`.
