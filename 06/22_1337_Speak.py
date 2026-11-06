leet_dictionary = {
    "a": "4",
    "e": "3",
    "g": "9",
    "i": "1",
    "l": "1",
    "o": "0",
    "s": "5",
    "t": "7",
}


def make_leet(s: str) -> str:
    return "".join([w if (w := leet_dictionary.get(c)) else c for c in s])
