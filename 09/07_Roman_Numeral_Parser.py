SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def parse_roman_numeral(numeral):
    result = 0
    current_value = 0
    for i in range(0, len(numeral) - 1):
        roman_digit_value = SYMBOLS[numeral[i]]
        roman_next_digit_value = SYMBOLS[numeral[i + 1]]
        current_value += roman_digit_value

        if roman_digit_value != roman_next_digit_value:
            if roman_digit_value < roman_next_digit_value:
                result -= current_value

            else:
                result += current_value

            current_value = 0

    result += current_value
    result += SYMBOLS[numeral[-1]]
    return result
