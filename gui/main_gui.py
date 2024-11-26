import tkinter as tk
from .table import Table
from config import save_window_position, restore_window_position
from clipboard_monitor import monitor_clipboard
from debug import DebugWindow

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EVE Trading Tool")
        self.debug_window = None
        self.create_ui()

    def create_ui(self):
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(side="top", fill="x")

        self.input_label = tk.Label(self.info_frame, text="Eingabe: 0.00")
        self.input_label.pack(side="left")

        self.output_label = tk.Label(self.info_frame, text="Ausgabe: 0.00")
        self.output_label.pack(side="left")

        self.threshold_label = tk.Label(self.info_frame, text="Prozent: 0")
        self.threshold_label.pack(side="left")

        self.debug_check = tk.Checkbutton(self.info_frame, text="Debug", command=self.toggle_debug)
        self.debug_check.pack(side="left")

        self.table = Table(self.root, self.save_table_data)
        self.table.pack(expand=True, fill="both")

    def save_table_data(self):
        data = self.table.get_data()
        save_window_position(self.root, data)

    def toggle_debug(self):
        if not self.debug_window:
            self.debug_window = DebugWindow(self.root)
        else:
            self.debug_window.window.destroy()
            self.debug_window = None

    def append_debug_log(self, message):
        if self.debug_window:
            self.debug_window.log(message)
