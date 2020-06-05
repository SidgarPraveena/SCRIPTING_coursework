#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:24:12 2019

@author: jyoti
"""

import time
import requests
from bs4 import BeautifulSoup
import os

""" fetch weather"""
country=input("Enter Country")
city=input("Enter current city")
url="https://www.timeanddate.com/weather/"+country+"/"+city
print(url);
req=requests.get(url)
soup=BeautifulSoup(req.content,'html5lib')
weather=soup.find('p').text
#weather=getdiv.attrs['data-mtt']
print(weather)

""" fetch time"""
t=time.localtime()
cur_time=time.strftime("%H",t)
print(cur_time)
current_time=int(cur_time)

if(weather == "Clear." and current_time>7 and current_time<11):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/clear_morn.jpg")
    
elif(weather == "Clear." and current_time>=11 and current_time<17):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/clear_noon.jpg")
    
elif(weather == "Clear." and ((current_time>=17 and current_time<24) or (current_time>=0 and current_time<=7))):
    #print("clear night")
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/clear_night.jpeg")

elif(weather == "Fog." and current_time>7 and current_time<11):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/fog_morn.jpg")
    
elif(weather == "Fog." and current_time>=11 and current_time<17):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/fog_noon.jpg")
    
elif(weather == "Fog." and ((current_time>=17 and current_time<24) or (current_time>=0 and current_time<=7))):
    #print("clear night")
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/fog_night.jpeg")
    
elif(weather == "Passing clouds." and current_time>7 and current_time<11):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/cloud_morn.jpg")
    
elif(weather == "Passing clouds." and current_time>=11 and current_time<17):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/cloud_noon.jpg")
    
elif(weather == "Passing clouds." and ((current_time>=17 and current_time<24) or (current_time>=0 and current_time<=7))):
    #print("clear night")
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/cloud_night.jpg")
    
elif(weather == "Haze." and current_time>7 and current_time<11):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/summer_morn.jpg")
    
elif(weather == "Haze." and current_time>=11 and current_time<17):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/summer_noon.jpg")
    
elif(weather == "Haze." and ((current_time>=17 and current_time<24) or (current_time>=0 and current_time<=7))):
    #print("clear night")
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/summer_night.jpg")

elif(weather == "Rain. Passing clouds." and current_time>7 and current_time<11):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/rain_morn.jpg")
    
elif(weather == "Rain. Passing clouds." and current_time>=11 and current_time<17):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/rain_noon.jpeg")
    
elif(weather == "Rain. Passing clouds." and ((current_time>=17 and current_time<24) or (current_time>=0 and current_time<=7))):
    #print("clear night")
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/rain_night.jpg")
    
elif(weather == "Overcast." and current_time>7 and current_time<11):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/overcast_morn.jpg")
    
elif(weather == "Overcast." and current_time>=11 and current_time<17):
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/overcast_noon.jpeg")
    
elif(weather == "Overcast." and ((current_time>=17 and current_time<24) or (current_time>=0 and current_time<=7))):
    #print("clear night")
    os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/overcast_night.jpeg")

else:
   os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/jyoti/Documents/scritping/assign2/fog_morn.jpg")     