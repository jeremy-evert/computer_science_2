# Prompt 020: The Transfer Portal — World Switching as a CS2 Migration Experience

**Status:** OPEN  
**Course:** COMSC-1053 Computer Science II, Fall 2026  
**Owner:** Cleo  
**Scope:** Student-facing world-switching policy and migration experience for the Reasoning Odyssey

## Mission

Turn the unresolved question "Can students switch worlds after choosing?" into a deliberate course feature.

The answer is **yes**.

Students may move from one Reasoning Odyssey world to another without a grade penalty and without restarting their semester project. A world switch should be treated as a small software migration/refactoring experience: the student carries their existing design forward, examines what still fits, identifies assumptions that no longer fit, and records the transition in the student's World Bible.

Call this experience **The Transfer Portal**.

Keep it lightweight, humane, and academically useful.

Do not build bureaucracy around a student changing their mind.

## Governing principle

A student is choosing **context and flavor**, not a different curriculum.

All four worlds share the same CS2 learning outcomes, grading contract, Odyssey gates, checkpoints, and technical expectations.

Therefore changing worlds must not:

- erase earned work
- reset grades
- create a harder or easier grading path
- require the student to redo already-accepted work simply because nouns and setting changed
- require lore knowledge
- require theatrical participation
- force a new software design when the existing design can be migrated honestly

The transfer should preserve student agency and reward reasoning.

## Core policy

Implement the following policy unless current authoritative course source creates a direct conflict. If a conflict exists, document it instead of silently overriding it.

### Early-semester transfer

Students receive **one simple, no-penalty transfer opportunity early in the semester**.

Do not over-engineer the exact calendar cutoff if current source does not already define one. If a concrete date is needed for publication and no source-backed date exists, surface that as a bounded instructor decision rather than inventing it.

The intended spirit is:

> If you discover early that another world is a better fit, move. No drama.

### Later-semester transfer

Students may still request a world transfer later.

A later transfer should require a brief conversation/check-in with Jeremy because more continuity and accumulated design decisions may need reconciliation, not because the student is being punished for switching.

The purpose of the check-in is to make the migration technically coherent and manageable.

## The migration receipt

Create a short, low-friction **Transfer Portal migration receipt** that becomes part of the student's World Bible.

It should ask the student to identify, in concise form:

1. **Where I am leaving**  
   Current world.

2. **Where I am going**  
   New world.

3. **What comes with me**  
   Existing classes, responsibilities, interfaces, data structures, invariants, assumptions, or other design elements that remain valid.

4. **What does not translate cleanly**  
   Terminology, assumptions, constraints, relationships, or design choices that no longer make sense in the new context.

5. **What I will refactor**  
   The smallest reasonable changes needed to make the software world coherent in the new setting.

6. **What I am deliberately preserving**  
   Important technical decisions the student believes should survive the move and why.

7. **New World Bible entry**  
   A concise record of the migration and its reasoning.

This is not an essay.

The migration receipt should feel like a practical engineering handoff.

## Academic treatment

The Transfer Portal is not a separate major graded assignment.

Prefer one of these implementation patterns, in this order:

1. attach the migration receipt to the student's normal World Bible evidence;
2. treat it as a small completion/check-in artifact;
3. incorporate it into the next relevant Odyssey gate if doing so does not distort that gate's rubric.

Do not create substantial new points or grading weight merely because the student changed worlds.

If current LMS/course mechanics require a discrete object, keep it low-stakes and clearly identified as migration evidence rather than a punishment fee.

## Preserve prior technical work

A transfer must not imply "start over."

The student should carry forward as much valid software structure as possible.

The instructional opportunity is the reconciliation itself:

- Which abstractions are genuinely reusable?
- Which names were domain-specific but the design was sound?
- Which assumptions were accidentally coupled to the old world?
- Which interfaces survive the move?
- Which invariants change?
- Which parts need adaptation rather than replacement?

This is software migration, refactoring, and requirements change in miniature.

## Relationship to the four living worlds

Use the accepted Four Living Worlds Bible from Prompt 017.

A transfer should feel native to the worlds without becoming required lore.

