import re

KEYWORDS = {"have", "must", "are", "will", "can"}


def wise_speak(sentence: str) -> str:
    sentence = re.sub(r"([!.,?])", r" \1", sentence).lower().split(" ")
    first_part = []
    index_keyword = -1
    for index, word in enumerate(sentence):
        first_part.append(word)
        if word in KEYWORDS:
            index_keyword = index
            break
    result = sentence[index_keyword + 1: len(sentence) - 2] + [sentence[len(sentence) - 2] + ","] + first_part

    return " ".join(result).capitalize() + sentence[-1]
