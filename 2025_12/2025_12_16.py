LOWER_VOWELS = "aeiou"


def has_consonant_count(text: str, target: int) -> bool:
    return sum(char.isalpha() and char.lower() not in LOWER_VOWELS for char in text) == target
