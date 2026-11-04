"""Insertion sort implementation used by the refactored experiment."""

from typing import TypeVar


T = TypeVar("T")


def insertion_sort(values: list[T]) -> list[T]:
    """Sort ``values`` in place with insertion sort and return the same list.

    The list must contain values that can be compared with ``>``. Equal
    values keep their original order because an item moves left only past
    values that are strictly greater than it.
    """
    for index in range(1, len(values)):
        item = values[index]
        position = index - 1

        while position >= 0 and values[position] > item:
            values[position + 1] = values[position]
            position -= 1

        values[position + 1] = item

    return values
