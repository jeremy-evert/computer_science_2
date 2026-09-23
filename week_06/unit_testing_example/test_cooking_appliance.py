import unittest

from cooking_appliance import Oven


class TestOven(unittest.TestCase):

    def test_oven_bakes_bread(self):
        oven = Oven()

        result = oven.cook("bread")

        self.assertEqual(
            result,
            "The oven bakes the bread."
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
