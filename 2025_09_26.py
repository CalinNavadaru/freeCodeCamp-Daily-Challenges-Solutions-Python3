def speeding(speeds, limit):
    sum_beyond_limit = 0
    count_beyond_limit = 0

    for speed in speeds:
        if speed > limit:
            count_beyond_limit += 1
            sum_beyond_limit += speed - limit
            
    return [count_beyond_limit, sum_beyond_limit / count_beyond_limit if count_beyond_limit else 0]
