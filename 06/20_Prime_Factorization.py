def prime_factorization(n: int) -> list[int]:

    r = []
    while n % 2 == 0:
        r.append(2)
        n //= 2

    d = 3
    while n > 1:
        while n % d == 0:
            r.append(d)
            n //= d

        d += 2
        if d * d > n:
            d = n
    
    if not r:
        return [n]
    return r