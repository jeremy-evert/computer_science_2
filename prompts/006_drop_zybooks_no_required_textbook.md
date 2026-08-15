# Prompt 006 — Drop ZyBooks, no required textbook (CS2)

## Status

READY. Jeremy, 2026-08-15 (live chat, not yet a written `questions/` card):
"we are not going to use zybooks for cs 1, cs 2, or dcst." CS1 already
walked this back on 2026-08-12 (`computer_science_1` commit `6ee41dd`,
"Pre-Savnac source reconciliation: no required textbook... walks back both
the 2026-07-27 Deitel-primary and 2026-08-11 ZyBooks-first decisions").
This prompt applies the same reversal to CS2. Computer Architecture is
explicitly **not** part of this decision — Jeremy said that course is still
an open question he's deciding separately today. Do not touch
`computer_architecture`.

## Mission

Reconcile CS2's source so it no longer presents ZyBooks as CS2's textbook or
organizing spine.

## Scope

1. `course_metadata.yaml`'s `textbook:` block currently carries a live
   `zybook_identifier`/`zybook_url` (`SWOSUCOMSC1053ZacharyFall2026`) as the
   operational adoption record. Reconcile this the way CS1's `6ee41dd` did:
   state plainly that CS2 has no required textbook/external course for Fall
   2026, and preserve the ZyBooks identifier/URL as **historical
   provenance** (CS1's file keeps its old ZyBooks facts as dated historical
   notes rather than deleting them — read `computer_science_1/course_metadata.yaml`
   for the exact shape to mirror) rather than erasing that Jeremy did once
   supply it.
2. Grep the rest of the repo (`docs/`, `planning/`, `lessons/`, `assignments/`,
   `rubrics/`) for "ZyBooks"/"zybook" and reconcile only current,
   student-facing or operative-doctrine references that assume ZyBooks is
   CS2's textbook/spine. Leave historical/provenance/dated-decision notes
   alone (mark superseded in place if genuinely load-bearing context, do not
   delete history).
3. Do not touch grading weights, assignment structure, or the Reasoning
   Odyssey work already reconciled in `prompts/005_...`/its report. This is
   a textbook-status change only.
4. Do not touch `computer_architecture` or any other repo.

## Deliverable

Write `reports/006_drop_zybooks_no_required_textbook.md`: every file
changed and why, every ZyBooks hit found and whether changed/left (with
reason), and explicit confirmation that no grading/structural content was
touched.
