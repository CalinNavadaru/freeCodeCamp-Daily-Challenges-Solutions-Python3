def celsius_to_fahrenheit(temp: float) -> float:
    return (temp * 1.8) + 32


def adjust_thermostat(current_f, target_c):
    target_f = celsius_to_fahrenheit(target_c)
    diff_f = target_f - current_f
    if diff_f > 0:
        return f"Heat: {round(diff_f, 1)} degrees Fahrenheit"
    if diff_f < 0:
        return f"Cool: {round(abs(diff_f), 1)} degrees Fahrenheit"
    return "Hold"
