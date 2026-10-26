#!/usr/bin/env python3
"""Additive, idempotent Canvas deploy: Week 11 micro-lab part 2, "The Story of Big O".

Course 74031 (id AND name verified), module 218895. Uploads the story harness files and the
deck PDF, creates one Page and its module item, and appends one link paragraph to the
part-1 micro-lab page (our own page). Backs up the module and both pages first.
Usage: python3 scripts/deploy_week11_bigo_story.py [--dry-run]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for _p in (ROOT.parent / "harbor", Path.home() / "git" / "harbor"):
    if _p.is_dir():
        sys.path.insert(0, str(_p)); break

from harbor.api import (  # type: ignore
    create_module_item, create_page, get_course, get_module_items, get_page,
    update_page, upload_course_file,
)
from harbor.client import CanvasClient  # type: ignore
from harbor.config import CanvasConfig, load_env, read_canvas_config  # type: ignore

COURSE_ID, MODULE_ID = 74031, 218895
COURSE_NAME = "Fall 2026 Computer Science II (COMSC-1053-1417)"
PART1_SLUG = "cs2-week-11-optional-micro-lab-benchmark-and-tell-the-story"
PAGE_TITLE = "CS2 Week 11 -- Optional Micro-Lab Part 2: The Story of Big O"
TOPIC_ID = 547375
CODE = ROOT / "lessons/code/week11_benchmark"
DECK = ROOT / "presentations/beamer/week11_bigo_story/week11_bigo_story.pdf"
FILES = [(CODE / "instrumented.py", "text/x-python"), (CODE / "count_and_time.py", "text/x-python"),
         (CODE / "story_charts.py", "text/x-python"), (CODE / "story_sample.csv", "text/csv"),
         (DECK, "application/pdf")]
FOLDER = "week_11/benchmark_microlab"
BACKUP = ROOT / "sidecar/reports/backup_2026-10-26_pre_week11_bigo_story.json"
RECEIPT = ROOT / "sidecar/reports/week11_bigo_story_deploy_receipt.json"
MARK = "<!-- part2-link -->"


def client() -> CanvasClient:
    load_env()
    cfg = read_canvas_config(enforce_course_allowlist=False)
    return CanvasClient(CanvasConfig(cfg.api_base_url, cfg.api_token, frozenset({COURSE_ID})))


def page_html(L: dict) -> str:
    a = lambda n: f'<a href="{L[n]}">{n}</a>'
    return f"""
<h2>Optional micro-lab, part 2: the story of Big O</h2>
<p><strong>Optional and experimental.</strong> Same Week 11 gate (question, visual, rationale, limitation,
evidence). This time we visualize the <em>process</em>, not just the result. You know bubble sort ends at
n&sup2;. Here is how it begins, and how to check the claim with evidence.</p>
<p>Deck: {a('week11_bigo_story.pdf')} (15 slides: annotated code, counters, graphs, the pitfall).</p>
<h3>The story arc</h3>
<ol>
<li><strong>Naive code</strong> &rarr; read the simple bubble sort.</li>
<li><strong>Highlight the drivers</strong> &rarr; two nested loops plus compare and swap; derive n(n&minus;1)/2.</li>
<li><strong>Mark what Big O ignores</strong> &rarr; copying, <code>len()</code>, per-pass reset, the flag.</li>
<li><strong>Count</strong> &rarr; an instrumented sort counts passes, inner trips, comparisons, swaps, index reads/writes, flag sets, bookkeeping.</li>
<li><strong>Graph it</strong> &rarr; operations vs n and wall-clock vs n, log and linear, with a fitted exponent.</li>
<li><strong>Was ignoring them right?</strong> &rarr; lower-order terms fade toward 0% of the work; constants stay a fixed share (they change speed, not shape).</li>
<li><strong>Bigger n</strong> &rarr; fit on small n, check on large n.</li>
<li><strong>Another CPU</strong> &rarr; operation counts are identical on every machine; time is not.</li>
<li><strong>Better algorithm</strong> &rarr; early exit, insertion, merge sort (n log n): new curve, and a crossover.</li>
</ol>
<h3>Run it yourself</h3>
<p>Download into the <strong>same folder</strong> as the part-1 files (<code>benchmark.py</code> is needed too):
{a('instrumented.py')}, {a('count_and_time.py')}, {a('story_charts.py')}, and the example data {a('story_sample.csv')}.</p>
<pre>python count_and_time.py --quick        # seconds
python count_and_time.py                # about 20 seconds to a minute; writes story_&lt;host&gt;.csv
python -m pip install matplotlib        # once
python story_charts.py story_&lt;host&gt;.csv --outdir story_charts
python story_charts.py story_&lt;host&gt;.csv friend.csv --outdir story_charts   # adds the hardware chart</pre>
<p>Counting slows a program down, so time is always measured on an uncounted copy of each sort.</p>
<h3>Your story</h3>
<p>Pick one question the data can answer, one chart, say why those axes, name a limitation (one run, one machine,
noisy tiny n), and include the misleading alternative (<code>S12_PITFALL_truncated_axis.png</code>) with one sentence on what it
hides. Share in <a href="/courses/{COURSE_ID}/discussion_topics/{TOPIC_ID}">the discussion</a> with your platform line.</p>
"""


def main() -> None:
    dry = "--dry-run" in sys.argv
    cl = client()
    status, course = get_course(cl, COURSE_ID)
    assert status == 200 and course["id"] == COURSE_ID and course["name"] == COURSE_NAME
    items = get_module_items(cl, COURSE_ID, MODULE_ID)
    _, part1 = get_page(cl, COURSE_ID, PART1_SLUG)
    BACKUP.write_text(json.dumps({"module_items": items, "part1_page": part1}, indent=1), encoding="utf-8")
    print("backup ok", len(items), "items")
    if dry:
        return
    L = {}
    for path, ctype in FILES:
        up = upload_course_file(cl, COURSE_ID, path, folder_path=FOLDER, content_type=ctype, on_duplicate="overwrite")
        assert up["size"] == path.stat().st_size, path.name
        L[path.name] = f"/courses/{COURSE_ID}/files/{up['id']}/download?download_frd=1"
    html = page_html(L)
    slug = next((i["page_url"] for i in items if i.get("title") == PAGE_TITLE), None)
    if slug:
        _, pg = update_page(cl, COURSE_ID, slug, {"wiki_page[body]": html})
    else:
        _, pg = create_page(cl, COURSE_ID, {"wiki_page[title]": PAGE_TITLE, "wiki_page[body]": html,
                                            "wiki_page[published]": "true"})
        create_module_item(cl, COURSE_ID, MODULE_ID, {
            "module_item[title]": PAGE_TITLE, "module_item[type]": "Page",
            "module_item[page_url]": pg["url"], "module_item[position]": 3})
    body = part1["body"]
    if MARK not in body:
        link = (f'{MARK}<p><strong>Part 2:</strong> <a href="/courses/{COURSE_ID}/pages/{pg["url"]}">'
                f'The Story of Big O</a> &mdash; count what the sort actually does, graph it, and compare algorithms.</p>')
        update_page(cl, COURSE_ID, PART1_SLUG, {"wiki_page[body]": body + link})
    RECEIPT.write_text(json.dumps({"page_url": pg["url"], "files": L}, indent=1), encoding="utf-8")
    print("page:", pg["url"])


if __name__ == "__main__":
    main()
