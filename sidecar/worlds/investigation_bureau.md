# World Bible: Investigation Bureau

Internal canon. See `README.md` for the shared firewall, safety
boundaries, and authoring rules before writing anything set here.

## 1. Core premise

The **Meridian Case Bureau** handles the unglamorous middle of
investigation work: not the chase, the paperwork after it. Evidence
logs, case files, witness statements, chain-of-custody records --
systems that must be exactly right, because "close enough" in a case
file is how the wrong person doesn't get justice.

Software matters here because **disagreement between two records is
itself the crime scene**. The student isn't a detective solving
mysteries by intuition -- they're the person who builds and maintains
the systems that make sure the Bureau's own records can be trusted.
The tension is procedural and structural, not violent.

## 2. Tone and flavor

**Is:** measured, professional, quietly tense. Procedural drama, not
pulp noir -- think "careful institution doing careful work," not
"hardboiled detective narrating in a rainstorm." Stakes are real
(getting a case right matters) without being grim. Humor is dry,
institutional -- the kind of deadpan that comes from people who've
seen a lot of paperwork.

**Must not become:** noir pastiche with a fedora and a monologue,
crime-as-entertainment, or anything that treats real harm (to victims,
to the wrongly accused) as a punchline. No violence as spectacle -- the
Bureau's drama is entirely about whether the records are right.

## 3. Setting and boundaries

- **Case Records Division** -- the student's default "workplace":
  rows of case files, a records terminal, evidence logs.
- **The Evidence Locker** -- physical custody meets its digital
  shadow; a natural source of invariant problems (an item can't be
  "checked out" by two people at once; custody chains can't have gaps).
- **Field Reports** -- investigators submit reports from the field
  that need to reconcile with what's already on file. A natural
  contract/interface problem (two report formats that don't match).
- **The Bureau itself** -- an institution, not a lone-wolf detective
  agency. Cases are worked by teams; the student's tools serve the
  team, not a single genius investigator.

Boundaries: no depiction of actual crimes in graphic detail, no
victims treated as plot devices, no "gotcha" mystery-solving that
requires the student to guess a twist -- the Bureau's problems are
about the integrity of records, not whodunit puzzles.

## 4. Recurring characters

- **Chief Nora Arana** -- runs Case Records Division. Exacting, calm
  under pressure, deeply committed to getting it right rather than
  getting it fast. The one who briefs the student and sets
  expectations. Jeremy's primary persona in this world -- see section
  5 and `four_faces/investigation_chief_arana.md` for the full dossier.
- **Records Clerk Doyle** -- meticulous, a little anxious, the person
  who actually notices when two numbers don't match. Useful voice for
  surfacing a discrepancy without narrating the whole mystery.
- **Investigator Reyes** -- a field investigator, competent and
  slightly impatient with "the paperwork side," who nonetheless needs
  the student's tools to work. Useful for injecting field-report
  contract mismatches.

## 5. Jeremy's playable personas

**Primary: Chief Nora Arana.** Visual language: a badge, a plain jacket or
blazer, a case folder as a prop, glasses. Voice: measured, precise,
economical with words -- says less than a detective-fiction chief
would, because the drama here is quiet, not theatrical.

**Alternate: Records Clerk Doyle**, for a scene needing anxious
precision rather than institutional calm -- same prop kit (folder,
badge optional), more clipped, faster cadence.

## 6. Visual identity

- **Palette:** cool slate/steel accent -- lean toward the base theme's
  `cs2ink`/`cs2inkSoft` rather than introducing a new saturated hue;
  Investigation Bureau should feel the most "monochrome-institutional"
  of the four worlds.
- **Type mood:** case-file stamp/typewriter-adjacent for in-world
  documents (case numbers, "FILED" stamps); classroom slides stay in
  the Prompt 015 theme.
- **Diagram motif:** timeline/chain-of-custody style linear diagrams;
  file-folder tabs as a recurring shape motif.
- **Iconography:** a case folder, a records stamp, a magnifying glass
  used sparingly (avoid overusing it -- it's the most cliche noir icon
  available and should appear rarely, not as a logo).
- **Title card:** "MERIDIAN CASE BUREAU -- CASE RECORDS DIVISION" over
  a slate accent bar, styled like a case-file stamp.

## 7. Artifact language

Case files, evidence logs, field reports, chain-of-custody forms,
incident reports, records-division memos, a "case status" summary
sheet.

## 8. CS2 problem generators

- **Composition/invariants:** an evidence log where an item can never
  be checked out by two people simultaneously and custody can never
  have a gap.
- **Contracts/interfaces:** two agencies' field-report formats that
  don't match and need a shared contract to reconcile.
- **Inheritance/polymorphism:** different case types (property,
  missing-persons, fraud) sharing a common "Case" contract with
  type-specific evidence requirements.
- **Collections/search/order:** sorting evidence by chain-of-custody
  order vs. relevance to the case; prioritizing the case backlog.
- **GUI/model-view:** a case-status dashboard for field investigators
  who don't want to read raw records.
- **Data visualization:** an honest chart of case backlog and closure
  rate over time.
- **Peer review/stabilization, source management:** Chief Arana and
  the student reconciling two versions of the same case file after a
  records-division review.

Full cross-world mapping: `capability_map.md`.

## 9. Continuity

See `continuity_ledger.md`, section "Investigation Bureau." Consult
before writing new material; add new named characters/threads there
in the same commit that introduces them.

## 10. Seeds and delayed payoffs

- A field report from Investigator Reyes contains a timestamp that
  doesn't quite reconcile with the records-division log -- initially a
  minor discrepancy, potentially a real data-integrity problem later.
- Records Clerk Doyle's early "just flag anything weird" instruction
  could become genuinely load-bearing once the case volume grows past
  what manual review can catch.
- An early assumption that the Bureau only handles one case type could
  quietly break once a second case type (with different evidence
  rules) needs the same system.
- A minor procedural shortcut Chief Arana approves early ("just for
  now") could resurface as a real design problem under audit pressure.

None of these are required to pay off. Garden, not railroad.

## 11. Injection menu

- 30-45s video: Chief Arana briefing the student on why the records
  system matters -- "close enough" is not a standard here.
- Written memo: Records Clerk Doyle flagging a discrepancy between two
  logs, asking the student to look into it.
- One-slide interruption: an incoming field report from Investigator
  Reyes in a format that doesn't match the existing system.
- Artifact drop: a case-file excerpt with a redacted section and a
  stamp date that raises a small question.
- Character update: Chief Arana's brief note that the backlog is
  finally trending down -- a rare positive beat, useful late in the
  semester.

## 12. Safety and taste

See `README.md`'s shared boundaries. Specific to this world: no
graphic crime depiction, no victims as plot devices, no treating real
harm as entertainment, no "detective genius" trope that requires the
student to solve a whodunit puzzle rather than build a records system.

## Prototype: one briefing concept

> **CHIEF ARANA, seated at a desk, case folder closed in front of her.**
>
> "You've been assigned to Case Records." *(opens folder, doesn't
> look up yet)* "Here's what you need to understand on day one: this
> Bureau doesn't run on hunches. It runs on records that agree with
> each other. When they don't --" *(looks up)* "-- that's not a
> mystery. That's a bug. And it's yours to find before it becomes
> someone's bad day in court. Welcome to the Division."

Runtime: ~30s. Establishes stakes (record integrity, not detective
work), character (Arana, measured and precise), and the ask.
