#!/usr/bin/python3
from math import factorial

sum=0
for digit in str(factorial(100)):
	sum+=int(digit)
print(sum)
