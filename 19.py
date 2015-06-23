# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:03:03 2015

@author: maks
"""

"""
Ця проста програма рахує скільки неділь випадало на перше число місяця в ХХ столітті,
враховуючи, що 1.01.1901 було вівторок.
"""

datecount=[1,1,1901]
whatday=2
sundays=0

while datecount[2]<2001:
    datecount[1]=1
    while datecount[1]<13:
        datecount[0]=1
        if whatday%7==0:
            sundays+=1
        while datecount[0]<28:
            datecount[0]+=1
            whatday+=1
        if datecount[1]==2:
            if datecount[2]%4==0  and datecount[2]%400!=0:
                datecount[0]+=2
                whatday+=2
                datecount[1]+=1
            else:
                datecount[0]+=1
                whatday+=1
                datecount[1]+=1
        elif datecount[1]==4 or datecount[1]==6 or datecount[1]==9 or datecount[1]==11:
            datecount[0]+=3
            whatday+=3
            datecount[1]+=1
        else:
            datecount[0]+=4
            whatday+=4
            datecount[1]+=1
    datecount[2]+=1
print (sundays)
    
