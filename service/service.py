import socket

s = socket.socket()
#host = socket.gethostname()
host ='1.52.48.85'
port = 12345
s.bind((host,port))
s.listen(5)

c, addr = s.accept()

print('Connection from : ', addr)
c.send(b'Enter option: ')
c.send(b'1. Check OS')
c.send(b'2. Check RAM')
c.send(b'3. Check Disk')
c.send(b'4. Check CPU')

# while True:
# 	print(c.recv(1024))
# 	name = input("Server: ")
# 	name = name.encode('utf-8')
# 	c.send(name)

c.close()