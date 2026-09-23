import unittest

from cooking_appliance import Grill, Oven, prepare_meal


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

    def test_oven_can_cook_pizza(self):
        oven = Oven()

        result = oven.can_cook("pizza")

        self.assertTrue(result)

    def test_grill_can_cook_burgers(self):
        grill = Grill()

        result = grill.can_cook("burgers")

        self.assertTrue(result)

    def test_grill_cannot_cook_cake(self):
        grill = Grill()

        result = grill.can_cook("cake")

        self.assertFalse(result)

    def test_grill_reports_direct_heat(self):
        grill = Grill()

        result = grill.cooking_method()

        self.assertEqual(
            result,
            "direct heat"
        )

    def test_prepare_meal_uses_each_appliances_cook_behavior(self):
        appliances = [
            Oven(),
            Grill(),
        ]

        results = [
            prepare_meal(appliance, "corn")
            for appliance in appliances
        ]

        self.assertEqual(
            results,
            [
                "The oven bakes the corn.",
                "The grill sears the corn.",
            ]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)