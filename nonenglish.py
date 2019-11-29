#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:46:15 2019

@author: davidguo
"""

from unidecode import unidecode

import csv

import pandas as pd


#reads csv file that has two columns, First Name and Last Name
eplnames = pd.read_csv('eplnames.csv')


#iterates through data frame and uses unidecode to convert from non english to english letters
for i, j in eplnames.iterrows():     
    eplnames.at[i,'First Name'] = unidecode(eplnames.at[i,'First Name'])
    if(isinstance(eplnames.at[i,'Last Name'],float)):
        eplnames.at[i,'Last Name'] = " "
    else:
        eplnames.at[i,'Last Name'] = unidecode(eplnames.at[i,'Last Name'])


export_csv = eplnames.to_csv ('/Users/davidguo/Documents/18-19/DSC 423/eplplayernames.csv', index = None, header=True)
    