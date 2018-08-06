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
     

experience=dict()      
for app in projectDate:
    for dev in date:
        if app in date[dev]:
            date[dev][app].sort()
            devStart=time.mktime(date[dev][app][0])
            projStart=time.mktime(projectDate[app][0])
            projCurr=time.mktime(projectDate[app][1])
            lenOfProject=(projCurr-projStart)/86400
            lenOfWork=(projCurr-devStart)/86400
            workedFor=(lenOfWork/lenOfProject)*100
            if workedFor>50:
                if dev in experience:
                    experience[dev][app]="Senior"
                else:
                    experience[dev]=dict()
                    experience[dev][app]="Senior"
            else:
                if dev in experience:
                    experience[dev][app]="junior"
                else:
                    experience[dev]=dict()
                    experience[dev][app]="junior"

inter=dict() 
frequency=dict()             
for app in projectDate:
    for dev in date:
        diff=[]
        if app in date[dev]:
            if len(date[dev][app])>1:
                for d in range(len(date[dev][app])-1):
                    diff.append((time.mktime(date[dev][app][d+1])-time.mktime(date[dev][app][d]))/86400)
            else:
                diff.append(np.nan)
            avg=float(sum(diff)) / float(len(diff))
            interval=len(date[dev][app])
            if dev in inter:
                inter[dev][app]=avg
                frequency[dev][app]=interval
            else:
                inter[dev]=dict()
                inter[dev][app]=[]
                inter[dev][app]=avg
                frequency[dev]=dict()
                frequency[dev][app]=[]
                frequency[dev][app]=interval
        

df1=pd.DataFrame(experience).transpose().reset_index()
df1 = pd.melt(df1, id_vars=["index"], var_name="Project", value_name="Experience")
df1.to_csv("experience.csv")
df2=pd.DataFrame(inter).transpose().reset_index()
df2 = pd.melt(df2, id_vars=["index"], var_name="Project", value_name="Interval")
df2.to_csv("interval.csv")
df3=pd.DataFrame(frequency).transpose().reset_index()
df3 = pd.melt(df3, id_vars=["index"], var_name="Project", value_name="Frequency")
df3.to_csv("frequency.csv")   
df4=pd.DataFrame(date).transpose().reset_index()   

i=0   
projects=[]
for email in date:
    line=[]
    line.append(str(email))
    for app in date[email]:
        line.append(str(app))
    projects.append(line)


    




    
                
    
    