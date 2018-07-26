week3_file.py

fname = input("Enter file name: ")
fh = open(fname)
count = 0
sUm = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count+1
    newline = float(line[line.find(':')+1:].strip())
    sUm = sUm+newline
print('Average spam confidence: '+ str(sUm/count))