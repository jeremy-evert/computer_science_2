# Prompt 021: Full Fucking Load — Render and Accept the Complete CS2 Semester in Savnac

**Status:** OPEN  
**Course:** COMSC-1053 Computer Science II, Fall 2026  
**Owner:** Cleo  
**Mode:** inspect → compile → full source-backed imprint → read back → walk → reconcile → accept

## Mission

Full fucking load.

Render the **entire honest, source-backed Fall 2026 Computer Science II course** into Savnac using the existing Course Foundry / Imprint machinery, then read the rendered course back and prove that what exists in Savnac is a coherent, inspectable, student-usable representation of the repository's current course truth.

This is not permission to invent a finished-looking course where source truth is unresolved.

It is permission to stop artificially thinking in a Week 1–3 inspection slice when the repository already supports a broader semester.

If the source owns it, render it.

If the source does not settle it, report the gap honestly rather than fabricating policy.

The desired outcome is simple:

> Jeremy can open Savnac and inspect the whole semester as a real course, not as a pile of repository files and not as a partial deployment experiment.

## Why this exists

The course architecture is substantially built. The Odyssey spine, Weeks 3–14 graded evidence, checkpoints, Week 16 shared Farkle work, shared Week 1/2 dependencies, grading declarations, and Savnac grading paths already exist in source or proven shared infrastructure.

Prompt 013 established the original imprint/read-back mission, but its acceptance debt was never fully closed even though later work proved much of the underlying machinery and live CS2 grading path.

Prompt 021 absorbs that debt and raises the bar:

**do not merely prove that CS2 can appear in Savnac. Put the whole source-backed semester there and accept it as a coherent course.**

## Source-of-truth rule

Git remains authoritative.

Savnac is the human inspection and dogfood surface.

Before writing anything, reconcile current source from at least:

- `START_HERE.md`
- `ROADMAP.md`
- `course_metadata.yaml`
- `planning/fall-2026-course-design.md`
- `planning/week-01.md` through `planning/week-17.md`
- `docs/grading-model.md`
- current assignments
- current Odyssey gates and rubrics
- current lessons
- current Reasoning Odyssey / World Bible materials where student-facing publication is appropriate
- shared Week 1 and Week 2 ownership boundaries
- current Prompt 015–020 outputs where they affect student-visible course structure
- `sidecar/prompts/013_imprint_cs2_to_savnac_and_read_back.md`
- `sidecar/reports/014_generalize_cs1_battery_and_apply_to_cs2.md`
- only the historical reports needed to understand accepted current state

Use the current main branch, not stale assumptions from an older sidecar note.

## Existing deployment architecture

Reuse the established Course Foundry / Imprint path.

Known historical CS2 entry points include:

- `course_foundry/cs2_desired_course.py`
- `course_foundry/cs2_dry_run.py`

Verify current paths before execution.

Do not create a second deployment stack because this prompt has an exciting name.

The excitement belongs in the scope. The plumbing should remain boring and proven.

## Target

The historical Savnac CS2 target is course ID **3**.

Verify that this is still the intended course before mutation.

Do not blindly create a new course if course 3 is the active CS2 inspection surface.

Production SWOSU Canvas is **not** the target of this prompt.

## Full-load principle

Compile the complete semester from current source.

The intended default is Weeks 1–17, including every student-visible object that current source and existing shared dependencies can support honestly.

That may include:

- course information / landing context
- module structure and ordering
- Week 1 shared kickoff material
- Week 2 local AI / classroom readiness material
- Weeks 3–14 Odyssey work
- Week 15 asynchronous closure/catch-up structure
- Week 16 shared Farkle / ML experience
- Week 17 reflection / closure
- assignments
- rubrics
- pages
- linked resources
- appropriate student-facing Reasoning Odyssey orientation materials
- any accepted slide decks that are ready for student use and belong in the LMS

Do not publish backstage world bibles, persona dossiers, hidden story seeds, continuity ledgers, private instructor notes, or other internal lore merely because they now exist in Git.

Respect the academic firewall and intended audience of each artifact.

## No fabrication rule

A full course does not mean a fake course.

Do **not** invent unresolved values for:

- due dates
- late penalties
- drop-lowest rules
- submission mappings
- grading behavior
- point values
- availability windows
- textbook requirements
- world-switching mechanics beyond accepted Prompt 020 policy
- production Canvas settings

Where current source settles a value, use it.

Where it does not, represent the object honestly, leave the unresolved mechanic unset where safe, or mark/report it as YELLOW.

Never make up policy just to make the LMS look complete.

## Required execution

### 1. Preflight Savnac

Before mutation, inspect the target and record:

- course identity
- instructor enrollment
- student-visible publication state
- current modules and ordering
- pages
- assignments
- rubrics
- duplicate or stale objects
- current ZyBooks references
- existing Odyssey material
- any obvious drift from current Git source

Run the current desired-state/dry-run path and identify blockers before writing.

### 2. Compile the whole semester

Compile the complete source-backed desired course.

Do not stop at Week 3 merely because Prompt 013 once used that as the minimum inspection slice.

If a later week cannot be compiled honestly, identify the exact blocker and continue with the rest of the course where safe rather than collapsing the entire load into a partial launch.

Produce a clear ledger of:

- GREEN: source-backed and ready to imprint
- YELLOW: source exists but some operational mechanic remains unresolved
- RED: cannot safely render without inventing or breaking something

The goal is maximum honest coverage.

### 3. Imprint into Savnac

Use the existing idempotent/reconciliation-aware write path.

