def tribonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    if length <= 3:
        return start_sequence[0:length]
    length -= 3
    for i in range(length, 0, -1):
        s = sum(start_sequence[-1:-4:-1])
        start_sequence.append(s)
        print(s)
    return start_sequence

