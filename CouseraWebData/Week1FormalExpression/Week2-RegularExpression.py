#Week2-RegularExpression.py

import re
###########
re.search()
hand = open('mbox-short.txt')
for line in hand:
	line = line.strip()
	if line.find('From:')>=0:
		print(line)
	####equals to:
	if re.rearch('From:',line):#return True & False
		print(line)

	if line.startswith('From:')
	####equals to:
	if re.research('^From: ', line)

eg: "X-\S+:" start with"X-", without any space, followed by ":"


re.findall()
eg: "[0-9]+" one or more digit
x = 'My 2 favourite number s are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
>>>y = ['2','19','42']
y = re.findall('[AEIOU]+',x)
print(y)
>>>y = []


Greedy matching: return longest string:
re.findall('^F.+',x)
Not greedy matching: return the shortest
re.findall('^F.+?',x)

Findout email:
'\S+@\S+'
'@([^ ]*)' match Non-blank character and other charactors
'^FROM .*@([^ ]*)': return garena.com (from xuwx@garena.com)
in the () is the content we need
'^ashfis: ([0-9.]+)'

remember to make comment because its not that readable


'^'	Matches the beginning of a line
'$'	Matches the end of the line
'.'	Matches any character
'\s'	Matches whitespace
'\S'	Matches any non-whitespace character
'*'	Repeats a character zero or more times
'*?'	Repeats a character zero or more times (non-greedy)
'+'	Repeats a character one or more times
'+?'	Repeats a character one or more times (non-greedy)
'[aeiou]'	Matches a single character in the listed set
'[^XYZ]'	Matches a single character not in the listed set
'[a-z0-9]'	The set of characters can include a range
'('	Indicates where string extraction is to start
')'	Indicates where string extraction is to end



