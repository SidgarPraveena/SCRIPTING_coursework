# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

"""list of dictionaries to store attributes for each mobile"""
product_details=[]

for i in range(2,10):
    try:
        """to fetch each page"""
        fetch_phone_list_url="https://www.mysmartprice.com/mobile/pricelist/pages/mobile-price-list-in-india-"+str(i)+".html"
        req=requests.get(fetch_phone_list_url)
        soup=BeautifulSoup(req.content,'html5lib')
        """fetch links corresponding to each mobile phone in the page"""
        for mobile_links in soup.find_all('a', attrs={'class':'prdct-item__name'}):
            if mobile_links.has_attr('href'):
                print(mobile_links.attrs['href'])
               #ignore
                if str(mobile_links.attrs['href']) == "https://www.mysmartprice.com/out/sendtostore.php?top_category=offers&l1=spons&url=https%3A%2F%2Fad.doubleclick.net%2Fddm%2Ftrackclk%2FN558202.2448703MYSMARTPRICE.COM%2FB23191222.256361490%3Bdc_trk_aid%3D452115990%3Bdc_trk_cid%3D113030700%3Bdc_lat%3D%3Bdc_rdid%3D%3Btag_for_child_directed_treatment%3D%3Btfua%3D":
                    continue
                URL=mobile_links.attrs['href']
                r=requests.get(URL)
                soup=BeautifulSoup(r.content,'html5lib')
                dict={}
                
                """fetch name for mobile phone"""
                pname=soup.find('h1', attrs={'class':'prdct-dtl__ttl' , 'itemprop':'name'}).text
                dict['Name']=pname
                try:
                    
                    g_tables=soup.find_all('table', attrs={'class':'tchncl-spcftn__tbl'})
                  
                    """extract data from tables 
                    get value for each attribute and add to dictionary"""
                    for i in range(0,2):
                        for val in g_tables[i].tbody.find_all("tr"):
                            td_val=val.find_all("td")
                            dict[td_val[0].text]=td_val[1].text
                           
                            product_details.append(dict)
                            
                except IndexError:
                    continue
                
                except BaseException:
                    continue
                
    except BaseException:
        continue
                
    
print("collected")
""" create csv file for the recorded data"""
df=pd.DataFrame({'Details':product_details})
df.to_csv('mobile.csv', index=False, encoding='utf-8')

#for m in product_details:
#    print(m)
        