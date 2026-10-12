"""Week 9: bubble sort vs Python's Timsort, three input scenarios.

Stdlib for the benchmark; the report step needs matplotlib and seaborn.
Run:  python timsort_vs_bubble.py   (a few minutes; bubble sort at n=50,000)

Writes timsort_results.json, then report/ charts and appends two sections to
report/index.html.
"""
import datetime
import json
import math
import os
import platform
import random
import time

from bubble_sort_benchmark import bubble_sort

HERE = os.path.dirname(os.path.abspath(__file__))
SIZES = [100, 500, 1000, 2500, 5000, 10000, 20000, 50000, 100000]
BUBBLE_HALT_SECONDS = 30.0
SCENARIOS = [("random", "RANDOM DATA"),
             ("nearly_sorted", "NEARLY SORTED DATA"),
             ("reverse", "REVERSE SORTED DATA")]
TIMSORT_REPEATS = 5  # timsort is microseconds at small n; take the best of 5


def timsort(data):
    return sorted(data)


def make_random(n, seed=None):
    rng = random.Random(42 + n if seed is None else seed)
    return [rng.randint(0, n * 10) for _ in range(n)]


def make_nearly_sorted(n, seed):
    """Sorted list with 2% of elements' worth of random pair swaps."""
    items = list(range(n))
    rng = random.Random(seed)
    if n >= 2:
        for _ in range(max(1, int(n * 0.02))):
            i, j = rng.randrange(n), rng.randrange(n)
            items[i], items[j] = items[j], items[i]
    return items


def make_reverse(n):
    return list(range(n, 0, -1))


def time_once(fn, data):
    start = time.perf_counter()
    fn(data)
    return time.perf_counter() - start


def time_timsort(data):
    return min(time_once(timsort, data) for _ in range(TIMSORT_REPEATS))


def run_assertions():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert timsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([]) == []
    assert timsort([7]) == [7]
    nearly = make_nearly_sorted(10, seed=1)
    assert sorted(nearly) == list(range(10))
    print("All assertions passed.")
    print()


def hardware_profile():
    timestamp = datetime.datetime.now().isoformat()
    processor = platform.processor() or "unknown"
    cores = os.cpu_count()
    print("=== HARDWARE PROFILE ===")
    print(f"Processor: {processor}")
    print(f"Logical cores: {cores}")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Run timestamp: {timestamp}")
    print()
    return processor, cores, timestamp


def benchmark():
    results = {key: [] for key, _ in SCENARIOS}
    halted = False
    halt_note = ""
    for n in SIZES:
        inputs = {
            "random": make_random(n),
            "nearly_sorted": make_nearly_sorted(n, seed=99 + n),
            "reverse": make_reverse(n),
        }
        for key, data in inputs.items():
            row = {"n": n, "bubble": None,
                   "timsort": time_timsort(data)}
            if not halted:
                assert bubble_sort(data) == sorted(data)  # correctness
                row["bubble"] = time_once(bubble_sort, data)
                if key == "random" and row["bubble"] > BUBBLE_HALT_SECONDS:
                    halted = True
                    halt_note = (f"Bubble sort halted after n={n:,}: random "
                                 f"data took {row['bubble']:.1f}s "
                                 f"(> {BUBBLE_HALT_SECONDS:.0f}s limit).")
            results[key].append(row)
        print(f"  done n={n:,}", flush=True)
    print()
    return results, halt_note


def fmt_t(t):
    return "-" if t is None else f"{t:.6f}"


def speedup(row):
    if row["bubble"] is None or row["timsort"] == 0:
        return None
    return row["bubble"] / row["timsort"]


def print_tables(results, halt_note):
    for key, title in SCENARIOS:
        print(f"=== {title} ===")
        print(f"{'n':>8} | {'bubble (s)':>12} | {'timsort (s)':>12} | "
              f"{'speedup':>12}")
        print(f"{'-' * 8}-+-{'-' * 12}-+-{'-' * 12}-+-{'-' * 12}")
        for row in results[key]:
            s = speedup(row)
            print(f"{row['n']:>8,} | {fmt_t(row['bubble']):>12} | "
                  f"{fmt_t(row['timsort']):>12} | "
                  f"{'-' if s is None else f'{s:,.0f}x':>12}")
        print()
    if halt_note:
        print(halt_note)
        print()


