import socket

def main():
	host_ip		= '1.52.48.85'
	host_port	= 12345

	s 			= socket.socket()
	s.bind((host_ip, host_port))

	message		= input(">_")
	message		= str(message)
	while message !='q':
		s.send(message)
		data	= s.recv(1024)
		print(b"Received from server: " + str(data))
		message	= input(">_")
	s.close()

if __name__ == '__main__':
	main()