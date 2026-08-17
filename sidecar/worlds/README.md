# The Four Living Worlds Bible (Master)

**Status:** internal canon. Built by Prompt 017
(`../prompts/017_build_four_living_worlds_bible.md`). Not student-facing.
Do not link this directory from `START_HERE.md`, `README.md`, or any
assignment/lesson file.

This is the backstage machinery behind the Reasoning Odyssey's four
optional worlds. It is for Jeremy, Cleo, ChatGPT, and future agents
authoring world material -- not for students. Students meet these
worlds only through carefully selected fragments (Prompt 016's
orientation deck, Prompt 018's Four Calls, and later in-world
injections). Never hand a student this directory.

## The firewall (do not weaken this)

> Classroom materials teach the curriculum.
> The Odyssey defines the work.
> The worlds make students care what happens next.

Three layers, three different audiences:

1. **Classroom slides** (weekly decks, `../prompts/015_build_cs2_slide_system.md`) --
   professional course material. Must work for a student who has never
   heard of any of this.
2. **Reasoning Odyssey orientation** (`../prompts/016_welcome_to_reasoning_odyssey.md`) --
   the shared academic contract. Explains gates, checkpoints, the
   World Bible, and the fact that four worlds exist. No lore.
3. **The four worlds** (this directory + Prompt 018 and beyond) --
   optional flavor. Amplifies engagement; never gates it.

A student who ignores every artifact in this directory must still be
able to earn full credit in the course. If a future prompt ever makes
that untrue, it is a defect, not a feature.

## The canonical four worlds

Reconciled against the only existing source of truth in the repository
(`assignments/A2-coding-odyssey-project.md`'s opening paragraph, which
lists these four names as bare working labels with a one-clause
example apiece and nothing else). No stronger or conflicting canonical
source exists anywhere else in the repo as of this bible's authoring.
These names and the one-clause examples they came with are therefore
**fixed** -- do not rename, merge, or add a fifth:

| World | File | One-line premise |
|---|---|---|
| **Frontier Settlement** | `frontier_settlement.md` | A new settlement is growing faster than its home-grown systems can track. |
| **Investigation Bureau** | `investigation_bureau.md` | A case bureau where the systems and the evidence don't always agree. |
| **Starship Log** | `starship_log.md` | A working ship whose interacting systems are under real operational pressure. |
| **Small Business** | `small_business.md` | A small business whose paper-and-memory systems are starting to buckle under real growth. |

Everything beyond the name and one-clause premise (cast, tone, visual
language, artifacts, seeds) is new creative work built by this prompt,
not extracted from an existing source -- there was nothing else to
extract.

## Design target: different textures, not noun substitution

The same CS2 capability surfaces differently in each world by design:

| CS2 capability | Frontier Settlement | Investigation Bureau | Starship Log | Small Business |
|---|---|---|---|---|
| Composition / invariants | a homestead record that must never show negative water rights | a case file that must never lose chain-of-custody | a subsystem whose readings must never contradict physical limits | an order that must never ship before payment clears |
| Contracts / interfaces | incompatible ledger formats between two settlements merging records | two agencies' report formats that don't match | two ship subsystems built to different eras' interface standards | a new POS vendor whose data format doesn't match the old one |
| Collections / search / order | prioritizing well-drilling requests by need vs. arrival order | sorting evidence by chain-of-custody vs. relevance | triaging sensor alerts by severity vs. arrival | prioritizing supplier orders by urgency vs. cost |
| GUI / model-view | a public-facing settlement notice board | a case-status dashboard for field investigators | a bridge status console | a shop's daily register/inventory screen |
| Data visualization | growth-vs-water-supply honesty chart | case backlog and closure-rate chart | fuel/resource consumption trend | margin-per-product honesty chart |

See `capability_map.md` for the full week-by-week mapping.

## Shared safety, inclusion, and taste boundaries

**Applies to all four worlds, all future material, without exception.**
No world may depend on:

- cultural caricature
- gender stereotypes
- race or nationality jokes
- disability jokes
- student humiliation
- political litmus tests
- violence as cheap spectacle
- inaccessible genre knowledge (a student who has never seen a western,
  a procedural, sci-fi, or run a business must still get the joke)
- roleplay participation as a grading requirement

Every character is written to be **believed**, not mocked -- including
by Jeremy performing them. The character believes the world is real;
that sincerity is what makes it work, not costume-gag energy. If a bit
only works by punching down or requiring insider genre knowledge, cut
it.

## World Bible vs. the student's World Bible -- do not confuse these

This directory (the **Four Living Worlds Bible**) is our internal
authoring canon.

The **student's World Bible** (defined in
`../../assignments/A2-coding-odyssey-project.md`) is the student's own
record of their software world -- their assumptions, invariants,
interfaces, design choices, revisions, and evidence.

World events (a call, an injection, a hook resolving) may create
**pressure and choices** for the student's design. They must never
secretly dictate the "one correct" object model. If a world-canon event
requires a specific technical response to make sense, that response
still has to be something the student could plausibly have designed
several different ways -- the world creates the problem, not the
student's solution.

## Continuity

See `continuity_ledger.md` for the format and current seeded entries.
Before writing any new world material (a call, an injection, a
character update), consult the ledger for that world first. Before
introducing a new named character, location, or unresolved thread,
add it to the ledger in the same commit.

## Guide for future agents: writing inside these worlds

1. **Read the specific world's bible file and the continuity ledger
   before writing anything.** Do not improvise a character's voice
   from vibes; the bible defines it.
2. **Never let world material become a prerequisite.** If a piece of
   in-world content is the only place a technical concept is explained,
   that's a defect -- move the explanation to the classroom layer and
   let the world material stay pure flavor.
3. **Restate technical context outside the lore whenever a callback
   affects graded work.** A student who missed the callback must not
   be at a disadvantage on the actual gate.
4. **Don't force every seed to pay off.** The continuity ledger is a
   garden, not railroad tracks -- an entry can sit unresolved
   indefinitely.
5. **Keep the four worlds' visual languages related, not identical.**
   Each should be recognizable at a glance (see each world's "Visual
   identity" section) while still clearly belonging to the same CS2
   presentation system (Prompt 015's theme colors/type/frame chrome
   remain the base; each world adds a restrained accent, not a full
   reskin).
5. **Protect the surprise.** Student-facing material (Prompt 016, 018,
   and beyond) reveals only what's needed to make an informed choice or
   understand the immediate moment -- never the full bible, never future
   seeds, never the complete cast.
6. **When in doubt about taste, cut it.** See "Shared safety, inclusion,
   and taste boundaries" above. This is not a place to relitigate that
   list per-world.
7. **Jeremy's personas are sparks, not scripts to follow rigidly.**
   Each world bible's persona section gives enough specificity to
   perform without needing theater-school prep -- leave room for Jeremy
   to inhabit the character rather than over-directing every line.

## Deliverables index (Prompt 017)

- This file -- master bible, shared rules, authoring boundaries.
- `frontier_settlement.md`, `investigation_bureau.md`,
  `starship_log.md`, `small_business.md` -- one substantial internal
  bible per world, each containing: core premise; tone and flavor;
  setting and boundaries; recurring characters; Jeremy's playable
  personas; visual identity; artifact language; CS2 problem generators;
  story seeds and delayed payoffs; injection menu; one prototype
  artifact or briefing concept.
- `capability_map.md` -- CS2 capability-to-world opportunity map across
  all four worlds.
- `continuity_ledger.md` -- ledger format and initial seeded entries
  for all four worlds.
