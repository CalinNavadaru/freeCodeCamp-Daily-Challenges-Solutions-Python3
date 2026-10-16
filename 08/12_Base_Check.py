** start of main.py **

def is_valid_number(n, base):
    n = n.upper()
    base_translation_dict = dict()

    for i in range(0, 10):
        base_translation_dict[str(i)] = i

    for i in range(10, 36):
        base_translation_dict[chr(ord("A") + i - 10)] = i

    for char in n:
        if base <= base_translation_dict[char]:
            return False

    return True

** end of main.py **

