#Week2_toturial.py

import socket
import re


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data)<1):
		break
	da = data.decode()
	print(da)
mysock.close()


for i in da:
	print(i)
	print(type(i))
	LastM = re.findall('^Last-Modified:[*]',i)
	if LastM:
		print('Last-Modified value is : ', LastM)



'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

'''