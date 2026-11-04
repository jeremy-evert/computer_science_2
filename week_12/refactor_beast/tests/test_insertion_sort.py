"""Tests for insertion sort."""

import unittest

from annabell_beast.models import OperationCounts
from annabell_beast.sorting import insertion_sort


class InsertionSortTests(unittest.TestCase):
    def test_insertion_sort_sorts_in_place(self):
        for values in ([], [1], [3, 1, 2], [1, 2, 3], [3, 2, 1], [2, 1, 2, 1]):
            with self.subTest(values=values):
                items = values.copy()
                result = insertion_sort(items, OperationCounts())
                self.assertIs(result, items)
                self.assertEqual(items, sorted(values))

    def test_counts_each_shift_as_a_move(self):
        counts = OperationCounts()
        insertion_sort([3, 2, 1], counts)
        self.assertEqual(counts.swaps_or_shifts, 3)
