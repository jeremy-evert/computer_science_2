"""Deterministic input generation and measurement for the sorting experiment."""

import random
import time
from dataclasses import dataclass
from typing import Callable, Iterable, Literal

from src.binary_search import binary_search
from src.bubble_sort import bubble_sort
from src.early_exit_bubble_sort import early_exit_bubble_sort
from src.insertion_sort import insertion_sort
from src.linear_search import linear_search
from src.metrics import OperationCounts
from src.python_sort import python_sort
from src.selection_sort import selection_sort


InputKind = Literal["random", "sorted", "reversed"]
SortFunction = Callable[[list[int], OperationCounts | None], list[int]]

DEFAULT_SIZES = (10, 20, 40, 80, 160)
DEFAULT_KINDS: tuple[InputKind, ...] = ("random", "sorted", "reversed")
DEFAULT_TRIALS = 5
DEFAULT_LOOKUPS = 200

SORTS: tuple[tuple[str, SortFunction], ...] = (
    ("bubble", bubble_sort),
    ("bubbleearly", early_exit_bubble_sort),
    ("insertion", insertion_sort),
    ("selection", selection_sort),
    ("python", python_sort),
)


@dataclass(frozen=True)
class SortMeasurement:
    kind: InputKind
    algorithm: str
    size: int
    average_comparisons: float
    average_swaps: float
    average_seconds: float


@dataclass(frozen=True)
class SearchMeasurement:
    size: int
    linear_average_probes: float
    binary_average_probes: float


def make_sort_input(kind: InputKind, size: int, trial: int) -> list[int]:
    """Create the same seeded input for a kind, size, and trial every time."""
    if size < 0:
        raise ValueError("size must not be negative")
    if trial < 0:
        raise ValueError("trial must not be negative")
    if kind not in DEFAULT_KINDS:
        raise ValueError(f"unknown input kind: {kind}")

    rng = random.Random(size * 1000 + trial)
    values = [rng.randint(0, 10 * size) for _ in range(size)]
    if kind == "sorted":
        return sorted(values)
    if kind == "reversed":
        return sorted(values, reverse=True)
    return values


def make_search_data(size: int, lookups: int = DEFAULT_LOOKUPS) -> tuple[list[int], list[int | float]]:
    """Create one sorted search list and the experiment's hit/miss targets."""
    if size <= 0:
        raise ValueError("size must be positive")
    if lookups < 0:
        raise ValueError("lookups must not be negative")

    rng = random.Random(size)
    values = sorted(rng.sample(range(0, 10 * size), size))
    targets: list[int | float] = []
    for index in range(lookups):
        if index % 2 == 0:
            targets.append(values[rng.randrange(size)])
        else:
            targets.append(rng.randrange(0, 10 * size) + 0.5)
    return values, targets


def collect_sort_measurements(
    sizes: Iterable[int] = DEFAULT_SIZES,
    kinds: Iterable[InputKind] = DEFAULT_KINDS,
    trials: int = DEFAULT_TRIALS,
) -> list[SortMeasurement]:
    """Run every sort on seeded inputs and return its average operations/time."""
    if trials <= 0:
        raise ValueError("trials must be positive")
    sizes = tuple(sizes)
    kinds = tuple(kinds)

    results: list[SortMeasurement] = []
    for kind in kinds:
        for algorithm, sort_function in SORTS:
            for size in sizes:
                total_comparisons = 0
                total_swaps = 0
                total_seconds = 0.0
                for trial in range(trials):
                    values = make_sort_input(kind, size, trial)
                    counts = OperationCounts()
                    started = time.perf_counter()
                    sorted_values = sort_function(values, counts)
                    total_seconds += time.perf_counter() - started
                    if sorted_values != sorted(values):
                        raise AssertionError(f"{algorithm} failed to sort {kind} input of size {size}")
                    total_comparisons += counts.comparisons
                    total_swaps += counts.swaps

                results.append(
                    SortMeasurement(
                        kind=kind,
                        algorithm=algorithm,
                        size=size,
                        average_comparisons=total_comparisons / trials,
                        average_swaps=total_swaps / trials,
                        average_seconds=total_seconds / trials,
                    )
                )
    return results


def collect_search_measurements(
    sizes: Iterable[int] = DEFAULT_SIZES,
    lookups: int = DEFAULT_LOOKUPS,
) -> list[SearchMeasurement]:
    """Measure average linear and binary search probes for seeded lookups."""
    if lookups <= 0:
        raise ValueError("lookups must be positive")

    results: list[SearchMeasurement] = []
    for size in sizes:
        values, targets = make_search_data(size, lookups)
        linear_counts = OperationCounts()
        binary_counts = OperationCounts()
        for target in targets:
            linear_search(values, target, linear_counts)
        for target in targets:
            binary_search(values, target, binary_counts)
        results.append(
            SearchMeasurement(
                size=size,
                linear_average_probes=linear_counts.probes / lookups,
                binary_average_probes=binary_counts.probes / lookups,
            )
        )
    return results
