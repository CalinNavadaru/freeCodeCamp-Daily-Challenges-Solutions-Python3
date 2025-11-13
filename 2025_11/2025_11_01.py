def compute_sum(message: str) -> int:
    sum_message = 0
    for char in message:
        if char.isalpha():
            if char.islower():
                sum_message += ord(char) - ord("a") + 1
            else:
                sum_message += ord(char) - ord("A") + 27

    return sum_message


def verify(message: str, key: str, signature: int) -> bool:
    return compute_sum(message) + compute_sum(key) == signature
