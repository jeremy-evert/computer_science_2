"""Entry point that runs the refactored sorting and searching experiment."""

from dataclasses import dataclass
from pathlib import Path

from src.csv_output import write_measurement_csvs
from src.data_collection import (
    SearchMeasurement,
    SortMeasurement,
    collect_search_measurements,
    collect_sort_measurements,
)
from src.latex_report import compile_latex_pdf, write_latex_report
from src.plot_output import write_plots


@dataclass(frozen=True)
class ExperimentRun:
    """Files and measurements created by one complete experiment run."""

    output_directory: Path
    sort_measurements: tuple[SortMeasurement, ...]
    search_measurements: tuple[SearchMeasurement, ...]
    plot_paths: tuple[Path, ...]
    report_path: Path
    pdf_exit_code: int | None


def run_experiment(output_directory: Path = Path("out")) -> ExperimentRun:
    """Collect measurements, write CSVs and plots, and create the report/PDF."""
    sort_measurements = tuple(collect_sort_measurements())
    search_measurements = tuple(collect_search_measurements())

    write_measurement_csvs(output_directory, sort_measurements, search_measurements)
    plot_paths = write_plots(output_directory, sort_measurements, search_measurements)
    report_path = write_latex_report(output_directory, sort_measurements, search_measurements)
    pdf_exit_code = compile_latex_pdf(report_path, output_directory)

    return ExperimentRun(
        output_directory=output_directory,
        sort_measurements=sort_measurements,
        search_measurements=search_measurements,
        plot_paths=plot_paths,
        report_path=report_path,
        pdf_exit_code=pdf_exit_code,
    )


def main() -> ExperimentRun:
    """Run the default experiment and print a concise completion summary."""
    result = run_experiment()
    if result.pdf_exit_code is None:
        print("pdflatex not found; skipped the PDF (report.tex is still written)")
    else:
        print("pdflatex exit code", result.pdf_exit_code)
    print(
        "done: "
        + str(len(result.sort_measurements))
        + " sort cells, "
        + str(len(result.search_measurements))
        + " search rows -> "
        + str(result.output_directory)
    )
    return result


if __name__ == "__main__":
    main()
