# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:01:54 2021

@author: ROHAN
"""

#Area of a circle,triangle,square
class Area:
     def __init__(self):
         self.pi=3.14
     def circle(self,radius):
        return 2*self.pi*radius
     def triangle(self,height,base):
        return 0.5*height*base
     def square(self,side):
        return side**2
     def rectangle(self,lenght,bright):
        return lenght*bright
        
a=Area()
print(a.circle(int(input())))
print(a.rectangle(int(input()),int(input())))
print(a.square(int(input())))
print(a.triangle(int(input()),int(input())))