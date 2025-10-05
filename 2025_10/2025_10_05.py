def get_reading_value(reading: str) -> int:
    if "0" <= reading <= "9":
        return int(reading)
    return 10 + ord(reading) - ord("A")


def has_exoplanet(readings: str) -> bool:
    readings_values = list(map(get_reading_value, readings))
    avg_value = sum(readings_values) / len(readings_values)
    return any(reading <= 0.8 * avg_value for reading in readings_values)
