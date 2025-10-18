def sock_pairs(pairs: int, cycles: int) -> int:
    socks = 2 * pairs

    for cycle in range(1, cycles + 1):
        if cycle % 2 == 0 and socks > 0:
            socks -= 1
        if cycle % 3 == 0:
            socks += 1
        if cycle % 5 == 0 and socks > 0:
            socks -= 1
        if cycle % 10 == 0:
            socks += 2

    return socks // 2
