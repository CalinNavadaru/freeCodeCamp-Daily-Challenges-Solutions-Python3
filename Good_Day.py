def convert_to_minutes(time: str) -> int:
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


def get_greeting(s: str) -> str:
    time = convert_to_minutes(s)
    a = convert_to_minutes("05:00")
    b = convert_to_minutes("11:59")
    c = convert_to_minutes("12:00")
    d = convert_to_minutes("17:59")
    e = convert_to_minutes("18:00")
    f = convert_to_minutes("21:59")

    if a <= time <= b:
        return "Good morning"
    elif c <= time <= d:
        return "Good afternoon"
    elif e <= time <= f:
        return "Good evening"
    return "Good night"
