import tkinter as tk
from tkinter import ttk
from threading import Thread
from clipboard_monitor import monitor_clipboard
from config import save_window_position, restore_window_position

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EVE Trading Tool")
        restore_window_position(self.root)

        self.debug_logs = []
        self.create_ui()
        self.start_clipboard_monitor()

    def create_ui(self):
        self.input_label = tk.Label(self.root, text="Eingabe: ")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)
        self.output_label = tk.Label(self.root, text="Ausgabe: ")
        self.output_label.grid(row=0, column=1, padx=5, pady=5)
        self.threshold_label = tk.Label(self.root, text="Prozent: ")
        self.threshold_label.grid(row=0, column=2, padx=5, pady=5)

        self.debug_checkbox = tk.Checkbutton(self.root, text="Debug")
        self.debug_checkbox.grid(row=1, column=0, sticky="w")

        self.table = ttk.Treeview(self.root, columns=("ISK", "Prozent"), show="headings")
        self.table.heading("ISK", text="ISK")
        self.table.heading("Prozent", text="Prozent")
        self.table.grid(row=2, column=0, columnspan=3, sticky="nsew")

    def toggle_debug_window(self):
        if self.debug_window and self.debug_window.winfo_exists():
            self.debug_window.deiconify()
            return

        self.debug_window = tk.Toplevel(self.root)
        self.debug_window.title("Debug-Fenster")
        self.debug_window.geometry("600x400")
        self.debug_log = tk.Text(self.debug_window, state="disabled")
        self.debug_log.pack(fill=tk.BOTH, expand=True)

        def close_debug_window():
            self.debug_window.withdraw()  # Debug-Fenster nur verstecken

        self.debug_window.protocol("WM_DELETE_WINDOW", close_debug_window)

    def start_clipboard_monitor(self):
        thresholds = [
            {'ISK': 1.0, 'Prozent': 75},
            {'ISK': 2000000.0, 'Prozent': 70},
            {'ISK': 4000000.0, 'Prozent': 65},
            {'ISK': 8000000.0, 'Prozent': 60},
            {'ISK': 16000000.0, 'Prozent': 55},
            {'ISK': 32000000.0, 'Prozent': 50},
        ]
        Thread(
            target=monitor_clipboard,
            args=(
                thresholds,
                self.append_debug_log,
                self.input_label,
                self.output_label,
                self.threshold_label,
                self.root
            ),
            daemon=True
        ).start()

    def append_debug_log(self, message):
        self.debug_logs.append(message)
        print(message)

    def on_close(self):
        save_window_position(self.root)
        self.root.destroy()
