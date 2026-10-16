MONTHS_NAMES = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def format_date(date_string: str) -> str:
    month, day, year = date_string.split(" ")
    day = day[:-1].rjust(2, "0")
    value_month = str(MONTHS_NAMES[month]).rjust(2, "0")
    return f"{year}-{value_month}-{day}"
