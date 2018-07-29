#Week1_toturial.py
import re

filename = 'regex_sum_120200.txt'
handle = open(filename)
sums = 0
for i in handle:
	num = re.findall('[0-9]+',i)
	for j in num:
		sums+= int(j) 
print(sums)
