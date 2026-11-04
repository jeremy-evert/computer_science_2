"""Correctness checks for the standalone early-exit bubble sort."""

import pytest

from src.early_exit_bubble_sort import early_exit_bubble_sort


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
def test_early_exit_bubble_sort_sorts_in_place_and_returns_the_same_list(
    values: list[int],
) -> None:
    expected = sorted(values)

    result = early_exit_bubble_sort(values)

    assert values == expected
    assert result == expected
    assert result is values


class ComparisonCountingInt:
    """Integer-like value that records how often bubble sort compares it."""

    comparisons = 0

    def __init__(self, value: int) -> None:
        self.value = value

    def __gt__(self, other: "ComparisonCountingInt") -> bool:
        type(self).comparisons += 1
        return self.value > other.value


def test_early_exit_bubble_sort_stops_after_one_pass_when_already_sorted() -> None:
    ComparisonCountingInt.comparisons = 0
    values = [ComparisonCountingInt(value) for value in [1, 2, 3, 4, 5]]

    early_exit_bubble_sort(values)

    assert [value.value for value in values] == [1, 2, 3, 4, 5]
    assert ComparisonCountingInt.comparisons == len(values) - 1
