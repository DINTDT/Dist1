import socket

#own_ip = socket.gethostbyname(socket.getfqdn())
own_ip = "0.0.0.0"
own_port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((own_ip, own_port))

log = open("log.txt","a+")
print "open @",s.getsockname()

s.listen(1)

while True:
	conn, addr =  s.accept()
	print "connection from",addr
	data=conn.recv(1024)
	print "received",data
	log.write(data+"\n")
	log.flush()
	conn.sendall("received message")
	break #this break is only because we expect only one message
