"""Unit tests for deterministic input and experiment helpers."""

import random
import unittest

from annabell_beast.experiments import average_probes, make_input, make_search_targets
from annabell_beast.searching import linear_search


class ExperimentTests(unittest.TestCase):
    def test_make_input_is_seeded_and_orders_values_by_kind(self):
        random_values = make_input("random", 8, random.Random(17))
        self.assertEqual(random_values, make_input("random", 8, random.Random(17)))
        self.assertEqual(make_input("sorted", 8, random.Random(17)), sorted(random_values))
        self.assertEqual(
            make_input("reversed", 8, random.Random(17)),
            sorted(random_values, reverse=True),
        )

    def test_make_input_rejects_unknown_kind(self):
        with self.assertRaisesRegex(ValueError, "Unknown input kind"):
            make_input("sideways", 3, random.Random(1))

    def test_search_targets_have_even_present_and_absent_split(self):
        data = [0, 2, 4, 6]
        targets = make_search_targets(data, random.Random(4))

        self.assertEqual(len(targets), 200)
        self.assertTrue(all(target in data for target in targets[::2]))
        self.assertTrue(all(target not in data for target in targets[1::2]))

    def test_average_probes_counts_each_lookup(self):
        self.assertEqual(average_probes(linear_search, [2, 4, 6], [2, 6]), 2)

    def test_average_probes_rejects_empty_targets(self):
        with self.assertRaisesRegex(ValueError, "At least one"):
            average_probes(linear_search, [1], [])
