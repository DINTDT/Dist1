import socket
import time
import threading
import random
import sys

own_ip = socket.gethostbyname(socket.getfqdn())
own_port = 6000
own_data_port= 5999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((own_ip,own_port))
d.bind((own_ip,own_data_port))

heartbeat = open("heartbeat_server.txt","a+")
log = open("registro_server.txt","a+")

datanodes=list()

class datanode:
	id=0
	conn=0
	addr=0
	def send(data):
		conn.sendall(data)
	def connect(tuple):
		self.conn, self.addr = tuple

def dataconnect(cont):
	node = datanode()
	node.connect(d.accept())
	datanodes.append(node)
	datanodes.id=datanodes.conn.recv(16)
	while cont:
		node = datanode()
		node.connect(d.accept())
		datanodes.append(node)
		datanodes.id=datanodes.conn.recv(16)

def checknodes():
	while True:
		for node in datanodes:
			node.send("respond")
			response=node.conn.recv(16)
			if response=="":
				datanodes.remove(node)
			else:
				heartbeat.write("["+node.id+"]")
		heartbeat.write("\n")
		time.sleep(5)

s.listen(1) #for the client
d.listen(3) # for each datanode
#Esperar conexiones de datanodes
for i in [0,1,2]:
	dataconnect(False)

badum = threading.Thread(target=checknodes)
print "starting heart"
sys.stdout.flush()
badum.start()

connect = threading.Thread(target=dataconnect, args=(True,))
connect.start()

while True:
	conn, addr = s.accept()
	print "connection from",addr
	sys.stdout.flush()
	data=conn.recv(1024)
	print "received",data
	sys.stdout.flush()
	chosen=random.choice(datanodes)
	chosen.send(data)
	ack=chosen.conn.recv(16)
	log.write(data+"[@"+str(chosen.id)+"]\n")
