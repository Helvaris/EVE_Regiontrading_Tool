import os
import tkinter as tk
from gui.main_gui import MainGUI

def main():
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()

if __name__ == "__main__":
    print(f"Current working directory: {os.getcwd()}")
    main()
