"""Correctness checks for the standalone insertion sort implementation."""

import pytest

from src.insertion_sort import insertion_sort


@pytest.mark.parametrize(
    "values",
    [
        [],
        [7],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [3, 1, 3, 2, 1],
        [-2, 5, 0, -7, 5],
    ],
    ids=["empty", "one-item", "already-sorted", "reverse-sorted", "duplicates", "negatives"],
)
def test_insertion_sort_sorts_in_place_and_returns_the_same_list(values: list[int]) -> None:
    expected = sorted(values)

    result = insertion_sort(values)

    assert values == expected
    assert result == expected
    assert result is values


def test_insertion_sort_keeps_equal_items_in_their_original_order() -> None:
    values = [(2, "first"), (1, "middle"), (2, "second")]

    insertion_sort(values)

    assert values == [(1, "middle"), (2, "first"), (2, "second")]
