import pyperclip
from time import sleep
from utils import is_valid_number, calculate_value

def monitor_clipboard(thresholds, debug_var, input_label, output_label, threshold_label, active_tab, append_debug_log, root):
    last_clipboard_value = None

    while True:
        try:
            clipboard_content = pyperclip.paste()
            if clipboard_content == last_clipboard_value:
                sleep(1)
                continue

            last_clipboard_value = clipboard_content
            if not is_valid_number(clipboard_content):
                append_debug_log(f"Invalid clipboard value: {clipboard_content}")
                sleep(1)
                continue

            input_value = float(clipboard_content.replace(",", "").replace("'", ""))
            output_value, applied_threshold = calculate_value(input_value, thresholds)

            input_label.config(text=f"Eingabe: {input_value:,.2f}")
            output_label.config(text=f"Ausgabe: {output_value:,.2f}")
            threshold_label.config(text=f"Prozent: {applied_threshold}%")

            root.update_idletasks()
            pyperclip.copy(f"{output_value:,.2f}")
            append_debug_log(f"Clipboard updated with: {output_value:,.2f}")

            sleep(1)
        except Exception as e:
            append_debug_log(f"Error: {e}")
            sleep(1)
