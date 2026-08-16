"""Plot one declared cost currency against Farkle effectiveness.

The plot intentionally requires the caller to name the x-axis currency instead
of collapsing training, runtime, model size, and complexity into one score.
"""

import argparse
import csv
from pathlib import Path


ALLOWED_X = {
    "preparation_seconds_a": "Preparation time (seconds)",
    "seconds_per_game": "Evaluation seconds per game",
    "model_size_bytes_a": "Persisted/estimated model size (bytes)",
    "training_turns_a": "Training turns",
}


def load_rows(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def plot_tradeoff(csv_path, output_path, x_field="preparation_seconds_a"):
    if x_field not in ALLOWED_X:
        raise ValueError(
            f"x_field must be one of {', '.join(sorted(ALLOWED_X))}"
        )

    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise RuntimeError(
            "matplotlib is not available; the experiment evidence is still valid, "
            "but this optional course plotting path cannot run here"
        ) from exc

    rows = load_rows(csv_path)
    if not rows:
        raise ValueError("result CSV has no rows")

    x_values = [float(row[x_field]) for row in rows]
    y_values = [float(row["win_rate_a"]) for row in rows]
    labels = [row["strategy_a"] for row in rows]

    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values)
    for x_value, y_value, label in zip(x_values, y_values, labels):
        ax.annotate(label, (x_value, y_value))
    ax.set_xlabel(ALLOWED_X[x_field])
    ax.set_ylabel("Validated win rate vs fixed baseline")
    ax.set_title("Farkle: what did the extra cost buy?")
    ax.set_ylim(0.0, 1.0)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path)
    plt.close(fig)
    return output_path


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("output_path")
    parser.add_argument("--x", dest="x_field", choices=sorted(ALLOWED_X),
                        default="preparation_seconds_a")
    args = parser.parse_args(argv)
    path = plot_tradeoff(args.csv_path, args.output_path, args.x_field)
    print(path)


if __name__ == "__main__":
    main()
