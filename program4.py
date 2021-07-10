## -*- coding: utf-8 -*-
#"""
#Created on Tue Jul  6 08:37:23 2021
#
#@author: ROHAN
#"""
#
#Program 6
#PRIME NUMBER WITH A TWIST
#Ques. Write a code to check whether no is prime or not. 
#Condition use function check() to find whether entered no is positive or negative ,if negative then enter the no, 
#And if yes pas no as a parameter to prime() and check whether no is prime or not?

def prime(n):
   for i in range(2,n//2):
       if n%i==0:
          print("not positive")
       else:
           print("positive")
n=int(input())
if n<0:
   n=int(input())
else:
   prime(n)
