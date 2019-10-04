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

#the class fo the datanodes
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
		node = datanode((d.accept(), d.accept()))
		node.id=len(datanodes)+1
		datanodes.append(node)
		node.send(str(node.id))

#this is the function that the thread will use to
#know the state of the datanodes
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
			#to kill the thread
			if "DYING" in response:
				break
		except:
			print "[Head] No datanodes, exiting"
			break
		time.sleep(5)

#this function does not close any socket, that's
#why is called badly
def shutdown_badly():
	for node in datanodes:
		node.check("kill")
		node.send("kill")

s.listen(1) #for the client
d.listen(6) # for each datanode

#waiting 4 datanodes connections
cantidad = list(range(3))
for i in cantidad:
	dataconnect(False)

#the thread that checks the state of the datanodes
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
	#print "received", data
	#sys.stdout.flush()
	chosen=random.choice(datanodes)
	chosen.send(data)
	#ack from the datanode
	ack=chosen.conn.recv(16)
	id_node = str(chosen.id)
	log.write(data+"[@"+id_node+"]\n")
	conn.sendall(id_node)

	#to kill everything just say "chao"
	if("chao" == data):
		shutdown_badly()
		break

print "server closing"