Bring Savnac course 3 into alignment with the current source-backed semester.

Prefer update/reconcile behavior over duplicate creation.

Preserve existing correct objects when the deployment system owns them and can reconcile them safely.

Do not delete unrelated or instructor-created material merely to achieve cosmetic purity unless ownership is explicit and the established deployment path supports that action safely.

### 4. Read the entire course back

After imprint, read Savnac back as data rather than trusting the write response.

Verify at minimum:

- course identity
- instructor enrollment
- module existence and order
- all expected weeks/modules represented
- pages attached to the right modules
- assignments attached to the right modules
- rubrics attached to the right assignments
- points and submission types where source settles them
- current names and descriptions
- student-visible navigation
- links between objects
- Reasoning Odyssey orientation placement where appropriate
- no private Four Living Worlds backstage material exposed
- no stale required-ZyBooks doctrine
- no obvious duplicate objects

### 5. Walk it like a professor

Perform a bounded instructor-side inspection of the whole-semester structure.

The acceptance question is not merely “are there 17 modules?”

Ask:

- Can Jeremy understand what each week is for?
- Is the semester sequence recognizable?
- Are shared upstream materials appearing in the right places?
- Are the Odyssey gates/checkpoints where the course design says they belong?
- Are assignments/rubrics coherent enough to inspect without opening GitHub beside Canvas?
- Are YELLOW operational gaps visible in the acceptance report rather than hidden?

### 6. Walk it like a student

Use supported student-view / synthetic-student / read-only methods to inspect the experience.

At minimum sample:

- opening course landing
- Week 1 → Week 2 → Week 3 transition
- an ordinary mid-semester Odyssey week
- a checkpoint week
- GUI/data-storytelling territory
- Week 14 professional workflow territory
- Week 15 async transition
- Week 16 Farkle / ML
- Week 17 closure

Check for:

- dead ends
- broken navigation
- missing required context
- student-visible instructor-only material
- inaccessible or nonsensical links
- accidental reliance on hidden lore

Do not run a giant research battery if the established acceptance tooling already provides sufficient bounded proof.

### 7. Re-run desired state and prove drift behavior

After the full imprint and read-back, immediately run the supported dry-run/diff/reconciliation path again.

The target state is:

- no duplicate objects proposed
- no unexplained source-owned drift
- no repeated creation of objects that should reconcile
- any known non-idempotent class documented explicitly

A clean no-op or understood bounded diff is part of launch acceptance.

### 8. Close Prompt 013 debt

Reconcile Prompt 013 against the evidence generated here.

If Prompt 021 has genuinely satisfied Prompt 013's requirements, produce the missing Prompt 013 report or equivalent accepted reconciliation record and move Prompt 013 to completed using the repository's established sidecar workflow.

Do not mark 013 complete merely because “021 supersedes it.”

Close it with evidence.

If some 013 criterion remains unsatisfied, state exactly what remains and why.

## Launch receipt

Write a definitive report:

`sidecar/reports/021_full_fucking_load_savnac.md`

Include:

- Git/source commit inspected
- Course Foundry / Imprint commits and paths used
- Savnac course identity
- preflight state
- compile coverage by week
- GREEN / YELLOW / RED ledger
- objects created/updated/left untouched
- whole-course read-back results
- professor-walk findings
- student-walk findings
- duplicate/drift/idempotence evidence
- unresolved LMS-policy questions
- runtime checks still deferred for later weeks
- Prompt 013 reconciliation outcome
- explicit confirmation that no production SWOSU Canvas write occurred
- final acceptance verdict

This report should be useful months later when someone asks:

> What exactly was in CS2 when we declared Savnac ready?

## Acceptance criteria

Prompt 021 is complete when:

1. the complete source-backed Fall 2026 semester has been compiled;
2. every safely renderable week is represented in Savnac;
3. unresolved mechanics were not fabricated;
4. the rendered course was read back and verified;
5. professor and student paths were inspected across the semester;
6. assignments, rubrics, modules, and links are coherent where source owns them;
7. no stale required-ZyBooks doctrine has returned;
8. internal lore/backstage world material is not accidentally student-visible;
9. repeat deployment behavior is understood and does not silently duplicate source-owned objects;
10. Prompt 013's acceptance debt is closed with evidence or a precise residual gap is recorded;
11. a durable Prompt 021 launch receipt exists;
12. no production SWOSU Canvas write occurred.

## What this prompt deliberately does not require

Do not block Savnac acceptance on:

- having every weekly lecture slide deck finished
- future lore injections being produced
- every persona video being recorded
- the Week 14 container runtime being proven months early
- unresolved late/drop policy being guessed
- production Canvas being touched

Those are separate concerns.

The purpose of Prompt 021 is to make the **whole honest course visible now**, so future enrichment lands into a living semester rather than chasing students from behind.

## Explicit safety boundary

**Savnac writes are authorized by this prompt.**

**Production SWOSU Canvas writes are not authorized by this prompt.**

Do not authenticate to or mutate production Canvas.

Do not perform ZyBooks writes.

Do not expose or commit credentials.

Do not broaden scope into unrelated course redesign merely because a full-semester inspection makes new ideas tempting.

## Done when

Computer Science II exists in Savnac as the full, current, source-backed Fall 2026 semester; Cleo can prove what was rendered, what remains unresolved, and what a professor and student actually see; Prompt 013 debt is reconciled; the deployment is repeatable enough to trust; and the course is standing at the production Canvas door waiting for a separate explicit launch decision.

Full fucking load means the whole honest course.

Not the whole imaginary course.