def all_unique(s):
    unique_chars = set()
    for char in s:
        if char in unique_chars:
            return False
        unique_chars.add(char)
    return True

