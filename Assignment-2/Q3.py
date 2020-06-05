#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import time
import simpleaudio as sa


URL = "https://www.cricbuzz.com/live-cricket-scores/23669/ts-vs-nmbg-5th-match-mzansi-super-league-2019"
prev = 0
prev1=0
for i in range(0,10):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,'html5lib')
    score = soup.find('span',{'class':'cb-font-20 text-bold'}).text
    x=score.split(' ')
    y=x[2].split('/')
    
    y = [int(i) for i in y]
    print(y)
    if (y[0]-prev) == 6:
        filename = 'b.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    
    if (y[1]-prev1) == 1:
        filename = 'a.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    
    prev = y[0]
    prev1 = y[1]
    time.sleep(10)
