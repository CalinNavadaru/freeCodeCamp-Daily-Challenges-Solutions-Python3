def to_binary(decimal):
    remainders = []
    while decimal:
        decimal, r = divmod(decimal, 2)
        remainders.append(r)

    return "".join(str(remainders[i]) for i in range(len(remainders) - 1, -1, -1))
