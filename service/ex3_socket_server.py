import socket

def main():
	host_ip 	= '1.52.48.85'
	host_port 	= 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host_ip, host_port))

	print('Server Start')

	while True:
		data,addr = s.recvfrom(1024)
		print("message From: " + str(addr))
		print("from connection user: " + str(data))
		data = str(data).upper()
		print("sending: " + str(data))
		s.sendto(data,addr)
	c.close()

if __name__ == '__main__':
	main()