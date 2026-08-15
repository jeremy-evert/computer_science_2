# CS2 textbook reconciliation — no required textbook

**Date:** 2026-08-15  
**Scope:** Fall 2026 COMSC-1053 source only. No Canvas, Savnac, production
zyBooks, student-system, or other-repository action was taken.

## Result

COMSC-1053 has **no required textbook, paid resource, or external course** for
Fall 2026. The course is organized through course-owned Reasoning Odyssey work,
shared Week 1/2 sources, and recommended no-cost references.

## Files changed

| File | Change and reason |
|---|---|
| `course_metadata.yaml` | Replaced live operational `zybook_identifier` and `zybook_url` fields with a dated `historical_zybooks_provenance` record; stated the no-required-textbook/external-course decision plainly; retained the supplied identifier and URL. |
| `reports/005_fall_2026_zybooks_design.md` | Added a dated supersession notice so its former section-design analysis remains historical provenance rather than an active reading or assignment plan. |
| `reports/006_drop_zybooks_no_required_textbook.md` | This reconciliation report. |

## ZyBooks inventory

The scan covered `course_metadata.yaml`, `docs/`, `planning/`, `lessons/`,
`assignments/`, `rubrics/`, and `reports/` case-insensitively.

| Location(s) | Status | Reason |
|---|---|---|
| `course_metadata.yaml` lines 51, 58–59, 68–73 (pre-change) | Changed | These live-looking metadata fields could be read as an operational adoption. The facts now live only in a dated historical-provenance block. |
| `planning/fall-2026-course-design.md` lines 17, 55 | Left | Explicitly says ZyBooks is optional historical/control context and prohibits production action. |
| `planning/zybooks-section-decisions.csv` header and row 256 | Left | Inherited section-decision catalog retained as provenance; active source expressly says it is not a required reading map. |
| `lessons/strings-collections.md` line 9; `lessons/classes-and-oop.md` line 9 | Left | Both label the labs as historical materials, not current assignments. |
| `docs/course-ethos.md` line 20 | Left | Explicitly rejects required paid dependencies. |
| `docs/curriculum/fall-2026-resource-map.md` lines 15–16 | Left | Explicitly labels ZyBooks historical/control and the CSV an inherited trail. |
| `docs/curriculum/course-sequence.md` line 29 | Left | Explicitly limits vendor mappings to provenance and rejects required readings/gates. |
| `docs/reports/curriculum-history-synthesis.md` lines 11, 17; `docs/philosophy/teaching-patterns.md` line 23 | Left | Historical curriculum-analysis statements. |
| `reports/003_cs2_odyssey_gates_weeks_2to6.md` line 30 | Left | Dated report preserving historical chapter-label context. |
| `reports/005_fall_2026_zybooks_design.md` lines 1, 5, 21 | Changed | Its historical design record is retained, with a clear 2026-08-15 supersession notice. |
| `reports/007_cs2_capability_spine_handoff_and_open_resources.md` lines 4, 11, 25, 81, 83, 89, 101–102, 110, 157, 173; `reports/007_cs2_resource_coverage_matrix.{json,csv}` | Left | Research/provenance material that already identifies ZyBooks as optional/control or rejected as the spine. |
| `reports/008_cs2_pre_savnac_source_reconciliation.md` lines 5, 15, 78, 85; `reports/009_data_storytelling_visualization_rebalance.md` lines 5, 50 | Left | Prior reconciliation reports; they already state the historical/provenance-only status. |
| `reports/codex/002_run.log`, `reports/codex/003_run.log`, `reports/codex/003_run_retry.log`, `reports/codex/004_run.log` (all matches) | Left | Immutable-style execution logs and archival evidence; not active course doctrine. |

No `ZyBooks`/`zybook` hits were found in `assignments/` or `rubrics/`.

## Protected content confirmation

No grading weights, assignment structure, rubrics, or Reasoning Odyssey
content were changed. This change only reconciles textbook/external-course
status and clarifies historical provenance.
