#week2_toturial.py
import urllib
import re
import sqlite3
import requests


conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter the file name: ')
data = open(fname,'r')


for i in data:
	#print(i)
	if not i.startswith('From: '): continue
	email = i.split()[1]
	org = email.split('@')[1]
	#print(org)
	#print(email)
	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count)
					VALUES (?, 1)''', (org,))
	else:
		cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?',(org,))
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
	print(str(row[0]),row[1])
cur.close()	