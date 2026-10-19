def calculate_handicap(scores: list[int], pars: list[int]) -> float:
    result = 0
    for score, par in zip(scores, pars):
        result += abs(score - par)

    return round(result / len(scores), 1)
