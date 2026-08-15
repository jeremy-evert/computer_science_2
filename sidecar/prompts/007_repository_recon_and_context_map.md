# Sidecar Prompt 007 — Repository recon and context map

**Status:** OPEN
**Owner:** Foreman
**Mode:** read first, report only

## Mission

Look around this repository and tell us what we actually have.

Do not reorganize the repository in this prompt. Do not rename, move, delete, normalize, or rewrite project files merely because the current layout looks inconsistent. The purpose of this pass is to build an evidence-backed map before Prompt 008 is allowed to move anything.

## Read this first

- repository `README.md`
- `sidecar/README.md`
- current top-level tree
- current `prompts/`, `reports/`, `raw/`, `archive/`, `docs/`, `planning/`, course-content directories, and any other top-level areas that matter
- recent Git history where it helps explain why something exists

Do not assume a directory is misplaced from its name alone. Inspect representative contents.

## Questions to answer

Build a concise map that answers:

1. What is the current course/project structure?
2. Which directories/files are clearly **course meat**: current content, configuration, planning, decisions, scripts, tests, source material, or other project truth that belongs outside the sidecar?
3. Which directories/files are clearly **sidecar work history**: prompts, agent/Foreman reports, execution receipts, raw worker output, questions, investigations, or process narration?
4. Which material is historical project source/provenance that belongs with the course rather than with agent process history?
5. Which items are ambiguous and should not be moved without a specific ownership decision?
6. What existing prompts are open, completed, superseded, or unclear? Use actual evidence such as matching reports, explicit status text, commits, or current project state rather than prompt number alone.
7. What reports and raw artifacts correspond to which prompts or workstreams?
8. Are there current files outside the sidecar that break the fourth wall by talking primarily about Jeremy, ChatGPT, Foreman, golems, prompts, or execution process rather than the course itself?
9. Are there sidecar-like artifacts whose conclusions should already have been promoted into durable course truth outside the sidecar?
10. What should Prompt 008 move, and what should it explicitly leave alone?

## Classification

For each top-level area and each questionable artifact, use one of these labels:

- `MEAT_CURRENT` — current project truth or working course material; stays outside sidecar.
- `MEAT_HISTORY` — historical course/source evidence that still belongs to the project itself; stays outside sidecar unless there is a stronger reason.
- `SIDECAR_OPEN` — active coordination/work artifact; belongs under sidecar.
- `SIDECAR_COMPLETED` — completed coordination/work artifact; belongs under the appropriate completed/history sidecar location.
- `SIDECAR_RUN_EVIDENCE` — raw/bulky execution evidence; belongs under `sidecar/runs/`.
- `PROMOTE_THEN_SIDECAR` — contains durable truth that should first be captured in the proper project file, after which the process artifact belongs in sidecar.
- `UNCLEAR` — evidence is insufficient; do not move automatically.

## Required report

Write:

`sidecar/reports/007_repository_recon_and_context_map.md`

The report should include:

- a top-level inventory;
- the classification table;
- prompt/report/run relationships you can prove;
- obvious fourth-wall leakage;
- proposed moves for Prompt 008;
- explicit `DO NOT MOVE` items;
- unresolved questions;
- a short recommended target tree.

Keep the report useful to a Foreman. It should be detailed enough to drive Prompt 008 without requiring the next worker to reread the entire repository.

## Safety

- Read-only except for writing this report.
- No Canvas writes.
- No credential work.
- No content redesign.
- No archival deletion.
- No speculative cleanup.

## Done when

The Foreman can read one report and understand what this repository contains, what is meat, what is sidecar/process history, what is uncertain, and exactly what Prompt 008 is authorized to reorganize.
