import socket

host_ip		= '1.52.48.85'
host_port	= 12345
sck = socket.socket()
host_name = socket.gethostname()

sck.connect((host_ip, host_port))
print(sck.recv(1024))
sck.send('Hell')
sck.close()