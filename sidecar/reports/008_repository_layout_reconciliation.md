# Sidecar Report 008 — Repository layout reconciliation

**Authority:** accepted `sidecar/reports/007_repository_recon_and_context_map.md`

## Exact moves performed

- Moved completed prompts 002–006 and the process README from `prompts/` to `sidecar/prompts/completed/`, except that the pre-existing completed-directory README was retained and the process README was placed at `sidecar/prompts/README.md` to avoid replacing it.
- Moved all root process reports 002–009 and their CSV/JSON companions from `reports/` to `sidecar/reports/`.
- Moved `reports/codex/*.log` to `sidecar/runs/`.
- Moved all six files from `raw/` to `sidecar/runs/`.
- Removed the now-empty tracked root `prompts/.gitkeep` and `reports/.gitkeep`, and removed the empty root `reports/`, `reports/codex/`, and `raw/` directories.
- Repaired the live course pointer in `planning/week-02-local-ai-lab-integration.md` from the old root report path to `sidecar/reports/006_week2_local_ai_stitch.md`.

All moves used `git mv` where the source was tracked. File contents were not rewritten except for the one live path repair above.

## Deliberately left in place

- `prompts/001_course_development_source_walk.md` remains at root because Prompt 007 classified it `UNCLEAR`; it was not moved by guesswork.
- `archive/`, `docs/reports/curriculum-history-synthesis.md`, `planning/zybooks-section-decisions.csv`, and `course_metadata.yaml` remain outside `sidecar/` as project history or current course truth.
- `assignments/`, `docs/`, `lessons/`, `monday_moments/`, `planning/`, `quizzes/`, `rubrics/`, `templates/`, `portfolio/`, `reflections/`, and `tests/` remain untouched as course material or project scaffolding.
- Existing sidecar prompts, reports, question README, run README, and completed-prompt README remain in place.
- Historical path mentions inside moved reports and completed prompts were retained where they describe the pre-reconciliation process or external repositories, rather than rewriting provenance.

## Current-truth promotion

No promotion was needed. The Prompt 007–009 findings were checked against current truth before filing:

- S01–S08 and the catalog spine are present in `planning/fall-2026-course-design.md` and `docs/curriculum/`.
- The contract, data-abstraction, GUI/event, and source-management decisions are present in the active weeks, assignments, and rubrics.
- The Week 9–11 visualization/storytelling refinement is present in active planning, lessons, assignments, and rubrics.
- The no-required-textbook decision is already represented in current course truth.

## Validation performed

- `git diff --check` passed.
- Confirmed moved prompts, reports, CSV/JSON companions, logs, raw transcripts, launcher logs, and summaries are readable at their new paths.
- Confirmed no `UNCLEAR` artifact was moved; Prompt 001 remains at its original path.
- Scanned the project surface for old root `prompts/`, `reports/`, and `raw/` dependencies; the one live course pointer was repaired. Remaining matches are intentional external provenance, the preserved UNCLEAR prompt, or historical sidecar documentation.
- No course content, grading weights, due dates, rubrics, or instructional policy was changed.
- No secrets or private student data were introduced; this reconciliation moved existing artifacts and made one path-only repair.

## Unresolved structural questions

1. Prompt 001 still needs an explicit ownership decision: standing guideline, completed prompt, or superseded artifact.
2. `docs/reports/` remains intentionally distinct from `sidecar/reports/`; a future naming clarification may reduce confusion.
3. `docs/planning/` remains empty scaffolding while top-level `planning/` is populated.

## Final top-level tree

```text
README.md
course_metadata.yaml
archive/
assignments/
docs/
lessons/
monday_moments/
planning/
portfolio/
prompts/
quizzes/
reflections/
rubrics/
sidecar/
templates/
tests/
```

The root `prompts/` directory contains only the deliberately unmoved Prompt 001.

## Final sidecar tree

```text
sidecar/
├── README.md
├── prompts/
│   ├── README.md
│   ├── 007_repository_recon_and_context_map.md
│   ├── 008_repository_layout_reconciliation.md
│   ├── 009_cs2_agents_from_cs1.md
│   ├── 010_steal_from_cs1_until_proven_wrong.md
│   ├── 011_promote_reusable_stolen_goods_to_swosu_cs_curriculum.md
│   ├── 012_rebox_course_and_firewall_sidecar_context.md
│   └── completed/
│       ├── README.md
│       └── 002–006 completed prompts
├── reports/
│   ├── README.md
│   ├── 007_repository_recon_and_context_map.md
│   ├── 008_repository_layout_reconciliation.md
│   └── moved 002–009 reports and companions
├── questions/
│   └── README.md
└── runs/
    ├── README.md
    ├── moved codex logs
    └── moved raw launcher/transcript/summary files
```

## Commit SHA(s)

No new commit was created in this worktree. The pre-reconciliation `HEAD` was `68ac82ac2857c73a665fde21f435c770adea8b83`; the reconciliation remains as a reviewable working-tree change.
