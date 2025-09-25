def second_largest(arr):
    max_value = max(arr)
    second_max_value = min(arr)
    for i in range(0, len(arr)):
        if max_value > arr[i] > second_max_value:
            second_max_value = arr[i]

    return second_max_value
