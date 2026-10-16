def format(seconds: int) -> str:
    result = []
    hours = seconds // 3600
    if hours:
        result.append(str(hours))
        seconds = seconds - hours * 3600

    minutes = seconds // 60
    if hours:
        result.append(str(minutes).rjust(2, "0"))
    else:
        result.append(str(minutes))
    seconds = seconds - minutes * 60
    if seconds:
        result.append(str(seconds).rjust(2, "0"))

    return ":".join(result)
