# World Bible: Frontier Settlement

Internal canon. See `README.md` for the shared firewall, safety
boundaries, and authoring rules before writing anything set here.

## 1. Core premise

**Docket Creek** is eighteen months old. It started as four families
and a well. It is now pushing four hundred people, and every system
that used to live in someone's head or a kitchen ledger is starting to
crack. Water rights, land claims, trade credits, who owes the mill
what -- it all used to be "ask Merrow, she remembers." Merrow can't
hold four hundred people in her head anymore.

Software matters here because **memory doesn't scale by itself**. The
student isn't a settler with a laptop -- they're the person Docket
Creek asks to build the record-keeping the town has outgrown: ledgers,
registries, allocation systems. The role is closer to "the person who
finally writes it down properly" than "frontier hero."

## 2. Tone and flavor

**Is:** plainspoken, warm, practical, a little weathered. Problems are
real (a bad harvest, a disputed well) and solved through competence and
stubbornness, not luck. Humor is dry and understated -- a shrug, not a
punchline.

**Must not become:** a Western pastiche, a "howdy pardner" costume
party, or a joke about frontier people being unsophisticated. Docket
Creek's residents are smart, resourceful, and busy. The comedy (when it
exists) comes from bureaucratic absurdity meeting a town too young to
have bureaucracy yet, never from mocking the setting itself.

## 3. Setting and boundaries

- **The Recorder's Office** -- one room, one desk, a wall of ledgers
  that no longer fit the wall. The student's default "workplace."
- **The Well Board** -- who gets water, when, and how much. A perennial
  source of contract/invariant problems (allocations must never go
  negative; two claims must never silently overlap).
- **The Trade Post** -- barter, credit, and the beginnings of a real
  ledger economy. A source of collections/ordering problems.
- **The Mill** -- shared infrastructure with a queue problem baked in
  (whose grain gets milled first, and by what rule).
- **The road out** -- Docket Creek is not isolated; wagons, letters,
  and the occasional inspector arrive. This is the world's connection
  to "outside pressure" (new settlers, new rules, a bad season).

Boundaries: no armed conflict, no lawlessness-as-spectacle. Docket
Creek's problems are administrative and structural, not violent.

## 4. Recurring characters

- **Garrett Boone** -- the founding Registrar who trained Merrow and
  officially "retired" a year ago, but still shows up to personally
  brief every new record-keeper. Jeremy's primary persona in this
  world -- see section 5 and `four_faces/frontier_garrett_boone.md`
  for the full dossier.
- **Merrow** -- the town's current record-keeper, Garrett's protégé. Sharp, tired,
  fiercely protective of accuracy. She's the one who asks the student
  to formalize what she used to carry by memory. Motivation: she is
  terrified of getting something wrong now that it matters this much.
- **Deputy Cassel** -- young, eager, slightly too confident, in charge
  of "keeping order" in a town that doesn't really need a deputy yet.
  Useful for injecting urgency and minor comic friction ("I need this
  by sundown" for something that doesn't need to be by sundown).
- **Old Tobin** -- a skeptical longtime resident who trusts paper more
  than "your computer thing." Useful voice for "why does this even
  need to change" pushback that the student's design has to answer.

## 5. Jeremy's playable personas

**Primary: Garrett Boone, the Settlement Registrar.** Docket Creek's
founding record-keeper -- the one who trained Merrow, and the one who
still shows up personally when a new record-keeper (the student) joins
the office. Semi-retired in title only; he can't quite let go of the
ledgers. Full character dossier: `four_faces/frontier_garrett_boone.md`.
Visual language: suspenders, rolled sleeves, a ledger book as a prop,
reading glasses pushed up. Voice: plain, direct, slightly exhausted,
deeply sincere about getting the record right.

**Alternate: Old Tobin**, for a scene needing skepticism rather than
urgency -- same prop kit, different posture (arms crossed, slower
speech).

Neither persona needs an accent or dialect performance -- plain modern
speech, weathered *demeanor*, not a costume of speech patterns.

## 6. Visual identity

- **Palette:** warm sepia/amber accent against the CS2 base theme
  (`cs2accent`'s amber already leans this direction -- lean into it
  for this world rather than introducing a new hue).
- **Type mood:** slab-serif or typewriter-adjacent feel for in-world
  documents (ledger pages, notices) -- never for actual classroom
  slides, which stay in the Prompt 015 theme's sans-serif.
  \\ **Diagram motif:** ledger-line tables, hand-drawn-feeling
  boundary sketches (kept simple, not literally hand-drawn).
- **Iconography:** a well, a ledger, a wagon wheel -- used sparingly,
  never all at once.
- **Title card:** "DOCKET CREEK -- RECORDER'S OFFICE" in slab type over
  the amber accent bar.

## 7. Artifact language

Ledger pages, well-allocation notices, trade-post credit slips, the
Recorder's weekly log, road dispatches (news/requests arriving from
outside), disputed-claim forms.

