#!/usr/bin/python3
def prime_factorization(n):
    """Returns the prime factorization of n as dictionary"""
    factors = {};
    d = 2
    while n > 1:
        while n % d == 0:
            n /= d
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
        d += 1
    return factors

def divisors(n):
    """Returns the number of divisors of n"""
    dict = prime_factorization(n)
    divisors = 1
    for v in dict.values():
        divisors *= (v + 1)
    return divisors

def triangular_number_divisors(div):
    """Returns the first triangular number with more than div divisors"""
    n = 1
    i = 2
    while divisors(n) < div:
        n += i
        i += 1
    return n

print(triangular_number_divisors(500))
