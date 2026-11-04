"""Correctness checks for the standalone selection sort implementation."""

from dataclasses import dataclass

import pytest

from src.selection_sort import selection_sort


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
def test_selection_sort_sorts_in_place_and_returns_the_same_list(values: list[int]) -> None:
    expected = sorted(values)

    result = selection_sort(values)

    assert values == expected
    assert result == expected
    assert result is values


@dataclass
class Item:
    """An item ordered by key, with a label to track equal-key order."""

    key: int
    label: str

    def __lt__(self, other: "Item") -> bool:
        return self.key < other.key


def test_selection_sort_can_reorder_items_with_equal_keys() -> None:
    values = [Item(2, "first"), Item(2, "second"), Item(1, "smallest")]

    selection_sort(values)

    assert [item.key for item in values] == [1, 2, 2]
    assert [item.label for item in values] == ["smallest", "second", "first"]
