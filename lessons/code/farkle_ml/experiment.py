"""Shared reproducible experiment runner and machine-readable receipts."""

from dataclasses import asdict, dataclass
import csv
import json
from pathlib import Path
import platform
import time

from . import BENCHMARK_VERSION, SCHEMA_VERSION
from .contract import FunctionStrategyAdapter
from .learner import ExperienceTable, train
from .simulate import run_many_games
from .strategies import LearnedTableStrategy, OneStepRolloutStrategy, resolve_strategy


@dataclass(frozen=True)
class ExperimentConfig:
    strategy_a: str
    strategy_b: str = "bank_at_425"
    games: int = 500
    seed: int = 1
    target_score: int = 4000
    execution_context: str = "cpu-local"


@dataclass
class BuiltStrategy:
    strategy: object
    specification: str
    preparation_seconds: float
    training_turns: int
    model_size_bytes: int
    complexity_note: str


@dataclass
class ExperimentResult:
    schema_version: str
    benchmark_version: str
    python_version: str
    execution_context: str
    seed: int
    games: int
    target_score: int
    strategy_a: str
    strategy_b: str
    preparation_seconds_a: float
    preparation_seconds_b: float
    training_turns_a: int
    training_turns_b: int
    model_size_bytes_a: int
    model_size_bytes_b: int
    complexity_note_a: str
    complexity_note_b: str
    evaluation_seconds: float
    games_per_second: float
    starts_a: int
    starts_b: int
    wins_a: int
    wins_b: int
    ties: int
    turns_a: int
    turns_b: int
    farkles_a: int
    farkles_b: int
    win_rate_a: float
    win_rate_b: float
    tie_rate: float
    win_rate_difference_pp: float
    avg_score_a: float
    avg_score_b: float
    farkle_rate_a: float
    farkle_rate_b: float
    avg_turns_per_game: float


def strategy_menu():
    return {
        "bank_at_N": "Human threshold, e.g. bank_at_425; negligible preparation.",
        "learner:N": "Transparent experience table trained for N solo turns.",
        "rollout:N": "One-step simulation using N sampled next rolls per decision.",
    }


def build_strategy(specification, seed):
    """Build one canonical strategy specification and measure preparation."""
    started = time.perf_counter()

    if specification.startswith("learner:"):
        turns = int(specification.split(":", 1)[1])
        if turns <= 0:
            raise ValueError("learner training turns must be positive")
        table = ExperienceTable(epsilon=0.2, seed=seed)
        train(table, num_turns=turns, seed=seed)
        strategy = LearnedTableStrategy(table, turns)
        model_size = len(repr(table.values).encode("utf-8"))
        training_turns = turns

    elif specification.startswith("rollout:"):
        rollouts = int(specification.split(":", 1)[1])
        strategy = OneStepRolloutStrategy(rollouts=rollouts, seed=seed)
        model_size = 0
        training_turns = 0

    else:
        function = resolve_strategy(specification)
        strategy = FunctionStrategyAdapter(function)
        model_size = 0
        training_turns = 0

    elapsed = time.perf_counter() - started
    return BuiltStrategy(
        strategy=strategy,
        specification=specification,
        preparation_seconds=elapsed,
        training_turns=training_turns,
        model_size_bytes=model_size,
        complexity_note=getattr(strategy, "complexity_note", "unspecified"),
    )


def run_experiment(config):
    """Build two strategies, run a fair comparison, and return one receipt."""
    if config.games <= 0:
        raise ValueError("games must be positive")
    if config.target_score <= 0:
        raise ValueError("target_score must be positive")

    built_a = build_strategy(config.strategy_a, config.seed + 101)
    built_b = build_strategy(config.strategy_b, config.seed + 202)

    started = time.perf_counter()
    summary = run_many_games(
        built_a.strategy,
        built_b.strategy,
        config.games,
        config.seed,
        target_score=config.target_score,
    )
    evaluation_seconds = time.perf_counter() - started
    games_per_second = (
        config.games / evaluation_seconds if evaluation_seconds > 0 else float("inf")
    )

    return ExperimentResult(
        schema_version=SCHEMA_VERSION,
        benchmark_version=BENCHMARK_VERSION,
        python_version=platform.python_version(),
        execution_context=config.execution_context,
        seed=config.seed,
        games=config.games,
        target_score=config.target_score,
        strategy_a=config.strategy_a,
        strategy_b=config.strategy_b,
        preparation_seconds_a=built_a.preparation_seconds,
        preparation_seconds_b=built_b.preparation_seconds,
        training_turns_a=built_a.training_turns,
        training_turns_b=built_b.training_turns,
        model_size_bytes_a=built_a.model_size_bytes,
        model_size_bytes_b=built_b.model_size_bytes,
        complexity_note_a=built_a.complexity_note,
        complexity_note_b=built_b.complexity_note,
        evaluation_seconds=evaluation_seconds,
        games_per_second=games_per_second,
        starts_a=summary["starts_a"],
        starts_b=summary["starts_b"],
        wins_a=summary["wins_a"],
        wins_b=summary["wins_b"],
        ties=summary["ties"],
        turns_a=summary["turns_a"],
        turns_b=summary["turns_b"],
        farkles_a=summary["farkles_a"],
        farkles_b=summary["farkles_b"],
        win_rate_a=summary["win_rate_a"],
        win_rate_b=summary["win_rate_b"],
        tie_rate=summary["tie_rate"],
        win_rate_difference_pp=(summary["win_rate_a"] - summary["win_rate_b"]) * 100,
        avg_score_a=summary["avg_score_a"],
        avg_score_b=summary["avg_score_b"],
        farkle_rate_a=summary["farkle_rate_a"],
        farkle_rate_b=summary["farkle_rate_b"],
        avg_turns_per_game=summary["avg_turns_per_game"],
    )


def result_row(result):
    row = asdict(result)
    row["seconds_per_game"] = (
        result.evaluation_seconds / result.games if result.games else 0.0
    )
    return row


def save_json(result, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(result_row(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def save_csv(results, path):
    rows = [result_row(result) for result in results]
    if not rows:
        raise ValueError("cannot save an empty result set")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def default_suite(games=100, seed=6262):
    """A bounded CPU-first validation/demo suite, not a grading leaderboard."""
    return [
        ExperimentConfig("bank_at_300", games=games, seed=seed),
        ExperimentConfig("learner:500", games=games, seed=seed + 10),
        ExperimentConfig("learner:2000", games=games, seed=seed + 20),
        ExperimentConfig("rollout:10", games=games, seed=seed + 30),
        ExperimentConfig("rollout:25", games=games, seed=seed + 40),
    ]
