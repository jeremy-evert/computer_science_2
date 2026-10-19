"""Same view with the trace prints. Click once, read the terminal."""
import tkinter as tk
from inventory import Inventory

model, root = Inventory(), tk.Tk()
text = tk.StringVar(value="Items: 0")
tk.Label(root, textvariable=text).pack()


def on_restock():
    print("click -> callback")
    n = model.restock("rope")
    print(f"model.restock -> {n} items")
    text.set(f"Items: {n}")
    print("label updated")


tk.Button(root, text="Restock", command=on_restock).pack()

if __name__ == "__main__":
    root.mainloop()
