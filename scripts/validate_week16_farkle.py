#!/usr/bin/env python3
"""One-command validation for the CS2 Week 16 Farkle + ML surface.

This script installs nothing and changes no machine configuration. It writes
only bounded artifacts/receipts under the repository.
"""

from datetime import datetime, timezone
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "lessons" / "code"
if str(CODE) not in sys.path:
    sys.path.insert(0, str(CODE))

from farkle_week16 import UPSTREAM_CS1_COMMIT  # noqa: E402
from farkle_week16.experiment import default_suite, run_experiment, save_csv, save_json  # noqa: E402


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ROOT / "artifacts" / "week16_farkle" / stamp
    receipt_dir = ROOT / "sidecar" / "runs"
    out_dir.mkdir(parents=True, exist_ok=True)
    receipt_dir.mkdir(parents=True, exist_ok=True)

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

    if tests.returncode != 0:
        receipt = receipt_dir / f"014_validation_{stamp}.md"
        receipt.write_text(
            "# CS2 Week 16 Farkle validation receipt\n\n"
            f"- UTC: {stamp}\n"
            f"- Python: {platform.python_version()}\n"
            f"- CS1 provenance: `{UPSTREAM_CS1_COMMIT}`\n"
            f"- tests: **FAIL** (exit {tests.returncode})\n"
            f"- log: `{test_log.relative_to(ROOT)}`\n",
            encoding="utf-8",
        )
        print(receipt)
        return tests.returncode

    results = []
    for index, config in enumerate(default_suite(games=100, seed=6262), start=1):
        result = run_experiment(config)
        results.append(result)
        safe_name = result.strategy_a.replace(":", "_")
        save_json(result, out_dir / f"{index:02d}_{safe_name}.json")

    csv_path = save_csv(results, out_dir / "suite_results.csv")

    plot_status = "YELLOW — matplotlib unavailable or plot failed"
    plot_path = out_dir / "tradeoff.png"
    try:
        from farkle_week16.plot_results import plot_tradeoff
        plot_tradeoff(csv_path, plot_path, "preparation_seconds_a")
        plot_status = f"GREEN — `{plot_path.relative_to(ROOT)}`"
    except Exception as exc:  # plotting is enrichment; correctness tests already passed
        (out_dir / "plot_yellow.txt").write_text(
            f"{type(exc).__name__}: {exc}\n", encoding="utf-8"
        )

    receipt = receipt_dir / f"014_validation_{stamp}.md"
    lines = [
        "# CS2 Week 16 Farkle validation receipt",
        "",
        f"- UTC: {stamp}",
        f"- Python: {platform.python_version()}",
        f"- Platform: {platform.platform()}",
        f"- CS1 provenance: `{UPSTREAM_CS1_COMMIT}`",
        f"- tests: **GREEN** (exit {tests.returncode})",
        f"- test log: `{test_log.relative_to(ROOT)}`",
        f"- result CSV: `{csv_path.relative_to(ROOT)}`",
        f"- plot: {plot_status}",
        "",
        "## Fixed validation suite",
        "",
        "| strategy | win rate vs bank_at_425 | prep s | eval s | games/s |",
        "|---|---:|---:|---:|---:|",
    ]
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
        "This receipt records observed evidence only; it does not claim one strategy is universally best.",
        "",
    ])
    receipt.write_text("\n".join(lines), encoding="utf-8")
    print(receipt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
