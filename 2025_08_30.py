from collections import Counter

def find_duplicates(arr):
    return list(sorted([key for key, value in Counter(arr).items() if value > 1]))



