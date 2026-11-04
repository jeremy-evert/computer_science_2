"""Coordinate a complete experiment run."""

import os

from .config import OUTPUT_DIR
from .experiments import run_search_experiments, run_sort_experiments
from .reporting import (
    build_report,
    compile_pdf,
    plot_search_probes,
    plot_sort_counts,
)


def main():
    """Run experiments, generate plots and report, then optionally compile PDF."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    sort_results = run_sort_experiments(OUTPUT_DIR)
    search_results = run_search_experiments(OUTPUT_DIR)

    plot_sort_counts(sort_results, OUTPUT_DIR)
    plot_search_probes(search_results, OUTPUT_DIR)

    report_path = os.path.join(OUTPUT_DIR, "report.tex")
    with open(report_path, "w") as report_file:
        report_file.write(build_report(sort_results, search_results, OUTPUT_DIR))
    compile_pdf(report_path, OUTPUT_DIR)

    print(
        f"done: {len(sort_results)} sort cells, "
        f"{len(search_results)} search rows -> {OUTPUT_DIR}"
    )
