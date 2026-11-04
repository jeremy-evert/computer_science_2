"""Plot generation and PNG resource validation checks."""

from pathlib import Path

import pytest

from src.data_collection import collect_search_measurements, collect_sort_measurements
from src.plot_output import inspect_png, plt, write_plots


pytestmark = pytest.mark.skipif(plt is None, reason="matplotlib is not installed")


def test_plot_files_are_valid_png_resources(tmp_path: Path) -> None:
    plots = write_plots(
        tmp_path,
        collect_sort_measurements(),
        collect_search_measurements(),
    )

    assert [path.name for path in plots] == ["sort_counts.png", "search_probes.png"]
    for plot in plots:
        info = inspect_png(plot)
        assert info.width == 720
        assert info.height == 480
        assert info.image_data_bytes > 0


def test_png_inspector_rejects_a_truncated_image(tmp_path: Path) -> None:
    truncated_png = tmp_path / "truncated.png"
    truncated_png.write_bytes(b"\x89PNG\r\n\x1a\n")

    with pytest.raises(ValueError, match="truncated"):
        inspect_png(truncated_png)
