import socket

own_ip = "0.0.0.0"
own_port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((own_ip, own_port))

print "open @",s.getsockname()

s.listen(1)

while True:
	conn, addr =  s.accept()
	print "connection from",addr
	print "received",conn.recv(1024)
	conn.sendall("received message")

