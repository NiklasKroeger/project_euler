#!/usr/bin/python3
done = 0
for a in range(1,1000):
	for b in range(a+1,1000):
		for c in range(b+1,1000):
			if a + b + c == 1000 and a**2 + b**2 == c**2 and a < b < c:
				print(a*b*c);
				done = 1
			if done == 1: break
		if done == 1: break
	if done == 1: break
