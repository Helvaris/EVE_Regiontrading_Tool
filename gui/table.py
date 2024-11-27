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

    def add_row(self, isk, percent):
        self.tree.insert("", "end", values=(isk, percent))

    def delete_selected_row(self):
        selected_item = self.tree.selection()
        for item in selected_item:
            self.tree.delete(item)
