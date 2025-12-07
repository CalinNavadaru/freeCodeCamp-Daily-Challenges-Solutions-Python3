def compress_string(sentence: str) -> str:
    words = sentence.split(" ")
    r = [words[0]]
    counter = 1
    for i in range(1, len(words)):
        if words[i] == r[-1]:
            counter += 1
        else:
            if counter > 1:
                r[-1] = f"{r[-1]}({counter})"
            r.append(words[i])
            counter = 1

    if counter > 1:
        r[-1] = f"{r[-1]}({counter})"
    return " ".join(r)
