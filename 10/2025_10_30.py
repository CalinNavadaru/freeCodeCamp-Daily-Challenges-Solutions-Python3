import math


def check_prime(value: int) -> bool:
    if value < 2 or value % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(value)) + 1, 2):
        if value % i == 0:
            return False

    return True


def nth_prime(n: int) -> int:
    first_five = [2, 3, 5, 7, 11]
    if n <= 5:
        return first_five[n - 1]

    result = first_five[-1] + 2
    n -= 5
    while n:
        if check_prime(result):
            n -= 1
        result += 2

    return result - 2
