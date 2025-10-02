def array_diff(arr1, arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    r = []
    for e in arr2:
        if e not in s1:
            r.append(e)
    for e in arr1:
        if e not in s2:
            r.append(e)
    r.sort()
    return r
