import socket

def main():
	host_ip		= ''
	host_port	= ''

	s 			= socket.socket()
	s.connect((host_ip, host_port))

	message		= raw_input(">_")
	while message !='q':
		s.send(message)
		data	= s.recv(1024)
		print("Received from server: " + str(data))
		message	= raw_input(">_")
	s.close()

if __name__ == '__main__':
	main()