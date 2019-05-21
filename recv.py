#!/usr/bin/python3

import  socket,time
ip="0.0.0.0"
port=8888   #  1024  -- 65535  free range of  port 
#  generate protocol  type of  socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #  udp docket  created 

#  to bind  i can  combine  ip  and port 
s.bind((ip,port))

#   now  we  can rec  data  from sender
while True:
	web=s.recvfrom(100)
	print(web)
	time.sleep(3)
#   eply  to  send
	s.sendto("niceeeeeeeeeeeeee".encode('ascii'),web[1])
