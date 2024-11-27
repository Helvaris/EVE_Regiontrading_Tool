import json
import os

CONFIG_FILE = "config.json"

def save_window_position(root):
    try:
        position = root.geometry()
        with open(CONFIG_FILE, "w") as f:
            json.dump({"window_position": position}, f)
    except Exception as e:
        print(f"Fehler beim Speichern der Fensterposition: {e}")

def restore_window_position(root):
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
            position = config.get("window_position")
            if position:
                root.geometry(position)
        except Exception as e:
            print(f"Fehler beim Wiederherstellen der Fensterposition: {e}")
