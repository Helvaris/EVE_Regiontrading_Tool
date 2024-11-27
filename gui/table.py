import tkinter as tk
from tkinter import ttk

class Table:
    def __init__(self, parent, data):
        self.tree = ttk.Treeview(parent, columns=("ISK", "Prozent"), show="headings")
        self.tree.heading("ISK", text="ISK")
        self.tree.heading("Prozent", text="Prozent")
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.data = data
        self.populate_table()

    def populate_table(self):
        for row in self.data:
            self.tree.insert("", "end", values=row)

    def add_row(self, row):
        self.tree.insert("", "end", values=row)
        self.data.append(row)

    def delete_selected(self):
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)
