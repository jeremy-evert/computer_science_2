"""Command-line cockpit for the CS2 Week 16 Farkle experiment bench."""

import argparse
from pathlib import Path
import sys

from .experiment import (
    ExperimentConfig,
    default_suite,
    run_experiment,
    save_csv,
    save_json,
    strategy_menu,
)


def _print_result(result):
    print(
        f"{result.strategy_a} vs {result.strategy_b}: "
        f"win {result.win_rate_a:.1%}/{result.win_rate_b:.1%}, "
        f"prep {result.preparation_seconds_a:.4f}s/{result.preparation_seconds_b:.4f}s, "
        f"eval {result.evaluation_seconds:.4f}s, "
        f"{result.games_per_second:.1f} games/s"
    )


def cmd_menu(_args):
    for name, description in strategy_menu().items():
        print(f"{name:<14} {description}")


def cmd_compare(args):
    result = run_experiment(
        ExperimentConfig(
            strategy_a=args.strategy_a,
            strategy_b=args.strategy_b,
            games=args.games,
            seed=args.seed,
            execution_context=args.context,
        )
    )
    _print_result(result)
    if args.out:
        path = save_json(result, args.out)
        print(f"saved {path}")


def cmd_suite(args):
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for index, config in enumerate(default_suite(args.games, args.seed), start=1):
        config = ExperimentConfig(
            strategy_a=config.strategy_a,
            strategy_b=config.strategy_b,
            games=config.games,
            seed=config.seed,
            execution_context=args.context,
        )
        result = run_experiment(config)
        results.append(result)
        _print_result(result)
        safe_name = result.strategy_a.replace(":", "_")
        save_json(result, out_dir / f"{index:02d}_{safe_name}.json")
    csv_path = save_csv(results, out_dir / "suite_results.csv")
    print(f"saved {csv_path}")


def build_parser():
    parser = argparse.ArgumentParser(
        description="CS2 Week 16 Farkle + ML experiment bench"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    menu = subparsers.add_parser("menu", help="Show supported strategy specs.")
    menu.set_defaults(func=cmd_menu)

    compare = subparsers.add_parser("compare", help="Run one controlled comparison.")
    compare.add_argument("--strategy-a", required=True)
    compare.add_argument("--strategy-b", default="bank_at_425")
    compare.add_argument("--games", type=int, default=1000)
    compare.add_argument("--seed", type=int, default=1)
    compare.add_argument("--context", default="cpu-local")
    compare.add_argument("--out")
    compare.set_defaults(func=cmd_compare)

    suite = subparsers.add_parser("suite", help="Run the fixed classroom suite.")
    suite.add_argument("--games", type=int, default=500)
    suite.add_argument("--seed", type=int, default=1)
    suite.add_argument("--context", default="cpu-local")
    suite.add_argument("--out-dir", default="artifacts/week16_farkle")
    suite.set_defaults(func=cmd_suite)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(sys.argv[1:])
