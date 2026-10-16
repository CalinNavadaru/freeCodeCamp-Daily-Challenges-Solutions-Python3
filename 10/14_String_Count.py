def count(text: str, parameter: str) -> int:
    appearances = 0
    index = text.find(parameter)
    while index != -1:
        appearances += 1
        text = text[index + 1:]
        index = text.find(parameter)

    return appearances
