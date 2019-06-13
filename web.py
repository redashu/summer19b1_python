#!/usr/bin/python3

import  requests
from  bs4  import BeautifulSoup
#print(dir(requests))
#  we are using  get  request to load website a browser
# loading url 
web=requests.get('http://192.168.10.30/adhoc.html')

print(web) #  http  response code 
#  web have more things also 
#print(dir(web)) 
#print(web.content)
#  text
s_data=web.text  #  this will print  orginal front end data 
print(web.url)
#  now calling  be model
#             webdata, html parser  --html5lib  , htmllib , xml , lxml
soup=BeautifulSoup(s_data,'lxml')  #  html5 and  css3 
#  only title tag
data=soup.select('title')
data1=soup.select('p')
print(data)

#  explore soup var
print(data[0].text)
print(data1)
for  i  in   data1:
	print(i.text)







