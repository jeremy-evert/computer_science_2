"""Linear search with an optional probe counter."""

from typing import TypeVar

from src.metrics import OperationCounts


T = TypeVar("T")


def linear_search(
    values: list[T], target: T, counts: OperationCounts | None = None
) -> int:
    """Return the first matching index, or ``-1`` when the target is absent."""
    for index, value in enumerate(values):
        if counts is not None:
            counts.probes += 1
        if value == target:
            return index
    return -1
