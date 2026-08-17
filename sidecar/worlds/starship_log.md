# World Bible: Starship Log

Internal canon. See `README.md` for the shared firewall, safety
boundaries, and authoring rules before writing anything set here.

## 1. Core premise

The **RSV Kestrel** is a research and survey vessel, months out from
home port, mapping and studying territory nobody's fully charted yet.
It is not a warship and this is not military space opera -- it's a
working ship with a working crew, and working ships run on systems
that have to actually agree with each other: navigation, life support,
sensor logs, the ship's own operational log.

Software matters here because **the mission depends on systems nobody
can walk over and double-check by hand** -- the Kestrel is too far out
for that. The student isn't a space hero; they're the systems officer
keeping the ship's actual operations honest and working while the
mission keeps pushing into unfamiliar territory.

## 2. Tone and flavor

**Is:** competent, curious, forward-leaning. The crew is good at their
jobs and genuinely wants to be out here. Tension comes from real
operational pressure (limited resources, systems under strain,
unfamiliar territory) handled with calm professionalism. Humor is dry
technical banter -- the kind of joke people make when they trust each
other and the stakes are real but not dire.

**Must not become:** a copyrighted-franchise pastiche (no Starfleet
insignia energy, no "Buzz Lightyear" impression), space opera melodrama,
or a war story. No hostile aliens, no combat, no "us vs. them." The
antagonist here is complexity and distance, not an enemy.

## 3. Setting and boundaries

- **The Bridge** -- command and coordination; where the Commander
  briefs the crew and where cross-system problems surface.
- **Engineering** -- where subsystems live and where interface
  mismatches between subsystems (built in different eras, to different
  standards) actually bite.
- **The Ship's Log** -- the master record of everything that happened,
  and the student's default "workplace": an append-only, must-never-
  contradict-itself record of ship state and events.
- **Sensor & Survey** -- the mission's actual purpose: gathering and
  making sense of real (simulated) data about the territory the
  Kestrel is surveying.

Boundaries: no combat, no hostile first contact, no crew-endangerment
horror. Pressure comes from resource limits, technical failure, and
distance from help -- not violence.

## 4. Recurring characters

- **Commander Elias Rourke** -- the Kestrel's commanding officer.
  Ambitious in the best sense: he wants to go somewhere and see
  something real, but he knows the mission only survives on systems
  that work. The one who briefs the student and sets the mission's
  stakes. Jeremy's primary persona in this world -- see section 5 and
  `four_faces/starship_commander_rourke.md` for the full dossier.
- **Ensign Priya Nandy** -- a junior engineer, sharp but still
  building confidence, prone to catching real problems and then
  second-guessing whether she's allowed to raise them. Useful voice
  for surfacing a technical anomaly with appropriate uncertainty.
- **Navigator Voss** -- a veteran crew member, unflappable, the person
  who's seen enough long missions to know which problems are routine
  and which aren't. Useful for grounding urgency without melodrama.

## 5. Jeremy's playable personas

**Primary: Commander Elias Rourke.** An original command persona --
explicitly not an impression of any existing franchise character.
Visual language: a simple utilitarian jacket or ship-branded pullover,
a name badge/patch (a nod to the "Buzz-style badge" spark from
Jeremy's original notes, kept generic and original -- ship crest only,
no copyrighted insignia), a tablet or clipboard as a ship's-log prop.
Voice: calm, forward-looking, economical -- speaks like someone used
to being heard the first time.

**Alternate: Navigator Voss**, for a scene needing weathered calm
rather than command energy -- same general setting, more relaxed
posture, slower and drier delivery.

## 6. Visual identity

- **Palette:** cool teal/cyan accent -- distinct from Investigation
  Bureau's slate and closer to (but not identical to) the base theme's
  `cs2odyssey` teal; lean the Starship world slightly bluer/brighter to
  stay distinguishable.
- **Type mood:** clean, technical, monospace-adjacent for ship's-log
  entries and status readouts; classroom slides stay in the Prompt 015
  theme.
- **Diagram motif:** system-status panels, clean node-and-line diagrams
  for subsystem relationships -- utilitarian, not decorative.
- **Iconography:** a simple ship silhouette, a log-entry timestamp
  format, a status-light motif (green/amber/red used sparingly and
  never as the sole carrier of meaning, per accessibility rules).
- **Title card:** "RSV KESTREL -- SHIP'S LOG" over a teal accent bar,
  styled like a status readout.

## 7. Artifact language

Ship's log entries, sensor reports, maintenance notes, systems status
reports, mission briefings, crew manifests, incident reports.

## 8. CS2 problem generators

- **Composition/invariants:** a life-support log where readings must
  never contradict known physical limits (e.g., oxygen level can't
  silently go negative or exceed capacity).
- **Contracts/interfaces:** two subsystems built to different eras'
  interface standards that need a shared contract to communicate.
- **Inheritance/polymorphism:** different sensor types (thermal,
  spectral, proximity) sharing a common "Sensor" contract with
  type-specific readings.
- **Collections/search/order:** triaging sensor alerts by severity vs.
  arrival order; prioritizing the maintenance queue.
- **GUI/model-view:** a bridge status console summarizing subsystem
  health without dumping raw logs.
- **Data visualization:** an honest chart of resource consumption
  (fuel, power, life support) trending over the mission.
- **Peer review/stabilization, source management:** Engineering and
  the student reconciling two versions of a subsystem's log after a
  diagnostic disagreement.

Full cross-world mapping: `capability_map.md`.

## 9. Continuity

See `continuity_ledger.md`, section "Starship Log." Consult before
writing new material; add new named characters/threads there in the
same commit that introduces them.

## 10. Seeds and delayed payoffs

- An early diagnostic assumption ("this subsystem always reports
  accurately") could quietly stop holding once a sensor starts
  disagreeing with physical readings later in the mission.
- Ensign Nandy's early hesitance to flag anomalies could evolve into a
  real trust arc -- what happens the first time she's right and
  believed, versus the first time she's right and ignored.
- Navigator Voss mentions "the last long mission" in passing -- an
  unspecified prior incident that could resurface as a callback without
  ever needing to become the Kestrel's own crisis.
- A resource-budget assumption made early (plenty of margin) could
  become genuinely tight later as the mission extends.

None of these are required to pay off. Garden, not railroad.

## 11. Injection menu

- 30-45s video: Commander Rourke briefing the student on why the ship's
  log has to be trustworthy -- "we're too far out to double-check by
  hand."
- Written memo: Ensign Nandy flagging a reading that doesn't look
  right, unsure if it's worth escalating.
- One-slide interruption: a sensor alert requiring the student's
  system to triage it correctly.
- Artifact drop: a maintenance note referencing an old subsystem
  quirk nobody's fully explained.
- Character update: Commander Rourke's brief log entry noting the
  mission is finally running smoothly -- a rare calm beat, useful late
  in the semester.

## 12. Safety and taste

See `README.md`'s shared boundaries. Specific to this world: no
combat, no hostile-alien framing, no impersonation of any existing
franchise character or franchise-specific insignia/terminology.

## Prototype: one briefing concept

> **COMMANDER ROURKE, standing, tablet in hand, calm and direct.**
>
> "Systems Officer. Good, you're here." *(glances at tablet)* "We're
> six weeks out from the nearest relay. Out here, if the ship's log
> doesn't agree with itself, there's no one to call and ask which
> version is true. That's your job now -- not glamorous, but it's the
> reason the rest of us get to do the interesting work. Keep the record
> honest, and we go somewhere worth going."

Runtime: ~30s. Establishes stakes (distance, self-reliance), character
(Rourke, calm and forward-looking), and the ask.
