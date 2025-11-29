import datetime


def check_leap_year(year: int):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def calculate_age(birthday: str) -> int:
    days = (datetime.date.fromisoformat("2025-11-27") - datetime.date.fromisoformat(birthday)).days
    year = int(birthday.split("-")[0])

    age = 0
    for y in range(year, 2026):
        if check_leap_year(y):
            days -= 366
        else:
            days -= 365

        age += 1

        if days <= 365:
            break

    return age


print(calculate_age("2000-12-01"))
