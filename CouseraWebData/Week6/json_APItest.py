#json_APItest.py
import urllib
import json

serviceur1 = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
	address = raw_input('Enter locations: ')
#inputurl: Ann Arbor, MI
	if len(address) < 1: break

	url = serviceur1 + urllib.urlencode({'address': address})
#output: http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
	print('Retriving',url)
	uh = urllib.urlopen(url)
	data = uh.read().decode()
	print('Retrived', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js["status"] != "OK":
		print('====Fail to Retrive====')
		#print(data)
		continue
	print("=========================")
	print(json.dumps(js, indent = 2))
	print("=========================")
	print('\n\n\n')
	print(js["results"][0])
	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lng"]
	print('lat',lat,'lng',lng)
	location = js['results'][0]['formatted_address']
	print(location)