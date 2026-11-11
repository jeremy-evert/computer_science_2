#!/usr/bin/env python3
"""Add the Week 13 showcase links to the CS2 Canvas front page.

Dry-run by default (prints the body diff, writes nothing). Pass --apply to write.
Target-locked: course id 74031 AND a name containing "Computer Science II" are
verified before any write. Additive and idempotent (marker data-showcase), takes a
before-backup of the page body, and reads the page back.

Usage: add_showcase_to_front_page.py [--apply] [--env ~/.config/canvas/canvas.env]
"""
import difflib, re, sys, time, urllib.parse
from pathlib import Path

COURSE_ID, COURSE_NAME_PART = 74031, "Computer Science II"
MARKER = 'data-showcase="sorting-and-searching"'
SITE = "https://jeremy-evert.github.io/sorting_and_searching/"
REPO = "https://github.com/jeremy-evert/sorting_and_searching"
BACKUP_DIR = Path(__file__).resolve().parent.parent / "week_13" / "showcase" / "canvas_backups"

BLOCK = f'''
<div {MARKER}>
<h2>Showcase: what a finished project can look like</h2>
<ul>
<li><a href="{SITE}"><strong>Sorting and Searching, Measured</strong></a> (project page) — a finished, clean-code project: tests, plots, and design notes. Look at how it is organized while you think about what you want your own portfolio to look like this weekend.</li>
<li><a href="{REPO}">The code and how it was built</a> (GitHub) — start with the README, then the tests.</li>
</ul>
</div>'''


def load_env(path):
    env = {}
    for line in Path(path).expanduser().read_text().splitlines():
        line = re.sub(r"^export\s+", "", line.strip())
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip("'\"")
    return env


def main():
    import requests
    apply = "--apply" in sys.argv
    env_path = sys.argv[sys.argv.index("--env") + 1] if "--env" in sys.argv else "~/.config/canvas/canvas.env"
    env = load_env(env_path)
    base = (env.get("CANVAS_API_BASE_URL") or env.get("CANVAS_BASE_URL") or "").rstrip("/")
    root = re.sub(r"/api/v1$", "", base)
    api, host = root + "/api/v1", urllib.parse.urlparse(root).netloc
    s = requests.Session()
    s.headers["Authorization"] = "Bearer " + env["CANVAS_API_TOKEN"]

    def call(method, path, **kw):
        url = api + path
        assert urllib.parse.urlparse(url).netloc == host
        r = s.request(method, url, timeout=60, allow_redirects=False, **kw)
        r.raise_for_status()
        return r.json()

    course = call("GET", f"/courses/{COURSE_ID}")
    if course.get("id") != COURSE_ID or COURSE_NAME_PART not in course.get("name", ""):
        sys.exit(f"STOP: course mismatch: {course.get('id')} {course.get('name')!r}")
    page = call("GET", f"/courses/{COURSE_ID}/front_page")
    body, slug = page["body"], page["url"]
    if MARKER in body:
        sys.exit("already present (idempotent no-op)")
    anchor = body.find('id="go-here-first"')
    end = body.find("</ul>", anchor)
    if anchor < 0 or end < 0:
        sys.exit("STOP: 'Go here first' list not found")
    k = end + len("</ul>")
    new = body[:k] + BLOCK + body[k:]
    print("".join(difflib.unified_diff(body.splitlines(True), new.splitlines(True), "before", "after", n=1)))
    if not apply:
        print("DRY RUN: nothing written."); return
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    bp = BACKUP_DIR / f"cs2-front-page_before_showcase_{time.strftime('%Y%m%dT%H%M%S')}.html"
    bp.write_text(body, encoding="utf-8"); print("backup:", bp)
    call("PUT", f"/courses/{COURSE_ID}/pages/{slug}", data={"wiki_page[body]": new})
    live = call("GET", f"/courses/{COURSE_ID}/front_page")["body"]
    ok = MARKER in live and SITE in live and REPO in live
    stripped = live.replace(BLOCK, "", 1)
    print("links present:", ok, "| rest of page unchanged vs backup:", stripped == body)
    if not ok:
        sys.exit("readback FAILED")
    print("readback OK")


if __name__ == "__main__":
    main()
