"""Vendored CS1 Farkle engine. Canonical owner: computer_science_1.

Rules used by the shared Fall 2026 Farkle experience:
- six standard dice;
- single 1 = 100, single 5 = 50;
- three 1s = 1000, three of V = V*100 for other values;
- each matching die beyond three doubles the three-of-a-kind value;
- no straight or three-pairs bonus;
- no scoring dice = Farkle and current turn score is lost;
- hot dice reroll all six while preserving turn score;
- all scoring dice are automatically kept;
- strategy chooses only ROLL or BANK;
- first to 4000 wins the classroom variant.
"""

DEFAULT_TARGET_SCORE = 4000
NUM_DICE = 6


def roll_dice(count, rng):
    dice = []
    for _ in range(count):
        dice.append(rng.randint(1, 6))
    return dice


def score_roll(dice):
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
    return {
        "turn_score": turn_score,
        "dice_remaining": dice_remaining,
        "total_score": total_score,
        "target_score": target_score,
        "opponent_score": opponent_score,
    }


def take_turn(rng, strategy, total_score, target_score=DEFAULT_TARGET_SCORE,
              opponent_score=None, trace=None):
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
                trace.append(
                    f"  FARKLE -- turn ends, {turn_score} points lost"
                )
            return 0
        turn_score += points
        dice_remaining -= used
        if dice_remaining == 0:
            dice_remaining = NUM_DICE
            if trace is not None:
                trace.append("  hot dice! rolling all 6 again")
        state = build_state(
            turn_score, dice_remaining, total_score, target_score, opponent_score
        )
        action = strategy(state)
        if trace is not None:
            trace.append(
                f"  turn score now {turn_score}, {dice_remaining} dice left "
                f"-> strategy says {action.upper()}"
            )
        if action == "bank":
            return turn_score
