# CS2 August 31 lecture distillation — Phase 4/5 evidence

Date: 2026-08-31
Course: Computer Science II, Canvas course `74031`
Target module: `218887`, `CS2 Week 3 -- Found Your World (World Bible v0.1)`
Assigned run: `ba5d401476d8c6e0bb0d8e354ab80d99`

## Source and transcript

Protected MP4 on April:
`/home/jevert/lecture_pipeline/protected_raw/2026-08-31/cs2/Fall 2026 Computer Science II (COMSC-1053-1417)-20260831_130202-Meeting Recording.mp4`

Expected MP4 SHA-256: `afc89f0576d77068d61ff54da139994a4113e29a30ddeb1e3980a9bc507f3b74`.
Fresh primary transcript: `whisper-ctranslate2 0.5.7`, `medium.en`, English,
CPU, CTranslate2 `int8`, 20 threads, VTT output.
Fresh transcript SHA-256: `141fefc01c5e72d83cd4f975a8b8deebd94243c7e657e90b19f824bbb91583e3`.
The protected VTT remains outside Git and was uploaded only as the
unpublished Instructor Review file. The Teams VTT was cross-check evidence.
Published artifacts contain no student names, faces, chat, or identifying
transcript snippets.

## Committed artifacts

- `lessons/2026-08-31_cs2_lecture_notes.md`
- `sidecar/lecture_notes/2026-08-31_cs2_lecture_digest.md`
- `presentations/beamer/week03_aug31_lecture_distillation/week03_aug31_lecture_distillation.tex`
- `presentations/beamer/week03_aug31_lecture_distillation/week03_aug31_lecture_distillation.pdf`
- `presentations/beamer/week03_aug31_lecture_distillation/img/` (eight frames)
- this report

The deck compiles to 10 pages with the existing CS2 `cs2theme` and
`cs2commands` system. April `latexmk -pdf -interaction=nonstopmode
-halt-on-error` completed successfully. The only warnings were the existing
theme footline overfull-box warning; there were no missing assets or fatal
errors.

## Screenshot evidence and crop proof

Frames were extracted with `ffmpeg -ss ... -frames:v 1 -q:v 3`. Each source
frame was 1920×1080. The fixed crop `1560x1080+0+0` removed the right-edge
roster strip; the required bottom-left self-label mask was applied. Browser
and M365 frames were re-opened and contained no remaining roster, face, chat,
email, or name fragment. The fixed geometry held for all eight frames.

| File | Approx. source time | Slide evidence |
|---|---:|---|
| `img/reframe.jpg` | 00:09:15 | reframe and five variables |
| `img/add_test.jpg` | 00:18:04 | bounded task, diff, independent `add(4, 4)` test |
| `img/model_list.jpg` | 00:32:20 | `ollama list` and model sizes |
| `img/world_prompt.jpg` | 00:34:19 | Starship Log World Bible prompt |
| `img/wrong_fit.jpg` | 00:35:15 | fictional prompt misread as engineering ticket |
| `img/model_sizes.jpg` | 00:38:04 | model-size comparison |
| `img/gpu_vram.jpg` | 00:40:02 | 8 GB VRAM / 10 GB working model |
| `img/split.jpg` | 00:45:00 | CPU/GPU split and fit tradeoff |

## Canvas readback and order

Pre-write readback confirmed module `218887` at position 1 with 13 existing
items and the exact authorized title. The additive write created:

| Position | Item ID | Type | Title | Published |
|---:|---:|---|---|---|
| 1 | 1531429 | ExternalUrl | Aug. 31 Lecture Recording (Optional Archive) | true |
| 2 | 1531430 | File | Aug. 31 Lecture Distillation — Slides (PDF) | false |
| 3 | 1531431 | Page | Aug. 31 Lecture Notes — Runs Usefully | true |
| 4 | 1531432 | Page | Aug. 31 Lecture Digest | true |
| 5 | 1531433 | File | Aug. 31 Lecture Transcript (Instructor Review) | false |

Slides file ID: `6579075`; transcript file ID: `6579076`. Notes page slug:
`aug-31-lecture-notes-runs-usefully-2`; digest slug:
`aug-31-lecture-digest-2`. The recording URL is the exact SharePoint URL
authorized by the work file.

Before order (positions 1–13): `1531231, 1531232, 1531233, 1531234, 1529982,
1531326, 1531328, 1531329, 1531330, 1531331, 1531332, 1531333, 1531334`.
After order (positions 6–18): the same IDs in the same sequence. Existing
membership and relative order were preserved.

## Conservative typo pass

No existing module Page body or item title was changed. Existing pages have
duplicated/rough instructional material, but no candidate met the
unambiguous-mechanical-error threshold without risking meaning. Flagged, not
changed: duplicate “World Bible Local Model Lab” page titles, mixed historical
Week 2/Week 3 labels, and rough prose in the existing local-model pages. No
due dates, points, rubrics, submissions, grades, or assignment titles were
touched.

## Preservation and repeatable pipeline

The deployment used only course `74031`, module `218887`, and the authorized
recording URL. It made no calls for grades, submissions, enrollments,
assignments, or other module writes. Existing 13-item membership was read
before and after; only five new links were added and the existing block shifted
to positions 6–18.

Future runs: hash and preserve MP4; generate fresh VTT; write the de-identified
digest; extract frames at digest timestamps; apply fixed crop/masks; visually
inspect every frame; compile with shared CS2 theme; write notes; refresh live
module immediately before additive writes; publish only authorized items; and
read back type, position, and published state. The fixed-region roster crop
held for this CS2 recording geometry without dropping an essential frame.

Commit and push verification are recorded in the final handoff.
