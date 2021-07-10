# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 08:06:48 2021

@author: ROHAN
"""
#
#Question 21
#
#Write a program to find the most occurring character in the string

str1=input()
max1=0
for i in str1:
    max2=str1.count(i)
    if max1<max2:
        max1=max2
        max3=i
print(f"max occurence is {max3} and count is {max1} times")        