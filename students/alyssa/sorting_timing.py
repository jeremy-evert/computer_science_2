import time
import random

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort


INPUT_SIZES = [100, 500, 1_000, 2_000, 5_000]
REPEATS = 3


def average_time(sort_function, numbers):
    """Run one sorting function three times and return its average time."""
    total_time = 0.0

    for _ in range(REPEATS):
        # Each run gets a fresh copy of the same unsorted input list.
        numbers_copy = numbers.copy()

        # Start the clock, sort the copy, and then stop the clock.
        start_time = time.perf_counter()
        sort_function(numbers_copy)
        end_time = time.perf_counter()

        total_time += end_time - start_time

    return total_time / REPEATS


if __name__ == "__main__":
    # Keep each heading and its values in the same-width, right-aligned column.
    input_width = 12
    time_width = 24

    print("Sorting Algorithm Performance")
    print(
        f"{'Input Size':>{input_width}} | "
        f"{'Bubble Sort (seconds)':>{time_width}} | "
        f"{'Selection Sort (seconds)':>{time_width}} | "
        f"{'Insertion Sort (seconds)':>{time_width}}"
    )
    # Make a separator that matches the width of the table above.
    print("-" * (input_width + 3 * (time_width + 3)))

    for size in INPUT_SIZES:
        # Generate one random list for this size and reuse it for every algorithm.
        numbers = [random.randint(1, 100) for _ in range(size)]

        bubble_average = average_time(bubble_sort, numbers)
        selection_average = average_time(selection_sort, numbers)
        insertion_average = average_time(insertion_sort, numbers)

        print(
            f"{size:>{input_width}} | {bubble_average:>{time_width}.6f} | "
            f"{selection_average:>{time_width}.6f} | "
            f"{insertion_average:>{time_width}.6f}"
        )
