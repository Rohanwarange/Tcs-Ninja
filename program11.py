## -*- coding: utf-8 -*-
#"""
#Created on Thu Jul  8 08:13:39 2021
#
#@author: ROHAN
#"""
#
#Question 20
#
#Given an array and a number (say s), find whether any two elements in the array whose sum is “s”:

n=int(input())
arr=[int(input()) for i in range(n)]
m=int(input())
for i in arr:
    for j in range(len(arr)):
        if i!=arr[j]: 
           if i+arr[j]==m:
              k,o=i,arr[j]
              print(f"yes two numbers are {k} and {o}") 
           else:
               print("no perfect couple are found")
