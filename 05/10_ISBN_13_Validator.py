def is_valid_isbn_13(s: str) -> bool:

    s = s.replace("-", "")
    if 13 != len(s):
        return False

    r = 0
    t = 0
    for digit in s:
        if not digit.isdigit():
            return False
        r += int(digit) * (1 + 2 * t)
        t = 1 - t
    return r % 10 == 0