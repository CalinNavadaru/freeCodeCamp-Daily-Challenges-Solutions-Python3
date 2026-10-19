def calculate_handicap(scores: list[int], pars: list[int]) -> float:
    result = 0
    for score, par in zip(scores, pars):
        result += abs(score - par)

    return round(result / len(scores), 1)

print(calculate_handicap([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37]))