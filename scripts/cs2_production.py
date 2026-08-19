#!/usr/bin/env python3
"""Guarded Fall 2026 CS2 production reconcile.

preflight: production reads only -> GREEN TO WRITE + a diff-bound token
write: fresh preflight + matching token -> Weeks 2-17 reconcile -> no-op closeout

Week 1 is intentionally excluded; semester_kickoff_week owns it.
"""
from __future__ import annotations

import argparse
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SIBLING_ROOT = ROOT.parent
PREFLIGHT_RECEIPT = ROOT / "sidecar/runs/flo_cs2_preflight.json"
CLOSEOUT_RECEIPT = ROOT / "sidecar/runs/flo_cs2_closeout.json"
RECEIPT_PATHS = {str(PREFLIGHT_RECEIPT.relative_to(ROOT)), str(CLOSEOUT_RECEIPT.relative_to(ROOT))}

# Exact DesiredCourse shape accepted at the final Savnac fixed point.
EXPECTED_MODULE_COUNT = 16
EXPECTED_OBJECT_COUNT = 155
EXPECTED_ASSIGNMENT_GROUP_COUNT = 14


def _bootstrap() -> None:
    for name in ("course_foundry", "harbor", "imprint"):
        path = SIBLING_ROOT / name
        if path.is_dir() and str(path) not in sys.path:
            sys.path.insert(0, str(path))


def _git(cwd: Path, *args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=cwd, text=True, capture_output=True)
    if proc.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed in {cwd}: {(proc.stderr or proc.stdout).strip()}")
    return proc.stdout.strip()


def _status_path(line: str) -> str:
    value = line[3:].strip() if len(line) >= 4 else line.strip()
    return value.rsplit(" -> ", 1)[-1]


def _repo_state(path: Path, *, cs2: bool = False) -> dict[str, Any]:
    try:
        inside = _git(path, "rev-parse", "--is-inside-work-tree") == "true"
    except Exception:
        inside = False
    if not inside:
        raise RuntimeError(f"required repository is not a Git checkout: {path}")
    dirty = _git(path, "status", "--porcelain").splitlines()
    if cs2:
        dirty = [line for line in dirty if _status_path(line) not in RECEIPT_PATHS]
    return {
        "path": str(path),
        "head": _git(path, "rev-parse", "HEAD"),
        "branch": _git(path, "rev-parse", "--abbrev-ref", "HEAD"),
        "dirty": dirty,
    }


def _source_states() -> dict[str, dict[str, Any]]:
    repos = {
        "computer_science_2": ROOT,
        "course_foundry": SIBLING_ROOT / "course_foundry",
        "harbor": SIBLING_ROOT / "harbor",
        "imprint": SIBLING_ROOT / "imprint",
        "local_ai_lab_setup": SIBLING_ROOT / "local_ai_lab_setup",
    }
    states = {name: _repo_state(path, cs2=name == "computer_science_2") for name, path in repos.items()}
    dirty = {name: state["dirty"] for name, state in states.items() if state["dirty"]}
    if dirty:
        detail = "\n".join(f"  {name}: {entries[:20]}" for name, entries in dirty.items())
        raise RuntimeError(f"source-bearing repositories are dirty; preserve them and stop:\n{detail}")
    return states


def _contract() -> dict[str, str]:
    import yaml

    data = yaml.safe_load((ROOT / "course_metadata.yaml").read_text())
    return {
        "title": str(data["course"]["title"]).strip(),
        "section_identity": f"{data['course']['course_code']}-{data['course']['section']}",
        "term": str(data["term"]["name"]).strip(),
        "instructor": str(data["instructor"]["name"]).strip(),
    }


def _require_production_config():
    from harbor.config import read_canvas_config
    from imprint.config import PRODUCTION_HOST_MARKER, require_host_marker

    env_url = os.environ.get("CANVAS_API_BASE_URL", "").strip().rstrip("/")
    require_host_marker(env_url, PRODUCTION_HOST_MARKER, tool_name="CS2 production deployer")
    config = read_canvas_config(enforce_course_allowlist=True)
    require_host_marker(config.api_base_url, PRODUCTION_HOST_MARKER, tool_name="CS2 production deployer")
    return config


def _discovery_client():
    from harbor.client import CanvasClient
    return CanvasClient(_require_production_config())


def _course_client(course_id: int):
    from harbor.client import CanvasClient
    from harbor.config import CanvasConfig

    config = _require_production_config()
    return CanvasClient(CanvasConfig(config.api_base_url, config.api_token, frozenset({course_id})))


def _normalized_title(value: str) -> str:
    return " ".join(value.strip().casefold().replace(" ii", " 2").split())


