import socket

file = open("target.txt","r")
log = open("respuestas.txt","a+")
serv_ip = file.readline().split()[1]
serv_port = file.readline().split()[1]
print "connecting to ip:",serv_ip
print "with port:",serv_port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serv_ip, int(serv_port)))
s.sendall("hello")
data = s.recv(1024)
print "got",repr(data)
log.write(repr(data)+"\n")
