"""CS2 strategy families that all satisfy one explicit decision contract."""

import random

from .contract import Strategy
from .vendor_cs1 import engine


class LearnedTableStrategy(Strategy):
    """Adapt a trained CS1 experience table as a CS2 strategy object."""

    def __init__(self, table, training_turns):
        self.table = table
        self.training_turns = training_turns
        self.name = f"learner_{training_turns}"
        self.complexity_note = (
            "transparent learned table; preparation required; "
            "turn-score bucket + dice-remaining state"
        )

    def decide(self, state):
        return self.table.choose_action(state, explore=False)


class OneStepRolloutStrategy(Strategy):
    """Spend runtime work estimating whether one more roll is worth it.

    This is intentionally bounded and transparent, not a full game-tree search.
    For each decision it simulates ``rollouts`` possible next rolls. A Farkle
    earns zero for the turn; a scoring roll is valued as if the player banks
    immediately after that roll. The strategy rolls only when the sampled
    average is better than banking now.
    """

    def __init__(self, rollouts=50, seed=1):
        if rollouts <= 0:
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
        dice_remaining = state["dice_remaining"]
        total_if_roll = 0.0

        for _ in range(self.rollouts):
            dice = engine.roll_dice(dice_remaining, self.rng)
            points, _used = engine.score_roll(dice)
            if engine.is_farkle(points):
                outcome = 0
            else:
                outcome = bank_value + points
            total_if_roll += outcome

        estimated_roll_value = total_if_roll / self.rollouts
        return "roll" if estimated_roll_value > bank_value else "bank"
