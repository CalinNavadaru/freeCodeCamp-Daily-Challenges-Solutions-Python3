def is_mirror(str1: str, str2: str) -> bool:
    i_str2 = len(str2) - 1
    for i in range(len(str1)):
        if not str1[i].isalpha():
            continue

        while i_str2 >= 0 and not str2[i_str2].isalpha():
            i_str2 -= 1

        if i_str2 < 0 or (str2[i_str2].isalpha() and str2[i_str2] != str1[i]):
            return False

        i_str2 -= 1

    return True
