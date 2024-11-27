import pyperclip
from time import sleep
from utils import is_valid_number, calculate_value

def monitor_clipboard(thresholds, append_debug_log, input_label, output_label, threshold_label, root):
    last_clipboard_value = None
    while True:
        try:
            clipboard_content = pyperclip.paste()
            if clipboard_content == last_clipboard_value:
                sleep(1)
                continue

            last_clipboard_value = clipboard_content

            if not is_valid_number(clipboard_content):
                append_debug_log(f"Ungültiger Wert im Clipboard: '{clipboard_content}'")
                sleep(1)
                continue

            input_value = float(clipboard_content.replace(",", "").replace("'", ""))
            output_value, applied_threshold = calculate_value(input_value, thresholds)

            input_label.config(text=f"Eingabe: {format(input_value, ',.2f').replace(',', ' ')}")
            output_label.config(text=f"Ausgabe: {format(output_value, ',.2f').replace(',', ' ')}")
            threshold_label.config(text=f"Prozent: {applied_threshold}%")

            root.update_idletasks()
            root.update()

            append_debug_log(f"Berechnet: Eingabe={input_value}, Ausgabe={output_value}, Prozent={applied_threshold}")
            pyperclip.copy(f"{format(output_value, ',.2f').replace(',', ' ')}")

            sleep(1)

        except Exception as e:
            append_debug_log(f"Fehler: {str(e)}")
            sleep(1)
