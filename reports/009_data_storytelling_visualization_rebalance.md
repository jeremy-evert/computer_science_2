# Report 009 — Data storytelling and visualization rebalance

**Prompt:** `jeremy_task_tracking/codex_prompts/cs2_021_data_storytelling_visualization_rebalance.md`
**Baseline:** Prompt 020 and Reports 007–008, preserved except for the deliberate Weeks 9–11 refinement.
**Scope:** Fall 2026 COMSC-1053 source only. No Savnac, Canvas, production ZyBooks, student-system, or shared-canonical-body write was performed.

## Refinement implemented

The catalog-required GUI/event experience is now a compact Week-9 supporting experience: a thin Tkinter view over a tested model, at least one meaningful callback/event path, independent model test/trace evidence, and a short model/view/event-flow explanation. Weeks 10–11 now give more instructional weight to data visualization and data storytelling.

S09, **Data visualization and storytelling**, is recorded as a course-priority enrichment rather than falsely presented as a catalog hard floor. It covers question-led use of authentic data, defensible and readable representation, honest scale/encoding, cautious plain-language takeaway, limitation/uncertainty, and a design or operational decision.

## Changed active source

- `planning/fall-2026-course-design.md`; `planning/week-09.md` through `planning/week-11.md`
- `assignments/A1-weekly-coding-practice.md`, `assignments/A2-coding-odyssey-project.md`, and Week 09–11 Odyssey gates
- Week 09–11 Odyssey rubrics
- `docs/course-ethos.md`, `docs/grading-model.md`, and curriculum sequence, resource-map, and unit-note sources
- Replaced the former combined Week 9–10 Tkinter micro-lab with `lessons/week-09-tkinter-model-view-lab.md`
- Added the bounded activity `lessons/week-10-data-storytelling-micro-lab.md`, its runnable Python source, and `lessons/data/frontier-resource-levels.csv`

## Final Weeks 9–11 sequence

| Week | Center of gravity | Required bounded evidence | Flex boundary |
|---|---|---|---|
| 9 | Compact GUI/event flow (S04) | real model state, meaningful callback, independent test/trace, model/view/event explanation | GUI stays thin; no widget catalog or desktop-app unit |
| 10 | Honest visualization (S09/S06/S08) | question, authentic project/world data, readable labeled visual, chart-choice rationale, misleading alternative/pitfall, runnable evidence | plain Python collections/CSV plus Matplotlib; no pandas requirement |
| 11 | Data storytelling / flex (S09 + S07/reinforcement) | supported claim, visual only when useful, limitation/uncertainty, design/operational decision | reinforce prior work or use a world-fit recursive/linked/nested extension when data is not yet rich |

## Catalog GUI/event coverage proof

The official catalog requirement remains explicit in the Week-9 plan, gate, and rubric: the student renders real model state in a modest Tkinter view; at least one meaningful event/callback invokes a model operation; the student explains the separation and flow; and model behavior is shown outside the GUI through a test or trace. Week 9 is therefore assessable without making GUI architecture the course identity.

## S09 evidence and four-world fit

| S09 evidence | Frontier Settlement | Investigation Bureau | Starship Log | Small Business |
|---|---|---|---|---|
| Question and authentic data | resource levels/events | case status, leads, evidence counts | mission/event categories, system metrics | inventory movement, orders, categories |
| Defensible visual/story | compare current resources without inventing a trend | show case-status distribution or timeline appropriate to actual dates | show logged event categories or a genuine resource trend | compare product/category movement or orders |
| Limitation and decision | current levels do not explain cause | status counts do not prove investigation quality | association does not prove a system caused an outcome | sales counts do not establish customer motives |

No genre is forced into one chart type, and no visual is required when it does not serve the supported story.

## Course-owned activity and resources

`lessons/week-10-data-storytelling-micro-lab.md` demonstrates question → data → chart → interpretation → limitation → decision with a four-row, included Frontier Settlement CSV. Its Python script uses built-in `csv` and Matplotlib when available. A standard-library SVG fallback makes the activity runnable in an environment without Matplotlib; it does not add a package or change the judgment goal. Matplotlib remains the small default visualization path. Pandas, accounts, paid text, and a standalone plotting treadmill are not student dependencies.

## Stale-reference and requirement scan

Active-source scans found no claim that Week 10 remains primarily GUI/events or that Weeks 9–10 are two GUI weeks. Remaining legacy plotting/GUI phrases are in provenance reports, archived curriculum material, prompts, or the historical ZyBooks decision CSV, not active requirements. The active source contains no requirement for pandas, paid resources, or a disconnected plotting homework track; explicit mentions of those terms state their absence.

## Validation

- Clean synchronization: `git pull --ff-only` passed after sandbox-safe SSH escalation; repository was already up to date.
- `git diff --check`: passed before the source commit.
- `course_metadata.yaml` parsed successfully with PyYAML.
- The included CSV parsed successfully (four rows; expected fields and nonnegative values).
- Week 9–11 referenced activity/data paths were verified to exist.
- `python lessons/week-10-data-storytelling-micro-lab.py`: passed using the standard-library SVG fallback because Matplotlib is not installed in this local environment; output existed and was removed after validation.
- `python -m py_compile lessons/week-10-data-storytelling-micro-lab.py`: passed.
- Active-source stale-claim and coverage-marker scans passed as described above.
- `make task-check`: unavailable — `make: *** No rule to make target 'task-check'.  Stop.` (exit 2).
- `make check`: unavailable — `make: *** No rule to make target 'check'.  Stop.` (exit 2).

## Commit and publication receipt

- Source reconciliation commit: `3cf00a3cf841112e2c62cc9e9e637152ebd60523`
- This report is committed separately as its companion receipt. Its commit, push status, and final clean worktree are recorded after that commit.

## Open item / stop point

There is no source-level blocker to Savnac candidate generation from this refinement. Matplotlib is absent from this local validation environment, but the activity has a runnable standard-library fallback and adds no package requirement. Do not create or deploy a Savnac candidate in this prompt.

## Next recommended prompt

Prepare a Savnac candidate build and smoke-test plan from the reconciled CS2 source, preserving the existing pre-Savnac blockers and validating the Week 9–11 sequence before any external write.
