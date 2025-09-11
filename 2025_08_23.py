** start of main.py **

def is_unnatural_prime(n):
    n = abs(n)
    if n in [0, 1] or n % 2 == 0:
        return False
    
    d = 3
    count = 0
    while n != 1:
        if n % d == 0:
            count += 1
        while n % d == 0:
            n /= d
        d += 2
        
    
    return count == 1

** end of main.py **

