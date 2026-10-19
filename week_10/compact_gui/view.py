"""The view: one label, one button, one callback. Needs a window (tkinter). Every class and object is labeled.

Vocabulary:  CLASS = a blueprint (Inventory, tk.Tk, tk.Label ...)
             OBJECT = one thing built from a blueprint (model, root, label ...)
"""
import tkinter as tk
from inventory import Inventory      # Inventory is a CLASS (the blueprint, from inventory.py)

# ---- OBJECTS: each name on the left holds one thing built from the class on the right ----
model = Inventory()                  # OBJECT of class Inventory: owns the data and the rules
root = tk.Tk()                       # OBJECT of class Tk: the window itself
text = tk.StringVar(value="Items: 0")  # OBJECT of class StringVar: a text box the label watches

# ---- WIDGETS: objects that live inside the window ----
label = tk.Label(root, textvariable=text)   # OBJECT of class Label; shows whatever `text` holds
label.pack()                                # pack = put the label in the window

# ---- THE PAIRING: event -> handler -> model -> view ----
#   event    : the user clicks the Restock button
#   handler  : on_restock (a function, called by Tkinter when the click happens)
#   model    : model.restock(...) changes the data and returns the new count
#   view     : text.set(...) changes what the label shows
def on_restock():
    n = model.restock("shovel")        # 1. ROUTE the event to the model (the rules live there)
    text.set(f"Items: {n}")          # 2. REFRESH the view with the model's answer

button = tk.Button(root, text="Restock Shovel", command=on_restock)   # OBJECT of class Button
#   command=on_restock  <- THE PAIR: this button click is wired to this handler.
#   Note: on_restock has NO parentheses. We hand Tkinter the function to call later.
button.pack()

if __name__ == "__main__":
    root.mainloop()                  # wait for events forever; each click calls on_restock
