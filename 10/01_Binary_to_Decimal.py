def to_decimal(binary: str) -> int:
    return sum([int(value) * (2 ** (len(binary) - 1 - index)) for index, value in enumerate(binary)])
