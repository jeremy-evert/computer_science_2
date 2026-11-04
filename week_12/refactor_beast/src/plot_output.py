"""Create and validate the experiment's PNG plots."""

import struct
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from src.data_collection import SearchMeasurement, SortMeasurement

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


@dataclass(frozen=True)
class PngInfo:
    """Basic verified image metadata from a PNG resource."""

    width: int
    height: int
    image_data_bytes: int


def write_plots(
    output_directory: Path,
    sort_measurements: Iterable[SortMeasurement],
    search_measurements: Iterable[SearchMeasurement],
) -> tuple[Path, ...]:
    """Write the sort-comparison and search-probe plots.

    Returns the generated paths, or an empty tuple when matplotlib is not
    installed. The plot styling and dimensions match the original program.
    """
    if plt is None:
        return ()

    sort_measurements = tuple(sort_measurements)
    search_measurements = tuple(search_measurements)
    random_results = [item for item in sort_measurements if item.kind == "random"]
    algorithms = list(dict.fromkeys(item.algorithm for item in random_results))
    sizes = sorted({item.size for item in random_results})
    if not algorithms or not sizes:
        raise ValueError("random-input sort measurements are required to plot sorting results")
    if not search_measurements:
        raise ValueError("search measurements are required to plot search results")

    output_directory.mkdir(parents=True, exist_ok=True)
    sort_plot_path = output_directory / "sort_counts.png"
    search_plot_path = output_directory / "search_probes.png"

    plt.figure(figsize=(6, 4))
    for algorithm in algorithms:
        comparisons_by_size = {
            item.size: item.average_comparisons
            for item in random_results
            if item.algorithm == algorithm
        }
        if any(size not in comparisons_by_size for size in sizes):
            raise ValueError(f"incomplete random-input measurements for {algorithm}")
        plt.plot(
            sizes,
            [comparisons_by_size[size] for size in sizes],
            marker="o",
            label=algorithm,
        )
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("comparisons")
    plt.title("Sorting a random list")
    plt.legend()
    plt.tight_layout()
    plt.savefig(sort_plot_path, dpi=120)
    plt.close()

    search_measurements = tuple(sorted(search_measurements, key=lambda item: item.size))
    search_sizes = [item.size for item in search_measurements]
    plt.figure(figsize=(6, 4))
    plt.plot(
        search_sizes,
        [item.linear_average_probes for item in search_measurements],
        marker="o",
        label="linear",
    )
    plt.plot(
        search_sizes,
        [item.binary_average_probes for item in search_measurements],
        marker="s",
        label="binary",
    )
    plt.xlabel("n")
    plt.ylabel("probes per lookup")
    plt.title("Searching a sorted list")
    plt.legend()
    plt.tight_layout()
    plt.savefig(search_plot_path, dpi=120)
    plt.close()

    return sort_plot_path, search_plot_path


def inspect_png(path: Path) -> PngInfo:
    """Validate PNG chunk structure and return its dimensions and data size.

    This checks the image resource without comparing rendered pixels, which
    can vary slightly across matplotlib and font versions.
    """
    file_size = path.stat().st_size
    with path.open("rb") as image:
        if image.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
            raise ValueError(f"not a PNG file: {path}")

        width = height = 0
        image_data_bytes = 0
        saw_header = saw_end = False
        while not saw_end:
            chunk_header = image.read(8)
            if len(chunk_header) != 8:
                raise ValueError(f"truncated PNG chunk header: {path}")
            length, chunk_type = struct.unpack(">I4s", chunk_header)
            if image.tell() + length + 4 > file_size:
                raise ValueError(f"truncated PNG chunk data: {path}")
            data = image.read(length)
            checksum_bytes = image.read(4)
            checksum = struct.unpack(">I", checksum_bytes)[0]
            if zlib.crc32(chunk_type + data) & 0xFFFFFFFF != checksum:
                raise ValueError(f"invalid PNG chunk checksum: {path}")

            if chunk_type == b"IHDR":
                if saw_header or length != 13:
                    raise ValueError(f"invalid PNG header: {path}")
                width, height = struct.unpack(">II", data[:8])
                saw_header = True
            elif chunk_type == b"IDAT":
                if not saw_header:
                    raise ValueError(f"PNG image data appears before its header: {path}")
                image_data_bytes += length
            elif chunk_type == b"IEND":
                if length != 0:
                    raise ValueError(f"invalid PNG end chunk: {path}")
                saw_end = True

        if not saw_header or width <= 0 or height <= 0 or image_data_bytes == 0:
            raise ValueError(f"PNG is missing required image content: {path}")
        if image.read(1):
            raise ValueError(f"unexpected data after PNG end chunk: {path}")

    return PngInfo(width, height, image_data_bytes)
