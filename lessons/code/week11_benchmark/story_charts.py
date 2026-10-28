"""Week 11 story micro-lab: charts and annotated-code images for the Big O story.

    python story_charts.py story_sample.csv --outdir story_charts
    python story_charts.py mine.csv friend.csv --outdir story_charts   # adds the hardware chart

Needs Matplotlib. Figure names are numbered in story order (S01..S12).
"""
import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path

ACCENT, INK, GREY, BLUE = "#d9480f", "#1f2933", "#9aa5b1", "#1c7ed6"
BUBBLE_SRC = [
    "def bubble_sort(data):",
    "    items = list(data)",
    "    n = len(items)",
    "    for end in range(n - 1, 0, -1):",
    "        swapped = False",
    "        for i in range(end):",
    "            if items[i] > items[i + 1]:",
    "                items[i], items[i + 1] = items[i + 1], items[i]",
    "                swapped = True",
    "    return items",
]
DRIVER_LINES = {3: "outer loop: n-1 passes", 5: "inner loop: shrinks each pass",
                6: "compare", 7: "swap"}
IGNORED_LINES = {1: "copy: n steps", 2: "len(): 1 step", 4: "reset flag: n-1 steps",
                 8: "flag set: a constant per swap", 9: "return: 1 step"}


def load(paths):
    rows = []
    for path in paths:
        with open(path, newline="", encoding="utf-8") as handle:
            for r in csv.DictReader(handle):
                r["n"] = int(r["n"]); r["wall_seconds"] = float(r["wall_seconds"])
                for k in ("outer_iters", "inner_iters", "comparisons", "swaps", "index_reads",
                          "index_writes", "flag_sets", "bookkeeping"):
                    r[k] = int(r[k])
                r["machine_label"] = f'{r["os"]} py{r["python"]} {r["cpu_count"]}cpu'
                rows.append(r)
    return rows


def pick(rows, algorithm, ordering="random", machine=None):
    machine = machine or rows[0]["machine_label"]
    pts = sorted((r for r in rows if r["algorithm"] == algorithm and r["ordering"] == ordering
                  and r["machine_label"] == machine), key=lambda r: r["n"])
    return pts


def loglog_fit(xs, ys):
    """Least-squares line on log-log axes. Returns (exponent, coefficient)."""
    lx, ly = [math.log(x) for x in xs], [math.log(y) for y in ys]
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    slope = sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)
    return slope, math.exp(my - slope * mx)


def code_image(plt, outdir, name, mode):
    fig, ax = plt.subplots(figsize=(13.5, 4.6))
    ax.set_xlim(0, 13.5); ax.set_ylim(0, len(BUBBLE_SRC) + 0.6); ax.axis("off")
    for i, line in enumerate(BUBBLE_SRC):
        y = len(BUBBLE_SRC) - i - 0.2
        face = None; note = None; color = INK
        if mode == "drivers" and i in DRIVER_LINES:
            face, note = ACCENT, DRIVER_LINES[i]
        if mode == "ignored":
            if i in DRIVER_LINES:
                face, note = ACCENT, DRIVER_LINES[i]
            elif i in IGNORED_LINES:
                face, note, color = GREY, IGNORED_LINES[i], "#6b7785"
        if face:
            ax.add_patch(plt.Rectangle((0.15, y - 0.38), 9.2, 0.8, color=face,
                                       alpha=0.22 if face == ACCENT else 0.35, lw=0))
        ax.text(0.25, y, line, family="monospace", fontsize=13.5, va="center", color=color)
        if note:
            ax.text(9.5, y, "<- " + note, fontsize=11.5, va="center", color=face if face == ACCENT else "#6b7785")
    if mode == "ignored":
        ax.text(0.2, -0.05, "orange = drives the behavior (n^2)     grey = Big O says ignore it",
                fontsize=11, color=INK)
    fig.tight_layout(); fig.savefig(outdir / name, dpi=150); plt.close(fig)