def _candidate_matches(course: dict[str, Any], contract: dict[str, str]) -> bool:
    identity = contract["section_identity"]
    course_code = str(course.get("course_code") or "").strip()
    sis_course_id = str(course.get("sis_course_id") or "").strip()
    term_name = str((course.get("term") or {}).get("name") or "").strip().casefold()
    return (
        (course_code == identity or identity in sis_course_id)
        and _normalized_title(contract["title"]) in _normalized_title(str(course.get("name") or ""))
        and term_name == contract["term"].casefold()
    )


def _discover_target(client, contract: dict[str, str]) -> dict[str, Any]:
    from harbor.api import list_courses

    matches = [course for course in list_courses(client) if _candidate_matches(course, contract)]
    if len(matches) != 1:
        compact = [
            {"id": c.get("id"), "name": c.get("name"), "course_code": c.get("course_code"),
             "sis_course_id": c.get("sis_course_id"), "term": (c.get("term") or {}).get("name")}
            for c in matches
        ]
        raise RuntimeError(
            f"expected exactly one Fall 2026 target matching {contract['section_identity']!r}; "
            f"found {len(matches)}: {compact}"
        )
    return matches[0]


def _verify_target(client, course_id: int, contract: dict[str, str], discovered: dict[str, Any]) -> dict[str, Any]:
    from harbor.api import get_course

    _, live = get_course(client, course_id)
    name = str(live.get("name") or "").strip()
    code = str(live.get("course_code") or "").strip()
    sis = str(live.get("sis_course_id") or "").strip()
    identity = contract["section_identity"]
    problems = []
    if int(discovered.get("id")) != course_id:
        problems.append("discovery result and allowlisted course id disagree")
    if not (code == identity or identity in sis):
        problems.append(f"expected {identity!r}; got course_code={code!r}, sis_course_id={sis!r}")
    if _normalized_title(contract["title"]) not in _normalized_title(name):
        problems.append(f"expected CS2 title; got {name!r}")
    if problems:
        raise RuntimeError("CS2 production target identity mismatch: " + "; ".join(problems))
    return {
        "id": course_id,
        "name": name,
        "course_code": code,
        "sis_course_id": sis,
        "term": (discovered.get("term") or {}).get("name"),
    }


def _build_plan(course_id: int):
    from course_foundry.savnac_deploy import SourcePaths, _build_cs2

    defaults = SourcePaths.defaults()
    plan = _build_cs2(
        replace(defaults, cs2_root=ROOT, lab_root=SIBLING_ROOT / "local_ai_lab_setup"),
        course_id,
    )
    positions = [module.position for module in plan.modules]
    objects = sum(len(module.objects) for module in plan.modules)
    groups = len(plan.assignment_groups)
    weight = sum(group.group_weight for group in plan.assignment_groups)
    checks = {
        "module positions": (positions, list(range(2, 18))),
        "module count": (len(plan.modules), EXPECTED_MODULE_COUNT),
        "object count": (objects, EXPECTED_OBJECT_COUNT),
        "assignment-group count": (groups, EXPECTED_ASSIGNMENT_GROUP_COUNT),
    }
    bad = [f"{name}: expected {expected}, got {actual}" for name, (actual, expected) in checks.items() if actual != expected]
    if abs(weight - 100.0) > 1e-9:
        bad.append(f"assignment-group weight: expected 100.0, got {weight}")
    if bad:
        raise RuntimeError("CS2 DesiredCourse drifted from Savnac acceptance: " + "; ".join(bad))
    return plan


def _result_dict(result) -> dict[str, Any]:
    if hasattr(result, "model_dump"):
        value = result.model_dump(mode="json")
    elif isinstance(result, dict):
        value = result
    else:
        fields = ("course_id", "succeeded", "created_count", "updated_count", "skipped_count",
                  "deleted_count", "aborted", "dry_run", "forced", "prune_scope", "detail", "log")
        value = {key: getattr(result, key) for key in fields if hasattr(result, key)}
    return json.loads(json.dumps(value, default=str))


def _plan_digest(plan) -> str:
    payload = plan.model_dump(mode="json") if hasattr(plan, "model_dump") else plan
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode()
    return hashlib.sha256(raw).hexdigest()


