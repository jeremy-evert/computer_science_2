"""Correctness and probe-count checks for the migrated searches."""

from src.binary_search import binary_search
from src.linear_search import linear_search
from src.metrics import OperationCounts


def test_linear_search_finds_a_value_and_counts_each_inspection() -> None:
    counts = OperationCounts()

    assert linear_search([4, 7, 9], 7, counts) == 1
    assert counts.probes == 2


def test_linear_search_returns_minus_one_for_a_missing_value() -> None:
    assert linear_search([4, 7, 9], 5) == -1


def test_binary_search_finds_a_value_and_counts_the_equality_probe() -> None:
    counts = OperationCounts()

    assert binary_search([1, 3, 5, 7, 9], 5, counts) == 2
    assert counts.probes == 1


def test_binary_search_returns_minus_one_for_a_missing_value() -> None:
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
