def is_valid_number(value):
    try:
        float(value.replace(",", "").replace("'", ""))
        return True
    except ValueError:
        return False

def calculate_value(input_value, thresholds):
    thresholds = sorted(thresholds, key=lambda x: x["ISK"], reverse=True)
    for threshold in thresholds:
        if input_value >= threshold["ISK"]:
            percentage = threshold["Prozent"]
            return input_value + (input_value * percentage / 100), percentage
    return input_value, 0
