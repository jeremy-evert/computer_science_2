import tkinter as tk

from stock import toilet_paper

root = tk.Tk()
root.title("Toilet Paper Stock")

tk.Label(root, text=f"Toilet paper stock: {toilet_paper}", font=("Arial", 24)).pack(pady=12)

# A small grid makes each roll easy to count.
canvas = tk.Canvas(root, width=340, height=190, background="white")
canvas.pack(padx=12, pady=12)
columns = 5
for index in range(toilet_paper):
    row, column = divmod(index, columns)
    x, y = 30 + column * 62, 30 + row * 42
    canvas.create_oval(x, y, x + 38, y + 28, fill="white", outline="gray", width=2)
    canvas.create_oval(x + 13, y + 8, x + 25, y + 20, fill="white", outline="gray")

root.mainloop()
