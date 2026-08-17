#!/usr/bin/env python3
"""One-command validation for the CS2 Week 16 Farkle + ML surface.

This script installs nothing and changes no machine configuration. It writes
only bounded artifacts/receipts under the repository. It validates both the
CS2 experiment lens and its canonical shared-core provenance.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "lessons" / "code"
if str(CODE) not in sys.path:
    sys.path.insert(0, str(CODE))

from farkle_week16 import (  # noqa: E402
    SHARED_REPOSITORY,
    SHARED_REPO_HEAD,
    SHARED_SOURCE_COMMIT,
)
from farkle_week16.experiment import (  # noqa: E402
    default_suite,
    run_experiment,
    save_csv,
    save_json,
)

EXPECTED_BASELINE_WIN_RATES = {
    "bank_at_300": 0.640,
    "learner:2000": 0.630,
    "learner:20000": 0.670,
    "rollout:25": 0.690,
    "rollout:100": 0.680,
}


def _validate_shared_snapshot():
    manifest_path = CODE / "farkle_ml" / "_SHARED_PROVENANCE.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = []

    if manifest.get("shared_repository") != SHARED_REPOSITORY:
        errors.append("shared repository constant does not match manifest")
    if manifest.get("shared_commit") != SHARED_SOURCE_COMMIT:
        errors.append("shared source commit constant does not match manifest")
    if manifest.get("shared_repo_head") != SHARED_REPO_HEAD:
        errors.append("shared repo head constant does not match manifest")

    for relative_path, expected_hash in manifest.get("files", {}).items():
        path = CODE / "farkle_ml" / relative_path
        if not path.is_file():
            errors.append(f"missing generated shared file: {relative_path}")
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            errors.append(f"shared file hash mismatch: {relative_path}")

    return errors


def _validate_active_path_has_no_vendor_imports():
    paths = [
        CODE / "farkle_week16" / "__init__.py",
        CODE / "farkle_week16" / "contract.py",
        CODE / "farkle_week16" / "strategies.py",
        CODE / "farkle_week16" / "experiment.py",
        CODE / "farkle_week16" / "cli.py",
        ROOT / "tests" / "test_week16_farkle.py",
    ]
    offenders = []
    for path in paths:
        if "vendor_cs1" in path.read_text(encoding="utf-8"):
            offenders.append(str(path.relative_to(ROOT)))
    return offenders


def _write_failure(receipt, stamp, tests, test_log, checks):
    lines = [
        "# CS2 Week 16 Farkle validation receipt",
        "",
        f"- UTC: {stamp}",
        "- status: **RED**",
        f"- Python: {platform.python_version()}",
        f"- Platform: {platform.platform()}",
        f"- shared repository: `{SHARED_REPOSITORY}`",
        f"- shared source commit: `{SHARED_SOURCE_COMMIT}`",
        f"- shared repo head at sync: `{SHARED_REPO_HEAD}`",
        f"- tests: {'GREEN' if tests.returncode == 0 else 'FAIL'} (exit {tests.returncode})",
        f"- test log: `{test_log.relative_to(ROOT)}`",
        "",
        "## Contract checks",
        "",
    ]
    lines.extend(f"- {item}" for item in checks)
    lines.append("")
    receipt.write_text("\n".join(lines), encoding="utf-8")


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ROOT / "artifacts" / "week16_farkle" / stamp
    receipt_dir = ROOT / "sidecar" / "runs"
    out_dir.mkdir(parents=True, exist_ok=True)
    receipt_dir.mkdir(parents=True, exist_ok=True)

    snapshot_errors = _validate_shared_snapshot()
    vendor_imports = _validate_active_path_has_no_vendor_imports()

    test_command = [
        sys.executable, "-m", "unittest", "discover",
        "-s", "tests", "-p", "test_week16_farkle.py", "-v",
    ]
    tests = subprocess.run(
        test_command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    test_log = out_dir / "unittest.txt"
    test_log.write_text(tests.stdout + tests.stderr, encoding="utf-8")

    required_checks = []
    if snapshot_errors:
        required_checks.extend(f"RED — {error}" for error in snapshot_errors)
    else:
        required_checks.append(
            "GREEN — generated shared snapshot hashes and provenance match manifest"
        )

    if vendor_imports:
        required_checks.append(
            "RED — active source still imports vendor_cs1: " + ", ".join(vendor_imports)
        )
    else:
        required_checks.append(
            "GREEN — active CS2 source/tests contain no vendor_cs1 imports"
        )

    required_checks.append(
        f"{'GREEN' if tests.returncode == 0 else 'RED'} — regression tests exit={tests.returncode}"
    )

    receipt = receipt_dir / f"014_validation_{stamp}.md"
    if snapshot_errors or vendor_imports or tests.returncode != 0:
        _write_failure(receipt, stamp, tests, test_log, required_checks)
        print(receipt)
        return 1

    results = []
    parity_errors = []
    for index, config in enumerate(default_suite(games=100, seed=6262), start=1):
        result = run_experiment(config)
        results.append(result)
        safe_name = result.strategy_a.replace(":", "_")
        save_json(result, out_dir / f"{index:02d}_{safe_name}.json")
        expected = EXPECTED_BASELINE_WIN_RATES[result.strategy_a]
        if result.win_rate_a != expected:
            parity_errors.append(
                f"{result.strategy_a}: expected baseline win rate {expected:.3f}, "
                f"observed {result.win_rate_a:.3f}"
            )

    csv_path = save_csv(results, out_dir / "suite_results.csv")

    if parity_errors:
        required_checks.extend(f"RED — behavioral parity: {error}" for error in parity_errors)
        _write_failure(receipt, stamp, tests, test_log, required_checks)
        print(receipt)
        return 1

    required_checks.append(
        "GREEN — fixed-suite win rates exactly match the pre-migration Brandy baseline"
    )

    plot_status = "YELLOW — matplotlib unavailable or plot failed"
    plot_path = out_dir / "tradeoff.png"
    try:
        from farkle_week16.plot_results import plot_tradeoff
        plot_tradeoff(csv_path, plot_path, "preparation_seconds_a")
        plot_status = f"GREEN — `{plot_path.relative_to(ROOT)}`"
    except Exception as exc:  # plotting is enrichment; correctness already passed
        (out_dir / "plot_yellow.txt").write_text(
            f"{type(exc).__name__}: {exc}\n", encoding="utf-8"
        )

    lines = [
        "# CS2 Week 16 Farkle validation receipt",
        "",
        f"- UTC: {stamp}",
        "- status: **GREEN**",
        f"- Python: {platform.python_version()}",
        f"- Platform: {platform.platform()}",
        f"- shared repository: `{SHARED_REPOSITORY}`",
        f"- shared source commit: `{SHARED_SOURCE_COMMIT}`",
        f"- shared repo head at sync: `{SHARED_REPO_HEAD}`",
        f"- tests: **GREEN** (exit {tests.returncode})",
        f"- test log: `{test_log.relative_to(ROOT)}`",
        f"- result CSV: `{csv_path.relative_to(ROOT)}`",
        f"- plot: {plot_status}",
        "",
        "## Contract checks",
        "",
    ]
    lines.extend(f"- {item}" for item in required_checks)
    lines.extend([
        "",
        "## Fixed validation suite",
        "",
        "| strategy | win rate vs bank_at_425 | prep s | eval s | games/s |",
        "|---|---:|---:|---:|---:|",
    ])
    for result in results:
        lines.append(
            f"| {result.strategy_a} | {result.win_rate_a:.3f} | "
            f"{result.preparation_seconds_a:.6f} | "
            f"{result.evaluation_seconds:.6f} | {result.games_per_second:.2f} |"
        )
    lines.extend([
        "",
        "## Command",
        "",
        "```text",
        "python scripts/validate_week16_farkle.py",
        "```",
        "",
        "The fixed-suite parity check compares deterministic outcomes to the retained",
        "pre-migration Brandy receipt. Timing is observed, not required to match.",
        "",
        "This receipt records observed evidence only; it does not claim one strategy is universally best.",
        "",
    ])
    receipt.write_text("\n".join(lines), encoding="utf-8")
    print(receipt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
