def get_longest_word(sentence: str) -> str:
    pair_length = {word: len(word) for word in sentence.replace(".", "").split(" ")}

    return max(pair_length.items(), key=lambda k: k[1])[0]