Each world may have its own light-touch transfer flavor, document title, or acknowledgment. For example, a transfer might appear as an immigration record, bureau reassignment, ship transfer order, or business transition document.

But the underlying academic migration receipt must remain equivalent across all four worlds.

Do not let flavor change what is required.

## Relationship to The Four Calls

Update the Four Calls student-choice materials from Prompt 018 so that students are not trapped by their first choice.

The choice moment should remain meaningful, but somewhere appropriate students should learn, in plain language:

> Choose the world you most want to return to. If you discover you chose wrong, there is a Transfer Portal. You can move without losing the work you have already earned.

Do not over-explain the transfer process during the initial world-selection experience.

The Four Calls should still feel like a choice, not a terms-of-service screen.

## Relationship to continuity

World continuity matters, but continuity belongs to the student's experience rather than becoming a cage.

When a student transfers:

- preserve the student's prior World Bible history;
- do not rewrite old entries to pretend they were always in the new world;
- record the transfer as a real event in the student's design history;
- allow future work to refer to "before the transfer" and "after the transfer" when pedagogically useful;
- do not require the student to understand hidden internal canon in order to migrate.

The student's software history should remain legible.

## Instructor workflow

Create a very small instructor workflow for Jeremy.

It should answer:

- how a student requests a transfer;
- what Jeremy needs to verify;
- what gets updated in the LMS or course records;
- what the student adds to the World Bible;
- how the old world choice is preserved historically;
- how the new world becomes the active choice;
- how to handle a second or unusually late transfer without creating policy theater.

Optimize for a process Jeremy can complete in a few minutes.

## Data / storage behavior

Prompt 018 intentionally defined world choice as one of four fixed values with no free text.

Preserve that clean model.

For a transfer, maintain:

- the new active world choice;
- enough history to know that a transfer occurred if the implementation already supports such history;
- the student's migration receipt in the World Bible or appropriate evidence location.

Do not redesign the whole data model unless a real implementation requirement demands it.

If the current system only stores one active world value, changing that value plus preserving the migration receipt is acceptable.

## Student-facing tone

The policy should feel permissive and confident.

Avoid language that sounds like:

- withdrawing from a program
- petitioning a committee
- requesting special dispensation
- admitting failure

The message is:

> You picked a place to build. If another world fits you better, move your software there and show us how you carried the design across.

## Deliverables

Produce:

1. the canonical **Transfer Portal policy** in the appropriate course documentation;
2. the short student-facing explanation;
3. the World Bible migration-receipt template;
4. a compact Jeremy/instructor workflow;
5. any necessary update to `four_calls/README.md` or the Prompt 018 choice materials so the previously unresolved switching question is closed;
6. light-touch world-specific transfer flavor for all four worlds, without changing academic requirements;
7. any minimal data/storage guidance needed to preserve the fixed four-value world-choice model;
8. a short report documenting what source files were changed and any remaining decision Jeremy genuinely must make.

## Acceptance criteria

Prompt 020 is complete when:

- students are explicitly allowed to switch worlds;
- an early switch is easy and carries no grade penalty;
- later switches remain possible through a brief instructor check-in;
- existing earned work carries forward rather than being reset;
- a short migration receipt records what translates, what breaks, and what changes;
- the migration receipt becomes part of the student's World Bible history;
- the four worlds may flavor the transfer differently while requiring the same academic work;
- Prompt 018 no longer contains an unresolved world-switching policy question;
- the active world choice remains one of the same four fixed values;
- no new substantial grading burden is invented;
- no student must participate in lore to use the transfer policy;
- the result teaches a small but real lesson about migration, refactoring, changing requirements, and preserving useful abstractions.

## Explicitly out of scope

Do **not** in this prompt:

- redesign the four worlds;
- create a fifth world;
- rewrite Odyssey grading;
- make switching a major assignment;
- require students to restart their project;
- require students to replay past lore;
- create a punitive transfer deadline;
- invent a large approval workflow;
- rebuild the whole LMS data model without evidence that it is necessary.

Students are allowed to change their minds.

Make that change useful.