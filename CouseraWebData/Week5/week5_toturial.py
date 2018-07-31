#week5_toturial.py

#import urllib.request, urllib.parse, urllib.error
import urllib
from urlparse import urlparse
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

#while True:
url = raw_input('Enter location: ')


#url = serviceurl + urlparse.urlencode({'address': address})
#print('Retrieving', url)
uh = urllib.urlopen(url)
data = uh.read()

#print('Retrieved', len(data), 'characters')
print(str(data.decode()))
data = str(data.decode())
tree = ET.fromstring(data)
print(tree)

results = tree.findall('comments/comment')
print(results)
countlist = []
count = 0
for i in results:
	#print(i)
    #countlist.append(str(i.find('count').text))
    data = i.find('count').text
    count = count+int(data)
    #print(i.find('count').text)
#print(countlist)
print(count)
