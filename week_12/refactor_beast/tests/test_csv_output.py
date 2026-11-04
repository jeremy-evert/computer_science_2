"""CSV output checks against the locked experiment baseline."""

import csv
import tempfile
from pathlib import Path

from src.csv_output import write_measurement_csvs
from src.data_collection import collect_search_measurements, collect_sort_measurements


BASELINE = Path(__file__).parents[1] / "baseline"


def test_count_csvs_match_the_locked_baseline_and_timings_are_written() -> None:
    sort_measurements = collect_sort_measurements()
    search_measurements = collect_search_measurements()

    with tempfile.TemporaryDirectory(dir=Path(__file__).parents[1]) as temporary_directory:
        output_directory = Path(temporary_directory)
        sort_path, timings_path, search_path = write_measurement_csvs(
            output_directory, sort_measurements, search_measurements
        )

        assert sort_path.read_bytes() == (BASELINE / "sort_counts.csv").read_bytes()
        assert search_path.read_bytes() == (BASELINE / "search_counts.csv").read_bytes()
        assert timings_path.exists()
        with timings_path.open(newline="", encoding="utf-8") as source:
            rows = list(csv.reader(source))
        assert rows[0] == ["kind", "algorithm", "n", "seconds"]
        assert len(rows) == len(sort_measurements) + 1
        assert all(float(row[3]) >= 0 for row in rows[1:])