def pct_off(actual, theory):
    return abs(actual - theory) / theory * 100


def print_reality_check(results):
    print("=== BIG O REALITY CHECK (random data) ===")
    print(f"{'n1 -> n2':>16} | {'bubble':>8} | {'n^2':>8} | {'off':>9} | "
          f"{'timsort':>8} | {'n log n':>8} | {'off':>9}")
    rows = [r for r in results["random"]
            if r["bubble"] is not None and r["timsort"] > 0]
    b_off, t_off = [], []
    for a, b in zip(rows, rows[1:]):
        n1, n2 = a["n"], b["n"]
        act_b = b["bubble"] / a["bubble"]
        th_b = (n2 / n1) ** 2
        act_t = b["timsort"] / a["timsort"]
        th_t = (n2 * math.log2(n2)) / (n1 * math.log2(n1))
        b_off.append(pct_off(act_b, th_b))
        t_off.append(pct_off(act_t, th_t))
        print(f"{f'{n1:,} -> {n2:,}':>16} | {act_b:>8.2f} | {th_b:>8.2f} | "
              f"{b_off[-1]:>7.1f}% | {act_t:>8.2f} | {th_t:>8.2f} | "
              f"{t_off[-1]:>7.1f}%")
    print()
    print(f"Bubble sort: average {sum(b_off) / len(b_off):.1f}% "
          f"from n^2 theory")
    print(f"Timsort: average {sum(t_off) / len(t_off):.1f}% "
          f"from n log n theory")
    print("(Small-n rows are dominated by timer resolution and fixed "
          "overhead, so they sit far from theory.)")
    print()


def print_scenario_comparison(results):
    print("=== TIMSORT: HOW INPUT ORDER AFFECTS O(n log n) ===")
    print(f"{'n':>8} | {'random (s)':>12} | {'nearly sorted (s)':>17} | "
          f"{'reverse (s)':>12} | {'random/nearly':>13}")
    print(f"{'-' * 8}-+-{'-' * 12}-+-{'-' * 17}-+-{'-' * 12}-+-{'-' * 13}")
    for r, ns, rv in zip(results["random"], results["nearly_sorted"],
                         results["reverse"]):
        ratio = r["timsort"] / ns["timsort"] if ns["timsort"] else 0
        print(f"{r['n']:>8,} | {r['timsort']:>12.6f} | "
              f"{ns['timsort']:>17.6f} | {rv['timsort']:>12.6f} | "
              f"{ratio:>12.1f}x")
    print()
    print("Timsort detects existing order (runs) and skips work it does not "
          "need to do. This is why O(n log n) is a WORST CASE bound -- on "
          "real-world data that is often partially sorted, Timsort "
          "approaches O(n).")
    print()


def print_explanation(results):
    biggest = [r for r in results["random"] if r["bubble"] is not None][-1]
    print("=== WHAT BIG O IS REALLY SAYING ===")
    print(
        "Big O describes how the cost of an algorithm scales as the input "
        "grows, not how fast any single run is. For bubble sort the cost is "
        "proportional to n squared, so doubling n quadruples the work, which "
        f"is why a random list of {biggest['n']:,} items took "
        f"{biggest['bubble']:.0f} seconds on this machine. For an n log n "
        "sort, doubling n only slightly more than doubles the work, because "
        "log2(2n) = log2(n) + 1 and that extra term barely grows. Timsort "
        "also has a much smaller constant factor, since it is written in C "
        "and works on memory in a cache-friendly way that a Python loop "
        "cannot. The ratio table is evidence that Big O is a real "
        "prediction and not just notation: when theory says about 4x and "
        "the measurement says about 4x, that is the model working. Merge "
        "sort and Timsort share the same Big O class, yet Timsort wins "
        "again on constant factor, cache behavior, and because it adapts to "
        "order already present in the input. Big O tells you which "
        "algorithm survives growth; the constant tells you who is faster "
        "today.")
    print()


