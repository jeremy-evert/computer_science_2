"""Plan B: the whole click trace with NO window. Same callback, no tkinter."""
from inventory import Inventory

model = Inventory()
label = {"text": "Items: 0"}   # stands in for the label


def on_restock():
    print("click -> callback")
    n = model.restock("rope")
    print(f"model.restock -> {n} items")
    label["text"] = f"Items: {n}"
    print("label updated")


if __name__ == "__main__":
    for _ in range(3):
        on_restock()
    print("label says:", label["text"])
