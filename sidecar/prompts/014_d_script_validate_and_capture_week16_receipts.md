# Prompt 014D — Script validation and capture raw Week 16 receipts

**Status:** WAITING ON 014B/014C  
**Parent:** Prompt 014

## Doctrine

This is the second serious course-specific Farkle build. Repeated validation must now be scripted.

## Build

Create:

`scripts/validate_week16_farkle.py`

The script must run from the repo root and, without installing or reconfiguring anything:

1. print runtime/source context;
2. run the Week 16 automated tests;
3. run a fixed baseline comparison;
4. run the transparent learner smoke path;
5. run one CS2 experiment bundle;
6. write JSON/CSV result evidence;
7. generate the Week 16 chart when the existing plotting dependency is available;
8. write a timestamped raw receipt under `sidecar/runs/`;
9. exit nonzero when correctness/test/required-run checks fail.

## Validation acceptance

A real checkout must be able to validate the required Week 16 surface with one command:

```text
python scripts/validate_week16_farkle.py
```

The receipt must include commands, exit codes, source/provenance, result paths, and any optional plotting yellow.

Do not silently install matplotlib, pytest, containers, or other tooling.

If this same validation orchestration is requested for a third course, stop copying it and promote the stable runner contract into shared automation.
