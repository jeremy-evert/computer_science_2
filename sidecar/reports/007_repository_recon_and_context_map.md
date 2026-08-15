# Sidecar Report 007 — Repository recon and context map

**Prompt:** `sidecar/prompts/007_repository_recon_and_context_map.md`
**Mode:** read-only recon. No files moved, renamed, or rewritten by this pass.

## Top-level inventory

```
computer_science_2/
├── README.md                  course placeholder blurb
├── course_metadata.yaml       durable catalog/section truth (COMSC-1053)
├── archive/                   11 semesters of Canvas JSON snapshots + files (2021–2026)
├── assignments/                current assignment briefs + odyssey_gates/ (weeks 2-16)
├── docs/
│   ├── course-ethos.md
│   ├── grading-model.md
│   ├── curriculum/             course-sequence, resource-map, judgment_toolkit, unit-notes
│   ├── philosophy/              teaching-patterns.md
│   ├── planning/                 empty (.gitkeep only)
│   └── reports/                curriculum-history-synthesis.md (+ .gitkeep)
├── lessons/                    current lesson content + lessons/data/
├── monday_moments/             README + template (cross-course strand, not process narration)
├── planning/                   week-01..17 + fall-2026-course-design.md + zybooks-section-decisions.csv
├── portfolio/                  empty (.gitkeep only)
├── prompts/                    001–006 course-development prompts + README (root-level, NOT sidecar)
├── quizzes/                    chapter-exam.md, getting-to-know-you.md
├── raw/                        6 files: 2 launcher runs (005, 006) — log/raw/summary triplets
├── reflections/                empty (.gitkeep only)
├── reports/                    002–009 reports (some paired with root prompts, some not) + codex/ run logs
├── rubrics/                    odyssey_gates/ rubrics, weeks 2-16
├── sidecar/                    README + prompts/{,completed/}, reports/, questions/, runs/ (all scaffolding, this report is first real content)
├── templates/                  assignment-brief, end-of-semester-reflection, project-rubric
└── tests/                      empty (.gitkeep only)
```

## Classification table

