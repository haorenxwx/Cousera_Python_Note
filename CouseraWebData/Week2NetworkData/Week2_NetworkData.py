Week2_NetworkData.py

nework socket:
- end point of a bidirectional inter-precess like internet

#dail a phone
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pre4e.org',80))
				hostname		port

# application layer
A set of rules Invert for web to retrieve HTML Images, Documents

# Get 
telnet www.dr-chuck.com 80
GET http://www.dr-chuck.com/page1.htm HTTP/1.0
# it will return the whole page


#HTTP request in python
import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1 \n\n'.encode()#（encode() change command form unicode to utfa）
mysocket.send(cmd)

while True:
	data = mysock.recv(512)
	if (len(data)<1):
		break
	print(data.decode())
mysock.close()
