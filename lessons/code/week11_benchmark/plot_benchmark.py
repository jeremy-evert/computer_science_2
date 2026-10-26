"""Week 11 optional micro-lab: turn benchmark CSV(s) into honest charts.

    python plot_benchmark.py results_mine.csv [results_friend.csv ...]
    python plot_benchmark.py sample_results.csv --outdir charts

Needs Matplotlib (python -m pip install matplotlib). Writes three PNGs:

  1_honest_sorts.png        log-log axes, one line per algorithm, titled with a claim
  2_honest_platforms.png    same algorithm across the machines you gave it
  3_PITFALL_linear_axis.png the MISLEADING alternative: same data on linear axes
                            starting at zero, where the fast algorithms are squashed
                            against the bottom and their growth is hidden. Use it as the 'misleading
                            alternative' in your Odyssey, not as your answer.
"""
import argparse
import csv
from collections import defaultdict
from pathlib import Path


def load(paths):
    rows = []
    for path in paths:
        with open(path, newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                row["n"] = int(row["n"])
                row["best_seconds"] = float(row["best_seconds"])
                row["label"] = f'{row["os"]} py{row["python"]} ({row["cpu_count"]} cpu)'
                rows.append(row)
    return rows


def series(rows, kind, ordering, label):
    grouped = defaultdict(list)
    for r in rows:
        if r["kind"] == kind and r["ordering"] == ordering and r["label"] == label:
            grouped[r["algorithm"]].append((r["n"], r["best_seconds"]))
    return {name: sorted(points) for name, points in grouped.items()}


def honest_sorts(plt, rows, label, outdir):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, kind, ordering, title in (
        (axes[0], "sort", "random", "Sorting random lists"),
        (axes[1], "search", "sorted", "Searching a sorted list (key at the end)"),
    ):
        for name, pts in series(rows, kind, ordering, label).items():
            ax.plot(*zip(*pts), marker="o", label=name)
        ax.set_xscale("log"); ax.set_yscale("log")
        ax.set_xlabel("list size n (log scale)")
        ax.set_ylabel("best time, seconds (log scale)")
        ax.set_title(title); ax.grid(True, which="both", alpha=0.3); ax.legend()
    fig.suptitle(f"Growth rate, not speed, separates the algorithms - {label}")
    fig.text(0.01, 0.01, "Log-log axes: a steeper line means worse growth. Best of "
             "several repeats; one machine, one run.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 0.95))
    fig.savefig(outdir / "1_honest_sorts.png", dpi=150)


def honest_platforms(plt, rows, outdir):
    labels = sorted({r["label"] for r in rows})
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for label in labels:
        pts = series(rows, "sort", "random", label).get("merge", [])
        if pts:
            ax.plot(*zip(*pts), marker="o", label=label)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("list size n (log scale)"); ax.set_ylabel("best time, seconds (log scale)")
    ax.set_title("Same merge sort, different machines")
    ax.grid(True, which="both", alpha=0.3); ax.legend(fontsize=8)
    fig.text(0.01, 0.01, "Different CPUs/OS/Python versions shift the line; "
             "they do not change its shape.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(outdir / "2_honest_platforms.png", dpi=150)


def pitfall(plt, rows, label, outdir):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for name, pts in series(rows, "sort", "random", label).items():
        ax.plot(*zip(*pts), marker="o", label=name)
    ax.set_xlim(left=0); ax.set_ylim(bottom=0)
    ax.set_title("MISLEADING: linear axes hide the growth of the fast sorts")
    ax.set_xlabel("list size n"); ax.set_ylabel("seconds")
    ax.legend()
    fig.text(0.01, 0.01, "Pitfall: bubble/insertion set the scale, so the other sorts are "
             "squashed against zero and their growth is unreadable; see chart 1.", fontsize=8, color="firebrick")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(outdir / "3_PITFALL_linear_axis.png", dpi=150)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("csv", nargs="+")
    parser.add_argument("--outdir", default=".")
    args = parser.parse_args(argv)
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        raise SystemExit("Matplotlib is needed: python -m pip install matplotlib")
    rows = load(args.csv)
    outdir = Path(args.outdir); outdir.mkdir(parents=True, exist_ok=True)
    label = sorted({r["label"] for r in rows})[0]
    honest_sorts(plt, rows, label, outdir)
    honest_platforms(plt, rows, outdir)
    pitfall(plt, rows, label, outdir)
    print(f"wrote 3 charts to {outdir}")


if __name__ == "__main__":
    main()
