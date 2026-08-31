#!/usr/bin/env python3
"""Additive, bounded Canvas deploy for the Week 2 hardware-confidence opening.

Adds a lecture page, a slide file, and a walkthrough page to the front of
the live "CS2 Week 2 -- Found Your World (World Bible v0.1)" module
(course 74031, module 218887), then repositions the existing World Bible
page after them. Does not touch any other module, assignment, grade,
submission, or enrollment. Uses harbor's raw Canvas primitives directly
(the full course_foundry/imprint Savnac reconcile pipeline is not available
on this checkout -- `imprint` has no local clone here -- and this change is
explicitly bounded/additive, not a full desired-state rebuild).

Usage: python3 scripts/deploy_week2_hardware_confidence.py
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SIBLING_ROOT = ROOT.parent
for name in ("harbor",):
    p = SIBLING_ROOT / name
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from harbor.api import (  # type: ignore
    create_module_item,
    create_page,
    get_module_items,
    update_module_item,
    upload_course_file,
)
from harbor.client import CanvasClient  # type: ignore
from harbor.config import CanvasConfig, load_env, read_canvas_config  # type: ignore

COURSE_ID = 74031
MODULE_ID = 218887
WORLD_BIBLE_ITEM_ID = 1529982
SLIDE_PDF = ROOT / "presentations/beamer/week02_hardware_confidence/hardware-confidence.pdf"
RECEIPT_PATH = ROOT / "sidecar/runs/week2_hardware_confidence_deploy.json"

LECTURE_MD = ROOT / "lessons/week-02-hardware-confidence.md"
WALKTHROUGH_MD = ROOT / "lessons/week-02-hardware-confidence-walkthrough.md"

COMMONS_AIDER_DAYS_URL = "https://swosu.instructure.com/courses/24298/modules/219031"


def _client() -> CanvasClient:
    load_env()
    config = read_canvas_config(enforce_course_allowlist=False)
    return CanvasClient(CanvasConfig(config.api_base_url, config.api_token, frozenset({COURSE_ID})))


def _lecture_html() -> str:
    return """
<h2>Week 2 opening — Your computer is more powerful than you think</h2>

<h3>The reframe</h3>
<p>Do not ask: <strong>&ldquo;Can my computer run AI?&rdquo;</strong> Ask: <strong>&ldquo;What AI can my computer run well?&rdquo;</strong></p>
<p>Every AI-assisted task in this course sits at the intersection of five variables:</p>
<ul>
<li><strong>Hardware</strong> — what you can run at all</li>
<li><strong>Model</strong> — what the loaded model is actually good at</li>
<li><strong>Task size</strong> — how much you asked for in one request</li>
<li><strong>Context</strong> — how much surrounding code or text the model has to hold</li>
<li><strong>Verification</strong> — how you will know whether the answer was right</li>
</ul>
<p>A larger model does not rescue a task that is too big, too vague, or unverified. The machine is powerful. <strong>You are the multiplier.</strong> Slogan for the semester: <strong>love AI more, trust AI less.</strong></p>

<h3>Hardware vocabulary, at a useful level</h3>
<ul>
<li><strong>CPU</strong> — general-purpose processor; always present; fine for small models and for orchestrating tools like Aider</li>
<li><strong>RAM</strong> — system memory; a model that will not fit in RAM cannot run on CPU alone</li>
<li><strong>GPU</strong> — a processor built for the parallel math models need</li>
<li><strong>VRAM</strong> — memory on the GPU itself; usually the real ceiling on which model sizes are practical, not raw GPU speed</li>
<li><strong>Quantization</strong> — compressing a model's numbers so it fits in less VRAM, at a small and usually acceptable cost in answer quality</li>
</ul>
<p>&ldquo;It runs&rdquo; and &ldquo;it runs usefully&rdquo; are different claims.</p>

