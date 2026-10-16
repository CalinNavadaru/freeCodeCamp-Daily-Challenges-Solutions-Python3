VOWELS = "aeiouAEIOU"


def count(s: str) -> list[int]:
    c = 0
    v = 0
    for char in s:
        if char.lower() in VOWELS:
            v += 1
        elif char.isalpha():
            c += 1

    return [v, c]