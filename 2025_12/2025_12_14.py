def title_case(title: str) -> str:
    words = title.split(" ")

    return " ".join(word.capitalize() for word in words)
