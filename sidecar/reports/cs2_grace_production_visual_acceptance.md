# CS2 Grace production visual acceptance — report

Job: `foreman_interface/jobs/tasks/cs2_grace_visual_acceptance_luna_helper_20260825.md` (Grace visual pass) followed by `foreman_interface/jobs/tasks/cs2_week15_title_fix_april_20260825.json` (april repair pass). Full narrative of the Grace-side capture run lives in `foreman_interface/sidecar/reports/luna/cs2_grace_visual_acceptance_luna_helper_20260825__report.md`; this is the CS2-owned durable record, reconstructed here on april from that report's account since the file was written locally on Grace but never pushed to this repo's remote before the repair pass began — noted here for provenance, not hidden.

## What the Grace visual pass did

Read-only visual acceptance against `sidecar/reports/cs2_grace_visual_qa_manifest.md`'s 14-stop route, using the dedicated isolated-profile Chrome capture pattern (`computing_commons/scripts/grace/start-savnac-capture-browser.ps1` + `capture-canvas-full-page.ps1`) against production Canvas `74031`. Two real human gates were hit and cleared by Jeremy directly (SWOSU SSO login in the dedicated profile; a local Windows-checkout fix for `computer_science_2` unrelated to Canvas — a colon-containing archived filename NTFS disallows, resolved via a local, reversible, index-only `git update-index --skip-worktree`, no history/remote mutation). After both gates cleared, all 14 manifest stops were captured and visually reviewed.

**Result: no student data exposed anywhere across any of the 14 stops. No P0 defects. One P1 defect found. Several pre-known P2 items recorded as deferred, not blockers.**

## P1 defect (now resolved)

**Week 15 page (`cs2-week-15-overview-3`) heading contained the word "Mexico"** — leaked verbatim from an internal planning-doc codename (`planning/week-15.md`'s working title, "Week 15 — Mexico: Asynchronous, Light, and Self-Contained," referring to Jeremy's own personal Thanksgiving travel plans, not course content). Inappropriate for student-facing production content.

**Fix (april, this pass):**
- Source already corrected: commit `9a47e91013c787a36cd4dcff74a927d80b8a9e53` changed `planning/week-15.md`'s H1 from "Week 15 — Mexico: ..." to "Week 15 — Buffer: ...".
- Live page repaired via a single-word `wiki_page[body]` substitution (`update_page`, not a rewrite) — confirmed exactly one occurrence of "Mexico" before the write, confirmed zero after, confirmed "Buffer" present in its place, and confirmed the entire rest of the 1052-character body is byte-for-byte identical before and after (programmatic diff against the pre-edit body, not eyeballed).

**Before/after snippet:**
- Before: `<h2>Week 15 -- Mexico: Asynchronous, Light, and Self-Contained</h2>`
- After: `<h2>Week 15 -- Buffer: Asynchronous, Light, and Self-Contained</h2>`

**Canvas API readback timestamp (page `updated_at`, post-write GET):** `2026-08-26T03:19:18Z`

No title, due date, points, publication state, or any other page/course field was touched. No other course was touched (allowlist restricted to `{74031, 24298}` for every call).

## P2 items (deferred, explicitly not fixed in this pass, not blockers)

- Accessibility-checker table-header warnings on the rubric tables (cosmetic).
- Roll Call Attendance sits in the `Assignments` group (0% weight) rather than `Attendance & participation` (8%) — a pre-existing structural mismatch, documented in `cs2_final_production_closeout.md`; fixing it requires `update_assignment` (group reassignment), out of scope for this pass.
- The 14 deployed gate/checkpoint assignments have no due dates set — documented in the same closeout report as an honest, intentional seam (no authoritative calendar source was available to derive them from safely).

None of these block visual acceptance.

## Confirmation

No P2 item, due date, grade, submission, rubric, assignment-group weight, or any course other than 74031 was touched in this repair pass.

## Commits

- `computer_science_2`: this report (see git log for this file's own commit).
- `foreman_interface`: helper report addendum recording this completion (see `sidecar/reports/luna/cs2_grace_visual_acceptance_luna_helper_20260825__report.md`).

## Final verdict

`CS2 VISUALLY ACCEPTED -- PRODUCTION COURSE CLOSED FOR ROUTINE DESIGN CHURN`
