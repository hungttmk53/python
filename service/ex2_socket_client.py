import socket
sck = socket.socket()
host_name = socket.gethostname()
host_ip = 'host_ip'
port_num = 12345
sck.connect((host_ip, port_num))
print(sck.recv(1024))
sck.close()