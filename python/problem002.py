#!/usr/bin/python3

fib = [1, 2]
while fib[len(fib)-1] <= 4000000:
    fib.append(fib[len(fib)-2] + fib[len(fib)-1])
summe = 0
for nummer in fib:
    if nummer % 2 == 0 and nummer < 4000000:
        summe += nummer
print(summe)
