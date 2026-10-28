"""Week 11 story micro-lab: run the instrumented sorts, write counts + time to CSV.

    python count_and_time.py --quick
    python count_and_time.py --out story_mine.csv

Columns: platform fingerprint, algorithm, ordering, n, seven operation counters
(identical on every machine), and wall_seconds (best of repeats, measured on the
UNcounted version, different on every machine).
"""
import argparse
import csv
import random
import socket
import sys
import time

from benchmark import best_time, fingerprint, make_data
from instrumented import ALGORITHMS, COUNTER_FIELDS

FIELDS = (["os", "os_release", "machine", "python", "implementation", "cpu_count",
           "algorithm", "ordering", "n"] + COUNTER_FIELDS + ["wall_seconds"])
QUAD_SIZES = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000]
FAST_EXTRA = [5000, 10000, 20000, 50000]          # only the n log n sort goes this far
QUICK_SIZES = [10, 50, 200, 500]


def run(sizes, orderings, repeats, seed=11):
    rng = random.Random(seed)
    base = fingerprint()
    rows = []
    for ordering in orderings:
        for n in sizes:
            data = make_data(n, ordering, rng)
            for name, (counted, plain) in ALGORITHMS.items():
                if n > QUAD_SIZES[-1] and name != "merge":
                    continue
                result, counters = counted(data)
                assert result == sorted(data), name
                secs = best_time(lambda: plain(data), repeats)
                rows.append({**base, "algorithm": name, "ordering": ordering, "n": n,
                             **{k: counters.get(k, 0) for k in COUNTER_FIELDS},
                             "wall_seconds": f"{secs:.9f}"})
        print(f"{ordering} done", file=sys.stderr)
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--out")
    args = parser.parse_args(argv)
    sizes = QUICK_SIZES if args.quick else QUAD_SIZES + FAST_EXTRA
    orderings = ("random",) if args.quick else ("random", "sorted", "reversed")
    rows = run(sizes, orderings, 2 if args.quick else 3)
    out = args.out or f"story_{socket.gethostname()}.csv"
    with open(out, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader(); writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
