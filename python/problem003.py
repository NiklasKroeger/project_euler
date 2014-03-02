#!/usr/bin/python3
i = 2
number = 600851475143
primes = []
while number >= 2:
    if number % i == 0:
        primes.append(i)
        number = number / i
    else:
        i += 1
print(max(primes))
