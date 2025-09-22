def digits_or_letters(s):
    digits = 0
    letters = 0
    for c in s:
        if "0" <= c <= "9":
            digits += 1
        elif "a" <= c.lower() <= "z":
            letters += 1

    if digits > letters:
        return "digits"
    if letters > digits:
        return "letters"
    return "tie"
