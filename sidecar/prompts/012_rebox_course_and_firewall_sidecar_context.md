# Sidecar Prompt 012 — Rebox the course and firewall sidecar context

**Status:** OPEN
**Owner:** Foreman
**Mode:** inspect, dispatch, reorganize, verify
**Prerequisites:** Prompt 008 repository-layout reconciliation accepted; Prompt 009 root `AGENTS.md` work should be accepted or coordinated with this prompt

## Problem

The repository needs two things at the same time:

1. the actual Computer Science II course should be arranged in predictable boxes that match the emerging course-repository pattern; and
2. normal agents working on course design should **not** automatically inhale the entire sidecar and spend their context window reading a doctoral dissertation on the skittering of agents and mammals over object-oriented programming.

The sidecar is useful. It is not the course.

## Core rule

> **Default agent context is the course surface, not the process archaeology.**

A worker asked to design, inspect, validate, package, or deploy CS2 should be able to start at the repository root, learn what the course is, find the authoritative course materials, and work without recursively reading `sidecar/`.

`sidecar/` should be entered deliberately for a specific prompt, report, unresolved question, or provenance investigation.

## Mission

Foreman should dispatch a worker/golem to reconcile the CS2 repository into the current course-repository pattern and establish an explicit context firewall around `sidecar/`.

Do not invent a brand-new taxonomy from aesthetics. Inspect:

- current `computer_science_1/` organization and orientation pattern;
- current `computer_science_2/` after Prompt 008;
- accepted Prompt 007/008 reports only as needed for structural authority;
- root `AGENTS.md` produced by Prompt 009, if accepted;
- `sidecar/README.md`;
- current `swosu_cs_curriculum` structure where it establishes shared-vs-course ownership.

## Part A — Put the course shit in the right boxes

Compare CS2 against the useful current course-repository pattern. Every current non-sidecar artifact should have an obvious home and purpose.

Use existing meaningful boxes where possible, such as the repository's real course-owned areas for:

- orientation/navigation;
- course metadata;
- assignments;
- curriculum/docs;
- lessons/modules;
- presentations/slides when applicable;
- planning;
- quizzes/assessments;
- rubrics;
- templates;
- tests/validation;
- portfolio/reflection artifacts;
- archives/provenance;
- scripts/deployment tooling when applicable.

Do not create empty taxonomy just because another repo has a folder. But when CS1 has a useful box or orientation artifact and CS2 lacks an equivalent, apply Prompt 010's default presumption: **CS2 probably wants an equivalent unless there is a reason it does not.**

Resolve obvious duplicate or misleading boxes when current evidence supports doing so. Leave genuinely ambiguous placement alone and report it rather than guessing.

## Part B — Establish the sidecar context firewall

The desired behavior is:

### Normal course worker

A worker starting at repo root should:

1. read the root agent/orientation instructions;
2. read the minimum authoritative course files needed for its task;
3. treat `sidecar/` as out-of-band work history;
4. **not recursively scan, summarize, index, or ingest `sidecar/` by default**;
5. enter sidecar only when the controlling task explicitly references a sidecar prompt/report/question or when current course truth cannot be understood without targeted provenance archaeology.

### Sidecar worker

A worker explicitly dispatched on a sidecar prompt should:

1. read `sidecar/README.md` and the **current prompt**;
2. read only the specific prior reports/questions needed by that prompt;
3. prefer current course truth outside sidecar when determining what CS2 currently is;
4. avoid recursively ingesting completed prompts, historical reports, and raw run evidence merely because they exist;
5. promote durable conclusions back into course-owned files when appropriate.

## Mechanism

Use repository-native agent/orientation mechanisms that actually apply to the tools in use. At minimum, ensure the boundary is stated clearly in the root course instructions and inside the sidecar itself.

A likely shape is:

- root `AGENTS.md` / `START_HERE.md` or equivalent: **course-first context; sidecar excluded by default**;
- `sidecar/AGENTS.md` or equivalent scoped instructions: **current-prompt-first; no recursive archaeology**;
- `sidecar/README.md`: concise explanation of purpose and access rule.

Do not invent fake ignore files or claim a technical access control exists unless the relevant agent/tool actually honors it. This is a context-routing boundary, not security theater.

If an actual supported ignore/context mechanism exists in the current toolchain and is already part of the project pattern, the worker may use it, but must prove what honors it.

## Part C — Make the course entry path obvious

A future worker should not need tribal knowledge to answer:

- What is this course?
- What semester/section is current?
- Where is the authoritative semester design?
- Where are assignments and rubrics?
- Where are student-facing lessons/modules/presentations?
- Where are shared upstream sources referenced?
- What is historical/archive material?
- Where is process history, and when should I ignore it?

Use the current CS1 orientation pattern as a donor where useful. If CS1 has `START_HERE.md`, `NAMING.md`, `ROADMAP.md`, or analogous orientation machinery that materially helps, CS2 should normally gain an adapted equivalent unless the worker documents why not.

## Do not change course meaning accidentally

This structural/context work must not silently alter:

- grading weights or points;
- due dates;
- submission policies;
- Reasoning Odyssey status;
- no-textbook policy;
- Week 1/Week 2/shared-source ownership;
- instructional content merely to fit a prettier directory tree.

No Canvas, Savnac, credentials, or production student-system writes are authorized.

## Validation and proof

The worker must prove:

- final top-level tree is coherent and each box has a clear purpose;
- no accepted course truth was stranded in sidecar;
- root instructions explicitly tell ordinary workers not to recursively ingest sidecar;
- sidecar-scoped instructions explicitly tell sidecar workers to start with the current prompt and read history selectively;
- course entry/orientation points to current authoritative course truth;
- moved references/links are repaired;
- no accidental CS1 residue was introduced;
- `git diff --check` passes;
- relevant repository validation passes;
- no course policy changed as an accidental side effect;
- commit SHA(s) are provided.

Include a short context simulation in the report:

### Simulation A — ordinary course worker

List exactly what a fresh worker should read first for a normal CS2 design task, showing that `sidecar/` is not part of default context.

### Simulation B — dispatched sidecar worker

List exactly what a worker assigned this prompt would read first, showing that it reads this prompt and targeted evidence rather than all sidecar history.

## Required report

Write:

`sidecar/reports/012_rebox_course_and_firewall_sidecar_context.md`

The report must include:

- before/after top-level tree;
- moves/renames/orientation artifacts added;
- ambiguous items deliberately left alone;
- exact context-firewall rules added and where;
- Simulation A and Simulation B;
- validation evidence;
- commit SHA(s).

## Foreman acceptance

The worker does not close this prompt.

Foreman reviews the final tree and performs the two context simulations conceptually. If a normal course worker would still be encouraged to read all of `sidecar/`, the work is not done. If important current course truth is now hidden in sidecar, the work is not done. If the boxes are merely prettier but harder to understand, the work is not done.

After Foreman accepts the result, Foreman moves this prompt to:

`sidecar/prompts/completed/012_rebox_course_and_firewall_sidecar_context.md`

## Done when

The repository presents itself first as **Computer Science II**, with current course truth in predictable course-owned boxes; `sidecar/` remains a durable but deliberately entered workbench; ordinary agents do not consume process archaeology by default; and Foreman has verified the boundary before filing the prompt as completed.
