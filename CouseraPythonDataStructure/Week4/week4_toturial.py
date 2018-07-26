#week4_toturial.py

fname = raw_input("Enter file name: ")
if len(fname) < 5 : fname = "mbox-short.txt"

count = 0
fh = open(fname)
for i in fh:
	if i.startswith('From') and not i.startswith('From:'):
		count = count + 1
		a = i.split()
		print(a[1])


print("There were", count, "lines in the file with From as the first word")
