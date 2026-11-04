"""Check deterministic experiment measurements against the locked baseline."""

import csv
from pathlib import Path

from src.data_collection import collect_search_measurements, collect_sort_measurements


BASELINE = Path(__file__).parents[1] / "baseline"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def test_sort_measurements_match_the_locked_baseline() -> None:
    expected = read_csv(BASELINE / "sort_counts.csv")
    measurements = collect_sort_measurements()
    actual = [
        {
            "kind": item.kind,
            "algorithm": item.algorithm,
            "n": str(item.size),
            "avg_comparisons": str(round(item.average_comparisons, 1)),
            "avg_swaps": str(round(item.average_swaps, 1)),
        }
        for item in measurements
    ]

    assert actual == expected


def test_search_measurements_match_the_locked_baseline() -> None:
    expected = read_csv(BASELINE / "search_counts.csv")
    measurements = collect_search_measurements()
    actual = [
        {
            "n": str(item.size),
            "linear_avg_probes": str(round(item.linear_average_probes, 2)),
            "binary_avg_probes": str(round(item.binary_average_probes, 2)),
        }
        for item in measurements
    ]

    assert actual == expected
