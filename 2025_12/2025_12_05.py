def difference(arr1: list, arr2: list) -> list:
    s1 = set(arr1)
    s2 = set(arr2)
    r = [x for x in arr1 if x not in s2]
    for y in arr2:
        if y not in s1:
            r.append(y)
    return r