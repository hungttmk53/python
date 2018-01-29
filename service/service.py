import socket

s = socket.socket()
#host = socket.gethostname()
host ='1.52.48.85'
port = 12345
s.bind((host,port))
s.listen(5)

c, addr = s.accept()

Enter_Option = "Enter option: 1. Check OS \n 2. Check RAM \n 3. Check Disk \n 4. Check CPU"
Enter_Option = Enter_Option.encode('utf-8')

print('Connection from : ', addr)
c.send(Enter_Option)


# while True:
# 	print(c.recv(1024))
# 	name = input("Server: ")
# 	name = name.encode('utf-8')
# 	c.send(name)

c.close()