from __future__ import annotations

# beast.py -- sorting & searching experiment report generator.
# Writes tables (csv), plots (png) and a LaTeX report into ./out
# Run:  python beast.py        (from this folder)
# NOTE from the previous maintainer: it works. Do not touch it.
import os, sys, random, csv, math, subprocess, time
from functools import cmp_to_key
from dataclasses import dataclass
from typing import Callable, Sequence

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except Exception:
    plt = None


@dataclass
class SortMetrics:
    comparisons: int = 0
    swaps: int = 0


@dataclass
class SearchMetrics:
    probes: int = 0


SortFn = Callable[[list[int], SortMetrics], tuple[list[int], SortMetrics]]
SearchFn = Callable[[Sequence[int], float, SearchMetrics], tuple[int, SearchMetrics]]


SIZES: list[int] = [10, 20, 40, 80, 160]
T = 5
LOOK = 200
OUTD = "out"
KINDS: list[str] = ["random", "sorted", "reversed"]



def _resolve_metrics(metrics, factory):
    if metrics is not None:
        return metrics, True
    return factory(), False



def _finish_with_metrics(result, metrics, provided):
    if provided:
        return result, metrics
    return result



def bubble_sort(data, metrics=None):
    metrics, provided = _resolve_metrics(metrics, SortMetrics)
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            metrics.comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                metrics.swaps += 1
    return _finish_with_metrics(data, metrics, provided)


def bubble_sort_early_exit(data, metrics=None):
    metrics, provided = _resolve_metrics(metrics, SortMetrics)
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            metrics.comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                metrics.swaps += 1
                swapped = True
        if not swapped:
            break
    return _finish_with_metrics(data, metrics, provided)


def insertion_sort(data, metrics=None):
    metrics, provided = _resolve_metrics(metrics, SortMetrics)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            metrics.comparisons += 1
            if data[j] > key:
                data[j + 1] = data[j]
                metrics.swaps += 1
                j -= 1
            else:
                break
        data[j + 1] = key
    return _finish_with_metrics(data, metrics, provided)


def selection_sort(data, metrics=None):
    metrics, provided = _resolve_metrics(metrics, SortMetrics)
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            metrics.comparisons += 1
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            metrics.swaps += 1
    return _finish_with_metrics(data, metrics, provided)


def python_sort(data, metrics=None):
    metrics, provided = _resolve_metrics(metrics, SortMetrics)

    def cmp(left, right):
        metrics.comparisons += 1
        return (left > right) - (left < right)

    data.sort(key=cmp_to_key(cmp))
    return _finish_with_metrics(data, metrics, provided)


def linear_search(values, target, metrics=None):
    metrics, provided = _resolve_metrics(metrics, SearchMetrics)
    for i in range(len(values)):
        metrics.probes += 1
        if values[i] == target:
            return _finish_with_metrics(i, metrics, provided)
    return _finish_with_metrics(-1, metrics, provided)


def binary_search(values, target, metrics=None):
    metrics, provided = _resolve_metrics(metrics, SearchMetrics)
    lo = 0
    hi = len(values) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        metrics.probes += 1
        if values[mid] == target:
            return _finish_with_metrics(mid, metrics, provided)
        metrics.probes += 1
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return _finish_with_metrics(-1, metrics, provided)


def generate_input(kind: str, n: int, rng: random.Random) -> list[int]:
    values = [rng.randint(0, 10 * n) for _ in range(n)]
    if kind == "random":
        return values
    if kind == "sorted":
        return sorted(values)
    return sorted(values, reverse=True)


def average_search_probes(search_fn: Callable, data: Sequence[int], targets: Sequence[float]) -> float:
    total = 0
    for x in targets:
        _, metrics = search_fn(data, x, SearchMetrics())
        total += metrics.probes
    return total / len(targets)


