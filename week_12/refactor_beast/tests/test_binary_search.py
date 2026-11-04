"""Tests for binary search."""

import unittest

from annabell_beast.models import OperationCounts
from annabell_beast.searching import binary_search


class BinarySearchTests(unittest.TestCase):
    def test_returns_matching_index_or_minus_one(self):
        for target, expected_index in ((1, 0), (5, 2), (9, 4), (6, -1)):
            with self.subTest(target=target):
                counts = OperationCounts()
                result = binary_search([1, 3, 5, 7, 9], target, counts)
                self.assertEqual(result, expected_index)
                self.assertGreater(counts.probes, 0)

    def test_counts_equality_and_order_checks_separately(self):
        counts = OperationCounts()
        self.assertEqual(binary_search([1, 3, 5], 4, counts), -1)
        self.assertEqual(counts.probes, 4)
