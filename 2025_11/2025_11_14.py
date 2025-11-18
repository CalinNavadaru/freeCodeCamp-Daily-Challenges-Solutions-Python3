import datetime


def days_until_weekend(date_string: str) -> str:
    day = datetime.date.fromisoformat(date_string).isoweekday()
    if day in [6, 7]:
        return "It's the weekend!"
    elif day == 5:
        return "1 day until the weekend."
    return f"{7 - day - 1} days until the weekend."
