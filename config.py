import json
import os

CONFIG_FILE = "config.json"

def save_window_position(root, config_path="config.json"):
    try:
        geometry = root.geometry()
        with open(config_path, "r") as f:
            config = json.load(f)
        config["window_position"] = geometry
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except FileNotFoundError:
        # Erstelle neue Config-Datei, falls sie nicht existiert
        with open(config_path, "w") as f:
            json.dump({"window_position": geometry}, f, indent=4)
    except Exception as e:
        print(f"Fehler beim Speichern der Fensterposition: {e}")

def restore_window_position(root, config_path="config.json"):
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
            geometry = config.get("window_position", "800x600")
            root.geometry(geometry)
    except FileNotFoundError:
        print("Fensterposition nicht gefunden, Standardgröße wird verwendet.")
    except Exception as e:
        print(f"Fehler beim Wiederherstellen der Fensterposition: {e}")
