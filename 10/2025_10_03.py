import re


def check_strength(password):
    count = 0

    if len(password) >= 8:
        count += 1

    if re.findall(r"[a-z]", password) and re.findall(r"[A-Z]", password):
        count += 1

    if re.findall(r"[!@#$%^&*]", password):
        count += 1

    if re.findall(r"[0-9]", password):
        count += 1

    if count < 2:
        return "weak"
    if count in [2, 3]:
        return "medium"
    return "strong"
