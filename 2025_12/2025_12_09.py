import collections


def most_frequent(arr: list) -> object:
    return collections.Counter(arr).most_common(1)[0][0]
