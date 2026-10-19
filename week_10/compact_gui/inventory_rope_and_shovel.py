"""The model for two items. It still knows nothing about windows.

One dictionary tracks both: {"rope": 2, "shovel": 1}.
"""


class Inventory:
    def __init__(self):
        self.stock = {}                       # item name -> how many we have

    def restock(self, name):
        self.stock[name] = self.stock.get(name, 0) + 1
        print(f"Restocked {name}. {name}: {self.stock[name]}, total: {self.total()}")
        return self.stock[name]               # the count for THIS item

    def count(self, name):
        return self.stock.get(name, 0)        # one item's count (0 if never restocked)

    def total(self):
        return sum(self.stock.values())       # all items together
