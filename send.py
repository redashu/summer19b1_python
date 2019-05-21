#!/usr/bin/python3
import  socket
#  creating  udp socket 
#                    ipv4     ,  UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  where to send data 
t_ip="3.82.4.173"    #  for  a  single  machine  ip  is  127.0.0.1
t_port=8888


while  True:
#  now  generating  message  to  send  
	data=input("plz  enter  your message  :---->   ")
#  converting  data to  ascii
	new=data.encode('ascii')
#  finally  sending  data
	s.sendto(new,(t_ip,t_port))
#  now  rec data
	print(s.recvfrom(100))








