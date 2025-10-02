def space_jam(s):
    a = [x.upper() for x in s.replace(" ", '')]
    return "  ".join(x for x in a)
