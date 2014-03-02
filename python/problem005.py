#!/usr/bin/python3
zahl = 1
i = 1
while i <= 20:
	if zahl % i != 0:
		i = 1
		zahl += 1
	else:
		i += 1
print(zahl)

