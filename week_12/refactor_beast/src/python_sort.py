"""Python's built-in stable sort, exposed for the refactored experiment."""

from typing import TypeVar
from functools import cmp_to_key

from src.metrics import OperationCounts


T = TypeVar("T")


def python_sort(values: list[T], counts: OperationCounts | None = None) -> list[T]:
    """Sort ``values`` in place with Python's built-in sort and return it.

    Items must be mutually orderable. Python's sort is stable, so items with
    equal sort keys keep their original order.
    """
    if counts is None:
        values.sort()
    else:
        def compare(left: T, right: T) -> int:
            counts.comparisons += 1
            return (left > right) - (left < right)

        values.sort(key=cmp_to_key(compare))
    return values
