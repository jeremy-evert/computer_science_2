#!/usr/bin/env python3
"""Repoint CS2 (74031) Week 5/6/7 module 'Overview' items at the right overview page.

Canvas ignores page_url changes on an existing module item (found 2026-09-24: the
PUT in fix_weeks5_7_overview_and_rail_2026-09-24.py returned 200 but changed nothing),
so this creates a correct Page item at the same position and removes the old item.
Only the module LINK is removed; no page is deleted. Dry-run by default.
  python3 scripts/fix_cs2_module_overview_items_2026-09-24.py [--live]
"""
import json, os, sys, urllib.parse, urllib.request

BASE = os.environ["CANVAS_API_BASE_URL"].rstrip("/") + "/api/v1/courses/74031"
TOK = os.environ["CANVAS_API_TOKEN"]
LIVE = "--live" in sys.argv
# module id, old item id, correct page slug, title
FIX = [(218889, 1530010, "cs2-week-05-overview-5", "CS2 Week 05 -- Overview"),
       (218890, 1530011, "cs2-week-06-overview-5", "CS2 Week 06 -- Overview"),
       (218891, 1530012, "cs2-week-07-overview-6", "CS2 Week 07 -- Overview")]


def call(method, path, data=None):
    req = urllib.request.Request(BASE + path, method=method,
                                 data=urllib.parse.urlencode(data, doseq=True).encode() if data else None,
                                 headers={"Authorization": f"Bearer {TOK}"})
    with urllib.request.urlopen(req) as r:
        b = r.read()
        return json.loads(b) if b else {}


print(f"## module overview item fix -- {'LIVE' if LIVE else 'DRY-RUN'}")
for mod, old, slug, title in FIX:
    items = call("GET", f"/modules/{mod}/items?per_page=100")
    if any(i.get("page_url") == slug for i in items):
        print(f"- module {mod}: already links {slug}; nothing to do"); continue
    olditem = next((i for i in items if i["id"] == old), None)
    if not olditem:
        print(f"- module {mod}: old item {old} not found; skipping (investigate)"); continue
    pos = olditem["position"]
    print(f"- module {mod}: item {old} ({olditem.get('page_url')}) -> new Page item {slug} at position {pos}")
    if not LIVE:
        continue
    new = call("POST", f"/modules/{mod}/items", {"module_item[title]": title, "module_item[type]": "Page",
                                                    "module_item[page_url]": slug, "module_item[position]": pos,
                                                    "module_item[indent]": olditem.get("indent", 0)})
    call("DELETE", f"/modules/{mod}/items/{old}")
    back = call("GET", f"/modules/{mod}/items?per_page=100")
    ok = any(i.get("page_url") == slug for i in back) and not any(i["id"] == old for i in back)
    print(f"  readback: new item {new.get('id')} page_url={new.get('page_url')} pos={new.get('position')} ok={ok}")
