#!/usr/bin/python3
def fib(n=1000):
	"""Returns the first term in the Fibonacci sequence with more than n digits"""
	numbers = [1,1]
	while len(str(numbers[-1])) < n:
		numbers.append(numbers[-1] + numbers[-2])
	return len(numbers)

print(fib())
