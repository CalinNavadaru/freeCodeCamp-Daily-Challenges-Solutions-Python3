from typing import Callable


def plus(a: int, b: int) -> int:
    return a + b


def minus(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def division(a: int, b: int) -> int:
    return a // b


def mod(a: int, b: int) -> int:
    return a % b


OPERATIONS: dict[str, Callable[[int, int], int]] = {
    "+": plus,
    "-": minus,
    "*": multiply,
    "/": division,
    "%": mod,
}


def evaluate(numbers: list[int], operators: list[str]):
    op = 0
    r = OPERATIONS[operators[op]](numbers[0], numbers[1])
    op = (op + 1) % len(operators)

    for i in range(2, len(numbers)):
        r = OPERATIONS[operators[op]](r, numbers[i])
        op = (op + 1) % len(operators)

    return r