<h3>Small models can be excellent at bounded work</h3>
<p>A small local model asked to make one narrow, well-specified change to one file — and checked against a real test — is a reliable tool. The goal is <strong>the smallest sufficient model for the bite</strong>, not the largest model you can technically load. A larger model does not fix an underspecified or oversized request.</p>

<h3>Local versus remote inference</h3>
<p>Both are legitimate architecture choices, not a hierarchy:</p>
<ul>
<li><strong>Local inference</strong> — the model runs on your own machine: private, works offline, bounded by your hardware</li>
<li><strong>Remote inference</strong> — your machine is a <strong>cockpit</strong> that sends the request to a model running elsewhere and receives the result over the network</li>
</ul>
<p>A tablet or other nontraditional device is not disqualified from this course — it is a cockpit. It may run a small model locally when practical, or connect to a remote Linux/model environment when that is the stronger architecture. This course does not promise unsupported native Aider behavior on iPadOS or similar platforms.</p>
<p>Your hardware determines your <strong>starting point</strong>, not your ceiling, as a programmer.</p>

<h3>The Bite Ladder</h3>
<ol>
<li>Give the model one small, bounded task</li>
<li>Inspect the diff — read every changed line</li>
<li>Run an independent test, not the model's own claim about itself</li>
<li>If it held, take one rung up: a slightly larger task or more context</li>
<li>If it broke, that is your current boundary — back off a rung</li>
</ol>

<h3>The course loop</h3>
<p><code>GOAL -&gt; BASELINE -&gt; AIDER -&gt; DIFF -&gt; PROOF -&gt; COMMIT</code></p>
<p>State the goal. See the failing baseline. Let Aider propose a bounded change. Read the diff. Run independent proof. Commit only what verified.</p>
<p><code>small model -&gt; small bite -&gt; inspect diff -&gt; test -&gt; trust earned</code></p>
<p>Model output is a proposal. The diff you actually read and the test you actually ran are verified software-engineering evidence.</p>

<h3>Where the technical setup lives</h3>
<p>This page is the concept and confidence layer. The exact install/verify steps live in the shared <a href="https://swosu.instructure.com/courses/24298/modules/218816">Computing Commons Week 2 — Build and Verify Local AI</a> road, so the same verified instructions serve every course. See the Week 2 walkthrough (next in this module) for the exact sequence.</p>

<h3>What this is not</h3>
<p>This is not a hardware-engineering lecture, and it is not a conversion of CS2 into an AI course. Local AI here is an engineering instrument used to make repository work, verification, and model boundaries visible. The Reasoning Odyssey / World Bible work below continues alongside this opening, not instead of it.</p>
""".strip()


def _walkthrough_html() -> str:
    return f"""
<h2>Week 2 walkthrough — How to get started</h2>
<p>This is the <strong>how</strong>, not the <strong>why</strong> — see the Hardware Confidence + Small Models page (previous in this module) for the concepts this walkthrough assumes. It does not repeat installation steps Computing Commons already owns as the shared, verified route.</p>

<h3>The sequence</h3>
<ol>
<li><strong>Inventory what you have.</strong> CPU, RAM, GPU/VRAM if present, and whether the machine is a managed lab machine or your own device.</li>
<li><strong>Choose your path.</strong> Managed CS lab machine, your own machine, or a cockpit device connecting to a remote environment.</li>
<li><strong>Reach the canonical Local AI setup/verification road:</strong> <a href="https://swosu.instructure.com/courses/24298/modules/218816">Computing Commons &rarr; 02 — Week 2: Build and Verify Local AI</a>. That module is the shared, verified sequence for installing and confirming Ollama, the approved model, and Aider.</li>
<li><strong>Prove a model can answer</strong> — locally through Ollama, or through the approved remote/cockpit architecture. This is the <code>BASELINE</code> step.</li>
<li><strong>Run one tiny bounded Aider task.</strong> Continue to the <a href="{COMMONS_AIDER_DAYS_URL}">Computing Commons Aider Days</a> road for the next bounded exercise and the Work First safe loop: one sentence, one bounded change, nothing else touched.</li>
<li><strong>Inspect the diff.</strong> Read every line Aider changed before you judge anything.</li>
<li><strong>Run independent proof.</strong> Run the supplied test yourself — a model claiming success is not evidence.</li>
<li><strong>Record what worked and where your confidence dropped.</strong> One or two honest sentences — the raw material for the Bite Ladder.</li>
</ol>

