"""Week 11 optional micro-lab: benchmark sorting and searching on YOUR machine.

Plain Python, standard library only. Run from this folder:

    python benchmark.py                 # default sizes, writes results_<host>.csv
    python benchmark.py --quick         # small and fast (a few seconds)
    python benchmark.py --out mine.csv

Every row carries a platform fingerprint (OS, Python version, CPU count) so
results from different machines can be pooled and compared honestly.
Timing uses time.perf_counter(); each measurement is the best of several
repeats, which reduces (but does not remove) noise from other programs.
"""
import argparse
import bisect
import csv
import os
import platform
import random
import socket
import sys
import time

FIELDS = ["os", "os_release", "machine", "python", "implementation", "cpu_count",
          "algorithm", "kind", "ordering", "n", "repeats", "best_seconds"]
ORDERINGS = ("random", "sorted", "reversed")


def bubble_sort(data):
    items = list(data)
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return items


def insertion_sort(data):
    items = list(data)
    for i in range(1, len(items)):
        value, j = items[i], i - 1
        while j >= 0 and items[j] > value:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = value
    return items


def merge_sort(data):
    if len(data) <= 1:
        return list(data)
    mid = len(data) // 2
    left, right = merge_sort(data[:mid]), merge_sort(data[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged


def builtin_sort(data):
    return sorted(data)


def linear_search(items, key):
    for i, value in enumerate(items):
        if value == key:
            return i
    return -1


def binary_search(items, key):
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == key:
            return mid
        if items[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def library_binary_search(items, key):
    i = bisect.bisect_left(items, key)
    return i if i < len(items) and items[i] == key else -1


SORTS = {"bubble": bubble_sort, "insertion": insertion_sort,
         "merge": merge_sort, "builtin_sorted": builtin_sort}
SEARCHES = {"linear": linear_search, "binary": binary_search,
            "bisect_library": library_binary_search}
# Quadratic sorts get skipped above this size so nobody waits minutes.
QUADRATIC = {"bubble", "insertion"}
QUADRATIC_LIMIT = 5000


def make_data(n, ordering, rng):
    data = rng.sample(range(n * 4), n)
    if ordering == "sorted":
        data.sort()
    elif ordering == "reversed":
        data.sort(reverse=True)
    return data


def best_time(func, repeats):
    best = float("inf")
    for _ in range(repeats):
        start = time.perf_counter()
        func()
        best = min(best, time.perf_counter() - start)
    return best


def fingerprint():
    return {"os": platform.system(), "os_release": platform.release(),
            "machine": platform.machine(), "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "cpu_count": os.cpu_count()}


def run(sizes, repeats, seed=11):
    rng = random.Random(seed)
    base = fingerprint()
    rows = []
    for n in sizes:
        for ordering in ORDERINGS:
            data = make_data(n, ordering, rng)
            for name, func in SORTS.items():
                if name in QUADRATIC and n > QUADRATIC_LIMIT:
                    continue
                secs = best_time(lambda: func(data), repeats)
                rows.append({**base, "algorithm": name, "kind": "sort",
                             "ordering": ordering, "n": n, "repeats": repeats,
                             "best_seconds": f"{secs:.9f}"})
        # Search: a key at the very end (worst case for linear) in sorted data.
        ordered = sorted(make_data(n, "random", rng))
        key = ordered[-1]
        inner = max(1, 2000 // max(1, n // 1000)) if n else 1
        for name, func in SEARCHES.items():
            secs = best_time(lambda: [func(ordered, key) for _ in range(inner)], repeats) / inner
            rows.append({**base, "algorithm": name, "kind": "search",
                         "ordering": "sorted", "n": n, "repeats": repeats,
                         "best_seconds": f"{secs:.9f}"})
        print(f"n={n} done", file=sys.stderr)
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--quick", action="store_true", help="small sizes, few repeats")
    parser.add_argument("--out", help="CSV path (default results_<hostname>.csv)")
    args = parser.parse_args(argv)
    sizes = [100, 500, 1000, 2000] if args.quick else [100, 250, 500, 1000, 2000, 5000, 20000, 100000]
    repeats = 2 if args.quick else 3
    out = args.out or f"results_{socket.gethostname()}.csv"
    rows = run(sizes, repeats)
    with open(out, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
