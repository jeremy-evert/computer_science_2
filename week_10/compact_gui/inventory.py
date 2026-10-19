"""The model. It knows nothing about windows."""


class Inventory:
    def __init__(self):
        self.items = []

    def restock(self, name):
        self.items.append(name)
        print(f"Restocked {name}. Total items: {len(self.items)}")
        print(f"Current inventory: {self.items}")
        return len(self.items)

    def count(self):
        print(f"Total items in inventory: {len(self.items)}")
        return len(self.items)
