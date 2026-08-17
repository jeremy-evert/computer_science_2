# The Transfer Portal -- World Switching Policy

Built by Prompt 020
(`../../prompts/020_transfer_portal_world_switching.md`), closing the
world-switch policy gap Prompt 018 explicitly flagged rather than
invented. This file is the canonical policy. Student-facing framing
lives in "Student-facing explanation" below and is echoed (briefly, on
purpose) in `../four_calls/README.md` and
`../../../presentations/beamer/four_calls/the-four-calls.tex`.

## The policy

**Students may switch Reasoning Odyssey worlds. Yes.**

All four worlds share the same CS2 learning outcomes, grading
contract, gates, checkpoints, and technical expectations
(`../../../docs/grading-model.md`,
`../../../assignments/A2-coding-odyssey-project.md`). A world switch
changes context and flavor, not curriculum -- so it costs nothing
academically and requires no restart.

### Early-semester transfer -- easy, no penalty

One simple, no-penalty transfer, early in the semester. No approval
needed beyond telling Jeremy which world you're moving to.

**Recommended cutoff (Jeremy's call -- see "Open decision" below):**
before the Week 6 checkpoint (`../../../docs/grading-model.md`'s first
larger Odyssey checkpoint). Week 6 is the first point where a
student's design decisions start carrying real accumulated weight, so
it's a natural place for "easy and free" to become "still fine, but
let's talk first" -- not because Week 6 is special in the source
material, but because it's the first checkpoint boundary that already
exists for other reasons.

### Later-semester transfer -- still possible, with a check-in

After the early window, a transfer still happens -- it just starts
with a short conversation with Jeremy first, because more accumulated
design decisions may need reconciling. The check-in is not an approval
gate to survive; it exists to make the migration technically coherent,
not to discourage it.

### What never changes

A transfer must never:

- erase earned work or reset a grade
- create a harder or easier grading path than staying put
- require redoing already-accepted work just because the setting changed
- require lore knowledge or theatrical participation
- force a full redesign when the existing design can honestly migrate

## The migration receipt

A short, practical document -- an engineering handoff, not an essay --
that becomes part of the student's own World Bible
(`../../../assignments/A2-coding-odyssey-project.md`'s "World Bible"
section). Seven fields:

1. **Where I am leaving** -- current world.
2. **Where I am going** -- new world.
3. **What comes with me** -- classes, responsibilities, interfaces,
   data structures, invariants, or assumptions that remain valid.
4. **What does not translate cleanly** -- terminology, assumptions,
   constraints, or relationships that no longer make sense.
5. **What I will refactor** -- the smallest reasonable changes needed
   to make the software world coherent in the new setting.
6. **What I am deliberately preserving** -- technical decisions the
   student believes should survive the move, and why.
7. **New World Bible entry** -- a concise record of the migration and
   its reasoning.

### Template (copy into the student's World Bible)

```markdown
## Transfer Portal migration receipt

- Leaving: [world]
- Going to: [world]
- Comes with me: [interfaces/classes/invariants that still hold]
- Doesn't translate: [what no longer makes sense in the new setting]
- Will refactor: [the smallest changes needed for coherence]
- Deliberately preserving: [decisions kept, and why]
- New World Bible entry: [one short paragraph]
```

## Academic treatment

The migration receipt attaches to the student's normal World Bible
evidence (grading pattern 1 from the prompt's ordered preference list)
-- it is not a new major assignment and carries no new substantial
points or weight. If a discrete LMS object is ever genuinely required
for workflow reasons, it must be low-stakes and clearly labeled as
migration evidence, never a fee for changing your mind.

## Preserving prior technical work

The point of the exercise is the reconciliation, not a fresh start.
Ask (and the receipt's fields already do): which abstractions are
genuinely reusable, which names were domain-specific but the design
was sound, which assumptions were accidentally coupled to the old
world, which interfaces survive, which invariants change, which parts
need adaptation rather than replacement. This is software migration,
refactoring, and requirements change in miniature -- a real CS2
lesson, not a formality.

## World-specific transfer flavor

Same academic requirement everywhere. Flavor only changes the
document's name and framing -- never what's required. Full world
context: `../frontier_settlement.md`, `../investigation_bureau.md`,
`../starship_log.md`, `../small_business.md`.

- **Frontier Settlement:** a **Claim Transfer Record** -- Garrett Boone
  treats it exactly like any other claim reassignment: practical, no
  drama, the ledger just needs to reflect where things actually stand
  now.
- **Investigation Bureau:** a **Case Reassignment Form** -- Chief Arana
  wants the chain of custody on the old work preserved, not erased;
  the case simply has a new assigned analyst.
- **Starship Log:** a **Transfer Order** -- Commander Rourke logs it
  like any crew reassignment: the ship's record shows who served where
  and when, and the work already logged stays logged.
- **Small Business:** a **Change of Role Memo** -- Frank treats it like
  moving an employee to a different part of the shop: the experience
  they've already built up comes with them.

## Continuity

When a student transfers: their prior World Bible history is
preserved as-is (old entries are never rewritten to pretend they
always belonged to the new world); the transfer itself is recorded as
a real event; future work may refer to "before the transfer" and
"after the transfer." See `../continuity_ledger.md` for the internal-
canon-side entry recording that this policy exists -- individual
student transfers are the student's own World Bible history, not
internal canon, and are never recorded in the internal ledger.

## Instructor workflow (Jeremy)

1. Student tells you which world they're moving to (early window: just
   tells you; later window: a short check-in conversation first).
2. You confirm the migration receipt's seven fields are filled in
   honestly and the reconciliation is coherent -- this is a few
   minutes, not a review board.
3. Update the student's active world-choice value (see "Data/storage
   behavior" below) to the new world.
4. The migration receipt is filed as part of the student's World
   Bible -- no separate grading object needed under the default
   pattern.
5. The old world choice is preserved historically (see below) so the
   student's record stays legible.
6. A second or unusually late transfer follows the same later-
   transfer check-in process -- there is no separate escalation tier.
   Don't build policy theater for an edge case that just needs the
   same conversation again.

## Data/storage behavior

Preserves Prompt 018's fixed four-value model
(`frontier_settlement` / `investigation_bureau` / `starship_log` /
`small_business`) exactly -- no free text, no fifth value, no redesign.

- The student's **active world choice** updates to the new value.
- If the storage mechanism already supports simple history (a log or
  timestamped field), record that a transfer occurred and when; if it
  only stores one active value, changing that value plus keeping the
  migration receipt in the World Bible is sufficient -- do not build
  new infrastructure to satisfy this on spec.
- The migration receipt itself lives in the student's World Bible, not
  in a new LMS object, under the default academic-treatment pattern
  above.

## Student-facing explanation

> You picked a place to build. If another world fits you better, move
> your software there and show us how you carried the design across.
>
> Early in the semester, that move is easy and free -- no penalty, no
> drama. Later, it still happens -- just start with a quick
> conversation with Jeremy so the move stays technically coherent.
> Either way, you don't restart. Your software comes with you, and
> your World Bible records what survived, what broke, and what you
> refactored to make it fit.

## Open decision for Jeremy

The exact early-transfer cutoff date is not defined anywhere in the
current course source (`docs/grading-model.md`,
`assignments/A2-coding-odyssey-project.md`, `ROADMAP.md` were all
checked; none set one). This document recommends "before the Week 6
checkpoint" as a natural, already-existing boundary rather than a new
invented deadline, but the actual cutoff is Jeremy's call to confirm
or change before this policy is published to students.
