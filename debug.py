import tkinter as tk

class DebugWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Debug Log")
        self.window.geometry("600x400")

        self.text_area = tk.Text(self.window, state="disabled")
        self.text_area.pack(expand=True, fill="both")

    def log(self, message):
        self.text_area.config(state="normal")
        self.text_area.insert("end", message + "\n")
        self.text_area.see("end")
        self.text_area.config(state="disabled")
