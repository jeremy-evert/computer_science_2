"""Week 9: bubble sort vs merge sort vs Python's sort, and a Big O reality check.

Stdlib only. Run:  python bubble_sort_benchmark.py

Goal: find the biggest list bubble sort can finish inside a 2-minute budget.
The size list runs past 10,000; bubble sort is skipped once its next run is
projected (from the O(n^2) curve) to blow the budget, so the run stays bounded.
"""
import datetime
import json
import math
import os
import platform
import random
import time

SIZES = [100, 250, 500, 1000, 2500, 5000, 10000,
         20000, 30000, 40000, 50000, 60000, 80000]
BUDGET_SECONDS = 120.0


def bubble_sort(data):
    items = list(data)
    n = len(items)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return items


def merge_sort(data):
    if len(data) <= 1:
        return list(data)
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def python_sort(data):
    return sorted(data)


def timed(fn, data):
    start = time.perf_counter()
    result = fn(data)
    return result, time.perf_counter() - start


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


def run_assertions():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([]) == []
    assert merge_sort([7]) == [7]
    print("All assertions passed.")
    print()


def fmt(seconds):
    return "-" if seconds is None else f"{seconds:.4f}"


def benchmark():
    results = []  # (n, bubble_s | None, merge_s, python_s)
    bubble_halted = False
    halt_note = None
    last_bubble = None  # (n, seconds)

    for n in SIZES:
        rng = random.Random(42 + n)
        data = [rng.randint(0, n * 10) for _ in range(n)]
        expected, python_s = timed(python_sort, data)
        merged, merge_s = timed(merge_sort, data)
        assert merged == expected

        bubble_s = None
        if not bubble_halted:
            if last_bubble:
                projected = last_bubble[1] * (n / last_bubble[0]) ** 2
                if projected > BUDGET_SECONDS:
                    bubble_halted = True
                    halt_note = (f"Bubble sort halted: exceeded 2-minute budget "
                                 f"at n={n} (projected {projected:.0f}s from "
                                 f"n={last_bubble[0]}).")
            if not bubble_halted:
                bubbled, bubble_s = timed(bubble_sort, data)
                assert bubbled == expected
                last_bubble = (n, bubble_s)
                if bubble_s > BUDGET_SECONDS:
                    bubble_halted = True
                    halt_note = (f"Bubble sort halted: exceeded 2-minute budget "
                                 f"at n={n}.")
        results.append((n, bubble_s, merge_s, python_s))
        print(f"  done n={n}", flush=True)
    print()
    return results, halt_note


def print_table(results, halt_note):
    print("=== RESULTS TABLE ===")
    print(f"{'n':>7} | {'bubble (s)':>12} | {'merge (s)':>12} | "
          f"{'python (s)':>12} | {'bubble/python':>14}")
    print(f"{'-' * 7}-+-{'-' * 12}-+-{'-' * 12}-+-{'-' * 12}-+-{'-' * 14}")
    for n, b, m, p in results:
        ratio = "-" if b is None or p == 0 else f"{b / p:,.0f}x"
        print(f"{n:>7} | {fmt(b):>12} | {fmt(m):>12} | "
              f"{fmt(p):>12} | {ratio:>14}")
    print()
    if halt_note:
        print(halt_note)
        print()
    done = [(n, b) for n, b, _, _ in results if b is not None]
    biggest_n, biggest_t = done[-1]
    print(f"Biggest bubble sort that finished: n={biggest_n:,} "
          f"in {biggest_t:.1f}s.")
    print()


def print_reality_check(results):
    print("=== BIG O REALITY CHECK ===")
    print(f"{'n1 -> n2':>16} | {'actual bubble ratio':>20} | "
          f"{'theoretical n^2':>16} | {'actual merge ratio':>19} | "
          f"{'theoretical n log n':>20}")
    done = [r for r in results if r[1] is not None]
    for (n1, b1, m1, _), (n2, b2, m2, _) in zip(done, done[1:]):
        t_sq = (n2 / n1) ** 2
        t_nlogn = (n2 * math.log2(n2)) / (n1 * math.log2(n1))
        print(f"{f'{n1} -> {n2}':>16} | {b2 / b1:>20.2f} | {t_sq:>16.2f} | "
              f"{m2 / m1:>19.2f} | {t_nlogn:>20.2f}")
    print()


def print_summary():
    print("=== WHAT THIS TELLS US ===")
    print("Bubble sort compares adjacent pairs again and again, so doubling "
          "the list roughly quadruples the work; at tens of thousands of "
          "items that is minutes, not milliseconds.")
    print("The ratio table shows Big O is a real prediction: when n grows by "
          "some factor, bubble sort's measured time grows by about that "
          "factor squared, while merge sort grows only a little faster than "
          "linearly.")
    print("O(n^2) sorts are still fine for tiny lists, or for nearly sorted "
          "data where the early-exit check finishes after one pass.")
    print("Merge sort costs more code and extra memory for the merged lists, "
          "but it scales dramatically better; Python's built-in sort is "
          "faster still because it is written in C and exploits existing "
          "order.")
    print()


def print_world_bible(processor, cores, timestamp, results):
    done = [(n, b) for n, b, _, _ in results if b is not None]
    biggest_n, biggest_t = done[-1]
    print("=== WORLD BIBLE: WEEK 9 BUBBLE SORT EXTENSION ===")
    print("Adds: bubble sort benchmark and Big O reality check against merge "
          "sort and Python's sorted().")
    print(f"Hardware: {processor} | {cores} cores | Run: {timestamp}")
    print(f"Debt: bubble sort is impractical past ~{biggest_n:,} items on "
          f"this machine (n={biggest_n:,} took {biggest_t:.0f}s).")


def save_json(path, processor, cores, timestamp, results, halt_note):
    """Dump raw numbers so report.py can graph them without re-running."""
    payload = {
        "processor": processor,
        "cores": cores,
        "timestamp": timestamp,
        "budget_seconds": BUDGET_SECONDS,
        "halt_note": halt_note,
        "results": [{"n": n, "bubble": b, "merge": m, "python": p}
                    for n, b, m, p in results],
    }
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)


def main():
    processor, cores, timestamp = hardware_profile()
    run_assertions()
    results, halt_note = benchmark()
    save_json(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "bubble_sort_results.json"),
              processor, cores, timestamp, results, halt_note)
    print_table(results, halt_note)
    print_reality_check(results)
    print_summary()
    print_world_bible(processor, cores, timestamp, results)


if __name__ == "__main__":
    main()
