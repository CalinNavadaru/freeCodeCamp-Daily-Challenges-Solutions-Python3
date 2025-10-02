def decode(message, shift):
    result = []
    for i in range(len(message)):
        new_char = message[i]
        if "a" <= message[i] <= "z":
            new_char = chr((ord(message[i]) - ord("a") - shift + 26) % 26 + ord("a"))

        elif "A" <= message[i] <= "Z":
            new_char = chr((ord(message[i]) - ord("A") - shift + 26) % 26 + ord("A"))
        result.append(new_char)
    r = "".join(x for x in result)
    print(r)
    return r
