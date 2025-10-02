def build_acronym(s):
    list_words = s.split(" ")
    special_words = {"a", "for", "an", "and", "by", "of"}
    result = [list_words[0][0].upper()]
    for index in range(1, len(list_words)):
        if not (list_words[index].lower() in special_words):
            result.append(list_words[index][0].upper())

    return "".join(result)