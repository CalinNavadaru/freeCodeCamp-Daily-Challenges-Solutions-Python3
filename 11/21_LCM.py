def lcm(a: int, b: int) -> int:
    if a > b:
        a, b = b, a

    val_b = b
    while b % a != 0:
        b += val_b
    return b