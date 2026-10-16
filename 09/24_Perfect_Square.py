import math


def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False

    return math.sqrt(n).is_integer()
