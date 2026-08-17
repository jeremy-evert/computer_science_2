# CS2 Presentation System -- Style Guide

Built by Prompt 015 (`sidecar/prompts/015_build_cs2_slide_system.md`) as
the shared foundation Cleo reuses when authoring weekly decks. This
document is deliberately short: it is meant to be consulted immediately
before class, not read as a design manual.

## What this is

- `theme/cs2theme.sty` -- colors, fonts, title page, frame title bar,
  footline. The visual identity.
- `theme/cs2commands.sty` -- the 21-pattern slide vocabulary, code
  standards, diagram standards, instructor-usability helpers.
- `demo/demo-deck.tex` -- a small Stack-ADT deck exercising every
  pattern, proving the system compiles and reads cleanly. Not a real
  week; do not extend it into one.

A weekly deck is a new `.tex` file (see "Starting a new week" below)
that loads both `.sty` files and picks whichever patterns that week
actually needs.

## The 21 patterns, and the one thing to know about each

Most patterns are ordinary environments:

```latex
\begin{conceptframe}{Encapsulation}
  ...
\end{conceptframe}
```

**Exception -- code-bearing and multi-column patterns cannot use that
form.** Beamer's own frame-body collector (`\beamer@collect@@body`)
breaks with "Runaway argument? File ended while scanning use of
\beamer@collect@@body" whenever a `\begin{frame}` is opened through
macro indirection (a custom `\newenvironment`) AND either (a) the frame
is `[fragile]` (needed for `\begin{lstlisting}`), or (b) the frame
contains another split environment nested inside it (`\begin{columns}`
plus per-column environments). This is a confirmed Beamer limitation,
not a guess -- reproduced in isolation during Prompt 015's build. It
affects patterns 5, 6, 7, 8, and 13. Those five instead ship as a
kicker command, called as the first line inside a frame the deck author
opens literally:

```latex
\begin{frame}[fragile]{Code Example: A Minimal Stack}
\codeframekicker
\begin{lstlisting}
class Stack:
    ...
\end{lstlisting}
\end{frame}
```

```latex
\begin{frame}{Concept + Diagram: push/pop}
\conceptdiagramkicker
\begin{conceptdiagrambody}
  \begin{concepttext} ... \end{concepttext}
  \begin{conceptdiagram} ... \end{conceptdiagram}
\end{conceptdiagrambody}
\end{frame}
```

```latex
\begin{frame}[fragile]{Compare: Array-Backed vs. Linked Stack}
\begin{comparebody}
  \begin{compareleft}{Array-backed} ... \end{compareleft}
  \begin{compareright}{Linked-node} ... \end{compareright}
\end{comparebody}
\end{frame}
```

| # | Pattern | Environment | Kicker command (if literal-frame) |
|---|---|---|---|
| 1 | Title / opening | `\maketitle` inside `\begin{frame}[plain]` | -- |
| 2 | Today's destination | `destinationframe` | -- |
| 3 | Why this matters | `whymattersframe` | -- |
| 4 | Core concept | `conceptframe` | -- |
| 5 | Concept with diagram | literal frame + `conceptdiagrambody` | `\conceptdiagramkicker` |
| 6 | Code example | literal `[fragile]` frame | `\codeframekicker` |
| 7 | Code walkthrough | literal `[fragile,t]` frame | `\codewalkthroughkicker` |
| 8 | Predict before running | literal `[fragile]` frame | `\predictkicker` |
| 9 | Live coding prompt | `livecodingframe` | -- |
| 10 | Worked problem | `workedproblemframe` | -- |
| 11 | Think / pair / discuss | `pairdiscussframe` (+ `\stopandwork`) | -- |
| 12 | Common failure/misconception | `misconceptionframe` | -- |
| 13 | Compare two approaches | literal `[fragile]` frame + `comparebody` | -- |
| 14 | Design decision | `designdecisionframe` | -- |
| 15 | AI collaboration/verification | `aimomentframe` | -- |
| 16 | Reasoning Odyssey connection | `odysseyframe` | -- |
| 17 | World Bible entry | `worldbibleframe` (wraps `worldbibleentry`) | -- |
| 18 | Odyssey checkpoint/gate | `odysseygateframe` | -- |
| 19 | Evidence to produce | `evidenceframe` | -- |
| 20 | Recap | `recapframe` | -- |
| 21 | Exit question/next move | `exitframe` | -- |

Not every pattern appears every week. This is a vocabulary to choose
from, not a checklist to exhaust.

## Weekly rhythm (default, flexible)

A normal CS2 week has three meetings (M/W/F). This is the recommended
default shape, not a rigid script -- skip or reorder patterns as the
actual content demands.

**Opening the week (Monday, first few minutes):**
`destinationframe` -> `whymattersframe`. Tell students where the week
goes and why it's worth the time before touching any technical content.

**Introducing a capability (any day, once per new idea):**
`conceptframe` or `conceptdiagramframe` -> `codeframe` or
`codewalkthroughframe`. Concept before code, always -- code without
the concept is memorization.

**Live coding belongs right after a walkthrough**, while the idea is
still fresh: `livecodingframe`. Type it live; let the first attempt be
wrong (see `\instructorcue` below).

