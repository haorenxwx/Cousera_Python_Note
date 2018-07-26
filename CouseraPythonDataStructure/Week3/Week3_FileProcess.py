Week3_FileProcess

## Read

handle = open(filename,mode)
fhand = open('mbox.txt','r')
# "r" for read and "w" for write

# Print file
for cheese in handle:
	print(cheese)

count = 1
# File length
for cheese in handle:
	count = count+1

# Read whole file to a single string
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# Search through file
for line in fhand:
	if line.startwith('From:'):
		print(line)
for line in fhand:
	line = line.strip()
	if not line.startwith('From:'):
		continue
	if not '@uct' in line:
		continue
	print(line)

# For bad file name
fname = input('Enter the file name:	')
try:
	fhand = open(fname)
except:
	print('File cannot be opened: ', fname)
	quit()
##
