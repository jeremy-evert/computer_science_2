"""Fair, deterministic repeated-game simulation with auditable raw evidence."""

import random

from . import engine

DEFAULT_MAX_TURNS = 400


def _strategy_name(strategy, fallback):
    return getattr(
        strategy,
        "name",
        getattr(strategy, "__name__", fallback),
    )


def play_game(rng, strategy_a, strategy_b,
              target_score=engine.DEFAULT_TARGET_SCORE,
              max_turns=DEFAULT_MAX_TURNS, starting_player=0):
    """Play one two-player game and return strategy-indexed raw evidence."""
    if starting_player not in (0, 1):
        raise ValueError("starting_player must be 0 or 1")

    scores = [0, 0]
    farkles = [0, 0]
    turns_by_player = [0, 0]
    turns_played = 0
    strategies = [strategy_a, strategy_b]

    while turns_played < max_turns:
        current_player = (starting_player + turns_played) % 2
        opponent_player = 1 - current_player
        points = engine.take_turn(
            rng,
            strategies[current_player],
            total_score=scores[current_player],
            target_score=target_score,
            opponent_score=scores[opponent_player],
        )
        turns_by_player[current_player] += 1
        if points == 0:
            farkles[current_player] += 1
        scores[current_player] += points
        turns_played += 1
        if scores[current_player] >= target_score:
            break

    if scores[0] > scores[1]:
        winner = 0
    elif scores[1] > scores[0]:
        winner = 1
    else:
        winner = None

    return {
        "scores": scores,
        "farkles": farkles,
        "turns_by_player": turns_by_player,
        "turns_played": turns_played,
        "starting_player": starting_player,
        "winner": winner,
    }


def run_many_games(strategy_a, strategy_b, num_games, seed,
                   target_score=engine.DEFAULT_TARGET_SCORE):
    """Run a balanced seeded comparison and preserve raw + derived evidence."""
    if num_games <= 0:
        raise ValueError("num_games must be positive")

    rng = random.Random(seed)
    wins = [0, 0]
    ties = 0
    total_scores = [0, 0]
    total_farkles = [0, 0]
    total_player_turns = [0, 0]
    starter_counts = [0, 0]
    total_turns = 0

    for game_index in range(num_games):
        starting_player = game_index % 2
        starter_counts[starting_player] += 1
        result = play_game(
            rng,
            strategy_a,
            strategy_b,
            target_score=target_score,
            starting_player=starting_player,
        )
        if result["winner"] == 0:
            wins[0] += 1
        elif result["winner"] == 1:
            wins[1] += 1
        else:
            ties += 1

        for player in (0, 1):
            total_scores[player] += result["scores"][player]
            total_farkles[player] += result["farkles"][player]
            total_player_turns[player] += result["turns_by_player"][player]
        total_turns += result["turns_played"]

    return {
        "num_games": num_games,
        "seed": seed,
        "target_score": target_score,
        "strategy_a": _strategy_name(strategy_a, "strategy_a"),
        "strategy_b": _strategy_name(strategy_b, "strategy_b"),
        "starts_a": starter_counts[0],
        "starts_b": starter_counts[1],
        "wins_a": wins[0],
        "wins_b": wins[1],
        "ties": ties,
        "turns_a": total_player_turns[0],
        "turns_b": total_player_turns[1],
        "farkles_a": total_farkles[0],
        "farkles_b": total_farkles[1],
        "win_rate_a": wins[0] / num_games,
        "win_rate_b": wins[1] / num_games,
        "tie_rate": ties / num_games,
        "avg_score_a": total_scores[0] / num_games,
        "avg_score_b": total_scores[1] / num_games,
        "avg_turns_per_game": total_turns / num_games,
        "farkle_rate_a": (
            total_farkles[0] / total_player_turns[0]
            if total_player_turns[0] else 0.0
        ),
        "farkle_rate_b": (
            total_farkles[1] / total_player_turns[1]
            if total_player_turns[1] else 0.0
        ),
    }


def format_comparison(summary):
    """Render a compact human-readable view without replacing raw evidence."""
    return "\n".join([
        (
            f"{summary['num_games']} games, seed={summary['seed']} "
            f"(starts A/B={summary['starts_a']}/{summary['starts_b']})"
        ),
        (
            f"  {summary['strategy_a']:<28} wins {summary['wins_a']:>5} "
            f"win rate {summary['win_rate_a']:.1%} "
            f"avg score {summary['avg_score_a']:.0f} "
            f"farkle/own-turn {summary['farkle_rate_a']:.1%}"
        ),
        (
            f"  {summary['strategy_b']:<28} wins {summary['wins_b']:>5} "
            f"win rate {summary['win_rate_b']:.1%} "
            f"avg score {summary['avg_score_b']:.0f} "
            f"farkle/own-turn {summary['farkle_rate_b']:.1%}"
        ),
        (
            f"  ties {summary['ties']} ({summary['tie_rate']:.1%}) "
            f"avg turns/game {summary['avg_turns_per_game']:.1f}"
        ),
    ])
