"""Tests for selection sort."""

import unittest

from annabell_beast.models import OperationCounts
from annabell_beast.sorting import selection_sort


class SelectionSortTests(unittest.TestCase):
    def test_selection_sort_sorts_in_place(self):
        for values in ([], [1], [3, 1, 2], [1, 2, 3], [3, 2, 1], [2, 1, 2, 1]):
            with self.subTest(values=values):
                items = values.copy()
                result = selection_sort(items, OperationCounts())
                self.assertIs(result, items)
                self.assertEqual(items, sorted(values))

    def test_counts_each_pair_comparison(self):
        counts = OperationCounts()
        selection_sort([3, 2, 1], counts)
        self.assertEqual(counts.comparisons, 3)
