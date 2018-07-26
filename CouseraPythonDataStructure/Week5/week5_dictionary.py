#week5_dictionary.py

purse = dict()
purse['Money'] = 12

# find key content
for 'Money' in purse:

# get : if exist key get the key value, otherwise return 0
x = counts.get(name,0)
###eg: calculate the
counts = dict()
names = ['aa','bb','cc','aa']
for name in names:
	counts[name] = counts.get(name,0)+1
print(counts)

# Retrieving list of keys and values
#key:
print(list(purse))/print(purse.key())
#value:
print(purse.values())
#tuple
print(purse.items())
# get 2 iteration variables
for aaa,bbb in purse.items:
	print(aaa,bbb)

eg:
handle = open('tile.txt')

counts = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(count,0)+1
bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
print(bigword,bigcount)







