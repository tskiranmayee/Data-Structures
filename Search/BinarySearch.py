# -*- coding: utf-8 -*-
"""
Created on Mon May 10 21:07:18 2021

@author: tskir
"""

"""Binary Search"""
a=[1,2,3,4,5] # always input a sorted array
x=2
lb=0
ub=len(a)-1

found=False
while(found!=True):
    m=(lb+(ub))//2
    if(ub<lb):
        break
    else:
        if(x==a[m]):
            found=True
            break
        elif(x>a[m]):
            lb=m+1
        elif(x<a[m]):
            ub=m-1
            
if(found==1):
    print("Found")
else:
    print("Not Found")
    