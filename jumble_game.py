#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:44:58 2019

@author: vaibhav
"""
import random
def choose():
    words=['computer','programming','mathematics','player','reverse','water','bottle']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,"Your score is :",p1)
    print(p2n,"your score is:",p2)
    print('thanks for playing')
    print("Have nice day")

def play():
    print('**********WELCOME TO JUMBLE WORD GAME*******************')
    p1name=input('player 1 ,Enter your name:  ')
    p2name=input('player 2 , Enter your name:  ')
    pp1=0
    pp2=0
    turn=0
    while(1):
      picked = choose()
      #comp.'s turn
      qn=jumble(picked)
      print (qn)
    #actual game
    
      if turn%2==0:
        print('Player 1:',p1name+'  its your turn......')
        p1word=input('guess the correct word: ')
        if p1word==picked:
            print('correct')
            pp1=pp1+1
            print('score of player1: ',pp1)
        else:
            print('better luck next time',picked)
            q = input('press 0 for continue and 1 for quit')
            c=int(q)
            print(c)
            if c==1:
                thank(p1name,p2name,pp1,pp2)
                break
        #player 2 ki turn
      else:
        print('Player 2:',p2name+'  its your turn......')
        p2word=input('guess the correct word:  ')
        if p2word==picked:
            print('correct')
            pp2=pp2+1
            print('points for player2',pp2)
        else:
            print('better luck next time')
            q = input('press 0 for continue and 1 for quit')
            c=int(q)
            print(c)
            if c==1:
                thank(p1name,p2name,pp1,pp2)
                
            break
      turn=turn+1    
    
play()