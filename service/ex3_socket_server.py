import socket

def main():
	host_ip 	= '1.52.48.85'
	host_port 	= 12345

	s = socket.socket()
	s.bind((host_ip, host_port))

	s.listen(1)
	c,addr = s.accept()
	print("Connection from: " + str(addr))
	while True:
		data = c.recv(1024)
		if not data:
			break
		print("From connected user: " + str(data))
		data = str(data).upper()
		print("Sending: " + str(data))
		c.send(data)
	c.close()

if __name__ == '__main__':
	main()