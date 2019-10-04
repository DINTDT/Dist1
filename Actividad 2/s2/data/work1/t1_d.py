import socket
import threading

#Function for the control socket thread
def th_ctrl(serv_ip, serv_port):
	#first the sockets and the connection
	s_CONTROL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s_CONTROL.connect((serv_ip, int(serv_port)))
	#the first receivement
	ctrl = s_CONTROL.recv(1024)
	print "[Heart] got",repr(ctrl)
	s_CONTROL.sendall("ack")
	#from now on, answering with heartbeats
	while True:
		ctrl = s_CONTROL.recv(1024)
		s_CONTROL.sendall("dokidoki") #message for the hertbeat
		#print "[Heart] got",repr(ctrl)
		#to kill the control side of this program
		if ctrl == "kill":
			break
	s_CONTROL.sendall("DYING")
	print "CONTROL THREAD HAS BEEN KILLED"

serv_ip = "head" #ip of the service
serv_port = "5999"
print "connecting to ip:",serv_ip
print "with port:",serv_port

#CREATION OF BOTH CHANNELS, DATA AND CONTROL
s_DATA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_DATA.connect((serv_ip, int(serv_port)))

th_CONTROL = threading.Thread(target=th_ctrl, args=(serv_ip, serv_port))
th_CONTROL.start()

#Telling the id to the datanodes
prev = str(s_DATA.recv(1024))
self_id = str(prev)

log = open("data"+prev+".txt","a+")
while True:
	data = s_DATA.recv(1024)
	#to kill the data side of this program
	if data == "kill":
		print "[Data] got",repr(data)
		break
	#if the string in the buffer has changed
	if prev != data:
		log.write(repr(data))
		log.write("\n")
		print "[Data] got",repr(data)
		s_DATA.sendall("ack")
	prev = str(data)
print "Datanode " + self_id + " is being closed"
