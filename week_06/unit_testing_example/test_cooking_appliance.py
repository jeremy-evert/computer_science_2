import unittest

from cooking_appliance import Grill, Oven


class TestCookingAppliance(unittest.TestCase):

    def test_oven_bakes_bread(self):
        oven = Oven()

        result = oven.cook("bread")

        self.assertEqual(
            result,
            "The oven bakes the bread."
        )

    def test_grill_sears_bread(self):
        grill = Grill()

        result = grill.cook("bread")

        self.assertEqual(
            result,
            "The grill sears the bread."
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)