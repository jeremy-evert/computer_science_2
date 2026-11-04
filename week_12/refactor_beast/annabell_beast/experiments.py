"""Input generation and repeated sorting/searching experiments."""

import csv
import os
import random
import time

from .config import INPUT_KINDS, LIST_SIZES, LOOKUPS_PER_SIZE, TRIALS, VALUE_RANGE_FACTOR
from .models import OperationCounts, SearchResult, SortResult
from .searching import binary_search, linear_search
from .sorting import SORT_ALGORITHMS


def make_input(kind, size, rng):
    """Build random, sorted, or reversed integer input of the requested size."""
    if kind not in INPUT_KINDS:
        raise ValueError(f"Unknown input kind: {kind!r}")
    values = [rng.randint(0, VALUE_RANGE_FACTOR * size) for _ in range(size)]
    if kind == "random":
        return values
    if kind == "sorted":
        return sorted(values)
    return sorted(values, reverse=True)


def run_sort_experiments(output_dir):
    """Run every sorting combination and write count and timing CSV files."""
    results = {}
    counts = OperationCounts()
    counts_path = os.path.join(output_dir, "sort_counts.csv")
    timings_path = os.path.join(output_dir, "timings.csv")

    with open(counts_path, "w", newline="") as counts_file, open(
        timings_path, "w", newline=""
    ) as timings_file:
        counts_writer = csv.writer(counts_file)
        counts_writer.writerow([
            "kind", "algorithm", "n", "avg_comparisons", "avg_swaps_or_shifts"
        ])
        timings_writer = csv.writer(timings_file)
        timings_writer.writerow(["kind", "algorithm", "n", "instrumented_seconds"])

        for kind in INPUT_KINDS:
            for algorithm_name, sort_function in SORT_ALGORITHMS.items():
                for size in LIST_SIZES:
                    total_comparisons = 0
                    total_swaps_or_shifts = 0
                    total_seconds = 0.0

                    for trial in range(TRIALS):
                        rng = random.Random(size * 1000 + trial)
                        values = make_input(kind, size, rng)
                        counts.reset()

                        start_time = time.perf_counter()
                        sorted_values = sort_function(values, counts)
                        total_seconds += time.perf_counter() - start_time

                        if sorted_values != sorted(sorted_values):
                            raise RuntimeError(
                                f"{algorithm_name} failed to sort a {kind} list "
                                f"of size {size}"
                            )

                        total_comparisons += counts.comparisons
                        total_swaps_or_shifts += counts.swaps_or_shifts

                    result = SortResult(
                        avg_comparisons=total_comparisons / TRIALS,
                        avg_swaps_or_shifts=total_swaps_or_shifts / TRIALS,
                        avg_seconds=total_seconds / TRIALS,
                    )
                    results[(kind, algorithm_name, size)] = result
                    counts_writer.writerow([
                        kind,
                        algorithm_name,
                        size,
                        round(result.avg_comparisons, 1),
                        round(result.avg_swaps_or_shifts, 1),
                    ])
                    timings_writer.writerow([
                        kind, algorithm_name, size, round(result.avg_seconds, 6)
                    ])

    return results


def make_search_targets(data, rng):
    """Make half present targets and half absent half-integers."""
    if not data:
        raise ValueError("Search data must not be empty")
    targets = []
    for lookup_index in range(LOOKUPS_PER_SIZE):
        if lookup_index % 2 == 0:
            targets.append(data[rng.randrange(len(data))])
        else:
            upper_bound = VALUE_RANGE_FACTOR * len(data)
            targets.append(rng.randrange(upper_bound) + 0.5)
    return targets


def average_probes(search_function, data, targets):
    """Return average probes per lookup for the supplied targets."""
    if not targets:
        raise ValueError("At least one search target is required")
    counts = OperationCounts()
    for target in targets:
        search_function(data, target, counts)
    return counts.probes / len(targets)


def run_search_experiments(output_dir):
    """Compare linear and binary search and write their average probes to CSV."""
    search_results = {}
    search_path = os.path.join(output_dir, "search_counts.csv")

    with open(search_path, "w", newline="") as search_file:
        writer = csv.writer(search_file)
        writer.writerow(["n", "linear_avg_probes", "binary_avg_probes"])

        for size in LIST_SIZES:
            rng = random.Random(size)
            values = sorted(rng.sample(range(VALUE_RANGE_FACTOR * size), size))
            targets = make_search_targets(values, rng)
            result = SearchResult(
                linear_avg_probes=average_probes(linear_search, values, targets),
                binary_avg_probes=average_probes(binary_search, values, targets),
            )
            search_results[size] = result
            writer.writerow([
                size,
                round(result.linear_avg_probes, 2),
                round(result.binary_avg_probes, 2),
            ])

    return search_results
