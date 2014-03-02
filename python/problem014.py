#!/usr/bin/python3
def Reihe(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return Reihe(n/2) + 1
    else:
        return Reihe(3*n+1) + 1

max = [0,0]
n=0
for i in range(2,1000000):
    n=Reihe(i)
    if n > max[0]:
        max[0] = n
        max[1] = i
print(max[1])
