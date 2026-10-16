def one_hundred(chars: str) -> str:
    r = list(chars[:100])

    if len(r) != 100:
        for i in range(0, 100 - len(r)):
            r.append(chars[i % len(chars)])

    return "".join(r)
