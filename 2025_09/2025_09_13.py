def find_missing_numbers(arr):
    s = set()
    n = -1
    r = []

    for val in arr:
        s.add(val)
        if val > n:
            n = val

    for i in range(1, n + 1):
        if i not in s:
            r.append(i)
    return r
