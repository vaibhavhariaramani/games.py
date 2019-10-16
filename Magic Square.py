#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 10:43:36 2019

@author: vaibhav
"""


def MagicSquare(n):
    magicSquare = []
    for i in range (3):
        l = []
        for j in range(3):
            l.append(0)
        magicSquare.append(l)
        
        
    i = n//2
    j = n-1
        
    num = n*n
    count =  1
    
    while(count<=num):
        if(i==-1 and j==n):    #condition 4
            j = n-2
            i = 0
        else:
            if(j==n):           #column value exceeds
                j = 0
            if(i<0):            #row is becoming -1
                i = n-1
            
        if(magicSquare[i][j]!=0):
              j = j-2
              i = i+1 
              continue
        
        else:
            magicSquare[i][j] = count
            count+=1
            
        i = i-1
        j = j+1       #condition 1

       
    for i in range (3):
       # l = []
       for j in range(3):
           # l.append(0)
            print( magicSquare[i][j], end=" ") 
       print()     
       
    print("The sum of each row/column/diagonal is :"+str(n*(n**2+1)/2))   

MagicSquare(7)    