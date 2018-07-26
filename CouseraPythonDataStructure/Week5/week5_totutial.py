#week5_totutial.py
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
name = []
for line in handle:
    if line.startswith('From '):
        name.append(line.split()[1])
result = {}
for i in name:
    result[i] = result.get(i,0)+1
maxcount = None
maxemail = None
for email,count in result.items():
    if maxcount == None or maxcount < count:
        maxcount = count
        maxemail = email
print(maxemail,maxcount)