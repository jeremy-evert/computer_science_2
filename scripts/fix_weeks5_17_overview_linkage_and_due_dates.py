#!/usr/bin/env python3
"""CS2 (74031) two-part live fix, DRAFTED BY ANNA'S INVESTIGATION FORK 2026-09-24, NOT YET RUN LIVE.

Part A -- overview linkage repair (Weeks 5-15a). Live read confirmed: every
overview PAGE already has body content that matches its OWN slug/week number
(e.g. page `cs2-week-07-overview-5`'s body is genuinely Week 7's "World-Fit
Data Abstraction", matching planning/week-07.md). The bug is not corrupted
page content -- it's that each week N's module (N=5..15a) has its "Overview"
module item pointing at week (N-1)'s page instead of its own. Concretely,
page P(k) [correct Week k content] is currently the module item inside
module (k+1), not module (k). This script re-points each affected module's
overview module item to the page that actually matches that module's own
week (a `update_module_item` PUT changing page_url/content target -- no
page body is rewritten). Week 4's module already has its own correct page
and is untouched; Week 16/17 are already correct and untouched. Week 15's
two modules (218899 Checkpoint 3, 218900 Buffer, the flagged "duplicated
Week 15") both end up pointing at the one Week-15 page -- confirmed no
distinct "buffer" content exists in planning/week-15.md to lose.

Part B -- weekly-gate due dates. Sets `due_at` on each course's weekly gate
assignment to Friday 11:59pm America/Chicago, ONLY for assignments that
currently have due_at=None (never touches an assignment that already has a
due date -- that is the "don't retroactively re-date the past" rule). Dates
must be supplied explicitly per assignment id (WEEK_FRIDAYS below) -- derived
from each course's own already-dated weeks (empirically Saturday 04:59 UTC
during CDT / 05:59 UTC after the Nov 1 2026 DST change), not invented by
arithmetic alone; verify against source before filling WEEK_FRIDAYS in.

STATUS: MAPPING TABLES BELOW ARE INCOMPLETE SKELETONS. Anna/Flo must fill in
and verify OVERVIEW_MODULE_FIXES and WEEK_FRIDAYS from the evidence in
sidecar/reports/weeks7_17_overview_diff_and_duedate_audit_2026-09-24.md
before this is ever run with --live. Default is --dry-run; nothing writes
without both an explicit --live flag AND a non-empty mapping.
"""
import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path.home() / "git" / "harbor"))
from harbor import api
from harbor.client import CanvasClient
from harbor.config import load_env, read_canvas_config, CanvasConfig

COURSE_ID = 74031
BACKUP_DIR = Path.home() / "git" / "computer_science_2" / "sidecar" / "reports"
EVIDENCE = BACKUP_DIR / "fix_weeks5_17_overview_and_due_dates_run.md"

# module_id -> (item_id currently in that module, correct target page_url)
# Fill from the live probe before running --live. Example shape (VERIFY IDs
# before uncommenting/using -- these are from the 2026-09-24 read-only probe
# and must be re-read fresh at run time, not trusted stale):
OVERVIEW_MODULE_FIXES: dict[int, dict] = {
    # 218889: {"item_id": 1530010, "new_page_url": "cs2-week-05-overview-5"},   # Week 5 module
    # 218890: {"item_id": 1530011, "new_page_url": "cs2-week-06-overview-5"},   # Week 6 module
    # 218891: {"item_id": 1530012, "new_page_url": "cs2-week-07-overview-5"},   # Week 7 module
    # ... through 218899 (Week 15 Checkpoint 3) -> cs2-week-15-overview-3
}

# assignment_id -> due_at (UTC ISO8601), only for currently-due_at=None gates.
WEEK_FRIDAYS: dict[int, str] = {
    # 914177: "2026-09-26T04:59:00Z",  # CS2 Week 6 gate -- VERIFY before use
    # ...
}


def die(msg):
    print("STOP:", msg)
    sys.exit(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="Actually write. Default is dry-run.")
    args = ap.parse_args()

    if not OVERVIEW_MODULE_FIXES and not WEEK_FRIDAYS:
        die("mapping tables are empty skeletons -- fill them from the audit report before running")

    load_env()
    cfg = read_canvas_config(enforce_course_allowlist=True)
    cfg = CanvasConfig(cfg.api_base_url, cfg.api_token, frozenset({COURSE_ID}))
    client = CanvasClient(cfg)

    course = client.get(f"/api/v1/courses/{COURSE_ID}").json()
    if course.get("id") != COURSE_ID:
        die("course identity mismatch: %r" % course.get("name"))

    ev = ["", "## CS2 overview-linkage + due-date fix -- %s UTC -- %s" %
          (time.strftime("%Y-%m-%dT%H:%M:%S"), "LIVE" if args.live else "DRY-RUN")]
    ev.append("- course: %s / %s" % (course["id"], course["name"]))

    # Part A: re-point module items
    for module_id, fix in OVERVIEW_MODULE_FIXES.items():
        items = api.get_module_items(client, COURSE_ID, module_id)
        item = next((i for i in items if i["id"] == fix["item_id"]), None)
        if item is None:
            ev.append(f"- SKIP module {module_id}: item {fix['item_id']} not found (already changed?)")
            continue
        current_page = item.get("page_url")
        target_page = fix["new_page_url"]
        if current_page == target_page:
            ev.append(f"- module {module_id} item {fix['item_id']}: already correct ({target_page}), no-op")
            continue
        ev.append(f"- module {module_id} item {fix['item_id']}: {current_page!r} -> {target_page!r}"
                   + ("" if args.live else " [DRY-RUN, not written]"))
        if args.live:
            status, body = api.update_module_item(
                client, COURSE_ID, module_id, fix["item_id"],
                {"module_item[page_url]": target_page},
            )
            readback = api.get_module_items(client, COURSE_ID, module_id)
            rb_item = next((i for i in readback if i["id"] == fix["item_id"]), None)
            ev.append(f"  readback page_url={rb_item.get('page_url') if rb_item else 'MISSING'}")

    # Part B: due_at fills
    for assignment_id, due_at in WEEK_FRIDAYS.items():
        status, a = api.get_assignment(client, COURSE_ID, assignment_id)
        if a.get("due_at") is not None:
            ev.append(f"- SKIP assignment {assignment_id}: due_at already set ({a['due_at']}) -- never overwrite")
            continue
        ev.append(f"- assignment {assignment_id} ({a.get('name')!r}): due_at None -> {due_at}"
                   + ("" if args.live else " [DRY-RUN, not written]"))
        if args.live:
            api.update_assignment(client, COURSE_ID, assignment_id, {"assignment[due_at]": due_at})
            status2, rb = api.get_assignment(client, COURSE_ID, assignment_id)
            ev.append(f"  readback due_at={rb.get('due_at')}")

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    with open(EVIDENCE, "a") as f:
        f.write("\n".join(ev) + "\n")
    print("\n".join(ev))


if __name__ == "__main__":
    main()
