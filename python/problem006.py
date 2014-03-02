#!/usr/bin/python3
summe1 = 0;	#Summe der Quadrate
summe2 = 0;	#Quadrat der Summe
for i in range(1,101):
	summe1 += (i*i);
	summe2 += i;
summe2 = (summe2*summe2);
print(summe2-summe1);

