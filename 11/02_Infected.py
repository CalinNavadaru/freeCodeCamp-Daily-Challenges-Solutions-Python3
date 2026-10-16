def infected(days: int) -> int:
    infected_comp = 1
    for i in range(1, days + 1):
        infected_comp *= 2
        if i % 3 == 0:
            infected_comp = int(0.8 * infected_comp)
    return infected_comp
