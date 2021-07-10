## -*- coding: utf-8 -*-
#"""
#Created on Fri Jul  9 11:02:32 2021
#
#@author: ROHAN
#"""
#
#Program 7
#NUMBER SERIES TYPE 1
#Ques. Find the 15th term of the series?
#
#0,0,7,6,14,12,21,18, 28
#
#Please add the answer in the comment section below.
n=int(input())
if n%2!=0:
    n=n//2
    print(7*n)
else:
    n=n//2
    n=n-1
    print(6*n)
