#!/usr/bin/python3
def divisorsum(n):
	"""Returns the sum of the divisors of n"""
	summe=0
	for i in range(1,(int((n/2)+1))):
		if n%i==0:
			summe+=i
	return summe
 
limit = 20162
s = 0
abn = set()
for n in range(1, limit):
  if (n%2==0 or n%3==0) and divisorsum(n) > n:
    abn.add(n)
  if not any( (n-a in abn) for a in abn ):
    s += n
 
print(s)
