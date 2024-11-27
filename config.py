import json
import os

CONFIG_FILE = "config.json"

def save_window_position(root):
    position = {
        "x": root.winfo_x(),
        "y": root.winfo_y(),
        "width": root.winfo_width(),
        "height": root.winfo_height(),
    }
    with open(CONFIG_FILE, "w") as file:
        json.dump(position, file)

def restore_window_position(root):
    if not os.path.exists(CONFIG_FILE):
        return
    with open(CONFIG_FILE, "r") as file:
        position = json.load(file)
        root.geometry(f"{position['width']}x{position['height']}+{position['x']}+{position['y']}")
