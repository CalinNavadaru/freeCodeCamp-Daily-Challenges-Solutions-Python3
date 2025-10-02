def is_balanced(s):
    vowels = 0
    for i in range(0, len(s) // 2):
        if s[i] in "AEIOUaeiou":
            vowels += 1

    for i in range(len(s) // 2 + (len(s) % 2), len(s)):
        if s[i] in "AEIOUaeiou":
            vowels -= 1
    return vowels == 0