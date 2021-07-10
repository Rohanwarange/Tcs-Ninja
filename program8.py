## -*- coding: utf-8 -*-
#"""
#Created on Tue Jul  6 10:00:21 2021
#
#@author: ROHAN
#"""
#
##Question
##
##Link to this Question
##
##1. The program will recieve 3 English words inputs from STDIN
##
##These three words will be read one at a time, in three separate line
##The first word should be changed like all vowels should be replaced by *
##The second word should be changed like all consonants should be replaced by @
##The third word should be changed like all char should be converted to upper case
##Then concatenate the three words and print them
##Other than these concatenated word, no other characters/string should or message should be written to STDOUT
##
##For example if you print how are you then output should be h*wa@eYOU.
##
##You can assume that input of each word will not exceed more than 5 chars
##
##Test Cases
##Case 1
##Input
##
##how
##are
##you
##Expected Output : h*wa@eYOU
##
##Case 2
##Input
##
##how
##999
##you
##Expected Output : h*w999YOU
#rohan sanjay WarGangde
p,q,r=input().split(" ")
a=""
b=""
for i in p:
    if i=="a"or i=="e" or i=="i" or i=="o" or i=="u":
       a+="*"
    else:
        a+=i
for i in q:
    if i=="a"or i=="e" or i=="i" or i=="o" or i=="u":
         b+=i
    else:
         b+="@"
print(f"{a}{b}{r.upper()}")    
        
    