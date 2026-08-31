# 2026-08-31 — Week 2 Hardware Confidence production deploy

Mission: `foreman_interface/jobs/tasks/cs2_week2_hardware_confidence_and_commons_aider_links_april_20260831.md`
(Phase 1). Urgent, for the 2026-08-31 11:00 CS2 class.

## Source HEAD

- `computer_science_2` HEAD at deploy time: `0e8f3d84f58913d84fbe4ffd0e726299ba193dcc`
- New source added this run (committed alongside this report):
  - `lessons/week-02-hardware-confidence.md`
  - `lessons/week-02-hardware-confidence-walkthrough.md`
  - `presentations/beamer/week02_hardware_confidence/hardware-confidence.tex`
  - `scripts/deploy_week2_hardware_confidence.py`
  - `sidecar/runs/week2_hardware_confidence_deploy.json` (raw before/after receipt)

## Canvas target

Course `74031` (Computer Science II), module `218887`
("CS2 Week 2 -- Found Your World (World Bible v0.1)"). Course allowlisted
on the Canvas client for this run — no other course id was reachable
through the script's client.

## Before / after module truth

Before (1 item):

| position | item id | title |
|---|---|---|
| 1 | 1529982 | CS2 Week 02 -- Found Your World (World Bible v0.1) |

After (5 items):

| position | item id | type | title |
|---|---|---|---|
| 1 | 1531231 | Page | Week 2 — Hardware Confidence + Small Models |
| 2 | 1531232 | File | Slides — Hardware Confidence, Small Models, and the Bite Ladder |
| 3 | 1531233 | Page | Walkthrough — How to Get Started |
| 4 | 1531234 | ExternalUrl | Next: Computing Commons Aider Days (Local AI) |
| 5 | 1529982 | Page | CS2 Week 02 -- Found Your World (World Bible v0.1) — unchanged content, repositioned only |

## Defect found and fixed during verification

Canvas creates `ExternalUrl` module items with `published: false` by
default (unlike `Page` and `File` items, which came back published from
this run's create call). The item-4 "Next: Computing Commons Aider Days"
link was therefore invisible to students immediately after the initial
deploy. Found during the acceptance readback pass, fixed with one
`update_module_item` call setting `module_item[published]=true`,
confirmed by re-fetching the item (`published: true`). All 5 items are
published as of this report.

## Artifacts

- Lecture page: `https://swosu.instructure.com/courses/74031/pages/week-2-hardware-confidence-+-small-models` — published, 4646-char body, opened and read back.
- Walkthrough page: `https://swosu.instructure.com/courses/74031/pages/week-2-how-to-get-started-walkthrough` — published, 2244-char body, opened and read back.
- Slides file: `https://swosu.instructure.com/files/6578290/download` (Canvas file id 6578290, `hardware-confidence.pdf`, 209308 bytes, 14-page Beamer deck built from `presentations/beamer/week02_hardware_confidence/hardware-confidence.tex` using the established CS2 slide system — `destinationframe`, `whymattersframe`, `conceptframe`, `misconceptionframe`, `odysseyframe`, `aimomentframe`, `evidenceframe`, `recapframe`, `exitframe` patterns). Compiled clean with `pdflatex` (only cosmetic overfull-hbox warnings, no errors).
- Aider Days external link: `https://swosu.instructure.com/courses/24298/modules/219031` — opened and read back (see Commons report for what that hub now contains).

## Validation / readback evidence

- Read back all 5 module items by exact id/position after the write; matches the receipt in `sidecar/runs/week2_hardware_confidence_deploy.json`.
- Fetched both new pages directly via the Canvas API: both `published: true`.
- Fetched the uploaded file object: correct size (209308 bytes, matches local build) and a resolvable download URL.
- Re-listed course `74031` modules: count unchanged at 21 (only module `218887`'s items changed).
- Re-listed assignment groups for course `74031`: 15 (untouched by this run — this script never calls any assignment/grade/enrollment endpoint).
- The Canvas client used by `scripts/deploy_week2_hardware_confidence.py` is allowlisted to course `74031` only, so no other course was reachable during this write.

## What was intentionally not changed

- No grade, submission, enrollment, due date, rubric, or assignment-group object.
- No other CS2 module (Weeks 4–17, Monday/Wednesday/Friday success-foundations modules).
- The existing World Bible page's own content — only its module-item position moved (1 → 5); the page object (id `1529982`) and its body are untouched.
- CS2 was not converted into an AI course: the World Bible / Reasoning Odyssey continuation remains immediately after the new opening, not replaced by it.

## Content notes

- Lecture and walkthrough content was authored fresh (no prior "hardware confidence" / "Bite Ladder" material existed anywhere in `computer_science_2`, `computing_commons`, `local_ai_lab_setup`, `windows_classroom`, or `computer_science_1` at the start of this run — confirmed by a case-insensitive search for "bite ladder", "hardware confidence", and "what ai can my computer" across those checkouts).
- Both pages deliberately point to the shared Computing Commons Week 2 / Aider Days road for the technical setup and Aider exercise steps rather than duplicating them, per `computer_science_2/docs/repo-map.md`'s existing ownership rule ("Week 2 ... CS2 keeps a thin wrapper").

## Remaining gate / follow-up

None for this phase. All acceptance-checklist items for CS2 in the controlling mission are satisfied: coherent Week 2 path, lecture accessible, slides rendered/linked/opening, walkthrough accessible and pointing to canonical setup truth, World Bible continuity preserved.
