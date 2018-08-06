#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:31:18 2018

@author: namanapawar
"""

# Importing the libraries
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import time
import datetime
from functools import reduce

# Importing the dataset
df = pd.read_csv('commits.csv')

date=dict()
projectDate=dict()
for index, row in df.iterrows():
    app=row['application']
    email=row['email']
    if type(row['cwhen'])==float:
        continue
    
    if len(row['cwhen'])>=11 and len(row['cwhen'])<=14 and ':' in row['cwhen']:
        value=time.strptime(row['cwhen'], "%m/%d/%y %H:%M")
        if email not in date:
            date[email]=dict()
            if app not in date[email]:
                date[email][app]=[]
                date[email][app].append(value)
        else:
            if app not in date[email]:
                date[email][app]=[]
                date[email][app].append(value)
            else:
                date[email][app].append(value)
                
        if app not in projectDate:
            projectDate[app]=[]
            projectDate[app].append(value)
            projectDate[app].append(value)
        elif value<projectDate[app][0]:
            projectDate[app][0]=value
        elif value>projectDate[app][1]:
            projectDate[app][1]=value
            
inter=dict()              
for app in projectDate:
    for dev in date:
        diff=[]
        if app in date[dev]:
            date[dev][app].sort()
            
            if len(date[dev][app])>1:
                for d in range(len(date[dev][app])-1):
                    diff.append((time.mktime(date[dev][app][d+1])-time.mktime(date[dev][app][d]))/86400)
            else:
                diff.append(np.nan)
            print(len(diff))
            #print(type(reduce(lambda x, y: x + y, diff)))
            #print(type(len(diff)))
            avg=float(sum(diff)) / float(len(diff))
            interval=len(date[dev][app])
            val=[avg,interval]
            if dev in inter:
                inter[dev][app]=avg
            else:
                inter[dev]=dict()
                inter[dev][app]=[]
                inter[dev][app]=avg

df2=pd.DataFrame(inter.items(), columns=['Developer', 'Application','Interval'])
        
                    