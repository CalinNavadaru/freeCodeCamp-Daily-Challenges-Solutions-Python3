import string


def is_pangram(sentence: str, letters: str) -> bool:
    sentence = sentence.lower()
    letters = letters.lower()
    missing_letters = set(string.ascii_lowercase) - set(letters)
    dict_letters = dict()
    for char in sentence:
        if char in missing_letters:
            return False

        dict_letters[char] = True

    return all(dict_letters.get(letter, False) for letter in letters)
