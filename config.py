import json

CONFIG_FILE = "config.json"

def save_window_position(root, table_data):
    try:
        position = {
            "geometry": root.geometry(),
            "table_data": table_data
        }
        with open(CONFIG_FILE, "w") as file:
            json.dump(position, file)
    except Exception as e:
        print(f"Error saving config: {e}")

def restore_window_position(root):
    try:
        with open(CONFIG_FILE, "r") as file:
            position = json.load(file)
            root.geometry(position.get("geometry", "800x600"))
            return position.get("table_data", [])
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error restoring config: {e}")
        return []
