import math

def combinations(cards: int) -> int:
    return math.factorial(52) // (math.factorial(cards) * math.factorial(52 - cards))