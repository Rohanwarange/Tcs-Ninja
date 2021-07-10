## -*- coding: utf-8 -*-
#"""
#Created on Thu Jul  8 09:45:34 2021
#
#@author: ROHAN
#"""
#
#Write a program to Check whether a given number is a prime number or not 
n=int(input())
flag=0
for i in range(2,n//2):
    if n%i==0:
       flag=1
       break
if flag==0:
   print(f"number {n} is prime") 
else:   
   print(f"number  is {n} not prime") 
       