<h3>Next step</h3>
<p>Once you have completed the loop once, keep the World Bible work for this week moving in parallel — this walkthrough is the on-ramp, not a detour from it.</p>
""".strip()


def main() -> int:
    client = _client()

    before = get_module_items(client, COURSE_ID, MODULE_ID)

    _, lecture_page = create_page(
        client,
        COURSE_ID,
        {
            "wiki_page[title]": "Week 2 — Hardware Confidence + Small Models",
            "wiki_page[body]": _lecture_html(),
            "wiki_page[published]": "true",
        },
    )

    _, walkthrough_page = create_page(
        client,
        COURSE_ID,
        {
            "wiki_page[title]": "Week 2 — How to Get Started (Walkthrough)",
            "wiki_page[body]": _walkthrough_html(),
            "wiki_page[published]": "true",
        },
    )

    uploaded_file = upload_course_file(
        client,
        COURSE_ID,
        SLIDE_PDF,
        folder_path="slides/week_02_hardware_confidence",
        content_type="application/pdf",
    )

    _, lecture_item = create_module_item(
        client,
        COURSE_ID,
        MODULE_ID,
        {
            "module_item[title]": "Week 2 — Hardware Confidence + Small Models",
            "module_item[type]": "Page",
            "module_item[page_url]": lecture_page["url"],
            "module_item[position]": "1",
        },
    )

    _, slides_item = create_module_item(
        client,
        COURSE_ID,
        MODULE_ID,
        {
            "module_item[title]": "Slides — Hardware Confidence, Small Models, and the Bite Ladder",
            "module_item[type]": "File",
            "module_item[content_id]": str(uploaded_file["id"]),
            "module_item[position]": "2",
        },
    )

    _, walkthrough_item = create_module_item(
        client,
        COURSE_ID,
        MODULE_ID,
        {
            "module_item[title]": "Walkthrough — How to Get Started",
            "module_item[type]": "Page",
            "module_item[page_url]": walkthrough_page["url"],
            "module_item[position]": "3",
        },
    )

    _, aider_link_item = create_module_item(
        client,
        COURSE_ID,
        MODULE_ID,
        {
            "module_item[title]": "Next: Computing Commons Aider Days (Local AI)",
            "module_item[type]": "ExternalUrl",
            "module_item[external_url]": COMMONS_AIDER_DAYS_URL,
            "module_item[new_tab]": "true",
            "module_item[position]": "4",
        },
    )

    _, world_bible_item = update_module_item(
        client,
        COURSE_ID,
        MODULE_ID,
        WORLD_BIBLE_ITEM_ID,
        {"module_item[position]": "5"},
    )

    after = get_module_items(client, COURSE_ID, MODULE_ID)

    receipt = {
        "course_id": COURSE_ID,
        "module_id": MODULE_ID,
        "before_items": [{"id": i["id"], "position": i["position"], "title": i["title"]} for i in before],
        "after_items": [{"id": i["id"], "position": i["position"], "title": i["title"]} for i in after],
        "created": {
            "lecture_page_url": lecture_page["url"],
            "walkthrough_page_url": walkthrough_page["url"],
            "uploaded_file_id": uploaded_file["id"],
            "uploaded_file_display_name": uploaded_file.get("display_name"),
            "lecture_item_id": lecture_item["id"],
            "slides_item_id": slides_item["id"],
            "walkthrough_item_id": walkthrough_item["id"],
            "aider_link_item_id": aider_link_item["id"],
            "world_bible_item_new_position": world_bible_item["position"],
        },
    }
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2))
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
