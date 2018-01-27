import socket

s = socket.socket()
#host = socket.gethostname()
host = '1.52.48.85'
port = 12345


s.connect((host, port))




print(s.recv(1024))

while True:
	string_send = input("Client: ")
	string_send = string_send.encode('utf-8')
	s.send(string_send)
	print(s.recv(1024))

s.close()