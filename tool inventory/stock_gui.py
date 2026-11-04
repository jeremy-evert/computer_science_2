import tkinter as tk
from stock import wrenches

root = tk.Tk()
root.title("Uncle Bob's Wrench Stock")

label = tk.Label(
    root,
    text=f"Pipe Wrench stock = {wrenches}",
    font=("Arial", 40)
)

label.pack(padx=20, pady=20)

root.mainloop()
