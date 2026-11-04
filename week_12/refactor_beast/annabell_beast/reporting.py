"""Plot and LaTeX report generation for the experiment."""

import os
import subprocess

from .config import INPUT_KINDS, LIST_SIZES, LOOKUPS_PER_SIZE, TRIALS
from .sorting import SORT_ALGORITHMS

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except Exception:
    plt = None


def plot_sort_counts(results, output_dir):
    """Save a log-log plot of sorting comparisons on random input."""
    if plt is None:
        return
    plt.figure(figsize=(6, 4))
    for algorithm_name in SORT_ALGORITHMS:
        comparisons = [
            results[("random", algorithm_name, size)].avg_comparisons
            for size in LIST_SIZES
        ]
        plt.plot(LIST_SIZES, comparisons, marker="o", label=algorithm_name)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("comparisons")
    plt.title("Sorting a random list")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "sort_counts.png"), dpi=120)
    plt.close()


def plot_search_probes(search_results, output_dir):
    """Save a plot of average probes per lookup."""
    if plt is None:
        return
    plt.figure(figsize=(6, 4))
    plt.plot(
        LIST_SIZES,
        [search_results[size].linear_avg_probes for size in LIST_SIZES],
        marker="o",
        label="linear",
    )
    plt.plot(
        LIST_SIZES,
        [search_results[size].binary_avg_probes for size in LIST_SIZES],
        marker="s",
        label="binary",
    )
    plt.xlabel("n")
    plt.ylabel("probes per lookup")
    plt.title("Searching a sorted list")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "search_probes.png"), dpi=120)
    plt.close()


def format_count(value):
    """Show whole numbers without decimals and other numbers to one decimal."""
    if value == int(value):
        return str(int(value))
    return str(round(value, 1))


def latex_text(value):
    """Escape underscores in labels inserted into ordinary LaTeX text."""
    return str(value).replace("_", r"\_")


def figure_block(output_dir, image_name, caption):
    """Return a LaTeX figure that shows a note if its image is missing."""
    image_path = os.path.join(output_dir, image_name).replace(os.sep, "/")
    return (
        "\\begin{figure}[h]\n\\centering\n"
        f"\\IfFileExists{{{image_path}}}"
        f"{{\\includegraphics[width=0.7\\textwidth]{{{image_path}}}}}"
        "{\\textit{(plot missing)}}\n"
        f"\\caption{{{caption}}}\n\\end{{figure}}\n"
    )


def sorting_table(results, kind):
    """Build a LaTeX table of average comparisons for one input kind."""
    latex = "\\begin{tabular}{l" + "r" * len(LIST_SIZES) + "}\n\\hline\nalgorithm"
    for size in LIST_SIZES:
        latex += f" & {size}"
    latex += " \\\\\n\\hline\n"
    for algorithm_name in SORT_ALGORITHMS:
        latex += latex_text(algorithm_name)
        for size in LIST_SIZES:
            comparisons = results[(kind, algorithm_name, size)].avg_comparisons
            latex += f" & {format_count(comparisons)}"
        latex += " \\\\\n"
    latex += "\\hline\n\\end{tabular}\n\n"
    return latex


def fewest_comparisons(results, kind, size):
    """Return the algorithm and count with fewest comparisons at this size."""
    return min(
        (
            (algorithm_name, results[(kind, algorithm_name, size)].avg_comparisons)
            for algorithm_name in SORT_ALGORITHMS
        ),
        key=lambda result: result[1],
    )


def sorting_section(results, output_dir):
    """Build the LaTeX sorting section."""
    largest_size = LIST_SIZES[-1]
    lines = [
        f"\\section{{Sorting}}\nEach cell is the average of {TRIALS} seeded trials. ",
        "Lists of sizes " + ", ".join(str(size) for size in LIST_SIZES) + ".\n",
    ]
    for kind in INPUT_KINDS:
        lines.append(f"\\subsection{{{kind.capitalize()} input}}\n")
        lines.append(sorting_table(results, kind))
        algorithm_name, comparison_count = fewest_comparisons(
            results, kind, largest_size
        )
        lines.append(
            f"At $n={largest_size}$ the fewest comparisons on {kind} input: "
            f"\\textbf{{{latex_text(algorithm_name)}}} "
            f"({round(comparison_count, 1)}).\n\n"
        )
    lines.append(figure_block(output_dir, "sort_counts.png", "Comparisons, random input."))
    return "".join(lines)


def searching_section(search_results, output_dir):
    """Build the LaTeX searching section."""
    largest_size = LIST_SIZES[-1]
    lines = [
        f"\\section{{Searching}}\nAverage probes per lookup over {LOOKUPS_PER_SIZE} "
        "lookups (half present, half absent).\n\n",
        "\\begin{tabular}{rrr}\n\\hline\nn & linear & binary \\\\\n\\hline\n",
    ]
    for size in LIST_SIZES:
        result = search_results[size]
        lines.append(
            f"{size} & {round(result.linear_avg_probes, 2)} & "
            f"{round(result.binary_avg_probes, 2)} \\\\\n"
        )
    lines.append("\\hline\n\\end{tabular}\n\n")
    speedup_ratio = (
        search_results[largest_size].linear_avg_probes
        / search_results[largest_size].binary_avg_probes
    )
    lines.append(
        f"At $n={largest_size}$ binary search used about "
        f"{round(speedup_ratio, 1)} times fewer probes.\n"
    )
    lines.append(figure_block(output_dir, "search_probes.png", "Probes per lookup."))
    return "".join(lines)


def build_report(results, search_results, output_dir):
    """Assemble the complete LaTeX report."""
    document_start = (
        "\\documentclass{article}\n\\usepackage{graphicx}\n"
        "\\usepackage[margin=1in]{geometry}\n"
        "\\begin{document}\n\\title{Sorting and Searching: What the Counts Say}\n"
        "\\author{CS2}\n\\date{}\n\\maketitle\n"
    )
    return (
        document_start
        + sorting_section(results, output_dir)
        + searching_section(search_results, output_dir)
        + "\\end{document}\n"
    )


def compile_pdf(tex_path, output_dir):
    """Run pdflatex when installed; the .tex report remains if it is absent."""
    try:
        exit_code = subprocess.call(
            ["pdflatex", "-interaction=nonstopmode", "-output-directory", output_dir, tex_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print("pdflatex exit code", exit_code)
    except OSError:
        print("pdflatex not found; skipped the PDF (report.tex is still written)")
