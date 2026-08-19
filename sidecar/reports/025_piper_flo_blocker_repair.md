# Report 025 — Piper repair of Flo preflight blockers

**Status:** READY FOR FRESH FLO PREFLIGHT  
**Course:** COMSC-1053-1417 Computer Science II, Fall 2026  
**Date:** 2026-08-19

## Trigger

Flo's isolated production campaign `20260819T141517Z-2586746` proved that the clean-runway design worked, then exposed two later blockers before any Canvas contact:

1. `scripts/cs2_production.py::_contract()` expected compatibility keys that `course_metadata.yaml` did not expose.
2. The isolated runway omitted source repositories that the current CS2 DesiredCourse compiler dereferences.

No production write occurred in the blocked run.

## Repair 1 — reconcile the CS2 production contract

`course_metadata.yaml` remains the durable source of the official Fall 2026 course facts. It now also exposes explicit compatibility aliases required by the guarded production wrapper:

- `course.title = Computer Science II`
- `course.course_code = COMSC-1053`
- `course.section = 1417`
- `term.name = Fall 2026`
- `instructor.name = Dr. Jeremy P. Evert`

These values duplicate, rather than replace, the already tracked official fields. A new production-wrapper test calls `_contract()` against the real repository YAML and requires the exact production identity:

`COMSC-1053-1417 / Computer Science II / Fall 2026 / Dr. Jeremy P. Evert`

This closes the untested schema-drift path that produced `STOP: 'title'`.

## Repair 2 — complete the isolated source runway

The launcher now provisions clean origin snapshots for every repository the current CS2 production path actually consumes:

- `computer_science_2`
- `course_foundry`
- `harbor`
- `imprint`
- `local_ai_lab_setup`
- `ai_fluency`
- `professional_minds`
- `computer_science_1`

The last three are pinned read-only source inputs. In particular, Computer Science 1 remains outside Flo's work lane; its isolated origin clone exists only because the current Course Foundry CS2 compiler reads two generic gradebook pages from it. The ordinary CS1 checkout and Chaz's active work remain untouched.

The launcher prints the exact HEAD of every isolated input before Claude starts. A regression test asserts that the launcher contains all eight required repositories.

## Safety properties preserved

- Architecture remains untouched.
- Ordinary CS1 worktrees remain untouched.
- No stash/reset/clean is used on human work.
- Week 1 remains outside CS2 write authority.
- Production writes remain forbidden until fresh read-only preflight reaches `GREEN TO WRITE` and Jeremy explicitly replies `WRITE CS2` in that Flo session.
- `prune_scope=none` remains mandatory.
- The production authorization token remains bound to the compiled DesiredCourse digest and full dry-run action log; therefore changes to consumed source content alter the plan digest and stale the token.

## Next action

Do not resume the prior Flo seat. Exit it and launch a fresh campaign from current CS2 `main` so all source clones are rebuilt from current origins.

Canonical launch from Brandy:

```bash
cd /mnt/brandy_nvme/jevert/git/computer_science_2
git pull --rebase origin main
bash ./sidecar/launch_flo.sh
```

Expected next useful state is either a newly proven blocker or the compact `GREEN TO WRITE` packet. No further Piper construction is justified before that fresh preflight.
