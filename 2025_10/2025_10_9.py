import datetime


def moon_phase(date_string: str) -> str:
    data = date_string.split("-")

    year, month, day = int(data[0]), int(data[1]), int(data[2])
    current_date = datetime.date(year, month, day)
    reference_date = datetime.date(2000, 1, 6)
    diff_days = (current_date - reference_date).days

    remainder = diff_days % 28

    if 0 <= remainder <= 6:
        return "New"

    if 7 <= remainder <= 13:
        return "Waxing"

    if 14 <= remainder <= 20:
        return "Full"

    return "Waning"
