# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:55:24 2023

@author: Mohadese
"""

n=int(input("pls enter num:"))
ov=0
for i in range(n):
    id1=int(input("pls enter your id:"))
    h=int(input("pls enter your h:"))
    hp=int(input("pls enter your hp:"))
    if h>40:
        ov=(3/2-1)*(h-40)*hp
    pay=ov+hp*h
    print("pay:",pay)
    
        