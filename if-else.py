# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 17:37:41 2025

@author: u2633446
"""

num = int(input("please enter an integer: "))

if num>=0:
    if num==0:
        print("zero")
    else:
        print("%d this number is positive number" %(num))
    
else:
    print(num, "this is a negative number")
    print("%4.2f is a negative number" %(num))