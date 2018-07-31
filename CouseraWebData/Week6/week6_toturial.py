#week6_toturial.py

import urllib
import json


while True:
	url = raw_input("Please input the url you want to process: ")
	uh = urllib.urlopen(url)
	data = uh.read().decode()
	print('Retrived', len(data), 'characters')
	try:
		js = json.loads(data)
	except:
		js = None
	#print(json.dumps(js,indent = 2))
	dictre = js["comments"]
	count = 0
	for i in dictre:
		count += i["count"]
	print(count)
		#print(type(i["count"]))


