"""The view for two items: two buttons, three labels, ONE model.

The model tracks both items. The view only shows what the model says.
"""
import tkinter as tk
from inventory_rope_and_shovel import Inventory   # CLASS (blueprint)

# ---- OBJECTS ----
model = Inventory()                  # ONE model object holds the count for BOTH items
root = tk.Tk()                       # the window
rope_text = tk.StringVar(value="Rope: 0")       # text the rope label watches
shovel_text = tk.StringVar(value="Shovel: 0")   # text the shovel label watches
total_text = tk.StringVar(value="Total: 0")     # text the total label watches

# ---- WIDGETS ----
tk.Label(root, textvariable=rope_text).pack()
tk.Label(root, textvariable=shovel_text).pack()
tk.Label(root, textvariable=total_text).pack()


# ---- THE PAIRINGS: two events, two handlers, one model ----
def refresh():
    """Ask the MODEL for every number, then show them. No rules here."""
    rope_text.set(f"Rope: {model.count('rope')}")
    shovel_text.set(f"Shovel: {model.count('shovel')}")
    total_text.set(f"Total: {model.total()}")


def on_restock_rope():
    model.restock("rope")            # 1. ROUTE the event to the model
    refresh()                        # 2. REFRESH the whole view


def on_restock_shovel():
    model.restock("shovel")          # same pattern, different item
    refresh()


tk.Button(root, text="Restock Rope", command=on_restock_rope).pack()       # PAIR 1
tk.Button(root, text="Restock Shovel", command=on_restock_shovel).pack()   # PAIR 2

if __name__ == "__main__":
    root.mainloop()
