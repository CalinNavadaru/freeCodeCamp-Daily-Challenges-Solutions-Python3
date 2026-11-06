def guess_number(secret: int, guess: int) -> str:
    if secret > guess:
        return "higher"
    elif secret < guess:
        return "lower"
    return "you got it!"
