# Sidecar Prompt 008 — Repository layout reconciliation

**Status:** CLOSED — accepted 2026-08-15, see `sidecar/reports/008_repository_layout_reconciliation.md`
**Status:** BLOCKED ON PROMPT 007
**Owner:** Foreman
**Prerequisite:** accepted `sidecar/reports/007_repository_recon_and_context_map.md`

## Mission

Use Prompt 007's accepted repository map to move material that is in the wrong context boundary into the right place.

This is a structural reconciliation, not a course redesign. Preserve meaning, provenance, and Git history wherever practical.

## Target shape

The desired high-level boundary is:

```text
computer_science_2/
├── README.md
├── course metadata / current course truth
├── assignments/
├── docs/
├── lessons/
├── planning/
├── quizzes/
├── rubrics/
├── tests / scripts / other current project-owned material as applicable
├── archive/                    # historical course/source material when Prompt 007 says it is project history
└── sidecar/
    ├── README.md
    ├── prompts/
    │   └── completed/
    ├── reports/
    ├── questions/
    └── runs/
```

The exact project directories outside `sidecar/` are determined by the actual repository, not by this illustrative list. Do not create fake taxonomy merely to match the picture.

## Core boundary

Outside `sidecar/` is the hard-nosed Computer Science II project. Those files describe the course, its current design, its source material, and its operation without narrating Jeremy/ChatGPT/Foreman/golem process.

Inside `sidecar/` is the self-aware work history: prompts, reports, questions, investigations, raw execution evidence, agent receipts, and coordination/process narration.

Prompts and reports remain first-class durable artifacts. Moving them under `sidecar/` is a context boundary, not demotion.

## Migration rules

1. Treat Prompt 007's accepted classifications as the move authority. Do not invent additional bulk moves from filenames alone.
2. Prefer `git mv` for tracked files so history remains easy to follow.
3. Existing root-level prompts should move to `sidecar/prompts/` or `sidecar/prompts/completed/` according to proven status.
4. A done prompt is still a prompt. Preserve it under `sidecar/prompts/completed/`; do not delete it merely because a report exists.
5. Existing process/agent reports should move to `sidecar/reports/` when Prompt 007 classifies them as sidecar history.
6. Raw worker transcripts, launch logs, and bulky execution receipts should move to `sidecar/runs/` when Prompt 007 classifies them as run evidence.
7. Historical course archives, imported Canvas snapshots, source materials, and other project history should remain outside sidecar when Prompt 007 classifies them as `MEAT_HISTORY`.
8. If an old process artifact contains durable current truth that exists nowhere else, first promote that truth into the appropriate project file. Then move the process artifact to sidecar. Do not strand current truth in archaeology.
9. Leave every `UNCLEAR` item alone and record it as a remaining question rather than guessing.
10. Do not rewrite content just to make the move prettier. This prompt is primarily about placement and boundary cleanup.

## Fourth-wall cleanup

After moves, inspect the hard-nosed project surface. If a current project file primarily narrates agent/human process, either:

- move it to sidecar if Prompt 007 authorized that classification; or
- extract the durable project truth into the correct current document and preserve the narrative artifact in sidecar.

Do not scrub useful provenance from Git history.

## Sidecar hygiene

- Keep active prompts directly under `sidecar/prompts/`.
- Keep completed prompts under `sidecar/prompts/completed/`.
- Keep reports under `sidecar/reports/`; reports do not become prompts when work finishes.
- Keep unresolved questions under `sidecar/questions/` when a durable question artifact is useful.
- Keep raw execution evidence under `sidecar/runs/`.
- Do not recursively consolidate or summarize old history unless needed to avoid losing current truth.

## Validation

Before reporting completion:

- `git diff --check` passes;
- no tracked artifact classified `UNCLEAR` was moved;
- moved files are still present and readable at their new paths;
- prompt/report references are repaired where the move would otherwise create broken local links or obviously stale path pointers;
- current course files do not depend on old root `prompts/`, `reports/`, or `raw/` paths without an intentional compatibility reason;
- no course content, grading weights, due dates, rubrics, or instructional policy changed merely as a side effect of the reorganization;
- no secrets or private student data are introduced into Git.

## Required report

Write:

`sidecar/reports/008_repository_layout_reconciliation.md`

Include:

- exact moves performed;
- exact items deliberately left in place and why;
- any current-truth promotions made before moving a process artifact;
- validation performed;
- unresolved structural questions;
- final top-level tree and sidecar tree;
- commit SHA(s).

## Done when

The repository has a clear context boundary: the normal project surface is focused on Computer Science II itself, the self-aware human/agent work history is gathered under `sidecar/`, nothing uncertain was moved by guesswork, and a future agent can work on the course without automatically ingesting years of skittering.
