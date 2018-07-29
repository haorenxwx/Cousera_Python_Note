#-*- coding:utf-8 -*-
#week4_toturial2.py

import urllib
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = raw_input('Enter - ')
nextnumber = 18
count = 0
# time means the time you open the html page
time = 7
nextlink = None


for count in range(0,time):
	print(count)
	count+=1

	html = urllib.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the anchor tags

	tags = soup('a')
	link = []
	for tag in tags:
	    link.append(str(tag.get('href', None)))
	url = link[nextnumber-1]
	print(url)

name = re.findall("_([A-Z][a-z]+).html",url)
print(name)




