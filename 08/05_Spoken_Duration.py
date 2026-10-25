def get_spoken_duration(seconds: int) -> str:
    time_hours = seconds // 3600
    seconds = seconds - time_hours * 3600
    time_minutes = seconds // 60
    seconds = seconds - time_minutes * 60

    result = []
    if time_hours:
        if time_hours == 1:
            result.append(f"{time_hours} hour")
        else:
            result.append(f"{time_hours} hours")
    if time_minutes:
        if time_minutes == 1:
            result.append(f"{time_minutes} minute")
        else:
            result.append(f"{time_minutes} minutes")
    if seconds:
        if seconds == 1:
            result.append(f"{seconds} second")
        else:
            result.append(f"{seconds} seconds")

    if len(result) == 1:
        return result[0]
    elif len(result) == 2:
        return result[0] + " and " + result[1]
    return result[0] + ", " + result[1] + " and " + result[2]