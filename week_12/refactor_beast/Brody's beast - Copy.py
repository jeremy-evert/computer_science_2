# beast.py -- sorting & searching experiment report generator.
# Writes tables (csv), plots (png) and a LaTeX report into ./out
# Run:  python beast.py        (from this folder)
# NOTE from the previous maintainer: it works. Do not touch it.
import os, sys, random, csv, math, subprocess, time
from functools import cmp_to_key
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except Exception:
    plt = None

from dataclasses import dataclass


@dataclass
class SortMetrics:
    comparisons: int = 0
    swaps: int = 0


@dataclass
class SearchMetrics:
    probes: int = 0


SIZES = [10, 20, 40, 80, 160]
T = 5
LOOK = 200
OUTD = "out"
KINDS = ["random", "sorted", "reversed"]


def bs(a, metrics=None):
    has_metrics = metrics is not None
    if not has_metrics:
        metrics = SortMetrics()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            metrics.comparisons += 1
            if a[j] > a[j + 1]:
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t
                metrics.swaps += 1
    if has_metrics:
        return a, metrics
    return a


def bs2(a, metrics=None):
    # same as bs but quits early
    has_metrics = metrics is not None
    if not has_metrics:
        metrics = SortMetrics()
    n = len(a)
    for i in range(n):
        sw = 0
        for j in range(0, n - i - 1):
            metrics.comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                metrics.swaps += 1
                sw = 1
        if sw == 0:
            break
    if has_metrics:
        return a, metrics
    return a


def ins(a, metrics=None):
    has_metrics = metrics is not None
    if not has_metrics:
        metrics = SortMetrics()
    for i in range(1, len(a)):
        k = a[i]
        j = i - 1
        while j >= 0:
            metrics.comparisons += 1
            if a[j] > k:
                a[j + 1] = a[j]
                metrics.swaps += 1
                j -= 1
            else:
                break
        a[j + 1] = k
    if has_metrics:
        return a, metrics
    return a


def sel(a, metrics=None):
    has_metrics = metrics is not None
    if not has_metrics:
        metrics = SortMetrics()
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            metrics.comparisons += 1
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            metrics.swaps += 1
    if has_metrics:
        return a, metrics
    return a


def pysort(a, metrics=None):
    has_metrics = metrics is not None
    if not has_metrics:
        metrics = SortMetrics()

    def cmp(x, y):
        metrics.comparisons += 1
        return (x > y) - (x < y)

    a.sort(key=cmp_to_key(cmp))
    if has_metrics:
        return a, metrics
    return a


def lin(a, x, metrics=None):
    has_metrics = metrics is not None
    if not has_metrics:
        metrics = SearchMetrics()
    for i in range(len(a)):
        metrics.probes += 1
        if a[i] == x:
            if has_metrics:
                return i, metrics
            return i
    if has_metrics:
        return -1, metrics
    return -1


def binr(a, x, metrics=None):
    has_metrics = metrics is not None
    if not has_metrics:
        metrics = SearchMetrics()
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        metrics.probes += 1
        if a[mid] == x:
            if has_metrics:
                return mid, metrics
            return mid
        metrics.probes += 1
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    if has_metrics:
        return -1, metrics
    return -1