**Practice belongs after live coding, not instead of it:**
`workedproblemframe` -> `pairdiscussframe` (with `\stopandwork` to mark
the deliberate pause) -> optionally `predictframe` before running
anything new.

**Misconceptions and comparisons are best placed right where students
are about to make the mistake**, not bundled into a separate "gotchas"
section: `misconceptionframe`, `compareframe`/`comparebody`,
`designdecisionframe`.

**The Reasoning Odyssey enters once there is a real capability to hang
it on** -- usually mid-week, never as the very first slide of a class
meeting: `odysseyframe`, `worldbibleframe`, `evidenceframe`. AI
collaboration moments (`aimomentframe`) fit naturally right after a
live-coding or worked-problem slide, where the "would I have caught
this?" question is concrete rather than abstract.

**Closing a class meeting:** `recapframe` -> `exitframe`. Every meeting
ends with a question students can't answer by having merely watched.

**Closing a week:** if the week has a checkpoint or gate, place
`odysseygateframe` at the actual close, pointing at the rubric rather
than restating it (see "Odyssey checkpoint" pattern -- it's a pointer,
not the rubric itself).

## Code standards

- **Python only** (matches CS1 and existing `lessons/code/`). No Java,
  no pseudocode dressed up as Python.
- `listings`, not screenshots. Code stays in version control, diffable,
  rebuildable, and copy-pasteable by students.
- Default style is `cs2python` (set globally via `\lstset`); nothing
  extra needed for a plain `\begin{lstlisting}`.
- Keep snippets short enough to read from the back row -- if a snippet
  needs `\footnotesize` to fit, it is too long for one slide. Split it
  across a `codewalkthroughframe`'s overlays instead of shrinking
  further.
- `\highlightline{...}` wraps the one or two lines students should
  notice; do not highlight more than that or it stops meaning anything.
- Before/after and broken/fixed pairs use the `comparebody` +
  `compareleft`/`compareright` combination (same visual grammar; use
  whichever label reads more naturally for the specific slide).

## Diagram standards

One visual grammar, defined as TikZ styles in `cs2commands.sty`:

- `cs2class` -- solid box, drop shadow: a class or object.
- `cs2interface` -- dashed box: an interface or contract.
- `cs2flow` -- rounded box: a step in a control/data-flow diagram.
- `cs2inherit` -- hollow-triangle arrow: "is-a" (inheritance).
- `cs2compose` -- filled-diamond arrow: "has-a" (composition).
- `cs2implement` -- dashed hollow-triangle arrow: "implements" (interface contract).
- `cs2dataflow` -- plain arrow: control/data flow, no UML claim.

Keep every diagram simple enough to redraw on a whiteboard in under a
minute. If a diagram needs a legend to be readable, it has too many
element types in it -- split it into two diagrams instead.

## Instructor usability

- `\instructorcue{...}` -- a short, always-visible cue (not a hidden
  speaker note nobody sees from a single classroom display). One line.
  If it needs two lines, it belongs in your own prep notes, not the
  slide.
- `\stopandwork{...}` -- the one and only "students work now" marker.
  Visually distinct from every content pattern so it can never be
  mistaken for lecture content mid-glance.
- Edit immediately before class without fear: every pattern is a
  self-contained environment or a two-line literal-frame block: there
  is no cross-slide state to break by reordering or deleting a slide.
- If a discussion runs long, just skip straight to `recapframe` --
  nothing in the system requires visiting every pattern in a deck.

## Accessibility

- Body text sizes are set for projection (`\normalsize` default, never
  smaller than `\footnotesize` for anything students must read).
- Every accent color (Odyssey teal, World Bible violet, danger red,
  good green) is always paired with a text kicker label -- color is
  never the sole carrier of meaning.
- `cs2codebg`/`cs2codefg` are a high-contrast dark-on-light-slide pair,
  chosen to survive a washed-out classroom projector.
- Diagrams use shape + arrowhead style (not color alone) to distinguish
  inheritance/composition/interface/flow.

## Known cosmetic yellow

`pdflatex` reports small (~7pt) "Overfull \hbox" warnings on most
frames, tied to the kicker rule (`\rule{\linewidth}{1.6pt}`) and
footline boxes. These are sub-pixel-at-projection-scale font-metric
rounding, not content bleeding off the slide (confirmed by rendering
and visually inspecting `demo-deck.pdf` at multiple pages) -- cosmetic
only. Worth a real fix before the system carries a full semester of
decks, but it does not block using the system now.

## Starting a new week

```latex
\documentclass[aspectratio=169]{beamer}
\usepackage{../theme/cs2theme}
\usepackage{../theme/cs2commands}

\setcsweek{Week 4}

\title{Week 4: <topic>}
\subtitle{<one-line framing>}
\author{Computer Science II \textbullet\ Dr. Jeremy P. Evert}
\date{Fall 2026}

\begin{document}
\begin{frame}[plain]\titlepage\end{frame}

% choose patterns from the table above -- see "Weekly rhythm"

\end{document}
```

**Use the CS2 slide system and build Week X** -- once this file exists
and picks its patterns, no presentation architecture needs reinventing.
