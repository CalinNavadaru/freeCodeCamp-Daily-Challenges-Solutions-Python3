def shift_array(arr: list[int], n: int):
    if n < 0:
        n = len(arr) - abs(n)
    n %= len(arr)
    return [arr[(i + n) % len(arr)] for i in range(0, len(arr))]
