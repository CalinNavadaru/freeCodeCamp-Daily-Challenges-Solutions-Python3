def gcd(x: int, y: int) -> int:
    while y:
        r = x % y
        x = y
        y = r
    return x
