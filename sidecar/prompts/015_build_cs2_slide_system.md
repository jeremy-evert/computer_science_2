# Prompt 015: Build the Computer Science II Slide System

**Status:** OPEN  
**Course:** COMSC-1053 Computer Science II, Fall 2026  
**Owner:** Cleo  
**Scope:** Presentation architecture and reusable slide system only

## Mission

Build the reusable **Computer Science II presentation system** that will become the foundation for the Fall 2026 course.

Do **not** build the semester's weekly slide decks yet.

The goal of this prompt is to create, test, and document a professional presentation pattern that Cleo can reuse aggressively when we begin producing the course **one week at a time**.

The finished system should make later slide production faster, more consistent, and easier to maintain without making every week feel mechanically identical.

## Source of truth

Before designing anything, inspect the current CS2 repository and understand:

- `START_HERE.md`
- `ROADMAP.md`
- `course_metadata.yaml`
- `planning/fall-2026-course-design.md`
- the weekly planning files
- the Reasoning Odyssey assignments and gates
- the rubrics
- existing lessons
- relevant sidecar reports
- the shared-course ownership boundaries documented in the repo

Do not invent a second course architecture inside the presentation system.

The slides should **express the course that already exists**.

## Design goal

The system should feel like a **modern, professional university computer science course**.

It should support:

- technical explanations
- readable code
- diagrams
- live coding
- worked examples
- student discussion
- short activities
- reasoning exercises
- assignment/gate explanations
- reflection
- AI-use guidance
- transitions into the Reasoning Odyssey

It should be visually distinctive without becoming theatrical, cluttered, gimmicky, or difficult to teach from.

## Build a reusable presentation grammar

Define a small set of reusable slide patterns rather than designing every slide independently.

At minimum, create patterns for:

1. Title / opening
2. Today's destination
3. Why this matters
4. Core concept
5. Concept with diagram
6. Code example
7. Code walkthrough
8. Predict before running
9. Live coding prompt
10. Worked problem
11. Think / pair / discuss
12. Common failure or misconception
13. Compare two approaches
14. Design decision
15. AI collaboration / verification moment
16. Reasoning Odyssey connection
17. World Bible entry
18. Odyssey checkpoint / gate
19. Evidence students need to produce
20. Recap
21. Exit question / next move

These do not all need to appear every week.

They are the vocabulary Cleo can choose from.

## Establish the weekly rhythm

Create a recommended default rhythm for a normal CS2 teaching week.

It should be flexible enough for Monday, Wednesday, and Friday teaching without requiring every class meeting to have the same structure.

The rhythm should answer questions such as:

- How do we open a week?
- When do we introduce the technical capability?
- Where does live coding belong?
- Where do students practice?
- When does the Reasoning Odyssey enter?
- How do we show the week's gate without turning the whole lesson into assignment instructions?
- How do we close a class meeting?
- How do we close a week?

The rhythm should support Jeremy teaching from the slides rather than reading the slides.

## Code is first-class content

Develop explicit standards for code slides.

Code must be:

- large enough to read in a classroom
- syntax-highlighted consistently
- short enough to comprehend
- cropped to the relevant idea
- accompanied by context when necessary
- split across slides rather than shrunk into oblivion

Create patterns for:

- before/after refactoring
- broken/fixed code
- progressive code reveals
- predicting output
- tracing state
- comparing implementations
- marking the one or two lines students should notice

Do not use screenshots of source code when editable/rendered code is practical.

## Diagrams are first-class content

Define a consistent diagram language for concepts such as:

- object relationships
- composition
- inheritance
- interfaces/contracts
- collections
- control/data flow
- model/view boundaries
- source-management workflow
- data-processing pipelines

Prefer simple diagrams that Jeremy can explain at a glance.

Avoid decorative complexity.

## Reasoning Odyssey integration

The presentation system must support the **Reasoning Odyssey** as a recurring course identity.

Create specific visual/presentation patterns for:

- entering an Odyssey problem
- identifying the capability students need
- making a design decision
- collecting evidence
- recording a World Bible decision
- reaching a checkpoint
- revisiting an earlier decision
- showing how the software world evolves over the semester

The Odyssey should feel meaningful and memorable while remaining academically professional.

## World Bible integration

Create a reusable **World Bible** slide pattern.

It should make it easy to capture things such as:

- rules of the student's software world
- object responsibilities
- assumptions
- invariants
- naming decisions
- interfaces/contracts
- architectural choices
- revisions and why they occurred

The World Bible should become a visible record of student reasoning, not decorative lore.

## Instructor usability

The system is for actual classroom delivery.

Account for:

- slides Jeremy can glance at while teaching
- presenter notes or instructor cues where useful
- clear live-demo transitions
- places where the deck should deliberately stop and let students work
- easy editing immediately before class
- graceful handling when a discussion takes longer than planned

Do not bury essential teaching instructions in a giant design manual nobody will consult.

## Accessibility

Build accessibility into the system from the beginning.

At minimum consider:

- readable type sizes
- sufficient contrast
- color not being the sole carrier of meaning
- code readability
- meaningful image/diagram descriptions where applicable
- layouts that survive projection onto mediocre classroom displays

## Technical implementation

Inspect the repository's current presentation tooling before deciding how the system should be implemented.

Prefer a system that:

- lives in version control
- can be regenerated
- minimizes manual formatting drift
- can reuse common presentation components
- allows week-specific customization
- does not require Jeremy to hand-edit dozens of duplicated design decisions

If a reusable theme/template/component layer is appropriate, create it.

Document how future agents should use it.

## Deliverables

Produce:

1. The reusable CS2 presentation system
2. A compact presentation style/design guide
3. The reusable slide patterns/components
4. The default weekly teaching rhythm
5. Reasoning Odyssey patterns
6. World Bible patterns
7. Code and diagram standards
8. A small demonstration deck proving the system works

The demonstration deck is **not** Week 3 and is **not** the Welcome to the Odyssey deck.

It should contain enough representative slides to validate the system without prematurely authoring course content.

## Acceptance criteria

This prompt is complete when:

- the presentation system can be reused without redesigning each deck
- code is classroom-readable
- diagrams follow a consistent visual grammar
- Reasoning Odyssey and World Bible content have defined patterns
- the weekly rhythm is documented
- accessibility requirements are addressed
- the system is easy for another agent to understand and use
- a demonstration deck successfully exercises the major slide types
- future work can say:

> **Use the CS2 slide system and build Week X**

without needing to reinvent presentation architecture.

## Explicitly out of scope

Do **not** yet build:

- Welcome to the Odyssey
- the full Reasoning Odyssey introduction
- Week 1
- Week 2
- Week 3
- later weekly decks
- the entire semester presentation library

Those are subsequent prompts.

**Build the factory first. Then we run the factory.**