| Path | Classification | Notes |
|---|---|---|
| `README.md` | MEAT_CURRENT | Course placeholder; no process narration. |
| `course_metadata.yaml` | MEAT_CURRENT | Traces to catalog record verbatim; explicitly "durable course metadata." |
| `archive/**` | MEAT_HISTORY | Read-only Canvas snapshots, 2021–2026. Clearly project source history, not agent process. |
| `assignments/**` | MEAT_CURRENT | Current assignment briefs and Odyssey Gate weekly assignments. |
| `docs/course-ethos.md`, `docs/grading-model.md` | MEAT_CURRENT | Current policy documents. |
| `docs/curriculum/**` | MEAT_CURRENT | Current curriculum reference docs. |
| `docs/philosophy/teaching-patterns.md` | MEAT_CURRENT | Teaching-philosophy reference, not process log. |
| `docs/planning/` | UNCLEAR (empty) | Only a `.gitkeep`. No content to classify; leave as-is pending real use. |
| `docs/reports/curriculum-history-synthesis.md` | MEAT_HISTORY | This is a synthesis *of the archive* (course source), written in first person about method, but its content is entirely about the course's historical curriculum — not about Jeremy/ChatGPT/Foreman/golem coordination. Recommend it stay under `docs/reports/` (course-history synthesis), distinct from the process `reports/` directory below. Flagged as borderline; see fourth-wall section. |
| `lessons/**` | MEAT_CURRENT | Current lesson content and supporting data. |
| `monday_moments/**` | MEAT_CURRENT | Cross-course strand content (explicitly identical across CS1/CS2/DSCT per prompt 002); describes the course, not the agents building it. |
| `planning/week-*.md`, `planning/fall-2026-course-design.md` | MEAT_CURRENT | Current week-by-week and semester design truth. |
| `planning/zybooks-section-decisions.csv` | MEAT_HISTORY | Superseded by prompt 006 (no required textbook), but is provenance for a real decision, referenced explicitly by `reports/005_fall_2026_zybooks_design.md`'s "Superseded" notice. Keep with planning as decision history, not sidecar process. |
| `portfolio/`, `reflections/`, `tests/` | MEAT_CURRENT (empty) | Scaffolding directories for current course/project structure; nothing to move. |
| `prompts/001-006_*.md` + `prompts/README.md` | SIDECAR_COMPLETED (with caveats) | These are course-development work orders (self-aware process artifacts: "Status: decided by Jeremy...", references to `jeremy_task_tracking`, worker execution instructions). All six have matching `reports/00N_*.md`. This is the clearest fourth-wall violation at root level — see below. `prompts/README.md` is process-instructions-as-README and should move with them. |
| `quizzes/**` | MEAT_CURRENT | Current quiz content. |
| `raw/*` (6 files, prompts 005 & 006) | SIDECAR_RUN_EVIDENCE | Launcher logs, raw transcripts, and summaries — textbook run evidence per sidecar's own definition. |
| `reports/002-004_*.md`, `reports/005_reasoning_odyssey_fabric_reconciliation.md`, `reports/006_*.md` | SIDECAR_COMPLETED | Match local `prompts/002-006`. Process/execution reports. |
| `reports/005_fall_2026_zybooks_design.md` | SIDECAR_COMPLETED | No matching local prompt (superseded design record, explicitly marked "historical design record" in its own header); still a process/decision report, not course truth — the superseded notice already promoted the one durable fact ("no required textbook") into current truth elsewhere. |
| `reports/007_*.md`, `reports/008_*.md`, `reports/009_*.md` (+ their .csv/.json pairs) | SIDECAR_COMPLETED, PROMOTE_THEN_SIDECAR flagged | No matching local `prompts/007-009` — these were driven by prompts living in the **external** `jeremy_task_tracking/codex_prompts/` repo (cited explicitly in each report's header), not in this repo's `prompts/`. They contain durable findings (capability spine, resource coverage, storytelling rebalance) that should be checked against current `planning/` and `docs/curriculum/` truth before/while moving — flagging as `PROMOTE_THEN_SIDECAR` rather than assuming promotion already happened. Prompt 008 should verify each report's conclusions are reflected in current `planning/fall-2026-course-design.md` and `docs/curriculum/` before moving, or leave `UNCLEAR` if not confirmable in this pass. |
| `reports/codex/*.log` | SIDECAR_RUN_EVIDENCE | Raw codex worker run logs for prompts 002-004. |
| `rubrics/**` | MEAT_CURRENT | Current grading rubrics, paired with `assignments/odyssey_gates/`. |
| `sidecar/**` | SIDECAR_OPEN / scaffolding | Already correctly placed; this report is the first substantive content beyond READMEs. |
| `templates/**` | MEAT_CURRENT | Current reusable templates (assignment brief, reflection, rubric). |

## Prompt/report/run relationships (proven by explicit filename/content matching)

- Prompt 002 (skeleton) ↔ Report 002 — matched by number and title.
- Prompt 003 (gates weeks 2-6) ↔ Report 003 — matched.
- Prompt 004 (gates weeks 7-17) ↔ Report 004 — matched.
- Prompt 005 (Reasoning Odyssey fabric) ↔ Report 005 (`005_reasoning_odyssey_fabric_reconciliation.md`) ↔ `raw/20260815T165119Z__cs2-005-*` (3 files) — matched by number, title, and raw-file naming.
- Prompt 006 (drop ZyBooks) ↔ Report 006 (`006_drop_zybooks_no_required_textbook.md`) ↔ `raw/20260815T192935Z__cs2-006-*` (3 files) — matched.
- Report `005_fall_2026_zybooks_design.md` — orphaned relative to local `prompts/`; self-marked "Superseded 2026-08-15" in its own header, effectively obsoleted by Prompt 006. No raw/ pair.
- Report `006_week2_local_ai_stitch.md` — orphaned relative to local `prompts/`; its own header cites `jeremy_task_tracking/codex_prompts/016_cs2_week2_local_ai_stitch.md` as source, not a local prompt. No raw/ pair.
- Reports 007/008/009 (`reports/007_*.md`, `008_*.md`, `009_*.md`) and their `.csv`/`.json` companions — all three cite `jeremy_task_tracking/codex_prompts/*` or `jeremy_task_tracking/prompts/126_*` as their driving work order, never a local `prompts/007+`. There is no local `prompts/007.md` or later — numbering in `prompts/` and `reports/` diverged once work orders moved to the external tracking repo. `reports/codex/002-004_run.log` pair with prompts 002-004 as raw worker transcripts (distinct from the `raw/` directory, which only holds 005/006).
- No local prompt is orphaned without a report: all of `prompts/001-006` have matching reports (001 has no report — see below).

## Prompt 001 special case

`prompts/001_course_development_source_walk.md` has no numbered status line and no matching `reports/001_*.md`. Content reads as a standing content-development guideline (how to write Monday Moments/AI content), not a one-shot work order — closer to a durable instruction than a completed/pending task. Classify `UNCLEAR`: do not assume it is either open or done; it may belong merged into `prompts/README.md` guidance rather than treated as a numbered prompt at all. Leave in place; flag as a question for Prompt 008 or a sidecar question card.

## Obvious fourth-wall leakage

- **`prompts/001-006_*.md` and `prompts/README.md` at repo root.** These are pure agent/human coordination artifacts (worker status lines, "Status: decided by Jeremy," instructions to read other repos, explicit worker-execution framing) living outside `sidecar/`. This is the single clearest violation of the sidecar's stated boundary and exactly what Prompt 008 exists to fix.
- **`reports/*.md` and `reports/codex/*.log` at repo root.** Same issue — execution reports and raw codex logs describing what an agent did, not what the course is.
- **`raw/*` at repo root.** Run evidence (launcher logs, raw transcripts, summaries) sitting outside `sidecar/runs/`, duplicating the purpose `sidecar/runs/README.md` already defines.
- No other current-course file (lessons, assignments, docs, planning, quizzes, rubrics, templates, archive) was found narrating agent/human process in its body text — spot-checked `docs/reports/curriculum-history-synthesis.md`, `planning/fall-2026-course-design.md`, `monday_moments/README.md`; all describe the course itself. `course_metadata.yaml`'s header comment cites a driving prompt for provenance (one line) but the file body is pure catalog data — not fourth-wall narration, leave as-is.

## Sidecar-like artifacts whose conclusions may need promotion first

- `reports/007_cs2_capability_spine_handoff_and_open_resources.md`, `reports/008_cs2_pre_savnac_source_reconciliation.md`, `reports/009_data_storytelling_visualization_rebalance.md` (+ their `.csv`/`.json` companions) contain decision-relevant findings (the "eight irreducible advances," Week 9-11 rebalance, textbook-status reconciliation). Report 009 states it baselines on 007-008 "preserved except for the deliberate Weeks 9-11 refinement" — suggesting the chain is self-consistent, but this recon pass did not cross-check every claim against current `planning/week-09.md` through `week-11.md` and `docs/curriculum/`. **This is a `PROMOTE_THEN_SIDECAR` candidate**, not a confirmed-safe move — Prompt 008 (or a dedicated verification prompt) should diff each report's conclusions against current `planning/`/`docs/curriculum/` content before or immediately after moving these reports to `sidecar/reports/`.
- `reports/005_fall_2026_zybooks_design.md` already self-marks its own supersession and points to current truth (`course_metadata.yaml`/no-textbook decision) — no further promotion needed, safe to move as-is.

## Proposed moves for Prompt 008

1. `prompts/001-006_*.md`, `prompts/README.md` → `sidecar/prompts/completed/` (numbers 002-006, proven done via matching reports); `001` → `UNCLEAR`, do not move without an explicit decision (see above).
2. `reports/002-006_*.md` (all of them, including the two 006/005 orphans and codex-sourced ones once verified) → `sidecar/reports/`.
3. `reports/007-009_*.md` + `.csv`/`.json` companions → `sidecar/reports/`, but only **after** the promotion check above, or moved now with an explicit `sidecar/questions/` card noting promotion is unverified.
4. `reports/codex/*.log` → `sidecar/runs/`.
5. `raw/*` (6 files) → `sidecar/runs/`.

## Explicit DO NOT MOVE list

- `archive/**` — course history, stays outside sidecar.
- `docs/reports/curriculum-history-synthesis.md` — course-history synthesis, not agent process; stays under `docs/reports/` (a different directory from the process `reports/` at root, despite the shared name — Prompt 008 should not conflate the two).
- `planning/zybooks-section-decisions.csv` — decision provenance, stays under `planning/`.
- `course_metadata.yaml` — leave its header comment's prompt citation alone; it is a one-line provenance pointer, not narration to strip.
- All of `assignments/`, `lessons/`, `docs/curriculum/`, `docs/philosophy/`, `monday_moments/`, `quizzes/`, `rubrics/`, `templates/`, `portfolio/`, `reflections/`, `tests/` — current course meat, untouched.
- `prompts/001_course_development_source_walk.md` — `UNCLEAR`, needs an explicit ownership decision before moving or merging.

## Unresolved questions

1. Is `prompts/001` a durable standing guideline (merge into `prompts/README.md` before moving, or keep as its own file under `sidecar/prompts/`) or a stale one-shot task that should be marked done/superseded? No report or status line resolves this.
2. Are the conclusions in reports 007-009 (and their csv/json companions) already fully reflected in current `planning/` and `docs/curriculum/` truth, or does something in those reports still need to be promoted into a current-course file before the report is filed as pure history?
3. `docs/reports/` vs. root `reports/` — two directories named "reports" with very different purposes (course-history synthesis vs. agent execution reports). Worth a naming/README clarification once Prompt 008 finishes, so a future agent doesn't conflate them.
4. `docs/planning/` is empty (`.gitkeep` only) while there is also a populated top-level `planning/`. Unclear if `docs/planning/` is planned for different content or is dead scaffolding; leave alone, but worth asking Jeremy.

## Recommended target tree (post Prompt 008)

```
computer_science_2/
├── README.md
├── course_metadata.yaml
├── archive/
├── assignments/
├── docs/
├── lessons/
├── monday_moments/
├── planning/
├── portfolio/
├── quizzes/
├── reflections/
├── rubrics/
├── templates/
├── tests/
└── sidecar/
    ├── README.md
    ├── prompts/
    │   ├── 007_repository_recon_and_context_map.md   (moves to completed/ once accepted)
    │   ├── 008_repository_layout_reconciliation.md
    │   └── completed/
    │       └── 001-006_*.md (001 pending resolution), prompts/README.md
    ├── reports/
    │   ├── 002-009_*.md (+ .csv/.json companions)
    │   ├── 007_repository_recon_and_context_map.md   (this report)
    │   └── codex/*.log
    ├── questions/
    │   └── (new cards for open items 1-4 above, if Jeremy wants them tracked durably)
    └── runs/
        └── raw/* (renamed/merged from root raw/)
```

Root-level `prompts/` and `raw/` directories would be empty after Prompt 008 and can be removed (or left as empty scaffolding with a pointer README to `sidecar/`, per Jeremy's preference).
