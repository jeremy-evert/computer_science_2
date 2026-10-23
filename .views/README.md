# Repository Views

This directory contains generated visualizations of the repository. The course files remain the source of truth; `.views/` contains no replacement lessons or concept notes.

## Regenerate

From `J:\git\computer_science_2`:

```powershell
python .views\generate_semester_topic_map.py
python -m json.tool .views\semester-topic-map.canvas > $null
```

The generator validates duplicate node IDs, edge endpoints, and every native Canvas file node’s source path before writing. The Canvas uses text cards for the teaching story and native file nodes for direct navigation to repository evidence. Arrows labeled `documented` reflect the active sequence; arrows labeled `inferred` are instructional synthesis.

Open the repository folder as an Obsidian vault and open `.views/semester-topic-map.canvas`.
