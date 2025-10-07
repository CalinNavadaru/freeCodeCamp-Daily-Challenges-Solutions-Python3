def burn_candles(candles: int, leftovers_needed: int):
    count = 0
    leftovers = 0
    while candles:
        leftovers += candles
        count += candles
        candles, leftovers = divmod(leftovers, leftovers_needed)
    return count
