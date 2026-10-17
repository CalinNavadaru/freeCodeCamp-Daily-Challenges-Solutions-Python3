def string_sum(s: str) -> int:
    from re import findall
    match = findall(r"\d+", s)
    return sum(map(int, match))
