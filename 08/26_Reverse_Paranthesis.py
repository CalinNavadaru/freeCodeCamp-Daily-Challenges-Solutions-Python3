PARENTHESES = {"(", ")"}


def decode_aux(s: str) -> str:
    initial_string = []
    count = 0
    first_open_parentheses_index = -1
    for i in range(0, len(s)):
        if s[i] not in PARENTHESES and not count:
            initial_string.append(s[i])
        elif s[i] == "(":
            if not count:
                first_open_parentheses_index = i
            count += 1
        elif s[i] == ")":
            count -= 1
            if not count:
                initial_string.extend(decode_aux(s[first_open_parentheses_index + 1: i]))
    return "".join(c for c in initial_string[::-1])


def decode(s: str) -> str:
    return decode_aux(s)[::-1]
