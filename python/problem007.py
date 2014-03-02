#!/usr/bin/python3
from math import sqrt
primes = [2, 3, 5, 7, 11, 13]
j = 3
while len(primes) < 10001:
	flag = 1
	for i in primes:
		if j % i == 0:
			flag = 0
			break
		if i > sqrt(j):
			break
	if flag == 1:
		primes.append(j)
	j += 2
print(primes[-1]);

