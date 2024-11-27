import tkinter as tk
from gui.main_gui import MainGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
