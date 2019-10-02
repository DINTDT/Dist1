import socket

#connect to server (port 5999, ip is probably 127.0.1.1)
#connect again. one channel is data, the other is control
	#that is, DATA is used for messages that need to be stored,
	#while CONTROL is used for the heartbeat.
	#CONTROL socket access should be made through a thread.

#when a message is received (DATA), store it in a file
#answer to the server

#when a message is received (CONTROL), answer "OK" or something like that
