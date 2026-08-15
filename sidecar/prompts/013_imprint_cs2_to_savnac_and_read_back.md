# Sidecar Prompt 013 — Imprint Computer Science II into Savnac and read it back

**Status:** OPEN
**Owner:** Foreman
**Mode:** inspect → dispatch → imprint → read back → verify

## Problem

Computer Science II can become increasingly correct in Git while still being difficult for Jeremy to inspect as an actual course.

That is not good enough for the Fall 2026 launch.

Git/course source remains authoritative, but **Savnac is the human inspection and dogfood surface** before production Canvas. Jeremy needs to be able to open the course, navigate it as a professor/student would, and see what the source actually turned into.

The CS2 repo already contains pre-Savnac source reconciliation, and Course Foundry already contains CS2 desired-course / dry-run machinery. The missing owned job is to take current source-backed CS2 through the proven Course Foundry + Imprint path into Savnac and then prove the rendered course by reading it back.

Do not invent a second CS2 deployment system.

## Mission

Make the current source-backed Computer Science II course visible, navigable, and reviewable in Savnac using the existing reusable Course Foundry / Imprint machinery wherever possible.

The goal is not merely "an API request succeeded." The goal is that Jeremy has a real Savnac course he can inspect.

## Read first

Before mutating Savnac, inspect the current truth and the existing deployment machinery. At minimum read:

### Computer Science II

- root `AGENTS.md` if Prompt 009 has landed; otherwise use the current authoritative CS2 source directly
- `course_metadata.yaml`
- `planning/fall-2026-course-design.md`
- `docs/grading-model.md`
- `docs/curriculum/fall-2026-resource-map.md`
- the current Week 1–3 planning/source
- representative assignments and rubrics used by those weeks
- `reports/008_cs2_pre_savnac_source_reconciliation.md`
- only the sidecar reports needed to understand accepted current state

### Course Foundry / Imprint

Inspect the current Course Foundry implementation, including the existing CS2 compiler/dry-run code and the proven CS1 Savnac deployment/read-back path. Current known CS2 entry points include:

- `course_foundry/cs2_desired_course.py`
- `course_foundry/cs2_dry_run.py`

Verify paths against the live checkout rather than assuming this prompt is newer than the code.

Study how CS1 is currently imprinted and verified. Reuse that machinery. Generalize shared machinery only when a real CS2 gap proves that generalization is necessary.

## Foreman job

Foreman should dispatch bounded worker/golem work for this prompt and independently verify the resulting evidence.

Do not hand the entire task to a worker with "go make Canvas work." Bound the work around reconnaissance, compilation, imprint, and read-back verification.

## Required execution

### 1. Reconcile before mutation

First inspect the current Savnac target for CS2.

Determine and report:

- the Savnac CS2 course identity / course ID if it already exists;
- instructor enrollment state;
- existing modules/pages/assignments/rubrics relevant to the current course;
- whether old or partial CS2 material is already present;
- whether the current CS2 desired-state compiler produces a clean dry run;
- any source/compiler blockers that would make an imprint unsafe.

Do not blindly create a second course if the intended CS2 course already exists.

### 2. Compile from current source

Use the existing Course Foundry CS2 desired-course path to compile current source into the Savnac-bound desired state.

Do not manufacture missing course policy during compilation.

If current source does not settle a value, do **not** invent:

- points;
- grading weights;
- due dates;
- late rules;
- submission mechanisms;
- textbook requirements;
- production Canvas configuration.

Represent unresolved mechanics honestly as missing/YELLOW where the tooling permits, or stop the affected object from being published if fabrication would otherwise be required.

### 3. Imprint into Savnac

Use the existing reusable Imprint / Course Foundry write path to bring current source-backed CS2 into Savnac.

At minimum, Jeremy needs a useful near-term inspection slice containing:

- Course Information / course landing context;
- Week 1;
- Week 2;
- Week 3;
- the assignments/rubrics/pages/navigation needed to understand those weeks.

If the existing compiler and source already support additional weeks cleanly, imprint the broader source-backed course rather than arbitrarily stopping at Week 3.

Do **not** fabricate later content merely to make all 17 weeks appear complete.

### 4. Verify the rendered course by reading Savnac back

After imprint, read the course back from Savnac and verify at minimum:

- intended instructor enrollment;
- module existence and ordering;
- page/assignment/rubric existence;
- links between modules and their objects;
- student-visible navigation where appropriate;
- Week 1 → Week 2 → Week 3 path;
- no obvious duplicate objects created by the imprint;
- no stale required-ZyBooks doctrine accidentally reintroduced;
- current source-backed names and descriptions match what Savnac renders.

Where the established acceptance tooling supports it, run a bounded professor/student walk or synthetic-student check. Do not turn this prompt into a new large-scale research battery.

### 5. Prove repeatability / drift behavior

After the successful imprint and read-back, run the supported dry-run/diff/no-op check again.

The desired result is that an immediate repeat does not propose duplicate course objects or unexplained source-owned drift.

If idempotence is not currently supported for a class of objects, report that as a concrete YELLOW with evidence rather than claiming success.

## Human-visible acceptance condition

This prompt is **not complete merely because deployment code ran successfully**.

The important acceptance condition is:

> Jeremy can open Savnac and inspect a recognizable, current Computer Science II course produced from the repository's current course truth.

Git remains the source of truth. Savnac is the inspection surface.

If the current source/compiler cannot yet produce a useful inspectable course, identify exactly what blocks that outcome and return the work to Foreman rather than declaring a hollow success.

## Safety boundaries

- Savnac writes are in scope for this prompt.
- Production SWOSU Canvas writes are **not** in scope.
- Do not authenticate to or mutate production Canvas.
- Do not perform ZyBooks writes.
- Do not read, echo, or commit credentials.
- Do not create a parallel CS2 deployment stack when Course Foundry / Imprint already owns the capability.
- Do not solve unrelated course-design questions merely because they are discovered during imprint. Record them as findings/work orders.

## Required report

Write:

`sidecar/reports/013_imprint_cs2_to_savnac_and_read_back.md`

Include:

- source commits inspected;
- Course Foundry / Imprint paths reused;
- Savnac CS2 course identity;
- pre-mutation reconnaissance;
- what was created/updated/left untouched;
- read-back verification results;
- repeat/dry-run/drift evidence;
- bounded human/student-path acceptance evidence if run;
- explicit YELLOWs / unresolved source gaps;
- worker commit SHA(s) and relevant execution receipt paths.

## Foreman acceptance

The worker does not self-certify completion.

Foreman independently reviews the diff/receipts/read-back evidence and confirms:

1. current CS2 source is visibly represented in Savnac;
2. the result is useful for Jeremy to inspect;
3. no production Canvas or ZyBooks write occurred;
4. unsupported course mechanics were not invented;
5. the deployment reused the established Course Foundry / Imprint path rather than creating a duplicate system;
6. immediate re-run behavior is understood and does not silently duplicate course objects.

If satisfactory, Foreman moves this prompt to:

`sidecar/prompts/completed/013_imprint_cs2_to_savnac_and_read_back.md`

Otherwise Foreman returns the work for repair and leaves the prompt open.

## Done when

Computer Science II is rendered from current source into Savnac through the established reusable deployment path, read back and verified, useful for Jeremy's inspection, supported by receipts, and accepted by Foreman.
