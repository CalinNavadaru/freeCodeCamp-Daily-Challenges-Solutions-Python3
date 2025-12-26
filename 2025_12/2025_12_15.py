MILE_KM = 1.60934

def speed_check(speed_mph: float, speed_limit_kph: float) -> str:

    speed_kph = speed_mph * MILE_KM
    if speed_kph <= speed_limit_kph:
        return "Not Speeding"
    if speed_kph <= speed_limit_kph + 5:
        return "Warning"
    return "Ticket"