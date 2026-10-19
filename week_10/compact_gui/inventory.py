"""The model. It knows nothing about windows."""


class Inventory:
    def __init__(self):
        self.items = []

    def restock(self, name):
        self.items.append(name)
        return len(self.items)

    def count(self):
        return len(self.items)
