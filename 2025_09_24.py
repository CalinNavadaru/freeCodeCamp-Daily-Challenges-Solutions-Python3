import math


def is_perfect_square(n):
    if n < 0:
        return False

    sq_r = int(math.sqrt(n))

    return sq_r * sq_r == n
