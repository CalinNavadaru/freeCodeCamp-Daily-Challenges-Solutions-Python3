def get_words(paragraph):
    freq = dict()
    paragraph = paragraph.lower()
    words = paragraph.split(" ")
    for word in words:
        word = word.strip(".,!")
        freq[word] = freq.get(word, 0) + 1

    return sorted(freq, key=lambda k: freq[k], reverse=True)[0:3]
