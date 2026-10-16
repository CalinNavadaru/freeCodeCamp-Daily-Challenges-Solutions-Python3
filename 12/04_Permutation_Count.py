import collections
import math


def count_permutations(s: str) -> int:
    c = collections.Counter(s)

    return math.factorial(len(s)) // (math.prod(math.factorial(c[x]) for x in c))
