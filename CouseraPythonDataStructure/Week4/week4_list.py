week4_list.py

# Different from string: can not change value for a position
# Concetenating list:
a = [1,2]
b = [3,4]
c = a+b

# Sliced
a[1:]

# Append
a = list() # create empty list
a.append('book')

# Something in the list
'book' in a
# it will return True

# List in order
a.sort()

# Build in function
min/max/sum/len/...
while True:
	inp = input('Enter a number: ')
	if inp == 'done': break
	value = float(inp)
	numlist.append(value)
average = sum(numlist)/len(numlist)
# cost too much memory then manaul count every loop

# Split: from string to a list
abc = 'With three words'
stuff = abc.split()# it can be many spaces

