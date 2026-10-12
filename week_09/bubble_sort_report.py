"""Turn bubble_sort_results.json into charts and a local HTML report.

Needs matplotlib and seaborn (pip install matplotlib seaborn).
Run:  python bubble_sort_report.py   then open report/index.html
"""
import html
import json
import math
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import seaborn as sns  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "report")


def load():
    with open(os.path.join(HERE, "bubble_sort_results.json")) as f:
        return json.load(f)


def plot_bubble(rows, budget):
    """The requested graph: n across the bottom, bubble sort seconds up."""
    done = [r for r in rows if r["bubble"] is not None]
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5.5))
    sns.lineplot(x=[r["n"] for r in done], y=[r["bubble"] for r in done],
                 marker="o", ax=ax, color="#c0392b")
    ax.axhline(budget, ls="--", color="gray")
    ax.text(done[0]["n"], budget * 1.02, f"{budget:.0f}s budget", color="gray")
    ax.set_xlabel("Input array size (n)")
    ax.set_ylabel("Bubble sort time (seconds)")
    ax.set_title("Bubble sort: time to complete vs input size")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "bubble_vs_n.png"), dpi=150)
    plt.close(fig)


def plot_compare(rows):
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for key, label, color in (("bubble", "bubble sort", "#c0392b"),
                              ("merge", "merge sort", "#2874a6"),
                              ("python", "python sorted()", "#1e8449")):
        pts = [(r["n"], r[key]) for r in rows if r[key] is not None]
        sns.lineplot(x=[p[0] for p in pts], y=[p[1] for p in pts],
                     marker="o", label=label, color=color, ax=ax)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Input array size (n, log scale)")
    ax.set_ylabel("Time (seconds, log scale)")
    ax.set_title("All three sorts, log-log (bubble's slope is ~2)")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "compare_loglog.png"), dpi=150)
    plt.close(fig)


def table(headers, body):
    head = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    rows = "".join(
        "<tr>" + "".join(f"<td>{html.escape(str(c))}</td>" for c in r) + "</tr>"
        for r in body)
    return f"<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>"


def build_html(data):
    rows = data["results"]
    f = lambda v: "-" if v is None else f"{v:.4f}"
    results = [(r["n"], f(r["bubble"]), f(r["merge"]), f(r["python"]),
                "-" if r["bubble"] is None else f"{r['bubble'] / r['python']:,.0f}x")
               for r in rows]
    done = [r for r in rows if r["bubble"] is not None]
    ratios = []
    for a, b in zip(done, done[1:]):
        ratios.append((f"{a['n']} -> {b['n']}",
                       f"{b['bubble'] / a['bubble']:.2f}",
                       f"{(b['n'] / a['n']) ** 2:.2f}",
                       f"{b['merge'] / a['merge']:.2f}",
                       f"{(b['n'] * math.log2(b['n'])) / (a['n'] * math.log2(a['n'])):.2f}"))
    biggest = done[-1]
    halt = html.escape(data.get("halt_note") or "")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bubble Sort Benchmark</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }}
table {{ border-collapse: collapse; margin: 1rem 0; }}
th, td {{ border: 1px solid #bbb; padding: .3rem .7rem; text-align: right; }}
th {{ background: #eee; }}
img {{ max-width: 100%; }}
code {{ background: #f2f2f2; padding: 0 .25rem; }}
</style></head><body>
<h1>Week 9: Bubble sort benchmark</h1>
<p><strong>Machine:</strong> {html.escape(str(data['processor']))},
{data['cores']} logical cores. <strong>Run:</strong> {html.escape(data['timestamp'])}.</p>
<p>Biggest bubble sort that finished inside the {data['budget_seconds']:.0f}s budget:
<strong>n = {biggest['n']:,}</strong> in <strong>{biggest['bubble']:.1f}s</strong>.
{halt}</p>
<h2>Bubble sort time vs input size</h2>
<img src="bubble_vs_n.png" alt="Bubble sort seconds against array size">
<h2>All three sorts (log-log)</h2>
<img src="compare_loglog.png" alt="Bubble, merge and python sort on log-log axes">
<h2>Results</h2>
{table(["n", "bubble (s)", "merge (s)", "python (s)", "bubble/python"], results)}
<h2>Big O reality check</h2>
{table(["n1 -> n2", "actual bubble ratio", "theoretical n^2",
        "actual merge ratio", "theoretical n log n"], ratios)}
<p>When n grows by a factor, bubble sort's time grows by about that factor
squared, and merge sort's by a little more than that factor: Big O is a real
prediction, not just notation.</p>
</body></html>
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    data = load()
    plot_bubble(data["results"], data["budget_seconds"])
    plot_compare(data["results"])
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_html(data))
    print(f"Report written: {os.path.join(OUT, 'index.html')}")


if __name__ == "__main__":
    main()
