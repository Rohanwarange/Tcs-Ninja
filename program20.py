# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:53:41 2021

@author: ROHAN
"""
#Armstrong Number

n1=input()
total=0
for i in n1:
    total+=int(i)**3
if str(total)==n1:
    print("number is amstrong ")
else:    
    print("number is not amstrong ")
