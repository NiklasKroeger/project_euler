#!/usr/bin/python3
"""
Google delivers as result the binomial coefficient as follows:

number of paths of length a+b from origin (0,0) to (a,b) only going east or south is equal to binomial coefficient of (a+b, a) a+b over a
"""

from math import factorial

#grid size: 20x20
n=40
k=20
print(int(factorial(n)/(factorial(k)*factorial(n-k))))
