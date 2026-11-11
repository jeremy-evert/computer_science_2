# Week 13 showcase: a finished project to look at

Source for the Canvas front-page "Showcase" section (CS2, course 74031), added 2026-11-11.

## What students are pointed at
- **Project page:** <https://jeremy-evert.github.io/sorting_and_searching/> (public, GitHub Pages).
- **Code and build record:** <https://github.com/jeremy-evert/sorting_and_searching> (public).

## Why
Weeks 12 to 14 ask students to stabilize, refactor and document their own projects. The showcase is a finished example of that: clean object-oriented Python, hand-worked tests, a one-command rebuild (`python scripts/regenerate.py --check`), claims that are checked by scripts, a home page with real alt text, and a `sidecar/` folder that keeps the build record apart from the product. Students use it over the weekend to think about what they want their own portfolio to look like.

## Where to look, in order
1. The README (what it is, how to run it, what reproduces and what does not).
2. `BIG_O.md` (Big O explained, checked against counted operations).
3. `tests/test_sorters.py` (expected values worked out by hand, in comments).
4. `docs/WHAT_IS_A_TEST.md` (a three-line unit test, with a passing and a failing run).
5. `sidecar/` and `AGENTS.md` (how the work was directed, and the pre-publish prompt in `sidecar/prompts/README.md`).

## Canvas change record
- Front page `start-here-this-week` (course 74031, id and name verified before write): one new section, "Showcase: what a finished project can look like", inserted directly after the "Go here first" list. Nothing else on the page was changed.
- Script: `scripts/add_showcase_to_front_page.py` (dry-run default; idempotent via `data-showcase` marker).
- Backup of the page before the write: `week_13/showcase/canvas_backups/`.

## Known, not changed here
- The front page's "Due Friday, Nov. 6" box and the "Week 12 gate" wording are stale for Week 13 (the Week 13 checkpoint is due 11/13). That is the weekly rollover's job; flagged to Flo.
- The showcase repo's improvements (regenerate command, CI, accurate claims) are on a pull request until Jeremy merges it: <https://github.com/jeremy-evert/sorting_and_searching/pull/2>.
