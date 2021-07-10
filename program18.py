## -*- coding: utf-8 -*-
#"""
#Created on Thu Jul  8 10:17:01 2021
#
#@author: ROHAN
#"""
#
#Fibonacci Series
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
n=int(input())
a=1
b=1
if n==1:
    print(a)
elif n==2:    
    print(a,b)
else:
   print(a,b,end=" ")
   for i in range(3,n+1):
       c=a+b
       a=b
       b=c   
       print(c,end=" ")
       
       
