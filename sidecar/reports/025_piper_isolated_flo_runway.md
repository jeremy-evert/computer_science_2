# Report 025 — Piper repair: isolate the CS2 Flo production runway

**Date:** 2026-08-19  
**Status:** READY TO RELAUNCH FLO  
**Scope:** Computer Science II only

## Trigger

The first Flo production-closeout attempt correctly stopped before production because the ordinary `course_foundry` checkout on Brandy contained active, unrelated CS1 work. The same run also proved that three validator module names carried in Prompt 022 were historical drift: they do not exist in current Course Foundry source.

The useful targeted tests were green:

- `computer_science_2/tests/test_cs2_production.py`: 4 passed
- `course_foundry/tests/test_cs2_desired_course.py`: 4 passed

No production Canvas write occurred.

## Root cause

The original launcher and production burn assumed the shared ordinary sibling checkouts themselves should be the production dependency runway. That made unrelated active work in another lane a hard CS2 blocker and implicitly invited a human to clean or adjudicate another worker's tree.

That violates the intended operating model. Jeremy should not be the message bus, and CS2 should not require Chaz's CS1 checkout to become idle before Flo can perform a read-only production preflight.

## Repair

`sidecar/launch_flo.sh` now treats the ordinary CS2 checkout only as a control plane and creates a new isolated campaign root under:

```text
../computer_science_2.worktrees/flo-production/<campaign-id>/
```

It shallow-clones fresh origin snapshots of:

- `computer_science_2`
- `course_foundry`
- `harbor`
- `imprint`
- `local_ai_lab_setup`

Flo launches inside the isolated `computer_science_2` clone with those four clean sibling dependencies. The launcher deliberately does not stash, reset, clean, merge, or otherwise alter ordinary working checkouts.

The existing Course Foundry `.venv` is used only as the Python interpreter/package environment; source imports come from the isolated origin clones.

## Prompt correction

Prompt 022 now requires only validators/tests that actually exist in current source:

```bash
python3 -m pytest -q tests/test_cs2_production.py
cd ../course_foundry
python3 -m pytest -q tests/test_cs2_desired_course.py
cd ../computer_science_2
```

The obsolete `week1_validator`, `completeness_validator`, and `cross_repo_integrity` module calls were removed from the burn rather than replaced with invented substitutes.

The production wrapper's own pinned DesiredCourse shape remains the runtime contract: 16 modules, 155 modeled objects, 14 CS2 assignment groups totaling 100%, Weeks 2-17 only, `prune_scope=none`.

## Boundaries preserved

- Computer Science 1 ordinary checkout: untouched.
- Computer Architecture: untouched.
- Luna branches: no promotion prerequisite.
- Week 1 shared kickoff: remains read-only/outside CS2 write authority.
- Production Canvas: no write during this repair.

## Relaunch

After bringing the local CS2 control checkout forward enough to contain the new launcher, relaunch with:

```bash
cd /mnt/brandy_nvme/jevert/git/computer_science_2 && ./sidecar/launch_flo.sh
```

The next meaningful blocker, if any, must now come from clean current origin source or the read-only production preflight itself, not unrelated dirt in another lane.
