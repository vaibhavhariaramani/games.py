#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 15:39:43 2019

@author: vaibhav
"""
def fizzBuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(str(i) +" = fizzBuzz")
        else:
            if(i%3==0):
                print(str(i) + " = Fizz")
            else:
                if(i%5==0):
                    print(str(i) + " = buzz")
                else:
                    print(str(i))
                    
                    
                    