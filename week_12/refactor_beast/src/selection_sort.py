"""Selection sort implementation used by the refactored experiment."""

from typing import TypeVar

from src.metrics import OperationCounts


T = TypeVar("T")


def selection_sort(values: list[T], counts: OperationCounts | None = None) -> list[T]:
    """Sort ``values`` in place with selection sort and return the same list.

    The list must contain values that can be compared with ``<``. This
    swap-based version is not stable: selecting a later minimum can move an
    item past an earlier item with an equal key.
    """
    length = len(values)
    for start in range(length):
        minimum = start
        for index in range(start + 1, length):
            if counts is not None:
                counts.comparisons += 1
            if values[index] < values[minimum]:
                minimum = index

        if minimum != start:
            values[start], values[minimum] = values[minimum], values[start]
            if counts is not None:
                counts.swaps += 1

    return values
