#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:45:55 2019

@author: davidguo
"""

import requests
from bs4 import BeautifulSoup

import pandas as pd

PlayersList = []
ValuesList = []

for j in range(1,26):
    headers = {'User-Agent': 
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    
    pageString = "https://www.transfermarkt.us/premier-league/marktwertaenderungen/wettbewerb/GB1/pos//detailpos/0/verein_id/0/land_id/0/page/"
        
    k = str(j)
    
    page = pageString+k
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    
    Players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})
    
    #Let's look at the first name in the Players list.
    Players[0].text
    
    Values = pageSoup.find_all("td", {"class": "rechts"})
    
    Values[0].text
    
    
    
    for i in range(1,len(Values)-5):
        
        PlayersList.append(Players[i].text)
        ValuesList.append(Values[i].text)
    
df = pd.DataFrame({"Players":PlayersList,"Values":ValuesList})

df.head()

export_csv = df.to_csv ('/Users/davidguo/Documents/18-19/DSC 423/transferMarktData.csv', index = None, header=True)