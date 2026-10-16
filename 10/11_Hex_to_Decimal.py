def hex_to_decimal(hex_value: str) -> int:
    hex_digits = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    decimal_result = 0
    hex_power = 1
    for i in range(len(hex_value) - 1, -1, -1):
        decimal_result += hex_power * hex_digits[hex_value[i]]
        hex_power *= 16

    return decimal_result