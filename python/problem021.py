#!/usr/bin/python3
def divisorsum(n):
	"""Returns the sum of the divisors of n"""
	summe=0
	for i in range(1,(int((n/2)+1))):
		if n%i==0:
			summe+=i
	return summe

def main(n):
	sums=[0]
	while len(sums)<n:
		sums.append(divisorsum(len(sums)))
	summe=0
	for i in range(0,len(sums)):
		for j in range(i+1,len(sums)):
			if sums[i]==j and sums[j]==i:
				summe+=i+j
	print(summe)

main(10000)
