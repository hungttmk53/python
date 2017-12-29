# Import module socket
import socket

# Tao mot doi tuong socket
sck = socket.socket()
# Lay ten thiet bi local
host_name = socket.gethostname()
# Khoi tao ip
host_ip = '1.52.48.85'
# Khoi tao port cho dich vu
port_num = 12345
# Ket noi toi port
sck.bind((host_ip, port_num))
# Doi 5s lang nghe tu client
string_ctn = str('Cam on ban')
sck.listen(5)
while True:
	cli, addr = sck.accept()
	print('Da ket noi voi: ',addr)
	cli.send(string_ctn)
	cli.close()