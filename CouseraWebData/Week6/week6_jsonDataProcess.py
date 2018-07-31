week6_jsonDataProcess.py


import json
data = '''{
	"name" : "Chuck",
	"phone" : {
	"type" : "int1",
	"number" : "+1 734 303 4456"
	},
	"email" : {
	"hide" : "yes"
	}
}'''

info = json.loads(data) #-------generate a dictionary from json
print('Name:',info["name"])
print('Hide',info["email"]["hide"])

Json represents data as nested "lists" and "dictionaries"


For services uses other applications system, 
Service pushed rules applications
must follow to make use of the service(API)---application program interface

Using API:
import urllib, urllib.parse, urllib.error
import json

serviceur1 = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
	address = input('Enter locations: ')
	if len(address) < 1: break

	url = serviceur1 + urllib.parse.urlencode({'address': address})

	print('Retriving',url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('Retrived', len(data), 'characters')

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js["status"] != "OK":
		print('====Fail to Retrive====')
		print(data)
		continue

	lat = js["result"][0]["geometry"]["location"]["lat"]
	lng = js["result"][0]["geometry"]["location"]["lng"]
	print('lat',lat,'lng',lng)
	location = js['result'][0]['formatted_address']
	print(location)





