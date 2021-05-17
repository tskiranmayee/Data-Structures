# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:58:33 2021

@author: tskiranmayee
"""

"""Linear Search-The Hard way
Best case:O(1)     - found at first location
Average case:O(n)  - found at the middle
Worst case:O(n)    - not found at all or found at the last position  """
found=False
q=8
a=[4,5,7,8,1,3]
for i in range(len(a)):
    if(q==a[i]):
        found=True
        break
    else:
        i=i+1
        
if(found==True):
     print("Found {} at index {} in array {}".format(q,i,a))
else:
     print("Not Found {} in the array {}".format(q,a))
     
     

        
    



