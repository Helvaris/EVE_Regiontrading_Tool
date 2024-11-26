import tkinter as tk
from tkinter import ttk

class Table(ttk.Frame):
    def __init__(self, parent, save_callback):
        super().__init__(parent)
        self.save_callback = save_callback

        self.tree = ttk.Treeview(self, columns=("ISK", "Prozent"), show="headings")
        self.tree.heading("ISK", text="ISK", command=lambda: self.sort_column("ISK", 0))
        self.tree.heading("Prozent", text="Prozent", command=lambda: self.sort_column("Prozent", 1))
        self.tree.pack(expand=True, fill="both")

        self.add_button = tk.Button(self, text="Add Row", command=self.add_row)
        self.add_button.pack(side="left")

        self.delete_button = tk.Button(self, text="Delete Row", command=self.delete_row)
        self.delete_button.pack(side="left")

    def add_row(self):
        self.tree.insert("", "end", values=("0", "0%"))
        self.save_callback()

    def delete_row(self):
        selected_item = self.tree.selection()
        for item in selected_item:
            self.tree.delete(item)
        self.save_callback()

    def sort_column(self, col, col_index):
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children()]
        data.sort(reverse=False, key=lambda x: int(x[0].replace("'", "")) if col == "ISK" else int(x[0].replace("%", "")))
        for index, (_, child) in enumerate(data):
            self.tree.move(child, "", index)
