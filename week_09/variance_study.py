"""Week 9 variance study: how noisy is the bubble sort timer?

Stdlib only. Run:  python variance_study.py   (takes roughly 10-15 minutes)

Sorts the SAME list repeatedly at n = 5,000 / 10,000 / 30,000 so any spread in
the times is machine noise, not data variance. Writes
variance_study_results.json next to this file.
"""
import datetime
import json
import math
import os
import random
import time

from bubble_sort_benchmark import bubble_sort

SIZES = [5_000, 10_000, 30_000]
TRIALS = 20
NOTES = {
    5_000: "baseline; a short job, so fixed-size hiccups loom large",
    10_000: "medium; a few seconds per trial",
    30_000: "large; long job, hiccups should be a small fraction",
}


def repeated_bubble(n, trials=TRIALS, seed=42, progress=True):
    """Time bubble_sort on copies of ONE list, `trials` times."""
    rng = random.Random(seed)
    data = [rng.randint(0, n * 10) for _ in range(n)]
    times = []
    if progress:
        print(f"Running n={n:,} x{trials} trials...", end="", flush=True)
    for i in range(trials):
        start = time.perf_counter()
        bubble_sort(list(data))
        times.append(time.perf_counter() - start)
        if progress:
            if i == 0:
                print(f" (this takes about {times[0] * trials:.0f}s) ",
                      end="", flush=True)
            print(".", end="", flush=True)
    if progress:
        print(" done")
    return times


def stats(times):
    n = len(times)
    mean = sum(times) / n
    ordered = sorted(times)
    mid = n // 2
    median = ordered[mid] if n % 2 else (ordered[mid - 1] + ordered[mid]) / 2
    std = math.sqrt(sum((t - mean) ** 2 for t in times) / (n - 1))
    return {
        "times": times,
        "min": min(times),
        "max": max(times),
        "mean": mean,
        "median": median,
        "std_dev": std,
        "cv_pct": std / mean * 100,
        "range": max(times) - min(times),
        "fastest_trial": times.index(min(times)) + 1,
        "slowest_trial": times.index(max(times)) + 1,
    }


def print_block(n, s):
    print(f"=== VARIANCE STUDY: n={n:,} ({len(s['times'])} trials) ===")
    print(f"min:     {s['min']:.4f}s   trial #{s['fastest_trial']}")
    print(f"max:     {s['max']:.4f}s   trial #{s['slowest_trial']}")
    print(f"mean:    {s['mean']:.4f}s")
    print(f"median:  {s['median']:.4f}s")
    print(f"std dev: {s['std_dev']:.4f}s")
    print(f"CV:      {s['cv_pct']:.2f}%   <-- coefficient of variation")
    print(f"range:   {s['range']:.4f}s")
    print()
    for i, t in enumerate(s["times"], 1):
        print(f"trial {i}: {t:.4f}s")
    print()


def print_why():
    print("=== WHY THE NUMBERS LIE ===")
    print(
        "The operating system can pause a running sort at any moment to "
        "service a timer interrupt, a network packet, or an antivirus scan, "
        "and perf_counter() keeps counting while we are paused. A fixed-size "
        "interruption is a large fraction of a short job and a small "
        "fraction of a long one, so small n tends to show a HIGH coefficient "
        "of variation and large n a LOW one. The first trial may also run "
        "slower or faster than later ones because of CPU cache and branch "
        "predictor warm-up, and a long run of sorts can heat the chip until "
        "it lowers its clock speed, which makes later trials slower on "
        "identical data. Python's garbage collector can pause execution too, "
        "though bubble sort allocates almost nothing, so it is an unlikely "
        "culprit here. Other programs matter most of all: in our original "
        "benchmark the 20,000 to 30,000 row came out near 3.4x instead of "
        "the theoretical 2.25x because a pip install was running during that "
        "measurement and stealing CPU time, which is an extreme case of the "
        "same scheduling noise. This study cannot say which cause hit which "
        "trial; it only measures how big the spread is.")
    print()


def print_comparison(results):
    print("=== COMPARISON ===")
    print(f"{'n':>7} | {'mean (s)':>9} | {'CV%':>6} | interpretation")
    print(f"{'-' * 7}-+-{'-' * 9}-+-{'-' * 6}-+-{'-' * 40}")
    for n, s in results.items():
        print(f"{n:>7,} | {s['mean']:>9.4f} | {s['cv_pct']:>5.2f}% | "
              f"{NOTES[n]}")
    print()


def print_world_bible(results):
    hi = max(results, key=lambda n: results[n]["cv_pct"])
    lo = min(results, key=lambda n: results[n]["cv_pct"])
    print("=== WORLD BIBLE: VARIANCE STUDY ===")
    print("Adds: repeated timing of bubble sort, coefficient of variation, "
          "and a noise explanation.")
    print(f"Finding: highest CV at n={hi:,} ({results[hi]['cv_pct']:.2f}%), "
          f"lowest at n={lo:,} ({results[lo]['cv_pct']:.2f}%). "
          "Short jobs are expected to be noisier, because a fixed hiccup is "
          "a bigger share of them; compare the numbers above to that "
          "prediction.")
    print("Debt: this measured timer noise on one fixed list, not "
          "algorithmic variance; repeating with different seeds is a "
          "separate study.")


def main():
    stamp = datetime.datetime.now().isoformat()
    results = {}
    for n in SIZES:
        results[n] = stats(repeated_bubble(n))
        print_block(n, results[n])
    print_why()
    print_comparison(results)
    print_world_bible(results)

    payload = {
        "timestamp": stamp,
        "trials": TRIALS,
        "sizes": {str(n): {k: v for k, v in s.items()
                           if k in ("times", "min", "max", "mean", "median",
                                    "std_dev", "cv_pct")}
                  for n, s in results.items()},
    }
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "variance_study_results.json")
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)


if __name__ == "__main__":
    main()
