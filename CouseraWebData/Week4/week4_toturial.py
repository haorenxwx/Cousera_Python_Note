#-*- coding:utf-8 -*-
#week4_toturial.py with python 2 = =

#from urllib.request import urlopen
import urllib 
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = raw_input('Enter - ')
html = urllib.urlopen(url, context=ctx).read()
# Retrieve all of the anchor tags

soup = BeautifulSoup(html,"html.parser")
tag = soup.findAll("span",{"class":"comments"})
#print('The tag: ',tag)
#tag2 = soup.findAll("span",re.compile(">([0-9]+)<"))
#print(tag2)
#方法1： 利用 text() 返回html所显示的字符串

number = []
sums = 0
count = 0
for d in tag:
	print(tag)
	number.append(d.text)
	sums+=int(d.text.encode('utf-8'))
	count+=1
print(number)
#numbers = [int(d.text.encode('utf-8')) for d in tag]
print("Count: ",count)
print('\n')
print("Sum: ", sums)


#方法2： 转换成string再用普通正则表达式处理
tags = soup('span')
result = []
count = 0
for tag in tags:
    # Look at the parts of a tag
    y = (str(tag))
    result.append(int(re.findall("[0-9]+",y)[0]))

    #print('URL:', tag.get('class', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
print(result)
