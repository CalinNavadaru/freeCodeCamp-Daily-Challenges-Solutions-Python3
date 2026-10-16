def adjust_thermostat(temp: float | int, target: float | int) -> str:
    if temp < target:
        return "heat"
    if temp > target:
        return "cool"
    return "hold"


