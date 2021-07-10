# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 10:17:01 2021

@author: ROHAN
"""

#greatest common factor

n1=int(input())
n2=int(input())
def gcd(n1,n2):
    if n2==0:
       return n1
    else:
       return gcd(n2,n1%n2)
print(gcd(n1,n2))       