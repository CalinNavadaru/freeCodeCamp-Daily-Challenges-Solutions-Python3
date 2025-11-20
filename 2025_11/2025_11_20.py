def get_stripped_word_length(word: str) -> tuple[int, str]:
    length = 0
    new_word = []
    for c in word:
        if c.isalpha():
            length += 1
            new_word.append(c)

    return length, "".join(new_word)


def longest_word(sentence: str) -> str:
    words = sentence.split(" ")
    max_length = -1
    max_word = ""
    for word in words:
        l, w = get_stripped_word_length(word)
        if l > max_length:
            max_length = l
            max_word = w
    return max_word
