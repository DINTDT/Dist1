import socket
import threading

#connect to server (port 5999, ip is probably 127.0.1.1)
#connect again. one channel is data, the other is control
	#that is, DATA is used for messages that need to be stored,
	#while CONTROL is used for the heartbeat.
	#CONTROL socket access was made through a thread.

#when a message is received (DATA), store it in a file,
#and answer an "OK" as an ack.
#when a message is received (CONTROL), answer "OK" 


#Function for the control socket thread
def th_ctrl(serv_ip, serv_port):
	s_CONTROL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s_CONTROL.connect((serv_ip, int(serv_port)))
	ctrl = s_CONTROL.recv(1024)
	print "[Heart] got",repr(ctrl)
	s_CONTROL.sendall("ack")
	while True:
		ctrl = s_CONTROL.recv(1024)
		s_CONTROL.sendall("dokidoki") #message for the hertbeat
		print "[Heart] got",repr(ctrl)

#log = open("data.txt","a+")
serv_ip = "head"
serv_port = "5999"
print "connecting to ip:",serv_ip
print "with port:",serv_port

#CREATION OF BOTH CHANNELS, DATA AND CONTROL
s_DATA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_DATA.connect((serv_ip, int(serv_port)))

th_CONTROL = threading.Thread(target=th_ctrl, args=(serv_ip, serv_port))
th_CONTROL.start()

prev = str(s_DATA.recv(1024))
log = open("data"+prev+".txt","a+")

while True:
	data = s_DATA.recv(1024)
	#if the string in the buffer has changed
	if prev != data:
		log.write(repr(data))
		print "[Data] got",repr(data)
		s_DATA.sendall("ack")
	prev = str(data)