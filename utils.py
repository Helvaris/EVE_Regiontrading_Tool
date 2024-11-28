def is_valid_number(value):
    try:
        float(value.replace(",", "").replace("'", ""))
        return True
    except ValueError:
        return False

def calculate_value(input_value, thresholds):
    if not thresholds:
        return input_value, 0
    for threshold in thresholds:
        if input_value >= threshold["ISK"]:
            return input_value * (1 + threshold["Prozent"] / 100), threshold["Prozent"]
    return input_value, 0
