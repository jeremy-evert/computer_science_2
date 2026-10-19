import unittest
from inventory import Inventory


class InventoryTest(unittest.TestCase):
    def test_restock_adds_one(self):
        inv = Inventory()
        self.assertEqual(inv.restock("rope"), 1)
        self.assertEqual(inv.count(), 1)

    def test_three_restocks(self):
        inv = Inventory()
        for _ in range(3):
            inv.restock("rope")
        self.assertEqual(inv.count(), 3)


if __name__ == "__main__":
    unittest.main()
