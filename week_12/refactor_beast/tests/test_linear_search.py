"""Tests for linear search."""

import unittest

from annabell_beast.models import OperationCounts
from annabell_beast.searching import linear_search


class LinearSearchTests(unittest.TestCase):
    def test_returns_matching_index_or_minus_one(self):
        for target, expected_index in ((1, 0), (5, 2), (9, 4), (6, -1)):
            with self.subTest(target=target):
                counts = OperationCounts()
                result = linear_search([1, 3, 5, 7, 9], target, counts)
                self.assertEqual(result, expected_index)
                self.assertGreater(counts.probes, 0)

    def test_empty_list_uses_no_probes(self):
        counts = OperationCounts()
        self.assertEqual(linear_search([], 1, counts), -1)
        self.assertEqual(counts.probes, 0)