## 8. CS2 problem generators

- **Composition/invariants:** a household's water allocation record
  that must never show a negative balance or double-claim a well slot.
- **Contracts/interfaces:** two neighboring claims merging their
  separate, incompatible ledger formats into one.
- **Inheritance/polymorphism:** different claim types (homestead, mill,
  trade-post) sharing a common "Claim" contract with type-specific
  rules.
- **Collections/search/order:** prioritizing well-drilling requests
  by need vs. arrival order; sorting the mill queue.
- **GUI/model-view:** a public notice board showing current well
  allocations and mill queue status.
- **Data visualization:** an honest chart of population growth vs.
  water supply -- the kind of chart that might make the town nervous.
- **Peer review/stabilization, source management:** Merrow and the
  student reconciling two versions of the same ledger after a dispute.

Full cross-world mapping: `capability_map.md`.

## 9. Continuity

See `continuity_ledger.md`, section "Frontier Settlement." Consult
before writing new material; add new named characters/threads there
in the same commit that introduces them.

## 10. Seeds and delayed payoffs

- An early well-allocation rule assumes the town won't exceed 200
  people. It quietly stops making sense around week 8-9 as Docket
  Creek keeps growing -- a natural callback to an early invariant that
  becomes expensive.
- Deputy Cassel's "keep order" requests start harmless (paperwork by
  sundown) and could escalate into a real resourcing conflict later
  (two urgent requests that can't both be first).
- Old Tobin's paper ledger, kept in parallel out of distrust, could
  eventually disagree with the digital one -- a real reconciliation
  problem, not a joke.
- A discrepancy in the mill queue (someone's grain "disappearing" from
  the count) that's initially a shrug and could become a genuine data
  problem later.

None of these are required to pay off. Garden, not railroad.

## 11. Injection menu

- 30-45s video: Merrow, harried, asking the student to formalize the
  well-allocation rule before the next dispute.
- Written memo: Deputy Cassel's "urgent" request that turns out to be
  mundane (light comic beat, low stakes).
- One-slide interruption: a road dispatch announcing new arrivals --
  "the town just grew by twelve people, does your system still hold?"
- Artifact drop: a photo/scan of Old Tobin's paper ledger with a
  number that doesn't match.
- Character update: Merrow's brief note admitting the office finally
  feels "under control" -- a rare warm beat, useful late in the
  semester.

## 12. Safety and taste

See `README.md`'s shared boundaries. Specific to this world: no
"noble savage" or "civilizing the frontier" framing, no treatment of
frontier life as unsophisticated, no Western-genre stereotype voices.

## Prototype: one briefing concept

> **MERROW, at the Recorder's desk, ledger open, not looking up at first.**
>
> "You're the one they sent about the records." *(looks up)* "Good.
> Sit down a second, I want to show you something before you touch
> anything." *(turns ledger around)* "This is every well claim in
> Docket Creek. All four hundred people. All in my handwriting. I
> have not slept well in about a month, because if I miscount one of
> these, somebody's crop doesn't get watered. I need this in something
> that can't forget. Can you build that?"

Runtime: ~30s. Establishes stakes (memory doesn't scale), character
(Merrow, sincere and tired), and the ask -- without over-explaining the
world.
