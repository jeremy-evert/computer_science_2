"""Binary search for sorted lists, with an optional probe counter."""

from typing import TypeVar

from src.metrics import OperationCounts


T = TypeVar("T")


def binary_search(
    values: list[T], target: T, counts: OperationCounts | None = None
) -> int:
    """Return a matching index, or ``-1`` when the target is absent.

    ``values`` must already be sorted. A probe counts each equality check and
    each less-than check separately, matching the original experiment.
    """
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if counts is not None:
            counts.probes += 1
        if values[middle] == target:
            return middle

        if counts is not None:
            counts.probes += 1
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
