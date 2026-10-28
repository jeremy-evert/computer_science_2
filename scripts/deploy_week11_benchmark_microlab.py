#!/usr/bin/env python3
"""Additive, idempotent Canvas deploy for the optional Week 11 benchmark micro-lab.

Course 74031 (identity verified by id AND name before any write). Adds, to
module 218895 ("CS2 Week 11 -- Honest Visualization from Project Data"):
  - 3 course files (benchmark.py, plot_benchmark.py, sample_results.csv)
  - one Page "CS2 Week 11 -- Optional Micro-Lab: Benchmark and Tell the Story"
  - one ungraded discussion for sharing results
  - module items for the page and the discussion, after the Overview
Never touches the existing Overview, the Odyssey Gate assignment, grades,
submissions, enrollments, or navigation. Backs up the module and Overview first.

Usage: python3 scripts/deploy_week11_benchmark_microlab.py [--dry-run]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for _p in (ROOT.parent / "harbor", Path.home() / "git" / "harbor"):
    if _p.is_dir():
        sys.path.insert(0, str(_p))
        break

from harbor.api import (  # type: ignore
    create_module_item, create_page, get_course, get_module_items,
    get_page, list_course_files, update_page, upload_course_file,
)
from harbor.client import CanvasClient  # type: ignore
from harbor.config import CanvasConfig, load_env, read_canvas_config  # type: ignore

COURSE_ID = 74031
COURSE_NAME = "Fall 2026 Computer Science II (COMSC-1053-1417)"
MODULE_ID = 218895
OVERVIEW_SLUG = "cs2-week-11-overview-5"
PAGE_TITLE = "CS2 Week 11 -- Optional Micro-Lab: Benchmark and Tell the Story"
TOPIC_TITLE = "Week 11 optional micro-lab: share your benchmark chart"
CODE = ROOT / "lessons/code/week11_benchmark"
FILES = [("benchmark.py", "text/x-python"), ("plot_benchmark.py", "text/x-python"),
         ("sample_results.csv", "text/csv")]
FOLDER = "week_11/benchmark_microlab"
BACKUP = ROOT / "sidecar/reports/backup_2026-10-26_pre_week11_microlab.json"
RECEIPT = ROOT / "sidecar/reports/week11_benchmark_microlab_deploy_receipt.json"


def client() -> CanvasClient:
    load_env()
    cfg = read_canvas_config(enforce_course_allowlist=False)
    return CanvasClient(CanvasConfig(cfg.api_base_url, cfg.api_token, frozenset({COURSE_ID})))


def page_html(links: dict, topic_url: str) -> str:
    def a(name):
        return f'<a href="{links[name]}">{name}</a>'
    return f"""
