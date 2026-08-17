# The Four Calls -- World Selection Experience

Built by Prompt 018
(`../../prompts/018_the_four_calls_world_selection_experience.md`),
consuming Prompt 016's shared Odyssey contract and Prompt 017/019's
world canon and personas rather than inventing replacements. See
`scripts.md` for the four call scripts and `../../../presentations/beamer/four_calls/`
for the visual package.

This is the students' actual first contact with the four worlds --
after Prompt 016's orientation deck has already established the shared
academic contract. Nothing here should re-explain gates, checkpoints,
or the World Bible; that ground is already covered.

## The experience, in order

1. **Shared setup** (~15s) -- see "Shared opening" below.
2. **Call One** -- Frontier Settlement (Garrett Boone).
3. **Call Two** -- Investigation Bureau (Chief Nora Arana).
4. **Call Three** -- Starship Log (Commander Elias Rourke).
5. **Call Four** -- Small Business (Frank Delgado).
6. **Comparison/choice screen** -- one slide, four one-line reminders,
   no replay of the full pitch.
7. **"Which call do you answer?"**
8. **Choice capture** -- see "Backend representation" below.
9. **Closing message** -- what happens next.

Total shared-setup + closing time is deliberately shorter than any
single call; the point is to hear from the worlds, not to hear from
the course again.

## Shared opening (~15s, spoken over the Prompt 015 title-card style)

> "Four places are about to reach out to you. Each one needs help. Each
> one will teach you the same things -- but you'll learn them
> differently depending on where you decide to spend your semester.
>
> Watch. Listen. Then answer one question: which call do you answer?"

## The choice moment

**Comparison screen** reminds students of the four names and their
one-clause premise only (matching Prompt 016's spoiler-light framing,
not the full call pitch):

- Frontier Settlement -- a growing settlement that's outrun its own
  record-keeping.
- Investigation Bureau -- a case bureau where the records don't always
  agree.
- Starship Log -- a working ship under real operational pressure.
- Small Business -- a real business whose systems are buckling under
  growth.

**Choice screen guidance, spoken/on-screen:**

> Choose the world you're most curious to return to. Don't choose
> based on perceived difficulty -- there isn't a harder or easier
> door here. You're choosing context, not a different grading
> standard. Overthinking this is unnecessary -- you can't choose wrong.

**Central prompt, large on screen:** **Which call do you answer?**

## Academic equivalence mapping

All four calls -- and all four worlds -- target the identical CS2
learning outcomes, gates, checkpoints, and grading weights defined in
`../../../docs/grading-model.md` and `../../../assignments/A2-coding-odyssey-project.md`.
No call implies a different technical bar, and none should ever be
edited to imply one. `../capability_map.md` is the proof of this: every
week's capability row has a genuinely equivalent (not merely
relabeled) scenario in all four worlds.

## Backend representation for storing world choice

**Not implemented or deployed here** -- specification only, per the
prompt's explicit "do not perform production LMS writes" boundary.

- **What students submit/select:** one of exactly four canonical
  values -- a single-select choice, never free text (free text
  produces naming chaos: "frontier," "Frontier Settlement," "the
  settlement one" would all need to be reconciled by hand otherwise).
- **The exact four canonical values:**
  - `frontier_settlement`
  - `investigation_bureau`
  - `starship_log`
  - `small_business`
- **Where the choice should eventually be stored:** a single graded-
  or ungraded-as-appropriate LMS object (a single-select quiz/survey
  question is the simplest Canvas/Savnac-native shape) whose response
  value is one of the four slugs above, plus the course roster's
  existing student identifier -- no new identity system needed.
- **What instructors/agents need to route future world-specific
  material correctly:** a simple roster-to-world lookup (student ID ->
  one of the four slugs) that any future world-specific injection or
  grouping logic can read. This does not need to be built until a real
  deployment workflow authorizes the LMS object itself.
- **Avoiding free-text naming chaos:** enforced entirely by using a
  single-select/enum field with exactly the four slugs above as the
  only valid values -- never accept an open text field for this
  choice.

## World-switch policy -- resolved (Prompt 020)

**Students may switch worlds.** Early in the semester it's easy and
free; later it just starts with a short check-in with Jeremy. Nobody
restarts -- the student's software and World Bible history carry
forward. Full policy: `../transfer_portal/README.md`.

Per that prompt's explicit instruction not to over-explain the
transfer process during initial world selection, the choice-moment
guidance (above, "The choice moment") now includes exactly one added
sentence about this rather than the full policy -- see the updated
choice-screen guidance below.

**Updated choice-screen guidance, spoken/on-screen:**

> Choose the world you're most curious to return to. Don't choose
> based on perceived difficulty -- there isn't a harder or easier
> door here. You're choosing context, not a different grading
> standard. If you discover you chose wrong, there's a Transfer
> Portal -- you can move without losing the work you've already
> earned. Overthinking this is unnecessary.

## Closing message (after the choice is recorded)

> "Your world has your answer now. You'll hear from them again. And if
> it turns out to be the wrong door -- the Transfer Portal is always
> there."

Still deliberately brief -- protects the surprise (no roadmap of
future contact, no explanation of the migration receipt here), confirms
the choice was received, and now also confirms the choice isn't a
trap, without turning the moment into a terms-of-service screen.

## Production checklist (for Jeremy, when recording)

1. Read the target call's full entry in `scripts.md` and the matching
   dossier in `../four_faces/` once, out loud, before recording.
2. Gather that world's props/wardrobe (see each call's "Props/wardrobe"
   line -- all four are deliberately cheap and quick to put on).
3. Plain background, good lighting -- no set required.
4. Record the full version first; only fall back to the "alternate
   line" shorter cut if runtime is a real constraint.
5. One take is the target. If a second take is needed, use whichever
   take sounds more like the character believes the world is real,
   not whichever is most polished.
6. Export/save the transcript alongside the video using the exact
   spoken script text in `scripts.md` -- no separate caption
   authoring needed.
7. Confirm the on-screen title card text (see each call's "On-screen
   text during call") is legible and matches `scripts.md` exactly.
8. Do not publish or link any of the four videos from student-facing
   course pages until all four exist -- the calls are designed as a
   set; releasing them unevenly breaks "four doors opening at once."

## Hooks introduced (captured back to continuity)

Each call plants exactly one small, unresolved hook (see each call's
"Tiny hook planted" in `scripts.md`). All four are now recorded in
`../continuity_ledger.md` under a new dedicated entry so future authors
know these exist and can consult them before writing new material:

- Frontier Settlement: the mill's short grain count.
- Investigation Bureau: the field report's mismatched timestamp.
- Starship Log: the two-day-old odd sensor reading.
- Small Business: inventory coming up short twice this month.

None of these require resolution. They exist so each world feels alive
from first contact, per Prompt 018's "make the world feel alive, not
turn the selection experience into a mystery puzzle."
