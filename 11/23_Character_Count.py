import collections


def count_characters(sentence):
    c = collections.Counter(sentence.lower())
    return sorted([f"{key} {c[key]}" for key in c if key.isalpha()])
