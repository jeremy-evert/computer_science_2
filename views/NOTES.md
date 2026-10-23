# Obsidian views: what we did and why (2026-10-23)

Durable history for the Obsidian work in this repo. For how to run things, see
[README.md](README.md). This file records decisions, findings, and what was
verified, so a later reader does not have to rediscover them.

## What exists

| Thing | Where | What it is |
|---|---|---|
| Semester topic map | `views/semester-topic-map.canvas` | Generated Obsidian Canvas of the eight-stage teaching story. Do not hand-edit. |
| Canvas generator | `views/generate_semester_topic_map.py` | Holds the view spec, builds the JSON, validates layout, optional `--svg` render. |
| Graph hub notes | `views/graph/*.md` | Generated wikilink hubs so Graph View shows structure. |
| Graph generator | `views/generate_repo_graph.py` | Writes the hubs and prints isolated-note counts before and after. |
| Launcher | `views/show-maps.ps1` | One command that opens the canvas and the graph in Obsidian via its CLI. |
| Practice note | `views/Bubble sort and lists.md` | Hand-written first link between the week 9 bubble sort results and the lists lesson. |

The course files remain the source of truth. Nothing in `views/` replaces a
lesson or concept note, and course markdown was not edited to add links.

## Timeline

| Commit | What changed |
|---|---|
| `b663c0e` | A previous agent added the first canvas, in `.views/`. |
| `9f4ef8a` | Renamed `.views/` to `views/`; gitignored `.obsidian/`; fixed a stale `J:\` path in the README. |
| `b623739` | Graph hubs (isolated notes 137 to 0); canvas rebuilt with computed card heights, phase columns, neighbor-only edges, geometry checks. |
| `e75abed` | Practice note for the first hand-made Obsidian link. |
| `26e4ab7` | One-word edge labels after checking in real Obsidian; `show-maps.ps1`; `--svg` render. |

## Decisions and the reasons for them

- **`views/`, not `.views/`.** Obsidian excludes dot-prefixed folders from its
  index, so Ctrl+O and Quick Switcher cannot find files in them.
- **`.obsidian/` is gitignored.** Workspace and cache files are personal. The
  canvas and generators in `views/` are tracked.
- **Course markdown stays plain-link.** Graph hubs are generated, so the
  source files remain readable on GitHub and unchanged.
- **Excluded files:** `recordings/` and `sidecar/` are set in
  `.obsidian/app.json` (`userIgnoreFilters`). That file is untracked, so a new
  machine must set this again under Settings, Files & Links, Excluded files.
  `recordings/` holds student voices and must never be indexed or published.
- **Reasoning about arrows.** Edges are only between neighbors in dependency
  order. `documented` follows the active sequence; `inferred` (orange) is
  instructional synthesis.
- **Wilbur or memory notes** belong in the private `character_garden` repo,
  never in this public course repo.

## Findings worth remembering

1. **Obsidian has a CLI.** Enable it in Settings, General, Advanced, Command
   line interface. The shim is `Obsidian.com` next to `Obsidian.exe`; `obsidian`
   is on PATH only after "Register CLI". Useful commands: `open path=...
   [newtab]`, `tab:open view=graph`, `orphans`, `deadends`, `unresolved`,
   `eval code=...`, `dev:screenshot path=...`. `open` reuses the active tab.
   Pass JavaScript to `eval` as one line with no double quotes.
2. **Excluded folders are hidden, not unindexed.** `orphans` and `deadends`
   still list `sidecar/`. Only the graph and search display hides them.
3. **Canvas edge labels do not scale with zoom.** A long label spills over
   neighboring cards at fit-to-view zoom. Keep labels to one word and put the
   reasoning in the card text.
4. **My own geometry check was not enough.** It passed while real Obsidian
   showed labels hidden behind cards. Verify in Obsidian, not only in a script.
5. **A freshly opened canvas can screenshot blank.** Cards looked empty until
   the canvas finished painting; the text was in the DOM the whole time. Wait a
   few seconds before judging a screenshot.

## What was verified, and how

- **Graph:** 137 notes were isolated by wikilinks before (125 counting plain
  markdown links) and 0 after. Obsidian's own `orphans` and `deadends` agreed;
  the only linkless notes are in the excluded `sidecar/` folder.
- **Canvas:** measured inside Obsidian through `eval`: every card's text fits
  with 10 to 107 px to spare, so no card needs scrolling. A real screenshot
  shows no arrow crossing a card and labels sitting in the gaps.
- **Not verified:** the launcher when Obsidian is not already running (it would
  start the app through `obsidian://open?vault=computer_science_2`, untested);
  and the CS1 `validate_canvas_layout.py`, which was not available here, so
  CS2 has its own stdlib-only check instead.

## Known open items

- The five course files that show modified in `git status` had line-ending-only
  changes at the end of this session (`ROADMAP.md`, `START_HERE.md`,
  `docs/repo-map.md`, `lessons/strings-collections.md`,
  `week_09/BUBBLE_SORT_RESULTS.md`). Cause not identified. Not committed.
- Re-run `python views/generate_repo_graph.py` after adding or renaming notes,
  otherwise the hubs go stale. Isolated notes are reported by the script.
- `python views/generate_semester_topic_map.py` fails loudly if the layout
  breaks or a cited file moves.
