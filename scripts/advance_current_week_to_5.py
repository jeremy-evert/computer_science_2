#!/usr/bin/env python3
"""Fix CS2's front page: the H1 text says Week 5 but its own anchor id
still reads "week-4" and the "This week" narrative + "Go here first" list
were never advanced past Week 4 -- confirmed live before writing this
script. No Week 5 "lesson" sub-page exists yet (only the overview page),
so the Go-here-first list drops that item rather than inventing one.
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path.home() / "git" / "harbor"))
from harbor import api
from harbor.client import CanvasClient
from harbor.config import load_env, read_canvas_config

COURSE_ID = 74031
EVIDENCE = Path.home() / "git" / "computer_science_2" / "sidecar" / "reports" / "advance_current_week_to_5.md"

OLD_H1 = '<h1 id="start-here--you-are-in-week-4">Start Here — you are in Week 5</h1>'
NEW_H1 = '<h1 id="start-here--you-are-in-week-5">Start Here — you are in Week 5</h1>'

OLD_SUMMARY = '''<p><strong>This week: Cohesive Object Boundary.</strong> Reopen your <a href="https://swosu.instructure.com/courses/74031/pages/cs2-week-03-overview-found-your-world-slash-world-bible-v0-dot-1" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74031/pages/cs2-week-03-overview-found-your-world-slash-world-bible-v0-dot-1" data-api-returntype="Page">Week 3 World
Bible</a>, test whether one predicted noun deserves to be its own
object, and write one focused <code>unittest</code>.</p>'''
NEW_SUMMARY = '''<p><strong>This week: Collaborating Objects and Invariant.</strong> Reopen your Week 4 object, refactor it into two or more collaborating objects using composition, and protect one invariant with an automated test.</p>'''

OLD_GO_HERE = '''<h2 id="go-here-first">Go here first</h2>
<ul>
<li><strong><a href="https://swosu.instructure.com/courses/74031/pages/cs2-week-04-overview-cohesive-object-boundary" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74031/pages/cs2-week-04-overview-cohesive-object-boundary" data-api-returntype="Page">Week
4 — Overview</a></strong> — what the week asks and what you turn
in.</li>
<li><strong><a href="https://swosu.instructure.com/courses/74031/pages/cs2-week-04-cohesive-object-boundary-lesson" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74031/pages/cs2-week-04-cohesive-object-boundary-lesson" data-api-returntype="Page">Week
4 — Lesson</a></strong> — the worked example and the testing habit.</li>
<li><strong><a href="https://swosu.instructure.com/courses/74031/discussion_topics/542906" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74031/discussion_topics/542906" data-api-returntype="Discussion">Week 4 Odyssey
Gate discussion</a></strong> — 25 points, graded discussion. Post the
object, the focused test, the boundary explanation, and your World Bible
entry, then reply to a classmate.</li>
</ul>'''
NEW_GO_HERE = '''<h2 id="go-here-first">Go here first</h2>
<ul>
<li><strong><a href="https://swosu.instructure.com/courses/74031/pages/cs2-week-05-overview-5" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74031/pages/cs2-week-05-overview-5" data-api-returntype="Page">Week
5 — Overview</a></strong> — what the week asks and what you turn
in.</li>
<li><strong><a href="https://swosu.instructure.com/courses/74031/discussion_topics/543064" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74031/discussion_topics/543064" data-api-returntype="Discussion">Week 5 Odyssey
Gate discussion</a></strong> — 25 points, graded discussion, due 9/19. Post
your refactor into collaborating objects, the invariant you protected,
and the automated test, then reply to a classmate.</li>
</ul>'''

SUBSTITUTIONS = [
    ("h1 anchor id", OLD_H1, NEW_H1),
    ("this-week summary", OLD_SUMMARY, NEW_SUMMARY),
    ("go-here-first list", OLD_GO_HERE, NEW_GO_HERE),
]


def die(msg):
    print("STOP:", msg)
    sys.exit(2)


def main():
    load_env()
    client = CanvasClient(read_canvas_config(enforce_course_allowlist=True))
    ev = ["", "## CS2 front page: advance This-week/Go-here-first to Week 5 — %s UTC" % time.strftime("%Y-%m-%dT%H:%M:%S")]

    if not client.config.api_base_url.startswith("https://swosu.instructure.com"):
        die("base_url not SWOSU")
    course = client.get(f"/api/v1/courses/{COURSE_ID}").json()
    if course.get("id") != COURSE_ID:
        die("course identity mismatch: %r" % course.get("name"))
    ev.append("- course: %s / %s" % (course["id"], course["name"]))

    fp_before = client.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
    body = fp_before.get("body") or ""
    page_url = fp_before["url"]

    if "discussion_topics/543064" in body and "cohesive-object-boundary" not in body:
        die("front page already advanced -- nothing to do (idempotent guard)")

    for label, old, new in SUBSTITUTIONS:
        if old not in body:
            die("expected content for %r not found -- front page changed since this script was written" % label)
        body = body.replace(old, new)
        ev.append("- applied: %s" % label)

    status, _ = api.update_page(client, COURSE_ID, page_url, {"wiki_page[body]": body})
    ev.append("- update_page status %s" % status)

    fp_after = client.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
    live_body = fp_after.get("body") or ""
    if live_body != body:
        die("readback mismatch: live front page body does not match what was sent")
    ev.append("- readback OK: live front page body matches exactly what was sent")

    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    with EVIDENCE.open("a", encoding="utf-8") as f:
        f.write("\n".join(ev) + "\n")
    print("\n".join(ev))
    print("\nDONE. Evidence appended to %s" % EVIDENCE)


if __name__ == "__main__":
    main()
