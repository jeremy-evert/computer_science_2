# CS2 content naming conventions

This repository is the source for COMSC-1053 Fall 2026. Filenames should make
the course's weekly spine and its reusable assessment templates easy to find.

## Core conventions

- `planning/week-NN.md` — the 17-week course plan; `week-17-finals.md` is the
  finals-period companion when a separate finals plan is useful.
- `lessons/<topic>.md` — durable lesson handouts; week-specific labs may use a
  `week-NN-` prefix.
- `assignments/A<n>-slug.md` — reusable assignment templates. A1 is weekly
  practice, A2 is the Coding/Reasoning Odyssey, A3/A4/A7 are recurring
  Wednesday/Friday artifacts, A5 is final reflection, and A6 is the staged
  professional-pathway portfolio.
- `assignments/odyssey_gates/week-NN.md` and
  `rubrics/odyssey_gates/week-NN_rubric.md` — paired weekly evidence and
  scoring documents. Week 2 is Local AI Lab setup; Week 3 is the ungraded
  World Bible seed; Weeks 4–15 are graded evidence with the larger
  checkpoints called out in the grading model; Week 16 is a retired
  shared-strand reservation.
- `monday_moments/` contains only the local pointer/template. Canonical
  Monday Moment content for Fall 2026 remains `../ai_fluency/ai_i/`.
- `sidecar/prompts/NNN_slug.md` pairs with the explicitly requested
  `sidecar/reports/NNN_slug.md`; completed prompts move only after Foreman
  accepts the work.

Do not create local copies of shared Week 1, Week 2, Professional Minds, or
AI Fluency lesson bodies when a source repository already owns them.
