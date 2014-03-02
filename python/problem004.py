#!/usr/bin/python2
produkteliste = []
nummer = []
reverse = []
for i in range(100, 1000):
	for j in range(100, 1000):
		if j >= i:
			hilf = i * j
			while hilf >= 10:
				nummer.append(hilf % 10)
				reverse.append(hilf % 10)
				hilf = hilf / 10
			nummer.append(hilf)
			reverse.append(hilf)
			reverse.reverse()
			if nummer == reverse:
				produkteliste.append(nummer)
			nummer = []
			reverse = []
produkte = []
for element in produkteliste:
	hilf = 0
	for digit in element:
		hilf = (hilf * 10) + digit
		produkte.append(hilf)
produkte.sort()
print(max(produkte))

