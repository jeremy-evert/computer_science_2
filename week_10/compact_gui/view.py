"""The view: one label, one button, one callback. Needs a window (tkinter)."""
import tkinter as tk
from inventory import Inventory

model, root = Inventory(), tk.Tk()
text = tk.StringVar(value="Items: 0")
tk.Label(root, textvariable=text).pack()


def on_restock():
    n = model.restock("rope")   # route to the model
    text.set(f"Items: {n}")     # then refresh the view


tk.Button(root, text="Restock", command=on_restock).pack()

if __name__ == "__main__":
    root.mainloop()
