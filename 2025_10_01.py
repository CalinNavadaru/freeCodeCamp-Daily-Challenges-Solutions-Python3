def to_decimal(binary):
    return sum([int(value) * (2 ** (len(binary) - 1 - index)) for index, value in enumerate(binary)])
