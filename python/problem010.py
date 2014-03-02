#!/usr/bin/python3
from math import sqrt
primes = [2]
j = 3
while j < 2000000:
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
summe = 0
for number in primes:
	summe += number
print(summe);

