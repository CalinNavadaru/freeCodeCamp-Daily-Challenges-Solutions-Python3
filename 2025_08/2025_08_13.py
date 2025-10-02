def fibonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    if length <= 2:
        return start_sequence[0: length]
    for i in range(2, length):
        start_sequence.append(start_sequence[i - 1] + start_sequence[i - 2])
    return start_sequence
