import socket

s = socket.socket()
#host = socket.gethostname()
host ='1.52.48.85'
port = 12345
s.bind((host,port))

s.listen(5)

c, addr = s.accept()
print('Ket noi tu: ', addr)
print('Hello ', c.recv(1024))
name = input("Enter name: ")
name = name.encode('utf-8')
c.send(name)

c.close()