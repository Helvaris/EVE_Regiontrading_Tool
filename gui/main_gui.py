from tkinter import ttk, Toplevel
from config import restore_window_position, save_window_position
from .table import Table
from .debug import DebugWindow
from clipboard_monitor import monitor_clipboard
import threading

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EVE Region Trading Tool")
        restore_window_position(self.root)
        self.thresholds = []  # Schwellenwerte für Clipboard
        self.create_ui()
        self.debug_window = None
        self.debug_enabled = False

        # Starte Clipboard-Monitor in eigenem Thread
        threading.Thread(
            target=monitor_clipboard,
            args=(self.thresholds, self.append_debug_log, self.input_label, self.output_label, self.threshold_label, root),
            daemon=True
        ).start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_ui(self):
        self.input_label = ttk.Label(self.root, text="Eingabe: ---")
        self.input_label.pack()

        self.output_label = ttk.Label(self.root, text="Ausgabe: ---")
        self.output_label.pack()

        self.threshold_label = ttk.Label(self.root, text="Prozent: ---")
        self.threshold_label.pack()

        self.table = Table(self.root, self.thresholds)

        self.debug_checkbox = ttk.Checkbutton(self.root, text="Debug anzeigen", command=self.toggle_debug)
        self.debug_checkbox.pack()

    def toggle_debug(self):
        if not self.debug_window:
            self.debug_window = DebugWindow(self.root)
        self.debug_enabled = not self.debug_enabled

    def append_debug_log(self, message):
        if self.debug_window and self.debug_enabled:
            self.debug_window.append_log(message)

    def on_close(self):
        save_window_position(self.root)
        self.root.destroy()
