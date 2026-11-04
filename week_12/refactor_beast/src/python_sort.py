"""Python's built-in stable sort, exposed for the refactored experiment."""

from typing import TypeVar


T = TypeVar("T")


def python_sort(values: list[T]) -> list[T]:
    """Sort ``values`` in place with Python's built-in sort and return it.

    Items must be mutually orderable. Python's sort is stable, so items with
    equal sort keys keep their original order.
    """
    values.sort()
    return values
