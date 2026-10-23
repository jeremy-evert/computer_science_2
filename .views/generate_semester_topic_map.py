"""Generate and validate the Fall 2026 semester topic map.

Run from the repository root:
    python .views/generate_semester_topic_map.py

The repository remains the source of truth. This script stores only a small
view specification and emits Obsidian's documented Canvas JSON format.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".views" / "semester-topic-map.canvas"


def text(node_id: str, x: int, y: int, width: int, height: int, value: str) -> dict:
    return {"id": node_id, "type": "text", "text": value,
            "x": x, "y": y, "width": width, "height": height}


def file_node(node_id: str, x: int, y: int, path: str, label: str) -> dict:
    return {"id": node_id, "type": "file", "file": path,
            "x": x, "y": y, "width": 260, "height": 110,
            "subpath": "", "label": label}


def edge(edge_id: str, source: str, target: str, label: str, color: str = "") -> dict:
    item = {"id": edge_id, "fromNode": source, "toNode": target,
            "fromSide": "right", "toSide": "left", "label": label}
    if color:
        item["color"] = color
    return item


def build() -> dict:
    nodes = [
        text("title", 0, -420, 1180, 150,
             "# Fall 2026 CS2 — Semester Topic Map\n\n"
             "Teaching story: earn a trustworthy boundary, then make it collaborate, substitute, swap, hold data, explain tradeoffs, respond to events, and tell an honest evidence-backed story.\n\n"
             "Solid dependency arrows are documented in the active sequence; dashed arrows are instructional inferences. Testing, documentation, AI accountability, and review recur throughout (S08)."),
        text("spine", 0, -230, 1180, 120,
             "## Progression\nWeeks 3–4 design → 5 substitution → 6 contracts → 7–8 data abstractions and search/order → 9 GUI/events → 10–11 visualization/storytelling. Recursion is an optional design lens when authentic.\n\nSource: docs/curriculum/course-sequence.md:15-22"),
        text("g1", 0, 0, 280, 230, "## 1 · Earn a boundary\nWeeks 3–4 · S01\n\nWhy it matters: state and behavior should make a small promise that can be explained and tested. Predictions may be rejected.\n\nEvidence: planning/week-04.md; lessons/week-04-cohesive-object-boundary.md; assignments/odyssey_gates/week-04.md"),
        text("g2", 360, 0, 280, 230, "## 2 · Collaborate and protect\nWeek 4–5 · S01/S08\n\nWhy it matters: composition gives responsibilities a boundary; an invariant makes correctness observable.\n\nEvidence: lessons/week-04-composition-and-invariants.md; planning/week-05.md"),
        text("g3", 720, 0, 280, 230, "## 3 · Earn substitution\nWeek 6 · S02\n\nWhy it matters: inheritance is used only when a genuine is-a relationship gives shared operations different meaning.\n\nEvidence: planning/week-06.md; assignments/odyssey_gates/week-06.md; week_06/03_test_substitution.py"),
        text("g4", 0, 320, 280, 230, "## 4 · Make a contract swappable\nWeek 7 · S03/S08\n\nWhy it matters: a caller can depend on a promise while implementations change.\n\nEvidence: planning/week-07.md; assignments/odyssey_gates/week-07.md; week_07/week_07_contract_and_swap/"),
        text("g5", 360, 320, 280, 230, "## 5 · Choose a world-fit data shape\nWeek 8 · S05\n\nWhy it matters: list/stack/queue behavior becomes meaningful when chosen for a real process and proved with a trace or test.\n\nEvidence: planning/week-08.md; assignments/odyssey_gates/week-08.md"),
        text("g6", 720, 320, 280, 230, "## 6 · Explain lookup/order tradeoffs\nWeek 9 · S05/S06\n\nWhy it matters: algorithm choice follows domain need, maintenance cost, and preconditions; binary search is conditional.\n\nEvidence: planning/week-09.md; assignments/odyssey_gates/week-09.md; lessons/plotting-searching-sorting.md"),
        text("g7", 0, 650, 280, 230, "## 7 · Put a thin view over the model\nWeek 10 · S04\n\nWhy it matters: an event can change real model state without making the GUI the only proof.\n\nEvidence: planning/week-10.md; lessons/week-10-tkinter-model-view-lab.md; assignments/odyssey_gates/week-10.md"),
        text("g8", 360, 650, 280, 230, "## 8 · Turn project data into a story\nWeeks 11–12 · S09/S07\n\nWhy it matters: a question, readable representation, limitation, and decision make evidence useful; recursion/linked/nested design is optional when authentic.\n\nEvidence: planning/week-11.md; planning/week-12.md; lessons/week-11-data-storytelling-micro-lab.md; assignments/odyssey_gates/week-11.md and week-12.md"),
        text("evidence", 720, 650, 280, 230, "## Recurring proof loop\nWeeks 2–15 · S08\n\nKnown baseline → bounded change → inspect diff/code → independent test or trace → explain limits → accept/reject and review.\n\nEvidence: planning/week-02.md; docs/curriculum/course-sequence.md:22; later Odyssey gates."),
        file_node("src-sequence", 1040, -390, "docs/curriculum/course-sequence.md", "Active sequence"),
        file_node("src-plans", 1040, -240, "planning/week-04.md", "Weekly plan example"),
        file_node("src-gates", 1040, -90, "assignments/odyssey_gates/week-09.md", "Assessment gate example"),
        file_node("src-lesson", 1040, 60, "lessons/week-10-tkinter-model-view-lab.md", "Lesson example"),
        file_node("src-test", 1040, 210, "planning/week-02.md", "Evidence loop"),
    ]
    edges = [
        edge("e12", "g1", "g2", "documented: boundary enables collaboration"),
        edge("e23", "g2", "g3", "documented: avoid hierarchy until is-a is earned"),
        edge("e34", "g3", "g4", "documented: shared behavior supports contract thinking"),
        edge("e45", "g4", "g5", "inferred: interfaces make data implementations discussable", "2"),
        edge("e56", "g5", "g6", "documented: data abstraction precedes search/order"),
        edge("e67", "g6", "g7", "inferred: tested model supplies GUI state", "2"),
        edge("e78", "g7", "g8", "documented: project evidence continues into story"),
        edge("proof1", "evidence", "g1", "recurs: proof of each claim", "2"),
        edge("proof2", "evidence", "g4", "recurs: contract test", "2"),
        edge("proof3", "evidence", "g8", "recurs: reproducible evidence and limits", "2"),
        edge("src1", "src-sequence", "spine", "source"),
        edge("src2", "src-plans", "g1", "source"),
        edge("src3", "src-gates", "g6", "source"),
        edge("src4", "src-lesson", "g7", "source"),
        edge("src5", "src-test", "evidence", "source"),
    ]
    return {"nodes": nodes, "edges": edges}


def validate(canvas: dict) -> None:
    ids = [n["id"] for n in canvas["nodes"]]
    assert len(ids) == len(set(ids)), "duplicate node IDs"
    known = set(ids)
    for item in canvas["edges"]:
        assert item["fromNode"] in known and item["toNode"] in known, item["id"]
    for node in canvas["nodes"]:
        if node["type"] == "file":
            assert (ROOT / node["file"]).is_file(), node["file"]
    json.dumps(canvas)


if __name__ == "__main__":
    result = build()
    validate(result)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(result['nodes'])} nodes, {len(result['edges'])} edges)")