def _authorization_token(*, target, source_states, plan_digest, dry_run) -> str:
    payload = {
        "target": target,
        "sources": {name: {"head": state["head"], "branch": state["branch"]} for name, state in source_states.items()},
        "plan_digest": plan_digest,
        "dry_run": {
            "created_count": dry_run.get("created_count", 0),
            "updated_count": dry_run.get("updated_count", 0),
            "deleted_count": dry_run.get("deleted_count", 0),
            "log": dry_run.get("log", []),
        },
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode()
    return hashlib.sha256(raw).hexdigest()[:24]


def _receipt(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _preflight(receipt: Path):
    _bootstrap()
    states = _source_states()
    contract = _contract()
    discovered = _discover_target(_discovery_client(), contract)
    course_id = int(discovered["id"])
    client = _course_client(course_id)
    target = _verify_target(client, course_id, contract, discovered)
    plan = _build_plan(course_id)

    from imprint.reconcile import push_course
    dry = _result_dict(push_course(client, plan, dry_run=True, force=False, prune_scope="none", confirm_live_write=False))
    if not dry.get("succeeded", True):
        raise RuntimeError(f"production dry-run failed: {dry.get('detail', '')}")
    if int(dry.get("deleted_count", 0)):
        raise RuntimeError("production dry-run proposed deletions despite prune_scope=none")
    digest = _plan_digest(plan)
    token = _authorization_token(target=target, source_states=states, plan_digest=digest, dry_run=dry)
    payload = {
        "schema": 1,
        "mode": "preflight",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "status": "GREEN TO WRITE",
        "production_write_occurred": False,
        "week_1": {"owner": "semester_kickoff_week", "cs2_write_scope": "read-only / excluded"},
        "target": target,
        "contract": contract,
        "source_states": states,
        "desired": {
            "module_positions": [m.position for m in plan.modules],
            "module_count": len(plan.modules),
            "object_count": sum(len(m.objects) for m in plan.modules),
            "assignment_group_count": len(plan.assignment_groups),
            "assignment_group_weight": sum(g.group_weight for g in plan.assignment_groups),
            "plan_sha256": digest,
            "prune_scope": "none",
        },
        "dry_run": dry,
        "authorization_token": token,
    }
    _receipt(receipt, payload)
    return payload, client, plan, token


def _print_preflight(payload: dict[str, Any]) -> None:
    t, d = payload["target"], payload["dry_run"]
    print(f"TARGET course_id={t['id']} name={t['name']!r} course_code={t['course_code']!r} term={t.get('term')!r}")
    print(f"DRY RUN create={d.get('created_count', 0)} update={d.get('updated_count', 0)} skip={d.get('skipped_count', 0)} delete={d.get('deleted_count', 0)}")
    print(f"AUTHORIZATION_TOKEN={payload['authorization_token']}")
    print("GREEN TO WRITE")


def _write(authorize: str, preflight_receipt: Path, closeout_receipt: Path) -> int:
    preflight, client, plan, token = _preflight(preflight_receipt)
    if authorize != token:
        raise RuntimeError("authorization token is stale or incorrect; no production write occurred")

    from imprint.reconcile import push_course
    write = _result_dict(push_course(client, plan, dry_run=False, force=False, prune_scope="none", confirm_live_write=True))
    if not write.get("succeeded", True):
        _receipt(closeout_receipt, {"schema": 1, "mode": "closeout", "status": "WRITE FAILED",
                                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                                    "production_write_occurred": True, "preflight": preflight, "write": write})
        raise RuntimeError(f"production reconcile failed: {write.get('detail', '')}")

    closeout = _result_dict(push_course(client, plan, dry_run=True, force=False, prune_scope="none", confirm_live_write=False))
    converged = closeout.get("succeeded", True) and all(int(closeout.get(key, 0)) == 0 for key in ("created_count", "updated_count", "deleted_count"))
    _receipt(closeout_receipt, {
        "schema": 1,
        "mode": "closeout",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "status": "DONE" if converged else "WRITE LANDED BUT CLOSEOUT IS NOT A FIXED POINT",
        "production_write_occurred": True,
        "preflight": preflight,
        "write": write,
        "closeout_dry_run": closeout,
    })
    if not converged:
        raise RuntimeError("write landed, but immediate closeout dry-run is not a no-op")
    print(f"WRITE create={write.get('created_count', 0)} update={write.get('updated_count', 0)} skip={write.get('skipped_count', 0)} delete={write.get('deleted_count', 0)}")
    print(f"CLOSEOUT create={closeout.get('created_count', 0)} update={closeout.get('updated_count', 0)} skip={closeout.get('skipped_count', 0)} delete={closeout.get('deleted_count', 0)}")
    print("DONE")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    pre = sub.add_parser("preflight", help="read-only production discovery + dry-run")
    pre.add_argument("--receipt", type=Path, default=PREFLIGHT_RECEIPT)
    write = sub.add_parser("write", help="authorized reconcile + no-op closeout")
    write.add_argument("--authorize", required=True)
    write.add_argument("--preflight-receipt", type=Path, default=PREFLIGHT_RECEIPT)
    write.add_argument("--receipt", type=Path, default=CLOSEOUT_RECEIPT)
    args = parser.parse_args(argv)
    try:
        if args.command == "preflight":
            payload, _, _, _ = _preflight(args.receipt)
            _print_preflight(payload)
            print(f"RECEIPT={args.receipt}")
            return 0
        return _write(args.authorize, args.preflight_receipt, args.receipt)
    except Exception as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