<h2>Optional micro-lab: benchmark sorting and searching, then tell the story</h2>
<p><strong>Optional and experimental.</strong> The required Week 11 work is unchanged:
<em>Honest Visualization from Project Data</em> and its Reasoning Odyssey gate. This is a
ready-made dataset you may use for the same gate if your own project data is thin, or just
to see your own machine's numbers.</p>
<h3>The idea</h3>
<p>Week 9 said bubble sort grows like n&sup2; and Python's sort is fast. Measure it on
<strong>your</strong> machine (Windows, WSL, Linux, or Mac) and decide what a reader should believe.
Different machines give different numbers. Is the <em>story</em> the same?</p>
<h3>Run it (1&ndash;2 minutes)</h3>
<p>Download: {a('benchmark.py')}, {a('plot_benchmark.py')}, and {a('sample_results.csv')}
(an example run, so you can try the charts first). Put them in one folder, then:</p>
<pre>python benchmark.py --quick          # a few seconds, sanity check
python benchmark.py                  # full run, writes results_&lt;your-host&gt;.csv
python -m pip install matplotlib     # once, if needed
python plot_benchmark.py results_&lt;your-host&gt;.csv --outdir charts</pre>
<p>On Windows use <code>py -3</code> if <code>python</code> is not found; on WSL/Linux/Mac use <code>python3</code>.
Each CSV row carries a platform fingerprint (OS, Python version, CPU count). No username goes inside the file;
the hostname is only in the file <em>name</em>, so rename it before sharing if you like.</p>
<p>It times bubble, insertion, merge, and built-in <code>sorted</code>, plus linear, binary, and library
<code>bisect</code> search, over several list sizes and orderings. Times are best-of-several using
<code>time.perf_counter()</code>.</p>
<h3>The story to tell (fits the Week 11 gate)</h3>
<ul>
<li><strong>Question</strong> &mdash; one answerable question, e.g. &ldquo;How much faster is binary than linear search at 100,000 items on my machine?&rdquo;</li>
<li><strong>Visual</strong> &mdash; one labeled chart (axis labels with units, a title that states a claim, a legend).</li>
<li><strong>Rationale</strong> &mdash; why these axes. Log-log is honest here because growth rate is the point.</li>
<li><strong>Limitation</strong> &mdash; one run, one machine, background programs, best-of-N timing, capped n; built-in <code>sorted</code> is C code, the others are Python. Claim no cause you did not test.</li>
<li><strong>Evidence</strong> &mdash; your CSV, the command you ran, and <code>3_PITFALL_linear_axis.png</code> named as the <strong>misleading alternative</strong> with one sentence on what it hides.</li>
</ul>
<p>The harness ships the pitfall: the same data on linear axes from zero, where the two slow sorts set the scale and the fast ones are squashed against the bottom. Explain why chart 1 is the honest one.</p>
<h3>Share and compare</h3>
<p>Post your chart, a one-paragraph story, and your platform line in the discussion:
<a href="{topic_url}">{TOPIC_TITLE}</a>. Read at least two classmates' posts and compare what changed
between machines and what stayed the same. Post nothing private (no usernames, no paths with your name).</p>
<h3>Honest cautions</h3>
<ul>
<li>Timings are noisy. Close other programs; run twice if a number looks odd.</li>
<li>Compare the <em>same algorithm</em> across machines, not a hand-written sort against <code>sorted</code>.</li>
<li>&ldquo;Binary search was about 1,000x faster here at n = 100,000&rdquo; is a claim. &ldquo;Linux is faster than Windows&rdquo; is not.</li>
</ul>
"""


def main() -> None:
    dry = "--dry-run" in sys.argv
    cl = client()
    status, course = get_course(cl, COURSE_ID)
    assert status == 200 and course["id"] == COURSE_ID and course["name"] == COURSE_NAME, course.get("name")
    items = get_module_items(cl, COURSE_ID, MODULE_ID)
    _, overview = get_page(cl, COURSE_ID, OVERVIEW_SLUG)
    BACKUP.write_text(json.dumps({"module_items": items, "overview_page": overview}, indent=1), encoding="utf-8")
    print("backup:", BACKUP.name, len(items), "items")
    if dry:
        return
    links = {}
    existing = {f["display_name"]: f for f in list_course_files(cl, COURSE_ID)}
    for name, ctype in FILES:
        up = upload_course_file(cl, COURSE_ID, CODE / name, folder_path=FOLDER, content_type=ctype,
                                on_duplicate="overwrite")
        links[name] = f"/courses/{COURSE_ID}/files/{up['id']}/download?download_frd=1"
        assert up["size"] == (CODE / name).stat().st_size, name
    # discussion (ungraded) -- create if no topic with this title
    r = cl.get(f"/api/v1/courses/{COURSE_ID}/discussion_topics?per_page=100&search_term=Week%2011%20optional")
    topics = [t for t in r.json() if t["title"] == TOPIC_TITLE]
    if topics:
        topic = topics[0]
    else:
        r = cl.post(f"/api/v1/courses/{COURSE_ID}/discussion_topics", {
            "title": TOPIC_TITLE, "published": True, "discussion_type": "threaded",
            "message": "<p>Post your chart (PNG), a one-paragraph story (question, what the chart shows, "
                       "limitation), and your platform line: OS, Python version, CPU count. Then reply to at "
                       "least two classmates: what changed between machines, and what stayed the same? "
                       "Optional; no usernames or private paths.</p>"})
        r.raise_for_status(); topic = r.json()
    topic_url = f"/courses/{COURSE_ID}/discussion_topics/{topic['id']}"
    html = page_html(links, topic_url)
    slug = None
    for it in items:
        if it.get("title") == PAGE_TITLE:
            slug = it["page_url"]
    if slug:
        _, pg = update_page(cl, COURSE_ID, slug, {"wiki_page[body]": html})
    else:
        _, pg = create_page(cl, COURSE_ID, {"wiki_page[title]": PAGE_TITLE, "wiki_page[body]": html,
                                            "wiki_page[published]": "true"})
        create_module_item(cl, COURSE_ID, MODULE_ID, {
            "module_item[title]": PAGE_TITLE, "module_item[type]": "Page",
            "module_item[page_url]": pg["url"], "module_item[position]": 2})
    if not any(it.get("title") == TOPIC_TITLE for it in items):
        create_module_item(cl, COURSE_ID, MODULE_ID, {
            "module_item[title]": TOPIC_TITLE, "module_item[type]": "Discussion",
            "module_item[content_id]": str(topic["id"]), "module_item[position]": 3})
    RECEIPT.write_text(json.dumps({"page_url": pg["url"], "topic_id": topic["id"], "files": links}, indent=1),
                       encoding="utf-8")
    print("page:", pg["url"], "topic:", topic["id"])


if __name__ == "__main__":
    main()
