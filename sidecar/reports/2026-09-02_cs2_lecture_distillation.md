# CS2 September 2 lecture distillation — Phase 4/5 evidence

Date: 2026-09-02
Course: Computer Science II, Canvas course `74031`
Target module: `218887`, `CS2 Week 3 -- Found Your World (World Bible v0.1)`

## Source and transcript

Protected MP4 on April:
`/home/jevert/lecture_pipeline/protected_raw/2026-09-02/cs2/Fall 2026 Computer Science II (COMSC-1053-1417)-20260902_130052-Meeting Recording.mp4`

MP4 SHA-256: `76fae0209b9e38d9abe12f4eb552f69790ac0abc02917607968bae3431f47f14`
(matches the hash taken on maise before transfer; the maise copy was deleted
after this verification).

Fresh transcript: `whisper-ctranslate2 0.5.7`, `medium.en`, English, CPU,
CTranslate2 `int8`, 20 threads, VTT output. Video duration ~23.5 minutes
(1413.5s). The transcript remains outside Git and was uploaded only as the
unpublished Instructor Review file (course file `6582714`). Published
artifacts (digest, notes, deck) contain no student names -- the class used
real first names constantly throughout this open-lab session, all omitted
from every published document; groups are referred to only by role
(Foreman/Worker/Navigator).

## Session shape note

This was an open-lab/pairing session, not a structured front-of-room
lecture -- the instructor circulated between small groups working on
Monday's "Found Your World" material. The opening ~2 minutes is an
unrelated instructor GPU-benchmarking aside, noted in the digest as
context, not course content.

## Committed artifacts

- `lessons/2026-09-02_cs2_lecture_notes.md`
- `sidecar/lecture_notes/2026-09-02_cs2_lecture_digest.md`
- `presentations/beamer/week03_sep02_lecture_distillation/week03_sep02_lecture_distillation.tex`
- `presentations/beamer/week03_sep02_lecture_distillation/week03_sep02_lecture_distillation.pdf`
- `presentations/beamer/week03_sep02_lecture_distillation/img/` (five frames)
- this report

The deck compiles to 10 pages with the existing CS2 `cs2theme` and
`cs2commands` system. `latexmk -pdf -interaction=nonstopmode -halt-on-error`
completed successfully. The only warnings were minor overfull-hbox notices
(~7pt) on three slides, consistent with the pre-existing theme footline
warning class noted in the Aug. 31 run; no missing assets or fatal errors.

## Screenshot evidence

Frames were extracted with `ffmpeg -ss ... -frames:v 1 -q:v 3` at five
timestamps chosen from the transcript. Unlike the Aug. 31 CS2 recording,
this call was a full-screen instructor screen-share with no Teams roster
strip or participant video visible in any frame -- only a small self-avatar
circle labeled with the instructor's own name in the bottom-right corner, so
the fixed `1560x1080+0+0` roster crop used on Aug. 31 was not needed here.
Each frame was still visually inspected before use; none contain a student
name, face, chat, or roster.

| File | Approx. source time | Slide evidence |
|---|---:|---|
| `img/monday_archive.jpg` | 00:06:29 | Monday's archived recording + slides, linked as review material |
| `img/answer_a_call.jpg` | 00:13:32 | The four World Bible scenarios ("Step 2 — Answer a call") |
| `img/copilot_prompt.jpg` | 00:13:49 | The instructor's plain-language Copilot prompt |
| `img/copilot_script.jpg` | 00:14:20 | The Copilot-generated PowerShell scaffold (`Start-Transcript`, `Get-CimInstance`, `nvidia-smi`) |
| `img/gpu_status.jpg` | 00:11:29 | Live `nvidia-smi` output (RTX 3060 Ti, ~2.3/8 GB VRAM at idle) |

## Canvas readback and order

Pre-write readback confirmed module `218887` still published, position 1,
with the same 18-item prefix present as of the Aug. 31 run (16 items visible
via the default listing plus two unpublished items only visible by direct
ID lookup: file item `1531433` at position 5, and the pre-existing duplicate
"World Bible Local Model Lab" page item `1531328` at position 12 — both
already flagged, unchanged, in the Aug. 31 report's conservative typo pass).

The additive write created:

| Position | Item ID | Type | Title | Published |
|---:|---:|---|---|---|
| 19 | 1532292 | ExternalUrl | Sept. 2 Lecture Recording (Optional Archive) | true |
| 20 | 1532293 | File | Sept. 2 Lecture Distillation — Slides (PDF) | false |
| 21 | 1532294 | Page | Sept. 2 Lecture Notes — Run It, Then Measure It | true |
| 22 | 1532295 | Page | Sept. 2 Lecture Digest | false |
| 23 | 1532296 | File | Sept. 2 Lecture Transcript (Instructor Review) | false |

Slides file ID: `6582713`; transcript file ID: `6582714`. Notes page slug:
`sept-2-lecture-notes-run-it-then-measure-it`; digest slug:
`sept-2-lecture-digest`. The recording URL is the exact SharePoint URL
authorized by the work file.

Full post-write readback (positions 1–23) confirmed the pre-existing 18-item
prefix is byte-for-byte unchanged in id, type, title, and order, and the five
new items landed exactly as specified above, additively, at the end.

## Conservative typo pass

No existing module Page body or item title was changed. The same items
flagged on Aug. 31 (duplicate "World Bible Local Model Lab" page titles,
mixed historical Week 2/Week 3 labels) remain present and unchanged; nothing
new met the unambiguous-mechanical-error threshold. No due dates, points,
rubrics, submissions, grades, or assignment titles were touched.

## Preservation

This run touched only course `74031`, module `218887`, and the five new
additive items above. No assignment, rubric, submission, grade, or
enrollment was read or written. The already-published "Week 3 — Which Model
Would You Hire?" discussion (item `1531326`, due Sept. 2) was not modified.

Implementation: committed directly to `main` in this session; see the git
log for the commit hash accompanying this report.
