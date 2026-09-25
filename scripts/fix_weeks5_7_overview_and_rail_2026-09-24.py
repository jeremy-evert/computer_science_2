#!/usr/bin/env python3
"""CS2 (74031) overview-page + week-rail fix, weeks 5-17. Anna, 2026-09-24.

Confirmed live (superseding the investigation fork's Part A draft, which
assumed page bodies already matched their own slugs -- they don't, for
weeks 7-14; see sidecar/reports/weeks7_17_overview_diff_and_duedate_audit_2026-09-24.md
and the corrected finding recorded in this run's own evidence file):

Two independent off-by-one bugs exist and mostly cancel out:
  1. Each week-N module's "Overview" item links to page-slug (N-1), not N.
  2. Each overview page-slug N's own body actually holds week (N+1)'s real
     content (for N=7..14) -- confirmed by reading every page body against
     planning/week-NN.md, not assumed from the slug name.
Combined: modules for weeks 8-15(checkpoint) already show CORRECT content
today (module N -> slug N-1 -> body is genuinely week N's topic). Only
weeks 5, 6, and 7 are actually broken live:
  - Week 5's module links to a duplicate of Week 4's page.
  - Week 6's module still links to Week 5's page -- the 2026-09-21/22 hand
    fix rewrote slug cs2-week-06-overview-5's BODY to real Week 6 content,
    but nobody repointed the MODULE LINK to it, so that fix was never
    actually visible to students.
  - Week 7's real content ("Contract and Swap") no longer exists anywhere
    live -- it was overwritten by the Week 6 hand fix -- so a NEW page is
    authored fresh from planning/week-07.md + assignments/odyssey_gates/week-07.md
    and linked in.

Separately, the course FRONT PAGE's "week rail" nav (a static nav baked
into the front page body, distinct from the per-module Overview links)
naively links week-N's chip to slug cs2-week-0N-overview-* for N=7..17,
with NO cancellation (it's a single direct link, not module->slug->body).
That makes the rail wrong for weeks 7-15 today, including Week 15's chip
pointing at the "buffer" page instead of the real Week-15 checkpoint
content. This script also repoints the rail.

Canonical corrected mapping (week -> the page slug that ACTUALLY holds
that week's real content, live-verified 2026-09-24):
  5: cs2-week-05-overview-5        (already correct body)
  6: cs2-week-06-overview-5        (already correct body, hand-fixed)
  7: <new page, created by this script on first --live run>
  8: cs2-week-07-overview-5        (body is genuinely Week 8 content)
  9: cs2-week-08-overview-5
  10: cs2-week-09-overview-4
  11: cs2-week-10-overview-4
  12: cs2-week-11-overview-4
  13: cs2-week-12-overview-5
  14: cs2-week-13-overview-4
  15: cs2-week-14-overview-5       (Checkpoint 3 content; the separate
                                     "Buffer" module/page 218900 /
                                     cs2-week-15-overview-3 is left as-is --
                                     legitimate secondary pacing content,
                                     not a content bug; see audit report)
  16: cs2-week-16-overview-5       (already correct)
  17: cs2-week-17-overview-4       (already correct)

Weeks 1-4 and the Week-15-buffer page are NOT touched by this script --
already correct or out of scope.

Idempotent: every write is guarded by a live read that only acts when the
current state differs from target; a second run reports all no-ops.
Default is --dry-run; --live is required to write. The Week 7 page is
created at most once (guarded by checking get_page for the known slug
this script recorded on its own first live run, stored in
WEEK7_PAGE_SLUG_FILE).
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path.home() / "git" / "harbor"))
from harbor import api
from harbor.client import CanvasClient
from harbor.config import load_env, read_canvas_config, CanvasConfig

COURSE_ID = 74031
BACKUP_DIR = Path.home() / "git" / "computer_science_2" / "sidecar" / "reports"
EVIDENCE = BACKUP_DIR / "fix_weeks5_7_overview_and_rail_run_2026-09-24.md"
WEEK7_PAGE_SLUG_FILE = BACKUP_DIR / "week7_page_slug.txt"

WEEK7_BODY = (
    '<h2>Reasoning Odyssey Gate -- Week 7 -- Contract and Swap (S03/S08)</h2>'
    '<p><strong>What are we learning?</strong> Make one collaborator promise explicit -- a contract -- using <code>abc.ABC</code> and an abstract method, then swap two conforming collaborators in a focused contract test. <code>typing.Protocol</code> is an optional comparison, not required.</p>'
    "<p><strong>What am I building/changing?</strong> This is your first checkpoint (40 points) -- pause and look back across Weeks 4-6 at what your world's growing system actually depends on right now. Pick one of those dependencies and turn it into an explicit contract: define a collaborator promise, use an ABC/abstract method as an explicit example, and swap two conforming collaborators in a focused contract test.</p>"
    '<p><strong>How does my world connect?</strong> This is the same <code>unittest</code> habit from Weeks 4-6, now proving the contract holds regardless of which concrete collaborator is plugged in. Explain the caller boundary clearly.</p>'
    '<p><strong>What evidence do I keep?</strong> One concise World Bible entry: what changed, what evidence you used, and any remaining debt. This is a small growth gate, not a weekly mini-project.</p>'
    '<p><strong>What exactly do I turn in?</strong> The <a href="https://swosu.instructure.com/courses/74031/assignments/914178" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74031/api/v1/courses/74031/assignments/914178" data-api-returntype="Assignment">Week 7 checkpoint assignment</a> -- your working baby project, contract test, explanation, demonstration, reflection, and World Bible entry. 40 points; Reasoning Odyssey checkpoints (15% group).</p>'
    "<p><strong>What carries forward?</strong> Week 8 asks you to choose a real List ADT, stack, or queue flow from your world's actual process and demonstrate world-fit data abstraction.</p>"
)

# module_id -> (item_id of its Page-type Overview item, target page_url)
MODULE_OVERVIEW_FIXES = {
    218889: {"item_id": 1530010, "target": "cs2-week-05-overview-5"},   # Week 5
    218890: {"item_id": 1530011, "target": "cs2-week-06-overview-5"},   # Week 6
    218891: {"item_id": 1530012, "target": None},                       # Week 7 -- filled from WEEK7_PAGE_SLUG_FILE
}

# canonical week -> slug map for the front-page rail (week 7 filled at runtime)
RAIL_MAP = {
    7: None,
    8: "cs2-week-07-overview-5",
    9: "cs2-week-08-overview-5",
    10: "cs2-week-09-overview-4",
    11: "cs2-week-10-overview-4",
    12: "cs2-week-11-overview-4",
    13: "cs2-week-12-overview-5",
    14: "cs2-week-13-overview-4",
    15: "cs2-week-14-overview-5",
}


def die(msg):
    print("STOP:", msg)
    sys.exit(2)


def log_evidence(lines):
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    with EVIDENCE.open("a") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Actually write. Default is dry-run.")
    args = ap.parse_args()

    load_env()
    cfg = read_canvas_config(enforce_course_allowlist=True)
    cfg = CanvasConfig(cfg.api_base_url, cfg.api_token, frozenset({COURSE_ID}))
    client = CanvasClient(cfg)

    course = client.get(f"/api/v1/courses/{COURSE_ID}").json()
    if course.get("id") != COURSE_ID:
        die("course identity mismatch: %r" % course.get("name"))

    ev = ["", "## fix_weeks5_7_overview_and_rail -- %s UTC -- %s" %
          (time.strftime("%Y-%m-%dT%H:%M:%S"), "LIVE" if args.live else "DRY-RUN")]
    ev.append("- course: %s / %s" % (course["id"], course["name"]))

    # Step 1: ensure the Week 7 page exists (create once, idempotent via slug file)
    week7_slug = None
    if WEEK7_PAGE_SLUG_FILE.exists():
        week7_slug = WEEK7_PAGE_SLUG_FILE.read_text().strip()
        status, p = api.get_page(client, COURSE_ID, week7_slug)
        if p.get("body") != WEEK7_BODY:
            die(f"existing Week 7 page {week7_slug!r} body no longer matches expected content -- investigate before continuing")
        ev.append(f"- Week 7 page already exists at {week7_slug!r}, no-op")
    else:
        if args.live:
            status, p = api.create_page(client, COURSE_ID, {
                "wiki_page[title]": "CS2 Week 07 -- Overview",
                "wiki_page[body]": WEEK7_BODY,
                "wiki_page[published]": True,
            })
            week7_slug = p["url"]
            WEEK7_PAGE_SLUG_FILE.write_text(week7_slug + "\n")
            ev.append(f"- created Week 7 page at slug {week7_slug!r} (status {status})")
        else:
            week7_slug = "cs2-week-07-overview-PENDING"
            ev.append("- [DRY-RUN] would create new Week 7 page from source (planning/week-07.md + odyssey_gates/week-07.md)")

    MODULE_OVERVIEW_FIXES[218891]["target"] = week7_slug
    RAIL_MAP[7] = week7_slug

    # Step 2: repoint module overview items for weeks 5, 6, 7
    for module_id, fix in MODULE_OVERVIEW_FIXES.items():
        items = api.get_module_items(client, COURSE_ID, module_id)
        item = next((i for i in items if i["id"] == fix["item_id"]), None)
        if item is None:
            ev.append(f"- SKIP module {module_id}: item {fix['item_id']} not found")
            continue
        current = item.get("page_url")
        target = fix["target"]
        if current == target:
            ev.append(f"- module {module_id} item {fix['item_id']}: already {target!r}, no-op")
            continue
        ev.append(f"- module {module_id} item {fix['item_id']}: {current!r} -> {target!r}"
                   + ("" if args.live else " [DRY-RUN]"))
        if args.live:
            api.update_module_item(client, COURSE_ID, module_id, fix["item_id"],
                                    {"module_item[page_url]": target})
            readback = api.get_module_items(client, COURSE_ID, module_id)
            rb = next((i for i in readback if i["id"] == fix["item_id"]), None)
            ev.append(f"  readback page_url={rb.get('page_url') if rb else 'MISSING'}")

    # Step 3: repoint the front-page week-rail chips for weeks 7-15
    fp = client.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
    body = fp["body"]
    page_url = fp["url"]
    changed = False
    for week, target_slug in RAIL_MAP.items():
        if target_slug is None or target_slug == "cs2-week-07-overview-PENDING":
            continue
        pattern = re.compile(
            r'(href="https://swosu\.instructure\.com/courses/74031/pages/)([a-z0-9\-]+)("\s+title="Week %d")' % week
        )
        m = pattern.search(body)
        if not m:
            ev.append(f"- rail week {week}: chip pattern not found (already changed or current-week no-link chip) -- skip")
            continue
        current_slug = m.group(2)
        if current_slug == target_slug:
            ev.append(f"- rail week {week}: already {target_slug!r}, no-op")
            continue
        ev.append(f"- rail week {week}: {current_slug!r} -> {target_slug!r}" + ("" if args.live else " [DRY-RUN]"))
        new_href = m.group(1) + target_slug + m.group(3)
        # also fix the data-api-endpoint on the same chip
        body = body[:m.start()] + new_href + body[m.end():]
        # fix data-api-endpoint separately (same slug substitution nearby)
        endpoint_pattern = re.compile(
            r'(data-api-endpoint="https://swosu\.instructure\.com/api/v1/courses/74031/pages/)%s(")' % re.escape(current_slug)
        )
        body = endpoint_pattern.sub(lambda mm: mm.group(1) + target_slug + mm.group(2), body, count=1)
        changed = True

    if changed:
        if args.live:
            status, _ = api.update_page(client, COURSE_ID, page_url, {"wiki_page[body]": body})
            fp_after = client.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
            ev.append(f"- front page updated (status {status}); readback body len {len(fp_after.get('body') or '')}")
            for week, target_slug in RAIL_MAP.items():
                if target_slug and target_slug != "cs2-week-07-overview-PENDING" and target_slug not in (fp_after.get("body") or ""):
                    ev.append(f"  WARNING: week {week} target {target_slug!r} not found in readback body")
        else:
            ev.append("- [DRY-RUN] front page rail would be updated (see diffs above)")
    else:
        ev.append("- front page rail: no changes needed")

    log_evidence(ev)


if __name__ == "__main__":
    main()
