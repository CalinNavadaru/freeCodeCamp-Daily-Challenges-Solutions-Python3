def to_12(time: str) -> str:
    hour = int(time[0:2])
    minutes = int(time[2:])

    if hour == 0:
        return f"12:{minutes:0<2} AM"
    elif hour < 12:
        return f"{hour}:{minutes:0<2} AM"
    elif hour == 12:
        return f"12:{minutes:0<2} PM"

    return f"{hour - 12}:{minutes:0<2} PM"
