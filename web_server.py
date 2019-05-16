#!/usr/bin/python3

import  sys,time
import   webbrowser   #  to deal with  web browser 
#  take inline input from user or  URL  
data=sys.argv[1:]

print(data)

#  searching object 
for  i  in  data:
	#  write  code   here to google search 
	print(i)
	time.sleep(2)
	webbrowser.open_new_tab("https://www.google.com/search?q="+i)

