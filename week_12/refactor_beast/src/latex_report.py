"""Build the LaTeX summary and optionally compile it to PDF."""

import subprocess
from pathlib import Path
from typing import Iterable

from src.data_collection import (
    DEFAULT_KINDS,
    DEFAULT_LOOKUPS,
    DEFAULT_TRIALS,
    SearchMeasurement,
    SortMeasurement,
    SORTS,
)


def render_latex_report(
    sort_measurements: Iterable[SortMeasurement],
    search_measurements: Iterable[SearchMeasurement],
    trials: int = DEFAULT_TRIALS,
    lookups: int = DEFAULT_LOOKUPS,
) -> str:
    """Render the experiment report with the same content as the baseline."""
    sort_measurements = tuple(sort_measurements)
    search_measurements = tuple(search_measurements)
    sizes = sorted({item.size for item in sort_measurements})
    search_sizes = sorted({item.size for item in search_measurements})
    if not sizes or not search_sizes:
        raise ValueError("sort and search measurements are required")

    sort_values = {
        (item.kind, item.algorithm, item.size): item.average_comparisons
        for item in sort_measurements
    }
    search_values = {
        item.size: (item.linear_average_probes, item.binary_average_probes)
        for item in search_measurements
    }

    report = "\\documentclass{article}\n\\usepackage{graphicx}\n\\usepackage[margin=1in]{geometry}\n"
    report += "\\begin{document}\n\\title{Sorting and Searching: What the Counts Say}\n\\author{CS2}\n\\date{}\n\\maketitle\n"
    report += "\\section{Sorting}\nEach cell is the average of " + str(trials) + " seeded trials. "
    report += "Lists of sizes " + ", ".join(str(size) for size in sizes) + ".\n"

    for kind in DEFAULT_KINDS:
        report += "\\subsection{" + kind.capitalize() + " input}\n"
        report += "\\begin{tabular}{l" + "r" * len(sizes) + "}\n\\hline\nalgorithm"
        for size in sizes:
            report += " & " + str(size)
        report += " \\\\\n\\hline\n"
        for algorithm, _ in SORTS:
            report += algorithm
            for size in sizes:
                value = sort_values[(kind, algorithm, size)]
                if value == int(value):
                    report += " & " + str(int(value))
                else:
                    report += " & " + str(round(value, 1))
            report += " \\\\\n"
        report += "\\hline\n\\end{tabular}\n\n"

        largest_size = sizes[-1]
        best_algorithm = min(
            (algorithm for algorithm, _ in SORTS),
            key=lambda algorithm: sort_values[(kind, algorithm, largest_size)],
        )
        best_value = sort_values[(kind, best_algorithm, largest_size)]
        report += (
            "At $n="
            + str(largest_size)
            + "$ the fewest comparisons on "
            + kind
            + " input: \\textbf{"
            + best_algorithm
            + "} ("
            + str(round(best_value, 1))
            + ").\n\n"
        )

    report += "\\begin{figure}[h]\n\\centering\n\\IfFileExists{out/sort_counts.png}{\\includegraphics[width=0.7\\textwidth]{out/sort_counts.png}}{\\textit{(plot missing)}}\n\\caption{Comparisons, random input.}\n\\end{figure}\n"
    report += "\\section{Searching}\nAverage probes per lookup over " + str(lookups) + " lookups (half present, half absent).\n\n"
    report += "\\begin{tabular}{rrr}\n\\hline\nn & linear & binary \\\\\n\\hline\n"
    for size in search_sizes:
        linear_probes, binary_probes = search_values[size]
        report += (
            str(size)
            + " & "
            + str(round(linear_probes, 2))
            + " & "
            + str(round(binary_probes, 2))
            + " \\\\\n"
        )
    report += "\\hline\n\\end{tabular}\n\n"
    largest_search_size = search_sizes[-1]
    linear_probes, binary_probes = search_values[largest_search_size]
    ratio = linear_probes / binary_probes
    report += (
        "At $n="
        + str(largest_search_size)
        + "$ binary search used about "
        + str(round(ratio, 1))
        + " times fewer probes.\n"
    )
    report += "\\begin{figure}[h]\n\\centering\n\\IfFileExists{out/search_probes.png}{\\includegraphics[width=0.7\\textwidth]{out/search_probes.png}}{\\textit{(plot missing)}}\n\\caption{Probes per lookup.}\n\\end{figure}\n"
    report += "\\end{document}\n"
    return report


def write_latex_report(
    output_directory: Path,
    sort_measurements: Iterable[SortMeasurement],
    search_measurements: Iterable[SearchMeasurement],
    trials: int = DEFAULT_TRIALS,
    lookups: int = DEFAULT_LOOKUPS,
) -> Path:
    """Write ``report.tex`` and return its path."""
    output_directory.mkdir(parents=True, exist_ok=True)
    report_path = output_directory / "report.tex"
    report_path.write_text(
        render_latex_report(sort_measurements, search_measurements, trials, lookups),
        encoding="utf-8",
    )
    return report_path


def compile_latex_pdf(
    report_path: Path,
    output_directory: Path,
    executable: str = "pdflatex",
) -> int | None:
    """Compile a LaTeX report; return its exit code or ``None`` if unavailable."""
    try:
        result = subprocess.run(
            [
                executable,
                "-interaction=nonstopmode",
                "-output-directory",
                str(output_directory),
                str(report_path),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except FileNotFoundError:
        return None
    return result.returncode
