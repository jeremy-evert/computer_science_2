"""Canonical transparent Farkle strategy families.

The baseline menu stays intentionally small. Courses may wrap or extend these
strategies, but the common game does not require course-specific forks.
"""

import random

from . import engine
from .contract import Strategy


def bank_at(threshold):
    """Return a human-readable threshold strategy."""
    if not isinstance(threshold, int) or threshold <= 0:
        raise ValueError("bank threshold must be a positive integer")

    def threshold_strategy(state):
        return "bank" if state["turn_score"] >= threshold else "roll"

    threshold_strategy.__name__ = f"bank_at_{threshold}"
    threshold_strategy.description = (
        f"Bank once turn score reaches {threshold}, else roll."
    )
    return threshold_strategy


bank_at_300 = bank_at(300)
bank_at_500 = bank_at(500)
bank_at_800 = bank_at(800)


def cautious_near_target(state):
    """Bank earlier once the player is within 500 points of the target."""
    threshold = 500
    distance_to_win = state["target_score"] - state["total_score"]
    local_threshold = threshold // 2 if distance_to_win <= 500 else threshold
    return "bank" if state["turn_score"] >= local_threshold else "roll"


cautious_near_target.description = (
    "Bank at 500 normally; bank at 250 once within 500 points of the target."
)


def aggressive_when_behind(state):
    """Require a larger turn before banking when far behind the opponent."""
    threshold = 500
    opponent_score = state["opponent_score"] or 0
    behind_by = opponent_score - state["total_score"]
    local_threshold = 1500 if behind_by > 1000 else threshold
    return "bank" if state["turn_score"] >= local_threshold else "roll"


aggressive_when_behind.description = (
    "Bank at 500 normally; require 1500 if more than 1000 points behind."
)


def always_bank_first_score(state):
    return "bank"


always_bank_first_score.description = "Bank the instant any points are available."


BUILT_IN_STRATEGIES = {
    "bank_at_300": bank_at_300,
    "bank_at_500": bank_at_500,
    "bank_at_800": bank_at_800,
    "cautious_near_target": cautious_near_target,
    "aggressive_when_behind": aggressive_when_behind,
    "always_bank_first_score": always_bank_first_score,
}


def resolve_strategy(name):
    """Resolve a built-in name or dynamic ``bank_at_N`` strategy."""
    if name in BUILT_IN_STRATEGIES:
        return BUILT_IN_STRATEGIES[name]

    prefix = "bank_at_"
    if name.startswith(prefix):
        raw_threshold = name[len(prefix):]
        try:
            threshold = int(raw_threshold)
        except ValueError as exc:
            raise ValueError(
                f"unknown strategy {name!r}; bank_at_N requires integer N"
            ) from exc
        return bank_at(threshold)

    known = ", ".join(sorted(BUILT_IN_STRATEGIES))
    raise ValueError(
        f"unknown strategy {name!r}. Use [{known}] or bank_at_N, e.g. bank_at_425"
    )


class LearnedTableStrategy(Strategy):
    """Adapt a trained transparent experience table as a strategy object."""

    def __init__(self, table, training_turns):
        self.table = table
        self.training_turns = int(training_turns)
        self.name = f"learner_{self.training_turns}"
        self.complexity_note = (
            "transparent learned table; preparation required; "
            "turn-score bucket + dice-remaining state"
        )

    def decide(self, state):
        return self.table.choose_action(state, explore=False)


class OneStepRolloutStrategy(Strategy):
    """Spend bounded runtime work estimating the value of one more roll.

    This is intentionally not a full game-tree search. Each decision samples
    possible next rolls; a scoring roll is valued as if it were banked
    immediately and a Farkle earns zero for the turn.
    """

    def __init__(self, rollouts=50, seed=1):
        if int(rollouts) <= 0:
            raise ValueError("rollouts must be positive")
        self.rollouts = int(rollouts)
        self.rng = random.Random(seed)
        self.name = f"rollout_{self.rollouts}"
        self.complexity_note = (
            f"one-step simulation; no training; {self.rollouts} sampled "
            "next rolls per decision"
        )

    def decide(self, state):
        bank_value = state["turn_score"]
        total_if_roll = 0.0

        for _ in range(self.rollouts):
            dice = engine.roll_dice(state["dice_remaining"], self.rng)
            points, _used = engine.score_roll(dice)
            outcome = 0 if engine.is_farkle(points) else bank_value + points
            total_if_roll += outcome

        estimated_roll_value = total_if_roll / self.rollouts
        return "roll" if estimated_roll_value > bank_value else "bank"
