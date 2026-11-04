"""LaTeX rendering and compiler wrapper regression checks."""

import subprocess
from pathlib import Path

from src.data_collection import collect_search_measurements, collect_sort_measurements
from src.latex_report import compile_latex_pdf, render_latex_report, write_latex_report


BASELINE = Path(__file__).parents[1] / "baseline" / "report.tex"


def test_rendered_report_matches_the_locked_baseline() -> None:
    rendered = render_latex_report(
        collect_sort_measurements(),
        collect_search_measurements(),
    )

    assert rendered == BASELINE.read_text(encoding="utf-8")


def test_write_report_creates_report_tex(tmp_path: Path) -> None:
    report_path = write_latex_report(
        tmp_path,
        collect_sort_measurements(),
        collect_search_measurements(),
    )

    assert report_path.name == "report.tex"
    assert report_path.read_text(encoding="utf-8") == BASELINE.read_text(encoding="utf-8")


def test_compile_latex_pdf_returns_compiler_exit_code(monkeypatch, tmp_path: Path) -> None:
    observed = {}

    def fake_run(command, **options):
        observed["command"] = command
        observed["options"] = options
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr("src.latex_report.subprocess.run", fake_run)

    result = compile_latex_pdf(tmp_path / "report.tex", tmp_path)

    assert result == 0
    assert observed["command"][0] == "pdflatex"
    assert observed["command"][1:3] == ["-interaction=nonstopmode", "-output-directory"]
    assert observed["options"]["check"] is False


def test_compile_latex_pdf_reports_missing_compiler(monkeypatch, tmp_path: Path) -> None:
    def missing_compiler(*_args, **_options):
        raise FileNotFoundError

    monkeypatch.setattr("src.latex_report.subprocess.run", missing_compiler)

    assert compile_latex_pdf(tmp_path / "report.tex", tmp_path) is None
