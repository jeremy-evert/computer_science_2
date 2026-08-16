# Prompt 014E — Postmortem and close the CS2 Week 16 Farkle build

**Status:** WAITING ON SCRIPTED VALIDATION  
**Parent:** Prompt 014

## Mission

Audit the implemented Week 16 surface against the current-state report, target map, implementation plan, and raw validation receipts.

Write:

`sidecar/reports/014_build_cs2_week16_farkle_ml_postmortem.md`

## Required postmortem contents

- what the pre-build report correctly identified;
- what changed during implementation;
- final package/data-flow architecture;
- exact hardened CS1 provenance consumed;
- files created/changed;
- validation script result and test counts;
- sample experiment evidence and what it demonstrates;
- student burden/runtime estimate;
- CS2 course concepts actually reused;
- Architecture cost/effectiveness ideas reused;
- what was deliberately omitted;
- remaining GREEN/YELLOW/RED items;
- raw receipt locations;
- commit SHA(s);
- automation promotion recommendation if this workflow is requested again.

## Closure acceptance

Do not call Week 16 ready unless:

- executable source exists;
- tests exist and were run on a real checkout;
- the one-command validator has a raw receipt;
- student/instructor artifacts point to the real implementation;
- no known-bad CS1 semantics were copied;
- no new technical checkpoint or paid/hardware requirement was introduced.

If a physical/runtime dependency remains, close as IMPLEMENTED WITH NAMED YELLOWS rather than pretending GREEN.
