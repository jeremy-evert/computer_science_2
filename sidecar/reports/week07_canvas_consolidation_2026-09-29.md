# CS2 Week 7 Canvas surface consolidation — 2026-09-29

Anna, run `ba8e0940aa62beb521c67300930cb724`, on April. Follows Jeremy's
2026-09-28 direct feedback: "cs2 sucked ass... I don't feel confident for
CS2 yet," and his ask to compare the OpenAI-origin and Anthropic-origin
material he built live in class, fold in what's better, cut what's
redundant, and produce one coherent Canvas surface.

## The comparison

Two candidate files, both committed live in class 2026-09-28:

- **`week_07/class_example.py`** (commit `3753498`, 13:23) — the
  OpenAI/Copilot-origin artifact ("the first file that was like classroom
  example"). Originally a 1697-line monolith: `SupplySource` ABC,
  `SettlementWarehouse`/`TradingPost` stateful collaborators,
  `ExpeditionPlanner` caller, extensive tests. Jeremy himself refactored
  this later the same session (commit `2206bed`, 13:41) into the numbered
  `step_01`–`step_09` teaching sequence plus a PDF/LaTeX handout
  (`week_07_guided_path.pdf`/`.tex`) — `class_example.py` is now just a
  34-line CLI entry point importing the step files. I verified this
  refactored version runs clean: `python class_example.py test` → 34/34
  pass; `python class_example.py demo` → real working swap output.
- **`week_07/week_07_contract_and_swap/`** (commit `2206bed`,
  `nuke_and_pave.ps1`) — the Anthropic-origin artifact (a single
  PowerShell bootstrap script that generates the whole project in one
  shot): `GrowthReporter` ABC, stateful `TrailScout`/`SignalTower`
  collaborators, `SettlementGrowthSystem` caller, 35 tests, a six-part
  `WORLD_BIBLE.md`. Verified: `python -m unittest -v` → 35/35 pass;
  `python demo.py` → real working swap output.

**Verdict: not actually competing on the same ground.** Both are
Frontier-Settlement-flavored, stateful, and teach the identical target
(explicit ABC contract, two conforming stateful collaborators, caller
boundary, swap test, World Bible entry) — but they're pedagogically
different in shape, not redundant with each other: the numbered path is
a *sequenced lesson* (one idea per file, meant to be read/run in order,
backed by a narrative PDF handout), while `week_07_contract_and_swap/`
is a *polished single reference* (one cohesive example to read end to
end). Jeremy's own `00_start_here.md` already made this call correctly
before I got involved: numbered path = primary (linked from the
assignment), `week_07_contract_and_swap/` = "a polished, alternate...
reference." I left that hierarchy as he set it rather than re-deciding
it — his own judgment on his own material.

**The actual redundancy was mine, not his.** My own
`contract_swap_example_frontier_settlement/` (built 2026-09-28, before I
knew about Jeremy's parallel work) used the *same* Frontier Settlement
world as `week_07_contract_and_swap/`, but with weaker, stateless
collaborators (`WellBoardIntake`/`TradePostIntake` vs. his stateful
`TrailScout`/`SignalTower`) — genuinely two competing versions of the
same thing, his better. **Cut** (commit `16e7cca`): deleted the
directory, removed it from `00_start_here.md`'s reference list. My other
three (kitchen, Investigation Bureau, Starship Log) use distinct worlds
with no Jeremy equivalent — kept, but relabeled "pre-stateful-update
illustrations" (already done 2026-09-28 evening, reconfirmed here) since
none of them meet the current stateful requirement either.

## Canvas surface rebuild

Before: module 218891 had only my original kitchen-only "Worked Example"
page and the assignment — none of Jeremy's numbered walkthrough, PDF
handout, or `week_07_contract_and_swap/` reference were reachable from
Canvas at all, despite the assignment text (repo version) already
pointing students at `week_07/00_start_here.md` and
`week_07_guided_path.pdf` — repo paths, unreachable to students
(`computer_science_2` is private). That's the real "messiness": Jeremy's
best material existed only in a private repo.

Fixed, target-locked and verified live before every write:

1. **Uploaded 13 files to Canvas** (course 74031): the PDF handout, all
   9 numbered step files, `class_example.py`, `test_settlement.py`, and
   `WORLD_BIBLE.md` — every upload's returned `size` byte-matched the
   local file before proceeding (see `/tmp/w7_guide_uploads.json`,
   ephemeral, not committed).
2. **New page: "Week 7 Guided Walkthrough — Contract and Swap"**
   (`week-7-guided-walkthrough-contract-and-swap`, id `457153`) —
   the numbered-step table (each step linked to its real uploaded file),
   the PDF handout link, the plain-language contract/caller-boundary
   explanation from Jeremy's own handout text, and a pointer forward to
   the Worked Examples page. Inserted at module position 2, right after
   the overview.
3. **Rebuilt "Worked Examples — Contract and Swap (Week 7)" page**
   (same URL, `worked-example-contract-and-swap-week-7`, so nothing
   orphaned) — now leads with Jeremy's `week_07_contract_and_swap/`
   reference (full `settlement.py` and `demo.py` embedded verbatim from
   the actual files, `test_settlement.py` and `WORLD_BIBLE.md` linked as
   uploaded files, a real summary of the v0.6→v0.7 World Bible change),
   then the three remaining pre-stateful-update illustrations
   (kitchen/bureau/starship) clearly separated and labeled, with the
   redundant frontier-settlement section gone entirely. Pushed to module
   position 3.
4. **Module item renamed** to match the rebuilt page title.
5. **Assignment stays untouched** — module position 4, no change to its
   text/points/submission type. (Separate finding below.)

## Other messiness found and fixed

- **Orphaned stale duplicate page, `cs2-week-07-overview-5`**: titled
  "CS2 Week 07 — Overview" but its actual body content is Week 8's
  "World-Fit Data Abstraction (S05)" topic — genuinely mislabeled, not
  linked from any module, already flagged by yesterday's
  `anna-week7-live-check` session's report. **Unpublished** (not
  deleted, reversible) rather than left live and confusing.

## Found, not fixed — flagging, not mine to decide

- **The live Canvas assignment (id `914178`) is stale relative to the
  repo on two fronts**: its description still says "Weeks 3-5" (repo
  said "Weeks 4-6" even before Jeremy's rewrite) and it's still a plain
  `online_text_entry`/`online_upload` assignment, not the graded
  discussion Jeremy's repo edit (`assignments/odyssey_gates/week-07.md`,
  commit `84da90b`) describes. I did not touch the assignment's text,
  points, or submission type — that's a real grading-mechanics decision
  (converting to a Discussion is a structural Canvas change, not a
  worked-example page), out of my authority to make solo per the
  standing "no production assignment/gradebook changes without an
  explicit Flo/Jeremy gate" rule. Flagging for Flo/Jeremy to decide
  whether and how to sync it.
- I also noticed module item id `1529997` (the module's pointer to the
  assignment) required going through its `content_id` field to reach the
  real assignment (`914178`) — a module-item id and its assignment's own
  id are different things; worth remembering for future Week 7 work on
  this course so no one else hits the same 404 I hit yesterday querying
  `assignments/1529997` directly.

## Independent readback (separate calls from every write above)

Module 218891, final state:

| Position | Type | Title |
|---|---|---|
| 1 | Page | CS2 Week 07 — Overview |
| 2 | Page | Week 7 Guided Walkthrough — Contract and Swap |
| 3 | Page | Worked Examples — Contract and Swap (Week 7) |
| 4 | Assignment | Reasoning Odyssey Gate — Week 7 — Contract and Swap (S03/S08) |

- `cs2-week-07-overview-5` confirmed `published: false`.
- Guided Walkthrough page: all 11 file links present, all resolve to
  real Canvas file downloads (spot-checked the PDF link: `302` to the
  real signed Canvas-user-content URL). No repo-path links.
- Worked Examples page: `GrowthReporter`/`TrailScout`/`SignalTower`
  (primary) and `KitchenBell`/`EvidenceLogger`/`SubsystemReporter`
  (secondary) all present verbatim from the real files; both file links
  (`test_settlement.py`, `WORLD_BIBLE.md`) and both page/assignment
  links resolve to real Canvas objects. No repo-path links, no
  `contract_swap_example_frontier_settlement` reference remaining
  anywhere live.

## DONE

One coherent Week 7 Canvas surface: overview → guided walkthrough
(primary, Jeremy's own, fully reachable) → worked examples (his stateful
reference first, three optional illustrations after, redundant one cut)
→ assignment. No duplicate/competing pages left live. Repo commits:
`16e7cca` (cut frontier-settlement). Canvas evidence: this report plus
the readback above.
