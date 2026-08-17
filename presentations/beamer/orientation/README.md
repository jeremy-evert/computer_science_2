# Orientation decks

Not weekly teaching material and not world-specific lore -- see
`../../../sidecar/prompts/016_welcome_to_reasoning_odyssey.md`,
"Architectural firewall." This directory holds the deck(s) that explain
the shared academic fabric connecting every student regardless of
which of the four worlds they choose.

## welcome-to-the-odyssey.tex

Built on the Prompt 015 CS2 slide system (`../theme/`). 12 slides,
compiles clean. Explains: the Odyssey as one evolving software world
(not disconnected assignments), the World Bible's real purpose, the
weekly-gate vs. checkpoint distinction (with real point values from
`docs/grading-model.md`), that all four worlds share one grading
standard, and a spoiler-light introduction to the four world choices.

### Deck-to-source mapping

| Deck content | Source of truth |
|---|---|
| "One software world all semester" framing | `assignments/A2-coding-odyssey-project.md` |
| World Bible definition and purpose | `assignments/A2-coding-odyssey-project.md`, "World Bible" section |
| Weekly gate mechanics (25 pts, Weeks 3-5/7-8/10-13) | `docs/grading-model.md`, "Odyssey gate grading shape" |
| Checkpoint mechanics (Weeks 6/9/14, 40/50/60 pts) | `docs/grading-model.md`, same section |
| Four-dimension gate rubric (world-fit, evidence, reasoning, AI accountability) | `docs/grading-model.md` |
| Four world names and one-line flavor (Frontier Settlement, Investigation Bureau, Starship Log, Small Business) | `assignments/A2-coding-odyssey-project.md`, "Growth path" intro paragraph -- the **only** place these four names currently exist in the repo |
| "All worlds share the same academic standard" | `assignments/A2-coding-odyssey-project.md`, "Grading" section |

### Source ambiguity discovered

The four world names exist in exactly one place in the current
repository (`assignments/A2-coding-odyssey-project.md`'s opening
paragraph) as a bare list with zero elaboration beyond four
one-clause examples ("settlement services, case workflows, ship
operations, business inventory/transactions"). There is no other
world-lore source anywhere in the repo as of this deck's build (no
character names, hooks, visual identity, or narrative material exists
yet). This deck's four one-line descriptions on the "Choose the World
You'll Build In" slide are written directly from that source
paragraph -- they do not add flavor, characters, or lore beyond what
A2 already states, per the prompt's "preserve surprise" and "do not
build the four world bibles" boundaries. Later Prompt 017/018 work
should treat A2's four names as the fixed, authoritative list (do not
invent a fifth or rename an existing one) and treat everything else
about each world as open to build.
