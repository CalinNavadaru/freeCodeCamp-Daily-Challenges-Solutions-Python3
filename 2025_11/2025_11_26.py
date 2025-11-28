def is_fizz_buzz(sequence: list) -> bool:
    for index, elem in enumerate(sequence, 1):
        if index % 15 == 0 and elem != "FizzBuzz":
            return False
        elif index % 3 != 0 and index % 5 == 0 and elem != "Buzz":
            return False
        elif index % 5 != 0 and index % 3 == 0 and elem != "Fizz":
            return False
        elif index % 3 != 0 and index % 5 != 0 and index != elem:
            return False
    return True