def go():
    global C, S, P, R
    if not os.path.exists(OUTD):
        os.makedirs(OUTD)
    algs = [("bubble", bs), ("bubbleearly", bs2), ("insertion", ins), ("selection", sel), ("python", pysort)]
    f = open(OUTD + "/sort_counts.csv", "w", newline="")
    w = csv.writer(f)
    w.writerow(["kind", "algorithm", "n", "avg_comparisons", "avg_swaps"])
    f2 = open(OUTD + "/timings.csv", "w", newline="")
    w2 = csv.writer(f2)
    w2.writerow(["kind", "algorithm", "n", "seconds"])
    for kind in KINDS:
        for name, fn in algs:
            for n in SIZES:
                tc = 0
                ts = 0
                tt = 0.0
                for t in range(T):
                    rr = random.Random(n * 1000 + t)
                    if kind == "random":
                        d = [rr.randint(0, 10 * n) for _ in range(n)]
                    elif kind == "sorted":
                        d = sorted([rr.randint(0, 10 * n) for _ in range(n)])
                    else:
                        d = sorted([rr.randint(0, 10 * n) for _ in range(n)], reverse=True)
                    C = 0
                    S = 0
                    t0 = time.perf_counter()
                    out = fn(d)
                    tt += time.perf_counter() - t0
                    if out != sorted(out):
                        print("BROKEN", name)
                    tc += C
                    ts += S
                R[kind + "|" + name + "|" + str(n)] = (tc / T, ts / T)
                w.writerow([kind, name, n, round(tc / T, 1), round(ts / T, 1)])
                w2.writerow([kind, name, n, round(tt / T, 6)])
    f.close()
    f2.close()

    f = open(OUTD + "/search_counts.csv", "w", newline="")
    w = csv.writer(f)
    w.writerow(["n", "linear_avg_probes", "binary_avg_probes"])
    SR = {}
    for n in SIZES:
        rr = random.Random(n)
        d = sorted(rr.sample(range(0, 10 * n), n))
        targets = []
        for i in range(LOOK):
            if i % 2 == 0:
                targets.append(d[rr.randrange(n)])
            else:
                targets.append(rr.randrange(0, 10 * n) + 0.5)
        P = 0
        for x in targets:
            lin(d, x)
        lp = P / LOOK
        P = 0
        for x in targets:
            binr(d, x)
        bp = P / LOOK
        SR[n] = (lp, bp)
        w.writerow([n, round(lp, 2), round(bp, 2)])
    f.close()

    if plt is not None:
        plt.figure(figsize=(6, 4))
        for name, fn in algs:
            ys = [R["random|" + name + "|" + str(n)][0] for n in SIZES]
            plt.plot(SIZES, ys, marker="o", label=name)
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("n")
        plt.ylabel("comparisons")
        plt.title("Sorting a random list")
        plt.legend()
        plt.tight_layout()
        plt.savefig(OUTD + "/sort_counts.png", dpi=120)
        plt.close()
        plt.figure(figsize=(6, 4))
        plt.plot(SIZES, [SR[n][0] for n in SIZES], marker="o", label="linear")
        plt.plot(SIZES, [SR[n][1] for n in SIZES], marker="s", label="binary")
        plt.xlabel("n")
        plt.ylabel("probes per lookup")
        plt.title("Searching a sorted list")
        plt.legend()
        plt.tight_layout()
        plt.savefig(OUTD + "/search_probes.png", dpi=120)
        plt.close()

    s = "\\documentclass{article}\n\\usepackage{graphicx}\n\\usepackage[margin=1in]{geometry}\n"
    s = s + "\\begin{document}\n\\title{Sorting and Searching: What the Counts Say}\n\\author{CS2}\n\\date{}\n\\maketitle\n"
    s = s + "\\section{Sorting}\nEach cell is the average of " + str(T) + " seeded trials. "
    s = s + "Lists of sizes " + ", ".join([str(n) for n in SIZES]) + ".\n"
    for kind in KINDS:
        s = s + "\\subsection{" + kind.capitalize() + " input}\n"
        s = s + "\\begin{tabular}{l" + "r" * (len(SIZES)) + "}\n\\hline\nalgorithm"
        for n in SIZES:
            s = s + " & " + str(n)
        s = s + " \\\\\n\\hline\n"
        for name, fn in algs:
            s = s + name
            for n in SIZES:
                v = R[kind + "|" + name + "|" + str(n)][0]
                if v == int(v):
                    s = s + " & " + str(int(v))
                else:
                    s = s + " & " + str(round(v, 1))
            s = s + " \\\\\n"
        s = s + "\\hline\n\\end{tabular}\n\n"
        best = None
        bv = 10 ** 12
        for name, fn in algs:
            v = R[kind + "|" + name + "|" + str(SIZES[-1])][0]
            if v < bv:
                bv = v
                best = name
        s = s + "At $n=" + str(SIZES[-1]) + "$ the fewest comparisons on " + kind + " input: \\textbf{" + best + "} (" + str(round(bv, 1)) + ").\n\n"
    s = s + "\\begin{figure}[h]\n\\centering\n\\IfFileExists{out/sort_counts.png}{\\includegraphics[width=0.7\\textwidth]{out/sort_counts.png}}{\\textit{(plot missing)}}\n\\caption{Comparisons, random input.}\n\\end{figure}\n"
    s = s + "\\section{Searching}\nAverage probes per lookup over " + str(LOOK) + " lookups (half present, half absent).\n\n"
    s = s + "\\begin{tabular}{rrr}\n\\hline\nn & linear & binary \\\\\n\\hline\n"
    for n in SIZES:
        s = s + str(n) + " & " + str(round(SR[n][0], 2)) + " & " + str(round(SR[n][1], 2)) + " \\\\\n"
    s = s + "\\hline\n\\end{tabular}\n\n"
    r = SR[SIZES[-1]][0] / SR[SIZES[-1]][1]
    s = s + "At $n=" + str(SIZES[-1]) + "$ binary search used about " + str(round(r, 1)) + " times fewer probes.\n"
    s = s + "\\begin{figure}[h]\n\\centering\n\\IfFileExists{out/search_probes.png}{\\includegraphics[width=0.7\\textwidth]{out/search_probes.png}}{\\textit{(plot missing)}}\n\\caption{Probes per lookup.}\n\\end{figure}\n"
    s = s + "\\end{document}\n"
    f = open(OUTD + "/report.tex", "w")
    f.write(s)
    f.close()

    try:
        rc = subprocess.call(["pdflatex", "-interaction=nonstopmode", "-output-directory", OUTD, OUTD + "/report.tex"],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("pdflatex exit code", rc)
    except Exception:
        print("pdflatex not found; skipped the PDF (report.tex is still written)")
    print("done: " + str(len(R)) + " sort cells, " + str(len(SR)) + " search rows -> " + OUTD)


if __name__ == "__main__":
    go()
