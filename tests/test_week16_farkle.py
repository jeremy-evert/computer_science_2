"""Standard-library tests for the CS2 Week 16 Farkle experiment bench."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "lessons" / "code"))

from farkle_week16 import UPSTREAM_CS1_COMMIT  # noqa: E402
from farkle_week16.contract import FunctionStrategyAdapter, Strategy  # noqa: E402
from farkle_week16.experiment import (  # noqa: E402
    ExperimentConfig,
    run_experiment,
    save_csv,
    save_json,
)
from farkle_week16.strategies import OneStepRolloutStrategy  # noqa: E402
from farkle_week16.vendor_cs1 import engine, simulate, strategies  # noqa: E402


class BadStrategy(Strategy):
    name = "bad"

    def decide(self, state):
        return "cheat"


class Week16FarkleTests(unittest.TestCase):
    def test_upstream_provenance_is_pinned(self):
        self.assertEqual(
            UPSTREAM_CS1_COMMIT,
            "b546ca2f846ea0c788ad17e5667b8b471efb33fa",
        )

    def test_vendored_public_rule_contract(self):
        self.assertEqual(engine.NUM_DICE, 6)
        self.assertEqual(engine.DEFAULT_TARGET_SCORE, 4000)
        self.assertEqual(engine.score_roll([1, 5, 2, 3, 4, 6]), (150, 2))
        self.assertEqual(
            set(engine.build_state(100, 4, 500, 4000, 200)),
            {
                "turn_score", "dice_remaining", "total_score",
                "target_score", "opponent_score",
            },
        )

    def test_dynamic_human_threshold_survives_boundary(self):
        function = strategies.resolve_strategy("bank_at_425")
        wrapped = FunctionStrategyAdapter(function)
        low = engine.build_state(400, 3, 0, 4000, None)
        high = engine.build_state(450, 3, 0, 4000, None)
        self.assertEqual(wrapped(low), "roll")
        self.assertEqual(wrapped(high), "bank")

    def test_strategy_contract_rejects_invalid_action(self):
        state = engine.build_state(300, 3, 0, 4000, None)
        with self.assertRaises(ValueError):
            BadStrategy()(state)

    def test_balanced_comparison_keeps_starter_and_turn_receipts(self):
        summary = simulate.run_many_games(
            strategies.bank_at_300, strategies.bank_at_800, 20, 5
        )
        self.assertEqual(summary["starts_a"], 10)
        self.assertEqual(summary["starts_b"], 10)
        self.assertGreater(summary["turns_a"], 0)
        self.assertGreater(summary["turns_b"], 0)
        self.assertGreaterEqual(summary["farkle_rate_a"], 0.0)
        self.assertLessEqual(summary["farkle_rate_a"], 1.0)

    def test_rollout_strategy_is_reproducible_and_contract_valid(self):
        state = engine.build_state(350, 3, 0, 4000, None)
        one = OneStepRolloutStrategy(rollouts=25, seed=9)
        two = OneStepRolloutStrategy(rollouts=25, seed=9)
        self.assertEqual(one(state), two(state))
        self.assertIn(one(state), ("roll", "bank"))

    def test_experiment_stochastic_metrics_reproduce(self):
        config = ExperimentConfig(
            strategy_a="learner:100",
            strategy_b="bank_at_425",
            games=30,
            seed=17,
        )
        first = run_experiment(config)
        second = run_experiment(config)
        self.assertEqual(first.win_rate_a, second.win_rate_a)
        self.assertEqual(first.win_rate_b, second.win_rate_b)
        self.assertEqual(first.farkle_rate_a, second.farkle_rate_a)
        self.assertEqual(first.starts_a, first.starts_b)
        self.assertEqual(first.training_turns_a, 100)

    def test_result_persistence_is_machine_readable(self):
        result = run_experiment(
            ExperimentConfig("bank_at_300", games=20, seed=3)
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            json_path = save_json(result, tmp_path / "result.json")
            csv_path = save_csv([result], tmp_path / "results.csv")
            data = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(data["strategy_a"], "bank_at_300")
            self.assertIn("seconds_per_game", data)
            self.assertIn("strategy_a", csv_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
