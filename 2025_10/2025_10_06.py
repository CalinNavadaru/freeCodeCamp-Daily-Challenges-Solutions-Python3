def send_message(route: list[int]) -> float:
    time_spent = 0.0
    for satellite in route:
        time_spent += satellite / 300_000
    return round(time_spent + 0.5 * (len(route) - 1), 4)
