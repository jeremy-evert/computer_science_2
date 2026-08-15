# CS2 Fall 2026 zyBooks design pass

> **Superseded 2026-08-15:** This is a historical design record, not the Fall
> 2026 course plan. COMSC-1053 has no required textbook or external course;
> the referenced zyBooks inventory and `planning/zybooks-section-decisions.csv`
> remain provenance only and must not be read as assigned sections or student
> dependencies.

## Evidence and result

Used the durable CS2 TOC/manifest at `/mnt/brandy_nvme/jevert/durable/zybooks_captures/SWOSUCOMSC1053ZacharyFall2026/`, `course_metadata.yaml`, the 17 existing week plans, curriculum sequence/unit notes, lessons, Odyssey assignments/rubrics, and prior spine report. The durable TOC has 466 instructional sections in 32 chapters.

| Decision | Sections | Share |
|---|---:|---:|
| KEEP | 44 | 9.4% |
| OPTIONAL | 100 | 21.5% |
| UNUSED | 322 | 69.1% |

Required material is the non-lab instructional core of chapters 10–16: exceptions, modules, files, inheritance, recursion, plotting, and searching/sorting. This confirms and makes section-level the pre-existing fall plan; it does not replace it with textbook order. Chapters 1–8 are prerequisite CS1 work, while classes are a targeted optional diagnostic/review. Extra labs are optional practice rather than a parallel graded workload.

## Lean configuration and unresolved work

Candidate vendor configuration is chapters 10–16 required, with selected review/labs/enrichment retained as optional. Ask the vendor for price comparison; no lower price is claimed. Open decisions are the CS1-to-CS2 Odyssey-continuity choice and final-deadline/shared-strand confirmation.

## Validation

`planning/zybooks-section-decisions.csv` has 466 data rows, matching the durable TOC; classifications total 44 KEEP + 100 OPTIONAL + 322 UNUSED = 466. Each KEEP has a target week/topic. Artifacts contain only identifiers, titles, and derived rationale—no captured section body. `git diff --check` is required before commit; this repository has no identified automated test suite for planning artifacts.
