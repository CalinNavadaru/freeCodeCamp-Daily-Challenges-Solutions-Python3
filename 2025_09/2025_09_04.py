def repeat_vowels(s: str):
    vowels = "aeiouAEIOU"
    r = []
    reps = 0
    for char in s:
        r.append(char)
        if char in vowels:
            r.extend([char.lower()] * reps)
            reps += 1

    return "".join(x for x in r)