def _format_numeric_value(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return str(round(value, 1))


def _best_sort_result(results: dict[str, tuple[float, float]], kind: str) -> tuple[str, float]:
    best_name = ""
    best_value = float("inf")
    for name, _ in SORT_ALGORITHMS:
        value = results[kind + "|" + name + "|" + str(SIZES[-1])][0]
        if value < best_value:
            best_value = value
            best_name = name
    return best_name, best_value


def _render_sort_table(kind: str, results: dict[str, tuple[float, float]]) -> str:
    lines = [
        "\\subsection{" + kind.capitalize() + " input}",
        "\\begin{tabular}{l" + "r" * (len(SIZES)) + "}",
        "\\hline",
        "algorithm",
    ]
    for n in SIZES:
        lines[-1] += " & " + str(n)
    lines.append("\\\\")
    lines.append("\\hline")
    for name, _ in SORT_ALGORITHMS:
        row = name
        for n in SIZES:
            value = results[kind + "|" + name + "|" + str(n)][0]
            row += " & " + _format_numeric_value(value)
        lines.append(row + " \\\\")
    lines.extend(["\\hline", "\\end{tabular}", ""])
    return "\n".join(lines) + "\n"


def _render_search_table(search_results: dict[int, tuple[float, float]]) -> str:
    lines = [
        "\\begin{tabular}{rrr}",
        "\\hline",
        "n & linear & binary \\\\",
        "\\hline",
    ]
    for n in SIZES:
        lines.append(str(n) + " & " + str(round(search_results[n][0], 2)) + " & " + str(round(search_results[n][1], 2)) + " \\\\")
    lines.extend(["\\hline", "\\end{tabular}", ""])
    return "\n".join(lines) + "\n"


def build_report(results: dict[str, tuple[float, float]], search_results: dict[int, tuple[float, float]]) -> str:
    s = "\\documentclass{article}\n\\usepackage{graphicx}\n\\usepackage[margin=1in]{geometry}\n"
    s += "\\begin{document}\n\\title{Sorting and Searching: What the Counts Say}\n\\author{CS2}\n\\date{}\n\\maketitle\n"
    s += "\\section{Sorting}\nEach cell is the average of " + str(T) + " seeded trials. "
    s += "Lists of sizes " + ", ".join(str(n) for n in SIZES) + ".\n"
    for kind in KINDS:
        s += _render_sort_table(kind, results)
        best_name, best_value = _best_sort_result(results, kind)
        s += "At $n=" + str(SIZES[-1]) + "$ the fewest comparisons on " + kind + " input: \\textbf{" + best_name + "} (" + str(round(best_value, 1)) + ").\n\n"
    s += "\\begin{figure}[h]\n\\centering\n\\IfFileExists{out/sort_counts.png}{\\includegraphics[width=0.7\\textwidth]{out/sort_counts.png}}{\\textit{(plot missing)}}\n\\caption{Comparisons, random input.}\n\\end{figure}\n"
    s += "\\section{Searching}\nAverage probes per lookup over " + str(LOOK) + " lookups (half present, half absent).\n\n"
    s += _render_search_table(search_results)
    r = search_results[SIZES[-1]][0] / search_results[SIZES[-1]][1]
    s += "At $n=" + str(SIZES[-1]) + "$ binary search used about " + str(round(r, 1)) + " times fewer probes.\n"
    s += "\\begin{figure}[h]\n\\centering\n\\IfFileExists{out/search_probes.png}{\\includegraphics[width=0.7\\textwidth]{out/search_probes.png}}{\\textit{(plot missing)}}\n\\caption{Probes per lookup.}\n\\end{figure}\n"
    s += "\\end{document}\n"
    return s


def _measure_sort_trial(sort_fn: SortFn, data: list[int]) -> tuple[list[int], SortMetrics, float]:
    metrics = SortMetrics()
    start = time.perf_counter()
    ordered, metrics = sort_fn(data, metrics)
    elapsed = time.perf_counter() - start
    return ordered, metrics, elapsed


def _run_sort_case(kind: str, name: str, size: int, sort_fn: SortFn) -> tuple[float, float, float]:
    total_comparisons = 0
    total_swaps = 0
    total_time = 0.0
    for trial in range(T):
        rr = random.Random(size * 1000 + trial)
        data = generate_input(kind, size, rr)
        ordered, metrics, elapsed = _measure_sort_trial(sort_fn, data)
        total_time += elapsed
        if ordered != sorted(ordered):
            print("BROKEN", name)
        total_comparisons += metrics.comparisons
        total_swaps += metrics.swaps
    return total_comparisons / T, total_swaps / T, total_time / T


def run_sort_experiments() -> dict[str, tuple[float, float]]:
    results: dict[str, tuple[float, float]] = {}
    with open(OUTD + "/sort_counts.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["kind", "algorithm", "n", "avg_comparisons", "avg_swaps"])
        with open(OUTD + "/timings.csv", "w", newline="") as f2:
            w2 = csv.writer(f2)
            w2.writerow(["kind", "algorithm", "n", "seconds"])
            for kind in KINDS:
                for name, fn in SORT_ALGORITHMS:
                    for n in SIZES:
                        average_comparisons, average_swaps, average_time = _run_sort_case(kind, name, n, fn)
                        results[kind + "|" + name + "|" + str(n)] = (average_comparisons, average_swaps)
                        w.writerow([kind, name, n, round(average_comparisons, 1), round(average_swaps, 1)])
                        w2.writerow([kind, name, n, round(average_time, 6)])
    return results


def _build_search_targets(data: Sequence[int], rng: random.Random) -> list[float]:
    targets: list[float] = []
    for i in range(LOOK):
        if i % 2 == 0:
            targets.append(data[rng.randrange(len(data))])
        else:
            targets.append(rng.randrange(0, 10 * len(data)) + 0.5)
    return targets


def _run_search_case(size: int) -> tuple[float, float]:
    rr = random.Random(size)
    data = sorted(rr.sample(range(0, 10 * size), size))
    targets = _build_search_targets(data, rr)
    linear_probes = average_search_probes(linear_search, data, targets)
    binary_probes = average_search_probes(binary_search, data, targets)
    return linear_probes, binary_probes


def run_search_experiments() -> dict[int, tuple[float, float]]:
    search_results: dict[int, tuple[float, float]] = {}
    with open(OUTD + "/search_counts.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "linear_avg_probes", "binary_avg_probes"])
        for n in SIZES:
            linear_probes, binary_probes = _run_search_case(n)
            search_results[n] = (linear_probes, binary_probes)
            w.writerow([n, round(linear_probes, 2), round(binary_probes, 2)])
    return search_results


def _plot_series(x_values, y_values, *, title: str, x_label: str, y_label: str, labels: list[str], markers: list[str], output_path: str, log_x: bool = False, log_y: bool = False) -> None:
    plt.figure(figsize=(6, 4))
    for values, label, marker in zip(y_values, labels, markers):
        plt.plot(x_values, values, marker=marker, label=label)
    if log_x:
        plt.xscale("log")
    if log_y:
        plt.yscale("log")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=120)
    plt.close()


def plot_results(results: dict[str, tuple[float, float]], search_results: dict[int, tuple[float, float]]) -> None:
    if plt is None:
        return

    sort_series = [
        [results["random|" + name + "|" + str(n)][0] for n in SIZES]
        for name, _ in SORT_ALGORITHMS
    ]
    _plot_series(
        SIZES,
        sort_series,
        title="Sorting a random list",
        x_label="n",
        y_label="comparisons",
        labels=[name for name, _ in SORT_ALGORITHMS],
        markers=["o"] * len(sort_series),
        output_path=OUTD + "/sort_counts.png",
        log_x=True,
        log_y=True,
    )

    search_series = [
        [search_results[n][0] for n in SIZES],
        [search_results[n][1] for n in SIZES],
    ]
    _plot_series(
        SIZES,
        search_series,
        title="Searching a sorted list",
        x_label="n",
        y_label="probes per lookup",
        labels=["linear", "binary"],
        markers=["o", "s"],
        output_path=OUTD + "/search_probes.png",
    )


def ensure_output_directory() -> None:
    if not os.path.exists(OUTD):
        os.makedirs(OUTD)


def write_report_file(report_text: str) -> None:
    with open(OUTD + "/report.tex", "w") as f:
        f.write(report_text)


def compile_report_pdf() -> None:
    try:
        rc = subprocess.call(["pdflatex", "-interaction=nonstopmode", "-output-directory", OUTD, OUTD + "/report.tex"],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("pdflatex exit code", rc)
    except Exception:
        print("pdflatex not found; skipped the PDF (report.tex is still written)")


def main():
    ensure_output_directory()

    results = run_sort_experiments()
    search_results = run_search_experiments()
    plot_results(results, search_results)

    report_text = build_report(results, search_results)
    write_report_file(report_text)
    compile_report_pdf()
    print("done: " + str(len(results)) + " sort cells, " + str(len(search_results)) + " search rows -> " + OUTD)


SORT_ALGORITHMS: list[tuple[str, SortFn]] = [
    ("bubble", bubble_sort),
    ("bubbleearly", bubble_sort_early_exit),
    ("insertion", insertion_sort),
    ("selection", selection_sort),
    ("python", python_sort),
]

bs = bubble_sort
bs2 = bubble_sort_early_exit
ins = insertion_sort
sel = selection_sort
pysort = python_sort
lin = linear_search
binr = binary_search
go = main


if __name__ == "__main__":
    main()
