#!/usr/bin/python3

import  sys
data=sys.argv[1:]
#  create a new file  and  write  data no read possible
f=open("ok.txt",'w')
for  i  in   data:
	f.write(i)
	f.write("\n")

f.close()

# read the just  create file 
f=open("ok.txt",'r')
print(f.read())
f.close()

# read &  write     w+







