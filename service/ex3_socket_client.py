import socket

def main():
	host_ip		= 'localhost'
	host_port	= 12346
	server		= ('1.52.48.85',12345)

	s 			= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host_ip, host_port))

	message		= input(">_")
	
	while message !='q':
		s.sendto(message,server)
		data,addr	= s.recvfrom(1024)
		print(b"Received from server: " + str(data))
		message	= input(">_")
	s.close()

if __name__ == '__main__':
	main()