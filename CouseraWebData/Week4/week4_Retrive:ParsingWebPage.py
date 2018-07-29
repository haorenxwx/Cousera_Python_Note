week4_Retrive/ParsingWebPage.py

=======
ASC||
- #ord() function tell us the numeric value of a simple ASC|| caracter
print(ord('E'))

=======
unicode
- combine all kinds of languages character

=======
Multy-Byte character
- represent the wide range of character
- UTF-8 
	1-4byte
	the best for moving data between systems

=======
Python2:
x = b'abc'
<type 'str'>
x = '一二三'
<type 'str'>
x = u'一二三'
<type 'unicode'>

python3
x = b'abc'
<class 'bytes'>
x = '一二三'
<class 'str'>
x = u'一二三'
<class 'str'>

=======
python string o bytes
while True:
	data = mysock.recv(512)
	if len(data)<1:
		break
	mystring = data.decode() #default utf8/ASC||
	print(mystring)

=======
An HTTP Request in Python2
import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romoe.txt HTTP/1.0\n\n'.encode() 
#default is UTF-8 from UTF-8 to string unicode
mysock.send(cmd) 
while True:
	data = mysock.recv(512)
	if (len(data)<1):
		break
	mystring = data.decode()
#default UTF-8 from string unicode to 
	print(data.decode())
mysock.close()
#default encode and decode are all utf-8

======
use urllib in python
help us so all the socket

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romoe.txt')
for line in fhand:
	print(line.decode().strip())

>>>>process a web page like a file
can also reading web page(content but not the head):


======
scrape web(spider)
easy way: Beautiful Soup
from www.crummy.com
https://pypi.org/project/beautifulsoup4/
https://pypi.org/project/beautifulsoup4/#files

include in the anaconda packages,
can also use the pip install beautifulsoup4

from bs4 import BeautifulSoup

举例：
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrive all of the anchor tags(in html the anchor should be the url links)
# from <a> to <\a>
tags = soup('a')
for tag in tags:
	print(tag.get('href',None))

应用：
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') 

...

http://py4e-data.dr-chuck.net/comments_120202.html





#方法1： 利用 text() 返回html所显示的字符串

#方法2： 转换成string再用普通正则表达式处理




