def convert_words(s: str) -> str:
    return " ".join(str(len(word)) for word in s.split(" "))