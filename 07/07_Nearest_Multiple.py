def round_to_nearest_multiple(num: int, multiple: int) -> int:
    lower_multiple = (num // multiple) * multiple
    higher_multiple = (num // multiple + 1) * multiple
    if abs(lower_multiple - num) < abs(higher_multiple - num):
        return lower_multiple
    return higher_multiple
