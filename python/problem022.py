#!/usr/bin/python3
def namescore(name, stelle):
	score=0
	for letter in name:
		score+=ord(letter)-64
	return score*(stelle+1)
		

file=open("../files/problem022_names.txt", "r")
str=file.readline()
file.close()
names=[]
name=[]
for element in str:
	if element==",":
		names.append("".join(name))
		name=[]
	elif element!="\"":
		name.append(element)
names.append("".join(name))
del name, str
names.sort()
score=0
for i in range(0,len(names)):
	score+=namescore(names[i], i)
print(score)
