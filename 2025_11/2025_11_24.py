def is_valid_message(message: str, validation: str) -> bool:
    words = message.split(" ")
    if len(words) != len(validation):
        return False

    for word, letter in zip(words, validation):
        if not word.lower().startswith(letter.lower()):
            return False
    return True
