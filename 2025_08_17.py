def find_target(arr, target):
    d = dict()
    for index, val in enumerate(arr):
        if val not in d:
            d[target - val] = index
        else:
            return [d[val], index]
    return "Target not found"
