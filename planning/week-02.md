# Week 2 — Robustness I: Exceptions, plus the Local AI Lab

**Date:** Mon Aug 24 / Wed Aug 26 / Fri Aug 28, 2026, MWF 1:00-1:50 PM (room TBD)

## Status

Full instructional week, MWF 1:00-1:50 PM.

## Weekly Focus

Exceptions, Round 1 (Ch. 10 in the confirmed CS2 map): invalid input, validation, and `try`/`except` reasoning. Source grounding: `docs/curriculum/course-sequence.md`; `lessons/exceptions-modules-files.md`.

Week 2 also carries **Build and Verify Your Local AI Lab**, the shared local-AI classroom module CS2 shares with DSCT (and historically Software Engineering). This is not an AI-tools survey; it is CS2's professional software-development environment — the same evidence discipline (baseline, request, diff, independent test, accept/reject) the course already asks of every AI-assisted claim (`docs/course-ethos.md`) — made concrete with a real local toolchain. See `planning/week-02-local-ai-lab-integration.md` for the full crosswalk. Exact meeting-day allocation between the exceptions spine and the local-AI lab is **unclaimed** — no current source specifies a Monday/Wednesday/Friday split, so none is asserted here.

The module's roles, at CS2 depth:

- **PowerShell** — the classroom command surface: navigation, running a command, reading output.
- **Python** — the runtime that executes the supplied exercise and its unit tests.
- **Git** — evidence of file change (`status`, `diff`) around the supplied disposable exercise.
- **Aider** — the coding client that sends a bounded, explicit change request against the project.
- **Ollama** — the local model server, reachable only at `localhost` (loopback), never exposed to the network.
- **The approved local model** (`qwen3:8b`) — generates a proposed change; it is fallible and is never treated as correct merely because it ran.

## Readiness/evidence workflow

Students run the shared `windows_classroom` command surface (`Check` → `Baseline` → `Launch` → `Diff` → `Final`, with `Reset -ConfirmReset` available) to establish, in layers, that the tool, the API, the model, and inference are each actually working — and to distinguish those four different claims from each other and from "the generated code is correct." `Check` must report `READY` before the bounded exercise begins.

## CS2 bounded Aider extension

Students use Aider to request one narrowly bounded change to a known-failing `format_student_name` baseline (replace all-uppercase formatting with title case), then independently verify it: inspect the `git diff`, rerun the supplied unit test, and decide for themselves — using the baseline, the diff, and the test result, not the fact that generation completed — whether to accept the change. This is the CS2-specific extension already defined in `local_ai_lab_setup/curriculum/cs2/week2_extension.md`; CS2 does not redefine it here.

## Gate-or-checkpoint tie-in

Coding Odyssey weekly gate: use a bounded exception-handling path in the world. The World Bible baseline is also due, but its exact form depends on the unresolved new-world versus CS1-continuation decision in A2.

The local-AI lab readiness experience runs alongside the Odyssey gate this week; it does not replace it. Both are due Week 2.

## Due this week

- Week 2 Odyssey gate (`assignments/odyssey_gates/week-02.md`) and World Bible baseline; fulfills `assignments/A1-weekly-coding-practice.md`.
- Local AI Lab readiness evidence and CS2 reflection; see `assignments/week-02-local-ai-readiness.md`.
