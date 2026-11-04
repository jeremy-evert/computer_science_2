"""End-to-end checks for the refactored experiment entry point."""

from pathlib import Path

from src.main import run_experiment
from src.plot_output import inspect_png, plt


BASELINE = Path(__file__).parents[1] / "baseline"


def test_run_experiment_writes_baseline_outputs_and_valid_plots(
    monkeypatch, tmp_path: Path
) -> None:
    monkeypatch.setattr("src.main.compile_latex_pdf", lambda *_args: None)

    result = run_experiment(tmp_path / "out")

    output = result.output_directory
    assert (output / "sort_counts.csv").read_bytes() == (BASELINE / "sort_counts.csv").read_bytes()
    assert (output / "search_counts.csv").read_bytes() == (BASELINE / "search_counts.csv").read_bytes()
    assert result.report_path.read_text(encoding="utf-8") == (BASELINE / "report.tex").read_text(encoding="utf-8")
    assert result.pdf_exit_code is None

    if plt is not None:
        assert [path.name for path in result.plot_paths] == ["sort_counts.png", "search_probes.png"]
        for plot_path in result.plot_paths:
            image = inspect_png(plot_path)
            assert (image.width, image.height) == (720, 480)
    else:
        assert result.plot_paths == ()
