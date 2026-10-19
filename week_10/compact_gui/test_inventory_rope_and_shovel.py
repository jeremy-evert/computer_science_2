import unittest
from inventory_rope_and_shovel import Inventory


class TwoItemTest(unittest.TestCase):
    def test_items_are_tracked_separately(self):
        inv = Inventory()
        self.assertEqual(inv.restock("rope"), 1)
        self.assertEqual(inv.restock("rope"), 2)
        self.assertEqual(inv.restock("shovel"), 1)
        self.assertEqual(inv.count("rope"), 2)
        self.assertEqual(inv.count("shovel"), 1)

    def test_total_adds_both(self):
        inv = Inventory()
        inv.restock("rope")
        inv.restock("shovel")
        inv.restock("shovel")
        self.assertEqual(inv.total(), 3)

    def test_never_restocked_is_zero(self):
        self.assertEqual(Inventory().count("rope"), 0)


if __name__ == "__main__":
    unittest.main()
