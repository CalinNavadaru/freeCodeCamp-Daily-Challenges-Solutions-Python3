def jbelmu(text):
    list_words = text.split(" ")

    for i in range(0, len(list_words)):
        if len(list_words[i]) > 2:
            list_words[i] = list_words[i][0] + "".join(sorted(list_words[i][1: len(list_words[i]) - 1])) + list_words[i][-1]

    return " ".join(x for x in list_words)


