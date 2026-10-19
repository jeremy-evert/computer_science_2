"""The LEFT slide: the view owns the data. Try to test this without a window."""
import tkinter as tk

root = tk.Tk()
text = tk.StringVar(value="Items: 0")
tk.Label(root, textvariable=text).pack()
items = []   # view owns data


def on_restock():
    items.append("rope")
    n = len(items)
    text.set(f"Items: {n}")


tk.Button(root, text="Restock", command=on_restock).pack()

if __name__ == "__main__":
    root.mainloop()
