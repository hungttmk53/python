import socket

HOST		= 'localhost'
PORT	= 12345
BUFSIZE		= 1024
ADDR		= (HOST, PORT)

server_socket = socket.socket()
server_socket.bind(ADDR)