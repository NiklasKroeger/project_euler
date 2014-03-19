#!/usr/bin/python3
from math import sqrt

def isPrime(number):
    if number > 1:
        if number <= 3:
            return True
        if number % 2 == 0 or number == 1:
            return False
        for i in range(3, int(sqrt(number))+1, 2):
            if number % i == 0:
                return False
        return True

def getCount(a, b):
    n = 0
    while isPrime((n*n)+(a*n)+b):
        n += 1
    return n

def main():
    maxN = 0
    currentA = -999
    currentB = -999
    maxA = 0
    maxB = 0
    BCount = 0
    ACount = 0
    while currentA < 1000:
        while currentB < 1000:
            current = (maxN*maxN)+(currentA*maxN)+currentB
            if isPrime(current):
                count = getCount(currentA, currentB)
                if count > maxN:
                    maxN = count
                    maxA = currentA
                    maxB = currentB
            currentB += 1
            BCount += 1
        currentA += 1
        currentB = -999
        ACount += 1
    print(maxA * maxB)

if __name__ == "__main__":
    main()
