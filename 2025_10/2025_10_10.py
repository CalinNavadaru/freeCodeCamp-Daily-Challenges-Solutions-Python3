def launch_fuel(payload: int) -> float:
    current_fuel_added = payload / 5
    result = current_fuel_added

    while current_fuel_added >= 1:
        current_fuel_added = current_fuel_added / 5
        result += current_fuel_added
    return round(result, 1)
