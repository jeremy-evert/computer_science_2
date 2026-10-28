"""Measure sorting times and graph the results with Matplotlib."""

import random
from pathlib import Path

import matplotlib.pyplot as plt

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort
from sorting_timing import INPUT_SIZES, average_time


def main():
    # Keep the averages for each algorithm so they can be drawn as separate lines.
    bubble_times = []
    selection_times = []
    insertion_times = []

    for size in INPUT_SIZES:
        # All algorithms get the same randomly generated list at this size.
        numbers = [random.randint(1, 100) for _ in range(size)]

        # average_time makes three timed runs, using a fresh copy each time.
        bubble_times.append(average_time(bubble_sort, numbers))
        selection_times.append(average_time(selection_sort, numbers))
        insertion_times.append(average_time(insertion_sort, numbers))

    # Draw one line per sorting algorithm to compare their average times.
    plt.plot(INPUT_SIZES, bubble_times, marker="o", label="Bubble Sort")
    plt.plot(INPUT_SIZES, selection_times, marker="o", label="Selection Sort")
    plt.plot(INPUT_SIZES, insertion_times, marker="o", label="Insertion Sort")

    # Add labels and a legend so the graph is easy to understand.
    plt.title("Sorting Algorithm Performance Comparison")
    plt.xlabel("Input Size (number of elements)")
    plt.ylabel("Average Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save the image beside this Python file, then open the graph on screen.
    output_file = Path(__file__).with_name("sorting_comparison.png")
    plt.savefig(output_file)
    print(f"Graph saved as: {output_file}")
    plt.show()


if __name__ == "__main__":
    main()
