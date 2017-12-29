import socket

host_ip		= '1.52.48.85'
host_port	= 12345

def service_connect(host_ip, host_port):
	s_socket	= socket.socket()
	s_socket.bind((host_ip, host_port))
	s_socket.listen(5)
	while True:
		cli, addr = s_socket.accept()
		print("Hello.", addr)
		cli.send(b'Hello Client.')
		print(s_socket.recv(1024))
		cli.close()

service_connect(host_ip, host_port)