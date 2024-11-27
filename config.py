import json
import os

CONFIG_FILE = "config.json"

def save_window_position(root):
    geometry = root.geometry().split("+")[0]  # Speichere nur Breite x Höhe
    with open("window_position.json", "w") as f:
        json.dump({"geometry": geometry}, f)

def restore_window_position(root):
    try:
        with open("window_position.json", "r") as f:
            config = json.load(f)
            geometry = config.get("geometry", "800x600")
            root.geometry(geometry)
    except Exception as e:
        print(f"Fehler beim Wiederherstellen der Fensterposition: {e}")
