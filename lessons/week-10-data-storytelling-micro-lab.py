"""Create the Week 10 Frontier Settlement visualization micro-lab output."""

import csv
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_PATH = SCRIPT_DIR / "data" / "frontier-resource-levels.csv"
OUTPUT_PATH = SCRIPT_DIR / "frontier-resource-levels.png"
FALLBACK_OUTPUT_PATH = SCRIPT_DIR / "frontier-resource-levels.svg"


def read_resource_levels(path):
    """Return resource labels and integer current levels from a small CSV."""
    with path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    return [row["resource"] for row in rows], [int(row["units"]) for row in rows]


def build_chart(labels, levels, output_path):
    """Write a zero-baseline comparison chart for the stated current-level question."""
    import matplotlib.pyplot as plt

    figure, axis = plt.subplots(figsize=(7, 4))
    bars = axis.bar(labels, levels, color="#4C78A8")
    axis.set_ylim(bottom=0)
    axis.set_ylabel("Current recorded units")
    axis.set_title("Water has the lowest recorded resource level")
    axis.bar_label(bars)
    figure.tight_layout()
    figure.savefig(output_path, dpi=150)


def build_svg_fallback(labels, levels, output_path):
    """Write a small zero-baseline SVG chart when Matplotlib is unavailable."""
    width, height, baseline = 700, 400, 330
    max_level = max(levels)
    bar_width, gap, left = 100, 45, 65
    bars = []
    for index, (label, level) in enumerate(zip(labels, levels)):
        bar_height = int(250 * level / max_level)
        x = left + index * (bar_width + gap)
        y = baseline - bar_height
        bars.append(
            '<rect x="{0}" y="{1}" width="{2}" height="{3}" fill="#4C78A8" />'
            '<text x="{4}" y="{5}" text-anchor="middle">{6}</text>'
            '<text x="{4}" y="{7}" text-anchor="middle">{8}</text>'.format(
                x, y, bar_width, bar_height, x + bar_width // 2, baseline + 20,
                label, y - 8, level
            )
        )
    output_path.write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}">'
        '<style>text {{ font-family: sans-serif; font-size: 13px; }}</style>'
        '<text x="350" y="32" text-anchor="middle" font-size="18px">'
        'Water has the lowest recorded resource level</text>'
        '<line x1="50" y1="{2}" x2="670" y2="{2}" stroke="black" />{3}'
        '<text x="20" y="80" transform="rotate(-90 20,80)">Current recorded units</text>'
        '</svg>'.format(width, height, baseline, ''.join(bars)),
        encoding="utf-8",
    )


if __name__ == "__main__":
    resource_labels, resource_levels = read_resource_levels(DATA_PATH)
    try:
        build_chart(resource_labels, resource_levels, OUTPUT_PATH)
        print("Wrote {} with Matplotlib".format(OUTPUT_PATH))
    except ImportError:
        build_svg_fallback(resource_labels, resource_levels, FALLBACK_OUTPUT_PATH)
        print("Matplotlib unavailable; wrote {} with the standard-library fallback".format(
            FALLBACK_OUTPUT_PATH
        ))
