#!/usr/bin/python3
def lettercount(n):
	"""Returns the number of letters used to write out the number."""
	if n<20:
		sd=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
		return len(sd[n])
	elif n>=20 and n<100:
		dd=["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
		return len(dd[int(n/10)])+lettercount(int(n%10))
	elif n>=100 and n<1000:
		if n%10==0 and n%100==0:
			return lettercount(int(n/100))+len("hundred")
		else:
			return lettercount(int(n/100))+len("hundred")+len("and")+lettercount(int((n%100)))
	elif n==1000:
		return 11
	else:
		print("Only supported for numbers <= 1000")
		return 0

sum=0
for i in range(1001):
	sum+=lettercount(i)
print(sum)
