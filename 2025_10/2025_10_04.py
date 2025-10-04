def classification(temp):
    if temp >= 30_000:
        return "O"

    if temp >= 10_000:
        return "B"

    if temp >= 7_500:
        return "A"

    if temp >= 6_000:
        return "F"

    if temp >= 5_200:
        return "G"

    if temp >= 3_700:
        return "K"

    return "M"
