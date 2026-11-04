"""Tests for standard and early-exit bubble sort."""

import unittest

from annabell_beast.models import OperationCounts
from annabell_beast.sorting import bubble_sort, bubble_sort_early_exit


class BubbleSortTests(unittest.TestCase):
    def test_standard_bubble_sort_sorts_in_place(self):
        for values in ([], [1], [3, 1, 2], [1, 2, 3], [3, 2, 1], [2, 1, 2, 1]):
            with self.subTest(values=values):
                items = values.copy()
                result = bubble_sort(items, OperationCounts())
                self.assertIs(result, items)
                self.assertEqual(items, sorted(values))

    def test_early_exit_bubble_sort_sorts_in_place(self):
        items = [4, 1, 3, 2]
        result = bubble_sort_early_exit(items, OperationCounts())
        self.assertIs(result, items)
        self.assertEqual(items, [1, 2, 3, 4])

    def test_early_exit_stops_after_ordered_pass(self):
        counts = OperationCounts()
        bubble_sort_early_exit([1, 2, 3, 4], counts)
        self.assertEqual(counts.comparisons, 3)
        self.assertEqual(counts.swaps_or_shifts, 0)
