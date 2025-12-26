import math

def sum_divisors(n: int) -> int:
    s = 1 + n
    sqrt_n = math.sqrt(n)
    for i in range(2, int(sqrt_n) + 1):
        if n % i == 0:
            s += i + (n // i)

    if sqrt_n.is_integer():
        s -= sqrt_n
    return s

print(sum_divisors(6))