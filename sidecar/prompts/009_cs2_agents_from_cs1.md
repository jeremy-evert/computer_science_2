# Sidecar Prompt 009 — Adapt CS1 AGENTS.md for Computer Science II

**Status:** OPEN
**Owner:** Foreman
**Mode:** inspect, dispatch, verify

## Problem

Computer Science II currently does not have a repo-local `AGENTS.md` that tells agents what is specifically true and important about working in this repository.

Computer Science I already has an `AGENTS.md` that should be used as the starting pattern rather than inventing another operating system from scratch.

Do not solve this by blindly copying CS1. Study the CS1 file, copy its useful shape, and then make the result honestly belong to CS2.

## Source to inspect first

Read the current Computer Science I `AGENTS.md` from the sibling CS1 repository.

On the Brandy course-development checkout, the expected source is:

`../computer_science_1/AGENTS.md`

If the repositories are checked out elsewhere, locate the current `computer_science_1` repository and inspect its root `AGENTS.md` there.

Also read enough current CS2 truth to adapt the file correctly, including at minimum:

- `README.md`
- `course_metadata.yaml`
- `sidecar/README.md`
- `planning/fall-2026-course-design.md`
- `docs/grading-model.md`
- `docs/curriculum/fall-2026-resource-map.md`
- representative current assignments and Reasoning Odyssey gates
- current `sidecar/prompts/` and `sidecar/reports/` only as needed to understand active repository boundaries

Do not recursively ingest the entire sidecar unless evidence requires it.

## Foreman job

Foreman should dispatch a worker/golem to create a root-level:

`AGENTS.md`

The worker should use CS1's `AGENTS.md` as the baseline pattern, then edit it so every instruction is appropriate for Computer Science II.

The result should be concise enough that an agent can actually use it. It should describe **CS2-specific repository truth**, not become a dumping ground for generic advice about Git, cleanliness, communication, or how agents should behave everywhere.

## Required CS2 adaptations

The worker must verify the repository and decide the exact wording, but the finished `AGENTS.md` should account for the following CS2-specific realities where supported by current source truth:

1. **Authority and source-of-truth boundaries**
   - Identify the current CS2 files that agents should trust first for course metadata, semester design, curriculum, grading, assignments, and rubrics.
   - Make clear that `sidecar/` is work history and coordination context, not automatically authoritative course truth.
   - Durable conclusions discovered in sidecar work should be promoted into the appropriate course-owned file outside the sidecar.

2. **Reasoning Odyssey is the technical spine**
   - Preserve the current doctrine that Reasoning Odyssey is the normal required authentic programming evidence for Fall 2026.
   - Do not accidentally recreate a second mandatory weekly problem-set/homework track.
   - Respect the existing Week 2 optional/no-graded-build status, active Weeks 3–14 gates, Week 15 no gate, and retired/non-gate Week 16 wrapper where current source truth says so.

3. **Shared-source ownership**
   - Respect shared upstream ownership where CS2 intentionally wraps rather than duplicates material, including Week 1 Success Foundations, Week 2 Local AI Lab/shared environment work, and other explicitly shared experiences.
   - Do not fork shared truth into CS2 merely for convenience.

4. **No required textbook**
   - Fall 2026 has no required textbook or required ZyBooks course.
   - Historical ZyBooks/Deitel material is provenance/reference only unless current course truth explicitly says otherwise.

5. **Do not invent unresolved mechanics**
   - Do not invent points, grading weights, due dates, submission locations, late rules, Canvas settings, or other deployment mechanics when current source files have not settled them.
   - Surface missing decisions instead of silently manufacturing them.

6. **Deployment boundary**
   - Repository/source preparation is not permission to write to Canvas, Savnac, production student systems, credentials, or external course infrastructure.
   - Those actions require explicit authorization from the controlling task/prompt.

7. **Repository-local scope**
   - Keep instructions that are genuinely useful for working on Computer Science II.
   - Remove or rewrite CS1-specific assumptions.
   - Do not copy generic orchestration rules into this file merely because CS1 happens to contain them. Generic operating doctrine belongs in the appropriate higher-level system, not buried in the CS2 course repo.

## Preserve useful CS1 structure

The worker should explicitly report which parts of CS1's `AGENTS.md` were:

- copied substantially unchanged because they apply equally to CS2;
- adapted for CS2;
- omitted because they are CS1-specific;
- omitted because they are generic system/process doctrine rather than CS2 truth;
- added because CS2 has a real repository-specific need that CS1 does not.

Do not force symmetry for its own sake. CS1 is the template, not the authority over CS2.

## Validation and proof

Before reporting completion, the worker must prove at minimum:

- `AGENTS.md` exists at the CS2 repository root;
- the file was derived from an actual inspection of CS1's current `AGENTS.md`, not from memory;
- no CS1 course codes, CS1-specific week structure, CS1 assignment names, or other accidental CS1 residue remain unless intentionally referenced as cross-course context;
- statements about CS2 agree with current CS2 source files;
- no unresolved points/dates/submission rules were invented;
- no Canvas/Savnac/external-system writes occurred;
- `git diff --check` passes;
- the diff is limited to the intended `AGENTS.md` work plus the worker's report/receipt if one is required;
- the worker provides the resulting commit SHA and a concise summary of evidence.

## Required report

Write:

`sidecar/reports/009_cs2_agents_from_cs1.md`

The report should include:

- source CS1 `AGENTS.md` path and commit/SHA if readily available;
- the CS2 source files consulted;
- what was copied, adapted, omitted, and added;
- validation performed;
- unresolved questions, if any;
- resulting commit SHA(s).

## Foreman acceptance

The worker does **not** declare the prompt completed merely because a file was written.

Foreman reviews the worker's diff and proof. If the result is satisfactory, Foreman accepts the work and moves this prompt from:

`sidecar/prompts/009_cs2_agents_from_cs1.md`

to the repository's existing completed-work location:

`sidecar/prompts/completed/009_cs2_agents_from_cs1.md`

If the proof is weak or the file contains unsupported/generic/CS1 residue, Foreman sends the work back for repair instead of filing the prompt as completed.

## Done when

CS2 has a concise root `AGENTS.md` derived from the working CS1 pattern, rewritten to express Computer Science II's actual repository-specific truth and boundaries; a worker has produced evidence that the file is correct; Foreman has accepted that evidence; and only then has Foreman moved this prompt into `sidecar/prompts/completed/`.
