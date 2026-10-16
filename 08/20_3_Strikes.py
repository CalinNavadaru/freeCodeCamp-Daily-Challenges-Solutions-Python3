def squares_with_three(n):
    count = 0
    for i in range(1, n + 1):
        if "3" in str(i * i):
            count += 1
    return count
