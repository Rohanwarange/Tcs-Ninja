## -*- coding: utf-8 -*-
#"""
#Created on Fri Jul  9 11:13:09 2021
#
#@author: ROHAN
#"""
#
#Problem
#Consider the below series :
#
#0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5, 12, 6, 14, 7, 16, 8

n=int(input())
if n%2==0:
    n=n//2-1
    print(1*n)
else:
    n=n//2
    print(2*n)
    
    