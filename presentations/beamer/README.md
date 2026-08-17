# CS2 presentation source

Course-owned Monday technical decks belong here when a lesson has a reviewed
slide source. Keep one directory per week and share a common theme/preamble
when the deck family is established.

## The reusable presentation system (Prompt 015)

`theme/cs2theme.sty` and `theme/cs2commands.sty` are the shared CS2 Beamer
theme and 21-pattern slide vocabulary built by
`../../sidecar/prompts/015_build_cs2_slide_system.md`. Read
`STYLE_GUIDE.md` before authoring a weekly deck -- it documents every
pattern, the weekly rhythm, code/diagram standards, and a real (confirmed
by hand) Beamer limitation that changes how five of the patterns must be
used. `demo/demo-deck.tex` is the validation deck exercising all 21
patterns; it is not Week 3 and not "Welcome to the Odyssey" -- do not
extend it into real course content.

A new week starts as its own `weekNN/` directory containing a `.tex` file
that loads both theme files -- see STYLE_GUIDE.md's "Starting a new week."

Professional Minds decks are not copied here: their source and compiled decks
remain in `../../../../professional_minds/presentations/`. Monday Moment
content is not copied here: it remains in `../../../../ai_fluency/ai_i/`.

Only reviewed source and intentional deliverables belong in this directory.
Do not commit LaTeX build intermediates (`.aux`, `.log`, `.nav`, `.out`, `.snm`,
`.toc`, or `.vrb`).
