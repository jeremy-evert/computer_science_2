"""A third front end: the same Inventory model in the terminal. Press Enter to restock, q to quit."""
from inventory import Inventory

model = Inventory()
print("Items: 0")
while input("[Enter]=restock, q=quit: ").strip().lower() != "q":
    print(f"Items: {model.restock('rope')}")
