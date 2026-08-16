"""Vendored human-strategy contract from hardened CS1 Week 16."""


def bank_at(threshold):
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
    threshold = 500
    safety_margin = 500
    distance_to_win = state["target_score"] - state["total_score"]
    if distance_to_win <= safety_margin:
        return "bank" if state["turn_score"] >= threshold // 2 else "roll"
    return "bank" if state["turn_score"] >= threshold else "roll"


cautious_near_target.description = (
    "Bank at 500 normally; bank at 250 once within 500 points of the target score."
)


def aggressive_when_behind(state):
    threshold = 500
    gap = 1000
    opponent_score = state["opponent_score"] or 0
    behind_by = opponent_score - state["total_score"]
    local_threshold = threshold + gap if behind_by > gap else threshold
    return "bank" if state["turn_score"] >= local_threshold else "roll"


aggressive_when_behind.description = (
    "Bank at 500 normally; require 1500 if more than 1000 points behind the opponent."
)


def always_bank_first_score(state):
    return "bank"


always_bank_first_score.description = "Bank the instant any points are on the board."


BUILT_IN_STRATEGIES = {
    "bank_at_300": bank_at_300,
    "bank_at_500": bank_at_500,
    "bank_at_800": bank_at_800,
    "cautious_near_target": cautious_near_target,
    "aggressive_when_behind": aggressive_when_behind,
    "always_bank_first_score": always_bank_first_score,
}


def resolve_strategy(name):
    if name in BUILT_IN_STRATEGIES:
        return BUILT_IN_STRATEGIES[name]
    prefix = "bank_at_"
    if name.startswith(prefix):
        raw_threshold = name[len(prefix):]
        try:
            threshold = int(raw_threshold)
        except ValueError as exc:
            raise ValueError(
                f"unknown strategy '{name}'; bank_at_N requires an integer N"
            ) from exc
        return bank_at(threshold)
    known = ", ".join(sorted(BUILT_IN_STRATEGIES))
    raise ValueError(
        f"unknown strategy '{name}'. Use one of [{known}] or bank_at_N, e.g. bank_at_425"
    )
