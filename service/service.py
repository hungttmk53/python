import socket

s = socket.socket()
#host = socket.gethostname()
host ='1.52.48.85'
port = 12345
s.bind((host,port))

s.listen(5)
while True:
	c, addr = s.accept()
	print('Ket noi tu: ', addr)
	c.send(b'Cam on.')
	c.close()