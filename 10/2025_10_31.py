def spookify(boo: str) -> str:
    r = []
    upper_case = 1
    for c in boo:
        if c.isalpha():
            r.append(c.upper() if upper_case else c.lower())
            upper_case = (1 - upper_case)
        elif c in "_-":
            r.append("~")
    return "".join(r)