def counters_vs_n(plt, rows, outdir):
    pts = pick(rows, "bubble")
    ns = [p["n"] for p in pts]
    fig, ax = plt.subplots(figsize=(8, 5))
    for key, style in (("comparisons", "o-"), ("swaps", "s-"), ("index_reads", "^-"),
                       ("index_writes", "v--"), ("flag_sets", "x:"), ("inner_iters", "+-"),
                       ("outer_iters", "d-"), ("bookkeeping", "*-")):
        ax.plot(ns, [max(p[key], 1) for p in pts], style, label=key, alpha=0.85)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("list size n (log scale)"); ax.set_ylabel("operations counted (log scale)")
    ax.set_title("Bubble sort, random list: every counter vs n")
    ax.grid(True, which="both", alpha=0.3); ax.legend(ncol=2, fontsize=9)
    fig.text(0.01, 0.01, "Steep lines (comparisons, swaps, reads, writes, flag_sets) grow like n^2; "
             "outer_iters and bookkeeping grow like n.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(outdir / "S04_counters_vs_n.png", dpi=150)
    plt.close(fig)


def ignored_share(plt, rows, outdir):
    pts = pick(rows, "bubble")
    ns = [p["n"] for p in pts]
    total = [sum(p[k] for k in ("comparisons", "swaps", "index_reads", "index_writes",
                                "flag_sets", "bookkeeping", "outer_iters")) for p in pts]
    low = [100 * (p["bookkeeping"] + p["outer_iters"]) / t for p, t in zip(pts, total)]
    const = [100 * (p["flag_sets"] + p["index_reads"] + p["index_writes"]) / t for p, t in zip(pts, total)]
    drive = [100 * (p["comparisons"] + p["swaps"]) / t for p, t in zip(pts, total)]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ns, low, "o-", color=GREY, label="lower-order terms (setup, per-pass work): O(n)")
    ax.plot(ns, const, "s-", color=BLUE, label="constant-factor work (reads, writes, flag): still O(n^2)")
    ax.plot(ns, drive, "^-", color=ACCENT, label="compare + swap")
    ax.set_xscale("log"); ax.set_ylim(0, 100)
    ax.set_xlabel("list size n (log scale)"); ax.set_ylabel("share of all counted operations (%)")
    ax.set_title("Was ignoring them the right call? Lower-order terms vanish; constants do not")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8, loc="center right")
    fig.text(0.01, 0.01, "Big O drops BOTH. Lower-order terms really do shrink toward 0%. "
             "Constants stay a fixed share, so they never change the shape.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(outdir / "S05_ignored_share.png", dpi=150)
    plt.close(fig)
    return ns[-1], low[0], low[-1]


def ops_and_time(plt, rows, outdir):
    pts = pick(rows, "bubble")
    ns = [p["n"] for p in pts]; ops = [p["comparisons"] + p["swaps"] for p in pts]
    secs = [p["wall_seconds"] for p in pts]
    e_ops, _ = loglog_fit(ns, ops); e_t, _ = loglog_fit(ns[3:], secs[3:])
    for scale in ("log", "linear"):
        fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
        for ax, ys, label, color, exp in ((axes[0], ops, "compare + swap count", ACCENT, e_ops),
                                          (axes[1], secs, "wall-clock seconds", BLUE, e_t)):
            ax.plot(ns, ys, "o-", color=color)
            ax.set_xlabel("list size n"); ax.set_ylabel(label)
            ax.set_title(f"{label}: fitted growth ~ n^{exp:.2f}")
            ax.grid(True, which="both", alpha=0.3)
            if scale == "log":
                ax.set_xscale("log"); ax.set_yscale("log")
            else:
                ax.set_xlim(left=0); ax.set_ylim(bottom=0)
        fig.suptitle(f"Same shape, two units: operations and time ({scale} axes)")
        fig.text(0.01, 0.01, "Fit = least-squares line on log-log axes; exponent 2 means n^2. "
                 "Time is the plain (uncounted) sort, best of 3.", fontsize=8)
        fig.tight_layout(rect=(0, 0.03, 1, 0.95))
        fig.savefig(outdir / f"S06_ops_and_time_{scale}.png", dpi=150); plt.close(fig)
    return e_ops, e_t


def extrapolation(plt, rows, outdir):
    pts = pick(rows, "bubble"); small = [p for p in pts if p["n"] <= 200]
    e, a = loglog_fit([p["n"] for p in small], [p["wall_seconds"] for p in small])
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot([p["n"] for p in pts], [p["wall_seconds"] for p in pts], "o", color=BLUE, label="measured")
    ns = [p["n"] for p in pts]
    ax.plot(ns, [a * n ** e for n in ns], "-", color=ACCENT, label=f"fit from n <= 200: n^{e:.2f}")
    ax.axvspan(0, 200, alpha=0.12, color=GREY, label="data the fit saw")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("list size n (log scale)"); ax.set_ylabel("wall-clock seconds (log scale)")
    ax.set_title("Fit on small n, predict big n: does the curve hold?")
    ax.grid(True, which="both", alpha=0.3); ax.legend()
    fig.text(0.01, 0.01, "Small-n timings are noisy (microseconds), so the early exponent is rougher "
             "than the later one.", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(outdir / "S07_extrapolation.png", dpi=150)
    plt.close(fig)
    return e


def better_algorithms(plt, rows, outdir):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for name, color in (("bubble", ACCENT), ("bubble_early", "#7048e8"), ("insertion", "#2b8a3e"),
                        ("merge", BLUE)):
        pts = pick(rows, name)
        ns = [p["n"] for p in pts]
        axes[0].plot(ns, [p["comparisons"] + p["swaps"] for p in pts], "o-", color=color, label=name)
        axes[1].plot(ns, [p["wall_seconds"] for p in pts], "o-", color=color, label=name)
    for ax, ylab in ((axes[0], "compare + move/swap count"), (axes[1], "wall-clock seconds")):
        ax.set_xscale("log"); ax.set_yscale("log"); ax.grid(True, which="both", alpha=0.3)
        ax.set_xlabel("list size n (log scale)"); ax.set_ylabel(ylab + " (log scale)"); ax.legend()
    axes[0].set_title("Operations: the same story"); axes[1].set_title("Time: constants decide the crossover")
    fig.suptitle("Less naive algorithms, random lists")
    fig.text(0.01, 0.01, "bubble_early barely helps on random data; insertion halves the work; "
             "merge changes the growth rate itself (n log n).", fontsize=8)
    fig.tight_layout(rect=(0, 0.03, 1, 0.95)); fig.savefig(outdir / "S10_better_algorithms.png", dpi=150)
    plt.close(fig)
    # ordering: early exit shines on sorted input
    fig, ax = plt.subplots(figsize=(8, 4.8))
    for ordering, style in (("random", "o-"), ("sorted", "s-"), ("reversed", "^-")):
        for name, color in (("bubble", ACCENT), ("bubble_early", "#7048e8")):
            pts = pick(rows, name, ordering)
            if pts:
                ax.plot([p["n"] for p in pts], [max(p["comparisons"], 1) for p in pts], style,
                        color=color, label=f"{name} / {ordering}", alpha=0.8)
    ax.set_xscale("log"); ax.set_yscale("log"); ax.grid(True, which="both", alpha=0.3)
    ax.set_xlabel("list size n (log scale)"); ax.set_ylabel("comparisons (log scale)")
    ax.set_title("Early exit changes the BEST case (sorted input), not the worst"); ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(outdir / "S11_early_exit_orderings.png", dpi=150); plt.close(fig)


def pitfall(plt, rows, outdir):
    pts = {p["n"]: p for p in pick(rows, "bubble")}
    a, b = pts[1000]["wall_seconds"], pts[2000]["wall_seconds"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    for ax, truncated in ((axes[0], False), (axes[1], True)):
        ax.bar(["n = 1000", "n = 2000"], [a, b], color=[GREY, ACCENT])
        ax.set_ylabel("seconds")
        if truncated:
            ax.set_ylim(a * 0.95, b * 1.02)
            ax.set_title("MISLEADING: truncated axis makes 4x look like 40x", color="firebrick", fontsize=10)
        else:
            ax.set_ylim(bottom=0); ax.set_title("Honest: axis starts at zero", fontsize=10)
    fig.text(0.01, 0.01, "Same two numbers in both charts; only the y-axis start changed.", fontsize=8)
    fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(outdir / "S12_PITFALL_truncated_axis.png", dpi=150)
    plt.close(fig)


def hardware(plt, rows, outdir):
    machines = sorted({r["machine_label"] for r in rows})
    if len(machines) < 2:
        return False
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for m in machines:
        pts = pick(rows, "bubble", machine=m)
        axes[0].plot([p["n"] for p in pts], [p["comparisons"] + p["swaps"] for p in pts], "o-", label=m)
        axes[1].plot([p["n"] for p in pts], [p["wall_seconds"] for p in pts], "o-", label=m)
    for ax, ylab in ((axes[0], "compare + swap count"), (axes[1], "wall-clock seconds")):
        ax.set_xscale("log"); ax.set_yscale("log"); ax.grid(True, which="both", alpha=0.3)
        ax.set_xlabel("list size n"); ax.set_ylabel(ylab); ax.legend(fontsize=7)
    axes[0].set_title("Operation counts: identical on every machine")
    axes[1].set_title("Wall-clock time: differs by machine")
    fig.tight_layout(); fig.savefig(outdir / "S08_hardware.png", dpi=150); plt.close(fig)
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("csv", nargs="+"); parser.add_argument("--outdir", default="story_charts")
    args = parser.parse_args(argv)
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    except ImportError:
        raise SystemExit("Matplotlib is needed: python -m pip install matplotlib")
    rows = load(args.csv); outdir = Path(args.outdir); outdir.mkdir(parents=True, exist_ok=True)
    code_image(plt, outdir, "S01_code_plain.png", "plain")
    code_image(plt, outdir, "S02_code_drivers.png", "drivers")
    code_image(plt, outdir, "S03_code_ignored.png", "ignored")
    counters_vs_n(plt, rows, outdir)
    share = ignored_share(plt, rows, outdir)
    e_ops, e_t = ops_and_time(plt, rows, outdir)
    e_small = extrapolation(plt, rows, outdir)
    better_algorithms(plt, rows, outdir); pitfall(plt, rows, outdir)
    hw = hardware(plt, rows, outdir)
    print(f"charts in {outdir}; lower-order share {share[1]:.1f}% at n=10 -> {share[2]:.1f}% at n={share[0]}; "
          f"ops exponent {e_ops:.2f}, time exponent {e_t:.2f}, small-n fit {e_small:.2f}; hardware chart: {hw}")


if __name__ == "__main__":
    main()
