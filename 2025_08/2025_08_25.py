import re

def to_camel_case(s):
    s = re.sub(r"[-_]", " ", s)
    list_words = s.split(" ")
    list_words[0] = list_words[0].lower()
    for i in range(1, len(list_words)):
        list_words[i] = list_words[i].capitalize()
    return "".join(word for word in list_words)
