#week6_toturial2_googleapi.py
import urllib
import json

serviceurl = "http://py4e-data.dr-chuck.net/geojson?"

while True:
	address = raw_input("Please input the school name you want to check: ")
	if len(address)<1: break
	url = serviceurl + urllib.urlencode({'address': address})
	print('Retriving',url)

	uh = urllib.urlopen(url)
	data = uh.read().decode()
	try:
		js = json.loads(data)
	except:
		js = None
	if not js or 'status' not in js or js["status"]!= "OK":
		print('Fail to retrive:< ==========')
		continue
	print(js["results"][0]["place_id"])
