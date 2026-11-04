"""Tests for the counted built-in Python sort."""

import unittest

from annabell_beast.models import OperationCounts
from annabell_beast.sorting import python_sort_counted


class PythonSortTests(unittest.TestCase):
    def test_python_sort_sorts_in_place(self):
        for values in ([], [1], [3, 1, 2], [1, 2, 3], [3, 2, 1], [2, 1, 2, 1]):
            with self.subTest(values=values):
                items = values.copy()
                result = python_sort_counted(items, OperationCounts())
                self.assertIs(result, items)
                self.assertEqual(items, sorted(values))

    def test_counts_comparison_calls(self):
        counts = OperationCounts()
        python_sort_counted([3, 2, 1], counts)
        self.assertGreater(counts.comparisons, 0)
