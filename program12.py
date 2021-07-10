## -*- coding: utf-8 -*-
#"""
#Created on Thu Jul  8 09:32:47 2021
#
#@author: ROHAN
#"""
#
#Write a program to change the case of the given alphabet and print

lenght=int(input())
arr=[input() for i in range(lenght)]
a="".join(arr)
print(a.swapcase())
    
