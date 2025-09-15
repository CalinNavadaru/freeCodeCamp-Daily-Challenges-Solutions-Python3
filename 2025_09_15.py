def adjust_thermostat(temp, target):
    if temp < target:
        return "heat"
    if temp > target:
        return "cool"
    return "hold"


