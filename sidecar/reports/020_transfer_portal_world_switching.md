# Report 020: The Transfer Portal -- World Switching Policy

Prompt: `../prompts/020_transfer_portal_world_switching.md`.

## What was built

- `sidecar/worlds/transfer_portal/README.md` -- the canonical policy:
  early transfer (free, easy), later transfer (short check-in), the
  seven-field migration receipt template, academic treatment (attaches
  to the student's existing World Bible evidence, no new grading
  weight), instructor workflow, data/storage guidance preserving
  Prompt 018's fixed four-value model, student-facing explanation, and
  world-specific transfer-document flavor for all four worlds (Claim
  Transfer Record / Case Reassignment Form / Transfer Order / Change
  of Role Memo).
- `sidecar/worlds/four_calls/README.md` -- "World-switch policy"
  section rewritten from "unresolved, flagged" to "resolved," with the
  choice-screen guidance and closing message each gaining exactly one
  added sentence pointing to the Transfer Portal, per the prompt's
  explicit "do not over-explain during initial world selection"
  instruction.
- `presentations/beamer/four_calls/the-four-calls.tex` -- matching
  one-sentence additions to the comparison/choice-screen frame and the
  closing `exitframe`. Recompiled clean, still 13 pages (no new slide
  added -- the policy fits inside two existing frames without needing
  a dedicated "terms and conditions" slide, matching the prompt's
  "make that change useful... not a terms-of-service screen").
- `sidecar/worlds/continuity_ledger.md` -- one new entry recording that
  the policy exists. Individual student transfers are **not** recorded
  here going forward -- those belong in each student's own World Bible
  (the migration receipt), never in this internal canon ledger.

## What was explicitly not built

Per the prompt's "explicitly out of scope" list: no fifth world, no
grading rewrite, no new major assignment, no large approval workflow,
no LMS data-model rebuild, no restart requirement, no punitive
deadline. The "Data/storage behavior" section states plainly that if
the eventual implementation only stores one active world value,
changing that value plus keeping the migration receipt in the
student's World Bible is sufficient -- no new infrastructure was
designed or implied beyond what Prompt 018 already specified.

## Remaining decision Jeremy genuinely must make

**The exact early-transfer cutoff date.** No source file in the repo
(`docs/grading-model.md`, `assignments/A2-coding-odyssey-project.md`,
`ROADMAP.md`) defines an add/drop-style date, and the prompt explicitly
said not to invent one if none exists. `transfer_portal/README.md`
recommends "before the Week 6 checkpoint" as a natural, already-
existing course boundary rather than a fabricated new one, but the
actual cutoff -- and whether Week 6 is the right anchor at all -- is
Jeremy's call before this policy is published to students.

No other open questions were identified; the policy is otherwise
publication-ready pending that one date.
