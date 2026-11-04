"""Bubble sort implementation used by the refactored experiment."""

from typing import TypeVar


T = TypeVar("T")


def bubble_sort(values: list[T]) -> list[T]:
    """Sort ``values`` in place with bubble sort and return the same list.

    The list must contain values that can be compared with ``>``. Equal
    values keep their original order because swaps happen only when the left
    value is greater than the right value.
    """
    length = len(values)
    for pass_number in range(length):
        for index in range(length - pass_number - 1):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
    return values
