import tkinter as tk
from tkinter import ttk

class Table:
    def __init__(self, parent, data):
        self.tree = ttk.Treeview(parent, columns=("ISK", "Prozent"), show="headings")
        self.tree.heading("ISK", text="ISK", command=lambda: self.sort_column("ISK", 0))
        self.tree.heading("Prozent", text="Prozent", command=lambda: self.sort_column("Prozent", 1))
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.data = data
        self.populate_table()

    def populate_table(self):
        for row in self.data:
            self.tree.insert("", "end", values=row)

    def sort_column(self, col, index):
        data = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        data.sort(reverse=False if index == 0 else True, key=lambda x: float(x[0].replace("'", "")))
        for index, (val, k) in enumerate(data):
            self.tree.move(k, "", index)
