#!/usr/bin/python3
import itertools

i=1
for perm in itertools.permutations(range(10)):
	if i<1000000:
		i+=1
	else:
		print(''.join(str(e) for e in perm))
		break
