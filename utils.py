def is_valid_number(value):
    try:
        float(value.replace(",", "").replace("'", ""))
        return True
    except ValueError:
        return False

def calculate_value(input_value, thresholds):
    for threshold in thresholds:
        if input_value >= threshold["ISK"]:
            return input_value + input_value * threshold["Prozent"] / 100, threshold["Prozent"]
    return input_value, 0