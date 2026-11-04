"""Early-exit bubble sort used by the refactored experiment."""

from typing import TypeVar

from src.metrics import OperationCounts


T = TypeVar("T")


def early_exit_bubble_sort(
    values: list[T], counts: OperationCounts | None = None
) -> list[T]:
    """Sort ``values`` in place and stop when a full pass makes no swaps.

    The list must contain values that can be compared with ``>``. Equal
    values keep their original order because swaps happen only when the left
    value is greater than the right value.
    """
    length = len(values)
    for pass_number in range(length):
        swapped = False
        for index in range(length - pass_number - 1):
            if counts is not None:
                counts.comparisons += 1
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True
                if counts is not None:
                    counts.swaps += 1

        if not swapped:
            break

    return values
