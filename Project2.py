"""
Created on Fri Mar  5 16:05:36 2021

@author: craig
"""
#Project #2

import time
from time import sleep

name = input("What is your name? ")

print("Hello, " + name, "Time to Play Hangman!")

time.sleep(1)

word = "python"
wrd = ''
 
chance = 10
 
while chance > 0:         
    failed = 0            
    for spell in word:   
        if spell in wrd:    
            print (spell)   
        else:
            print( "_")    
            failed += 1   
 
    if failed == 0:        
        print( "You won, Congratulations!" ) 
        break             
 
    guess = input("Guess a Letter: ") 
 
    wrd = wrd+guess                    
 
    if guess not in word:  
        chance -= 1       
        print ("Wrong Guess! Try Again")
        print ("You have", + chance, 'more turn(s)' )
        if chance == 0:           
            print ("You Lose!" )