def print_world_bible(processor, cores, timestamp, results):
    first = next((r["n"] for r in results["random"]
                  if (speedup(r) or 0) > 1000), None)
    print("=== WORLD BIBLE: TIMSORT VS BUBBLE ===")
    print("Adds: bubble vs Timsort on random, nearly sorted and reverse "
          "data, a Big O reality check, and charts.")
    print(f"Hardware: {processor} | {cores} cores | Run: {timestamp}")
    if first is None:
        print("Key finding: Timsort's speedup did not exceed 1,000x at any "
              "size bubble sort completed.")
    else:
        print(f"Key finding: Timsort's speedup on random data first exceeds "
              f"1,000x at n={first:,}.")
    print("Debt: insertion sort (also O(n^2), smaller constant) and heap "
          "sort (O(n log n), worse cache behavior) were not tested.")


def save_json(timestamp, halt_note, results):
    payload = {"timestamp": timestamp, "halt_note": halt_note}
    payload.update(results)
    path = os.path.join(HERE, "timsort_results.json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    return path


MARKER = "<!-- timsort-vs-bubble -->"


def make_report(json_path=None):
    """Draw the two charts and append sections to report/index.html."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns

    with open(json_path or os.path.join(HERE, "timsort_results.json")) as f:
        data = json.load(f)
    out = os.path.join(HERE, "report")
    os.makedirs(out, exist_ok=True)
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(9, 5.5))
    lines = [("random", "bubble", "bubble / random", "#c0392b", "o"),
             ("random", "timsort", "timsort / random", "#2874a6", "s"),
             ("nearly_sorted", "timsort", "timsort / nearly sorted",
              "#1e8449", "^"),
             ("reverse", "timsort", "timsort / reverse", "#b7950b", "D")]
    for scen, algo, label, color, marker in lines:
        pts = [(r["n"], r[algo]) for r in data[scen]
               if r[algo] is not None and r[algo] > 0]
        ax.plot([p[0] for p in pts], [p[1] for p in pts], marker=marker,
                color=color, label=label)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Input array size (n)")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("Bubble (O(n²)) vs Timsort (O(n log n)) — log-log")
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(out, "timsort_vs_bubble_loglog.png"), dpi=150)
    plt.close(fig)

    both = [(r["n"], r["bubble"] / r["timsort"]) for r in data["random"]
            if r["bubble"] is not None and r["timsort"] > 0]
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot([p[0] for p in both], [p[1] for p in both], marker="o",
            color="#2874a6")
    ax.axhline(1000, ls="--", color="gray")
    ax.text(both[0][0], 1000 * 1.1, "1,000x", color="gray")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Input array size (n)")
    ax.set_ylabel("Speedup (bubble time / timsort time)")
    ax.set_title("How many times faster is Timsort than bubble sort?")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "speedup.png"), dpi=150)
    plt.close(fig)

    index = os.path.join(out, "index.html")
    section = f"""{MARKER}
<h2>Timsort vs Bubble (log-log)</h2>
<img src="timsort_vs_bubble_loglog.png" alt="Bubble and Timsort on log-log axes, three input scenarios">
<h2>Timsort speedup factor</h2>
<img src="speedup.png" alt="Speedup of Timsort over bubble sort on random data">
"""
    with open(index, encoding="utf-8") as f:
        html = f.read()
    if MARKER not in html:  # idempotent: do not append twice
        html = html.replace("</body>", section + "</body>", 1)
        with open(index, "w", encoding="utf-8") as f:
            f.write(html)
    print(f"Report updated: {index}")


def main():
    processor, cores, timestamp = hardware_profile()
    run_assertions()
    results, halt_note = benchmark()
    print_tables(results, halt_note)
    print_reality_check(results)
    print_scenario_comparison(results)
    print_explanation(results)
    print_world_bible(processor, cores, timestamp, results)
    print()
    print(f"Results saved: {save_json(timestamp, halt_note, results)}")
    make_report()


if __name__ == "__main__":
    main()
