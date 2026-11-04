"""Write collected experiment measurements to CSV files."""

import csv
from pathlib import Path
from typing import Iterable

from src.data_collection import SearchMeasurement, SortMeasurement


def write_measurement_csvs(
    output_directory: Path,
    sort_measurements: Iterable[SortMeasurement],
    search_measurements: Iterable[SearchMeasurement],
) -> tuple[Path, Path, Path]:
    """Write sort counts, timings, and search counts into ``output_directory``.

    The sort and search count files use the same columns, row order, and
    rounding as the original experiment. Timings are intentionally recorded
    separately because they vary from run to run.
    """
    output_directory.mkdir(parents=True, exist_ok=True)
    sort_counts_path = output_directory / "sort_counts.csv"
    timings_path = output_directory / "timings.csv"
    search_counts_path = output_directory / "search_counts.csv"

    with sort_counts_path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["kind", "algorithm", "n", "avg_comparisons", "avg_swaps"])
        for item in sort_measurements:
            writer.writerow(
                [
                    item.kind,
                    item.algorithm,
                    item.size,
                    round(item.average_comparisons, 1),
                    round(item.average_swaps, 1),
                ]
            )

    with timings_path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["kind", "algorithm", "n", "seconds"])
        for item in sort_measurements:
            writer.writerow(
                [item.kind, item.algorithm, item.size, round(item.average_seconds, 6)]
            )

    with search_counts_path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["n", "linear_avg_probes", "binary_avg_probes"])
        for item in search_measurements:
            writer.writerow(
                [
                    item.size,
                    round(item.linear_average_probes, 2),
                    round(item.binary_average_probes, 2),
                ]
            )

    return sort_counts_path, timings_path, search_counts_path
