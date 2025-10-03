import re


def sum_digits(value: int) -> int:
    s = 0
    while value:
        value, digit = divmod(value, 10)
        s += digit

    return s


def is_spam(number: str) -> bool:
    groups = re.match(r"\+(\d+) \((\d\d\d)\) (\d\d\d)-(\d\d\d\d)", number)

    country_code = groups.group(1)
    area_code = groups.group(2)
    local_1 = groups.group(3)
    local_2 = groups.group(4)

    if len(country_code) > 2 or not country_code.startswith("0"):
        return True

    if not (200 <= int(area_code) <= 900):
        return True

    sum_local_1 = str(sum_digits(int(local_1)))

    if local_2.find(sum_local_1) != -1:
        return True

    formatted_number = country_code + area_code + local_1 + local_2

    for i in range(0, len(formatted_number) - 4):
        if all(formatted_number[j] == formatted_number[i] for j in range(i + 1, i + 4)):
            return True

    return False
