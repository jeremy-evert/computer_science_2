"""Generate and validate the Fall 2026 semester topic map.

Run from the repository root:
    python views/generate_semester_topic_map.py

The repository remains the source of truth. This script stores only a small
view specification and emits Obsidian's documented Canvas JSON format.

Layout rules (so the canvas is readable without scrolling or untangling):
  * Card height is computed from the wrapped text length, never fixed.
  * Cards sit in three phase columns, stacked in dependency order.
  * Edges join only neighbors in that order (vertical inside a column, one
    short hop between columns), so none can pass through an unrelated card.
  * validate() proves it: it fails if any edge line, edge bounding box, or
    edge label overlaps a card that is not one of its endpoints.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "views" / "semester-topic-map.canvas"

CARD_W = 340
COL_GAP = 280          # wide enough that a cross-column edge label fits in the gap
ROW_GAP = 100          # tall enough that a vertical edge label fits between cards
COLS = [i * (CARD_W + COL_GAP) for i in range(3)]
FULL_W = COLS[2] + CARD_W

CHAR_PX = 8.6          # conservative average glyph width
LINE_PX = 26           # wrapped body line
HEAD_PX = 38           # '#' heading line
PAD_PX = 44


def text_height(value: str, width: int) -> int:
    """Estimate rendered height from wrapped line count (errs tall, never short)."""
    chars_per_line = max(10, int((width - 40) / CHAR_PX))
    total = PAD_PX
    for line in value.split("\n"):
        if not line.strip():
            total += LINE_PX // 2
            continue
        wraps = max(1, math.ceil(len(line) / chars_per_line))
        total += wraps * (HEAD_PX if line.startswith("#") else LINE_PX)
    return total


def text(node_id: str, x: int, y: int, width: int, value: str) -> dict:
    return {"id": node_id, "type": "text", "text": value,
            "x": x, "y": y, "width": width, "height": text_height(value, width)}


SRC_W = 260


def file_node(node_id: str, x: int, y: int, path: str, label: str) -> dict:
    return {"id": node_id, "type": "file", "file": path,
            "x": x, "y": y, "width": SRC_W, "height": 110,
            "subpath": "", "label": label}


def edge(edge_id: str, source: str, target: str, label: str,
         from_side: str, to_side: str, color: str = "") -> dict:
    item = {"id": edge_id, "fromNode": source, "toNode": target,
            "fromSide": from_side, "toSide": to_side, "label": label}
    if color:
        item["color"] = color
    return item


TITLE = (
    "# Fall 2026 CS2 — Semester Topic Map\n\n"
    "Teaching story: earn a trustworthy boundary, then make it collaborate, substitute, swap, hold data, explain tradeoffs, respond to events, and tell an honest evidence-backed story.\n\n"
    "Arrows labeled documented follow the active sequence; arrows labeled inferred (orange) are instructional synthesis. Testing, documentation, AI accountability, and review recur throughout (S08)."
)
SPINE = (
    "## Progression\n"
    "Weeks 3–4 design → 5 substitution → 6 contracts → 7–8 data abstractions and search/order → 9 GUI/events → 10–11 visualization/storytelling. Recursion is an optional design lens when authentic.\n\n"
    "Source: docs/curriculum/course-sequence.md:15-22"
)
EVIDENCE = (
    "## Recurring proof loop (Weeks 2–15 · S08)\n"
    "Known baseline → bounded change → inspect diff/code → independent test or trace → explain limits → accept/reject and review. This loop applies to every card above; it is not an arrow because it recurs everywhere.\n\n"
    "Evidence: planning/week-02.md; docs/curriculum/course-sequence.md:22; later Odyssey gates."
)

# (id, phase column, card text) in dependency order within each column.
PHASES = [
    ("Phase 1 · Design a boundary", [
        ("g1", "## 1 · Earn a boundary\nWeeks 3–4 · S01\n\nWhy it matters: state and behavior should make a small promise that can be explained and tested. Predictions may be rejected.\n\nEvidence: planning/week-04.md; lessons/week-04-cohesive-object-boundary.md; assignments/odyssey_gates/week-04.md"),
        ("g2", "## 2 · Collaborate and protect\nWeek 4–5 · S01/S08\n\nWhy it matters: composition gives responsibilities a boundary; an invariant makes correctness observable.\n\nEvidence: lessons/week-04-composition-and-invariants.md; planning/week-05.md"),
        ("g3", "## 3 · Earn substitution\nWeek 6 · S02\n\nWhy it matters: inheritance is used only when a genuine is-a relationship gives shared operations different meaning.\n\nEvidence: planning/week-06.md; assignments/odyssey_gates/week-06.md; week_06/03_test_substitution.py"),
    ]),
    ("Phase 2 · Contracts and data", [
        ("g4", "## 4 · Make a contract swappable\nWeek 7 · S03/S08\n\nWhy it matters: a caller can depend on a promise while implementations change.\n\nEvidence: planning/week-07.md; assignments/odyssey_gates/week-07.md; week_07/week_07_contract_and_swap/"),
        ("g5", "## 5 · Choose a world-fit data shape\nWeek 8 · S05\n\nWhy it matters: list/stack/queue behavior becomes meaningful when chosen for a real process and proved with a trace or test.\n\nEvidence: planning/week-08.md; assignments/odyssey_gates/week-08.md"),
        ("g6", "## 6 · Explain lookup/order tradeoffs\nWeek 9 · S05/S06\n\nWhy it matters: algorithm choice follows domain need, maintenance cost, and preconditions; binary search is conditional.\n\nEvidence: planning/week-09.md; assignments/odyssey_gates/week-09.md; lessons/plotting-searching-sorting.md"),
    ]),
    ("Phase 3 · Events and story", [
        ("g7", "## 7 · Put a thin view over the model\nWeek 10 · S04\n\nWhy it matters: an event can change real model state without making the GUI the only proof.\n\nEvidence: planning/week-10.md; lessons/week-10-tkinter-model-view-lab.md; assignments/odyssey_gates/week-10.md"),
        ("g8", "## 8 · Turn project data into a story\nWeeks 11–12 · S09/S07\n\nWhy it matters: a question, readable representation, limitation, and decision make evidence useful; recursion/linked/nested design is optional when authentic.\n\nEvidence: planning/week-11.md; planning/week-12.md; lessons/week-11-data-storytelling-micro-lab.md; assignments/odyssey_gates/week-11.md and week-12.md"),
    ]),
]

SOURCES = [
    ("src-sequence", "docs/curriculum/course-sequence.md", "Active sequence"),
    ("src-plans", "planning/week-04.md", "Weekly plan example"),
    ("src-gates", "assignments/odyssey_gates/week-09.md", "Assessment gate example"),
    ("src-lesson", "lessons/week-10-tkinter-model-view-lab.md", "Lesson example"),
    ("src-test", "planning/week-02.md", "Evidence loop"),
]

# (id, from, to, label, color). Order inside a column is vertical; between
# columns it is one right→left hop from the last card to the next column's first.
LINKS = [
    ("e12", "g1", "g2", "documented: enables collaboration", ""),
    ("e23", "g2", "g3", "documented: is-a must be earned", ""),
    ("e34", "g3", "g4", "documented: shared behavior", ""),
    ("e45", "g4", "g5", "inferred: interfaces → data", "2"),
    ("e56", "g5", "g6", "documented: data before search/order", ""),
    ("e67", "g6", "g7", "inferred: model feeds GUI", "2"),
    ("e78", "g7", "g8", "documented: project → story", ""),
]


def build() -> dict:
    nodes = [text("title", 0, 0, FULL_W, TITLE)]
    y = nodes[-1]["height"] + ROW_GAP // 2
    nodes.append(text("spine", 0, y, FULL_W, SPINE))
    top = y + nodes[-1]["height"] + ROW_GAP

    bottoms = []
    for col, (phase, cards) in enumerate(PHASES):
        cy = top
        nodes.append(text(f"phase{col + 1}", COLS[col], cy, CARD_W, f"# {phase}"))
        cy += nodes[-1]["height"] + ROW_GAP // 2
        for node_id, body in cards:
            nodes.append(text(node_id, COLS[col], cy, CARD_W, body))
            cy += nodes[-1]["height"] + ROW_GAP
        bottoms.append(cy)

    ey = max(bottoms)
    nodes.append(text("evidence", 0, ey, FULL_W, EVIDENCE))
    sy = ey + nodes[-1]["height"] + ROW_GAP // 2
    step = (FULL_W - SRC_W) // (len(SOURCES) - 1)
    for i, (node_id, path, label) in enumerate(SOURCES):
        nodes.append(file_node(node_id, i * step, sy, path, label))

    column_of = {card[0]: c for c, (_, cards) in enumerate(PHASES) for card in cards}
    edges = []
    for edge_id, src, dst, label, color in LINKS:
        if column_of[src] == column_of[dst]:
            edges.append(edge(edge_id, src, dst, label, "bottom", "top", color))
        else:
            edges.append(edge(edge_id, src, dst, label, "right", "left", color))
    return {"nodes": nodes, "edges": edges}


def anchor(node: dict, side: str) -> tuple[float, float]:
    x, y, w, h = node["x"], node["y"], node["width"], node["height"]
    return {"left": (x, y + h / 2), "right": (x + w, y + h / 2),
            "top": (x + w / 2, y), "bottom": (x + w / 2, y + h)}[side]


def overlaps(rect: tuple[float, float, float, float], node: dict) -> bool:
    x0, y0, x1, y1 = rect
    return not (x1 <= node["x"] or x0 >= node["x"] + node["width"]
                or y1 <= node["y"] or y0 >= node["y"] + node["height"])


def segment_hits(p: tuple[float, float], q: tuple[float, float], node: dict) -> bool:
    """Sample the segment; True if any point lies strictly inside the node."""
    for i in range(1, 100):
        t = i / 100
        px, py = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        if (node["x"] < px < node["x"] + node["width"]
                and node["y"] < py < node["y"] + node["height"]):
            return True
    return False


def crossings(canvas: dict) -> list[str]:
    by_id = {n["id"]: n for n in canvas["nodes"]}
    problems = []
    for item in canvas["edges"]:
        a = anchor(by_id[item["fromNode"]], item["fromSide"])
        b = anchor(by_id[item["toNode"]], item["toSide"])
        # The line, and the box a curved edge stays inside, must avoid other cards.
        box = (min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1]))
        mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        lw = len(item.get("label", "")) * 8 + 24
        label_box = (mid[0] - lw / 2, mid[1] - 16, mid[0] + lw / 2, mid[1] + 16)
        for node in canvas["nodes"]:
            ends = node["id"] in (item["fromNode"], item["toNode"])
            if not ends and (segment_hits(a, b, node) or overlaps(box, node)):
                problems.append(f"edge {item['id']} crosses card {node['id']}")
            if overlaps(label_box, node):
                problems.append(f"label of {item['id']} overlaps card {node['id']}")
    return problems


def card_overlaps(canvas: dict) -> list[str]:
    nodes, problems = canvas["nodes"], []
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            if overlaps((a["x"], a["y"], a["x"] + a["width"], a["y"] + a["height"]), b):
                problems.append(f"cards {a['id']} and {b['id']} overlap")
    return problems


def validate(canvas: dict) -> None:
    ids = [n["id"] for n in canvas["nodes"]]
    assert len(ids) == len(set(ids)), "duplicate node IDs"
    known = set(ids)
    for item in canvas["edges"]:
        assert item["fromNode"] in known and item["toNode"] in known, item["id"]
    for node in canvas["nodes"]:
        if node["type"] == "file":
            assert (ROOT / node["file"]).is_file(), node["file"]
    found = crossings(canvas) + card_overlaps(canvas)
    assert not found, "layout problems:\n  " + "\n  ".join(found)
    json.dumps(canvas)


if __name__ == "__main__":
    result = build()
    validate(result)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(result['nodes'])} nodes, {len(result['edges'])} edges); "
          "0 edge/label crossings, 0 card overlaps")
