import datetime

DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


def get_weekday(date_string: str) -> str:
    day = datetime.date.fromisoformat(date_string).isoweekday()
    return DAYS[day]
