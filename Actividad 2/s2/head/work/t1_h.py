import socket
import time
import threading
import random
import sys

own_ip = "0.0.0.0"
own_port = 6000
own_data_port= 5999

#port 4 clients
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#port 4 datanodes
d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((own_ip,own_port))
d.bind((own_ip,own_data_port))


heartbeat = open("heartbeat_server.txt","a+")
log = open("registro_server.txt","a+")

datanodes=list()

class datanode:
	id=0
	#conn=None
	#addr=0
	#heart = None
	#addr_heart = 0

	def __init__(self, ((a, b), (c, d))):
		self.conn, self.addr = a, b
		self.heart, self.addr_heart = c, d
	def send(self, data, d = "trash"):
		self.conn.sendall(data)
	def connect(self, a, b):
		self.conn, self.addr = a, b
	def pacemaker(self, a, b):
		self.heart, self.addr_heart = a, b
	def check(self, beat, b = "trash"):
		self.heart.sendall(beat)

#as we use this function in the threads,
#we give it a parameter to do this one
#or several times, we mean, keep it waiting
def dataconnect(cont):
	node = datanode((d.accept(), d.accept()))
	#node.connect(node, d.accept())
	#node.pacemaker(node, d.accept())
	node.id=len(datanodes)+1
	datanodes.append(node)
	node.send(str(node.id))
	while cont:
		node = datanode()
		node.connect(tuple(d.accept()))
		node.pacemaker(tuple(d.accept()))
		node.id=len(datanodes)+1
		datanodes.append(node)

def checknodes():
	i = -1
	while True:
		i += 1
		try:
			for node in datanodes:
				node.check(("respond " + str(i)))
				response=node.heart.recv(128)
				print "[Head] got",repr(response)
				if response=="":
					datanodes.remove(node)
				else:
					heartbeat.write("["+ str(node.id)+"]")
			heartbeat.write("\n")
			if "DYING" in response:
				break
		except:
			print "[Head] No datanodes, exiting"
			break
		time.sleep(5)

def shutdown_badly():
	for node in datanodes:
		node.check("kill")
		node.send("kill")

s.listen(1) #for the client
d.listen(6) # for each datanode

#Esperar conexiones de datanodes
cantidad = list(range(3))
for i in cantidad:
	dataconnect(False)

badum = threading.Thread(target=checknodes)
print "starting heart"
sys.stdout.flush()
badum.start()

#if some datanodes turn off, and try to connect again,
#this thread will add it again
#connect = threading.Thread(target=dataconnect, args=True)
#connect.start()

conn, addr = s.accept()
print "connection from",addr
sys.stdout.flush()
while True:
	data=str(conn.recv(1024))
	print "received", data
	sys.stdout.flush()
	chosen=random.choice(datanodes)
	chosen.send(data)
	#ack from the datanode
	ack=chosen.conn.recv(16)
	id_node = str(chosen.id)
	log.write(data+"[@"+id_node+"]\n")
	conn.sendall(id_node)
	if("chao\r\n" == data):
		shutdown_badly()
		break

print "server closing"