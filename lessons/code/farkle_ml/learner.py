"""Transparent experience-table learner used across the shared Farkle week.

This is intentionally simple: a dictionary of running averages, not a claim to
full modern reinforcement learning. Its value is that students can inspect the
state, action, evidence count, and learned preference directly.
"""

import json
import random


class ExperienceTable:
    """A small table-based learner with explicit exploration."""

    def __init__(self, epsilon=0.2, bucket_size=50, seed=None):
        self.values = {}
        self.epsilon = epsilon
        self.bucket_size = bucket_size
        self.rng = random.Random(seed)

    def _state_key(self, state):
        bucketed_turn_score = min(
            state["turn_score"] // self.bucket_size, 20
        ) * self.bucket_size
        return (bucketed_turn_score, state["dice_remaining"])

    def _average(self, state_key, action):
        return self.values.get((state_key, action), [0.0, 0])[0]

    def choose_action(self, state, explore=True):
        if explore and self.rng.random() < self.epsilon:
            return self.rng.choice(["roll", "bank"])

        state_key = self._state_key(state)
        roll_average = self._average(state_key, "roll")
        bank_average = self._average(state_key, "bank")
        return "bank" if bank_average >= roll_average else "roll"

    def update(self, state, action, outcome):
        key = (self._state_key(state), action)
        average, count = self.values.get(key, [0.0, 0])
        count += 1
        average += (outcome - average) / count
        self.values[key] = [average, count]

    def as_strategy(self):
        def learned_strategy(state):
            return self.choose_action(state, explore=False)

        learned_strategy.__name__ = "learned_experience_table"
        learned_strategy.description = (
            "Whatever the transparent experience table currently believes is best."
        )
        return learned_strategy

    def situations_seen(self):
        return len(self.values)

    def table_rows(self):
        state_keys = sorted({key[0] for key in self.values})
        rows = []
        for state_key in state_keys:
            turn_score_bucket, dice_remaining = state_key
            roll_avg, roll_n = self.values.get((state_key, "roll"), [0.0, 0])
            bank_avg, bank_n = self.values.get((state_key, "bank"), [0.0, 0])
            preferred = "bank" if bank_avg >= roll_avg else "roll"
            rows.append({
                "turn_score_bucket": turn_score_bucket,
                "dice_remaining": dice_remaining,
                "roll_average": round(roll_avg, 1),
                "roll_seen": roll_n,
                "bank_average": round(bank_avg, 1),
                "bank_seen": bank_n,
                "current_preference": preferred,
            })
        return rows

    def save(self, path):
        serializable = {}
        for key, value in self.values.items():
            state_key, action = key
            turn_score_bucket, dice_remaining = state_key
            serializable[f"{turn_score_bucket}|{dice_remaining}|{action}"] = value

        with open(path, "w", encoding="utf-8") as handle:
            json.dump({
                "epsilon": self.epsilon,
                "bucket_size": self.bucket_size,
                "values": serializable,
            }, handle, indent=2, sort_keys=True)


def load_table(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)

    table = ExperienceTable(
        epsilon=data["epsilon"], bucket_size=data["bucket_size"]
    )
    for key_str, value in data["values"].items():
        turn_score_bucket, dice_remaining, action = key_str.split("|")
        table.values[((int(turn_score_bucket), int(dice_remaining)), action)] = value
    return table


def train_one_turn(rng, table):
    from . import engine

    dice_remaining = engine.NUM_DICE
    turn_score = 0
    visited = []

    while True:
        dice = engine.roll_dice(dice_remaining, rng)
        points, used = engine.score_roll(dice)

        if engine.is_farkle(points):
            outcome = -turn_score
            for state, action in visited:
                table.update(state, action, outcome)
            return 0

        turn_score += points
        dice_remaining -= used
        if dice_remaining == 0:
            dice_remaining = engine.NUM_DICE

        state = engine.build_state(
            turn_score,
            dice_remaining,
            total_score=0,
            target_score=0,
            opponent_score=None,
        )
        action = table.choose_action(state, explore=True)
        visited.append((state, action))

        if action == "bank":
            outcome = turn_score
            for visited_state, visited_action in visited:
                table.update(visited_state, visited_action, outcome)
            return turn_score


def train(table, num_turns, seed):
    if num_turns < 0:
        raise ValueError("num_turns must be non-negative")
    rng = random.Random(seed)
    for _ in range(num_turns):
        train_one_turn(rng, table)
