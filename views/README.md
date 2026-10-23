# Repository Views

This directory contains generated visualizations of the repository. The course files remain the source of truth; `views/` contains no replacement lessons or concept notes.

## Regenerate

From `C:\Users\evertj\git\computer_science_2`:

```powershell
python views\generate_semester_topic_map.py
python -m json.tool views\semester-topic-map.canvas > $null
```

The generator validates duplicate node IDs, edge endpoints, and every native Canvas file node’s source path before writing. The Canvas uses text cards for the teaching story and native file nodes for direct navigation to repository evidence. Arrows labeled `documented` reflect the active sequence; arrows labeled `inferred` are instructional synthesis.

Open the repository folder as an Obsidian vault and open `views/semester-topic-map.canvas`.

## Vault setup (Obsidian)

- This folder is `views/`, not `.views/`: Obsidian excludes dot-folders from its index, so Quick Switcher (Ctrl+O) cannot find files in them.
- Install per-user: `winget install --id Obsidian.Obsidian -e --scope user`. No plugins are needed for Canvas.
- Under Settings → Files & Links → Excluded files, add `recordings/` and `sidecar/` (student voices and raw recon output must not be indexed).
- `.obsidian/` is gitignored; vault settings are personal and are not tracked.
- Any Wilbur context pack or memory notes belong in the private `character_garden` repo, never in this public course repo.

## Graph View hubs (`views/graph/`)

Obsidian's Graph View only gets edges from links, and the course markdown has almost none between notes. `python views/generate_repo_graph.py` writes generated hub notes with `[[wikilinks]]`: one index, one hub per area (links to every note in it), and one hub per week (previous/next week plus that week's plan, lesson, gate, and rubric). Course files are not modified. The script prints zero-degree (isolated) note counts before and after.

2026-10-23 result: 137 notes, 137 isolated by wikilinks (125 counting plain markdown links) before; 0 after.

## Canvas layout checks

`generate_semester_topic_map.py` computes card height from text length, lays cards out in three phase columns, and links only neighbors. `validate()` fails the run if an edge, its curve bounding box, or its label overlaps any card that is not its endpoint, or if two cards overlap. These are geometric checks plus a rendered image; they are not a substitute for opening the canvas in Obsidian once.
