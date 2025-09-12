def reverse_sentence(sentence):
    words = sentence.split(" ")
    return " ".join(x for x in words[::-1] if x)
