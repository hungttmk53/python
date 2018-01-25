import socket

s = socket.socket()
#host = socket.gethostname()
host = '1.52.48.85'
port = 12345

s.connect((host, port))
s.sendall(b'Hello Server')
print(s.recv(1024))
s.close()