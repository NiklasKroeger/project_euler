#!/usr/bin/python3
file=open("../files/problem013_numbers.txt", "r")
sum=0
numbers=file.readlines()
for number in numbers:
	sum+=int(number)
print(str(sum)[0:10])
