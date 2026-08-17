"""Canonical classroom Farkle rules and one-turn engine.

This begins from the hardened Fall 2026 CS1 implementation. The only deliberate
shared-layer tightening is that an invalid strategy action now raises clearly
instead of being treated as an implicit roll.
"""

DEFAULT_TARGET_SCORE = 4000
NUM_DICE = 6
VALID_ACTIONS = {"roll", "bank"}


def roll_dice(count, rng):
    """Roll ``count`` six-sided dice using the supplied RNG."""
    return [rng.randint(1, 6) for _ in range(count)]


def score_roll(dice):
    """Return ``(points, dice_used)`` under the shared classroom variant."""
    counts = {value: dice.count(value) for value in range(1, 7)}
    points = 0
    dice_used = 0

    for value in range(1, 7):
        count = counts[value]
        if count >= 3:
            base = 1000 if value == 1 else value * 100
            points += base * (2 ** (count - 3))
            dice_used += count
            counts[value] = 0

    points += counts[1] * 100
    dice_used += counts[1]
    points += counts[5] * 50
    dice_used += counts[5]
    return points, dice_used


def is_farkle(points):
    return points == 0


def build_state(turn_score, dice_remaining, total_score, target_score,
                opponent_score):
    """Build the complete public state a strategy may inspect."""
    return {
        "turn_score": turn_score,
        "dice_remaining": dice_remaining,
        "total_score": total_score,
        "target_score": target_score,
        "opponent_score": opponent_score,
    }


def take_turn(rng, strategy, total_score,
              target_score=DEFAULT_TARGET_SCORE,
              opponent_score=None, trace=None):
    """Play one complete turn and return points banked, or 0 on a Farkle."""
    dice_remaining = NUM_DICE
    turn_score = 0

    while True:
        dice = roll_dice(dice_remaining, rng)
        points, used = score_roll(dice)

        if trace is not None:
            trace.append(
                f"  rolled {dice} -> scores {points} points using {used} of the dice"
            )

        if is_farkle(points):
            if trace is not None:
                trace.append(f"  FARKLE -- turn ends, {turn_score} points lost")
            return 0

        turn_score += points
        dice_remaining -= used
        if dice_remaining == 0:
            dice_remaining = NUM_DICE
            if trace is not None:
                trace.append("  hot dice! rolling all 6 again")

        state = build_state(
            turn_score,
            dice_remaining,
            total_score,
            target_score,
            opponent_score,
        )
        action = strategy(state)
        if action not in VALID_ACTIONS:
            name = getattr(strategy, "name", getattr(strategy, "__name__", "strategy"))
            raise ValueError(
                f"{name} returned {action!r}; expected 'roll' or 'bank'"
            )

        if trace is not None:
            trace.append(
                f"  turn score now {turn_score}, {dice_remaining} dice left "
                f"-> strategy says {action.upper()}"
            )

        if action == "bank":
            return turn_score
