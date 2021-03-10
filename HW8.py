# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:49:25 2021

@author: craig
"""

# Homework #8 - I/Os - Note Taking

filename = input("Please enter the file name: ")
#Does file exist
import os.path
from os import path

def main():

	print ("Is it a File? " + str(path.isfile("./" + filename)))
if __name__== "__main__":
    print("This file does not exist, please enter your text")
    text = input("Please enter your text: ")
    with open(filename,"w") as write_file:
        write_file.write(text + "\n")

else:
    print("File located. ")
    action = input("What would you like to do with the file?\nRead\nDelete and start over\nAppend the file")
    
    if action == "Read":
        print("Show contents of file: ")
        with open (filename, "r") as read_file:
            print(read_file.read())
    elif action == "Delete and start over":
        os.remove("./" + filename)
        print("{} File has been deleted.".format(filename))
        with open(filename, "w") as write_file:
            write_file.write("")
    elif action == "Append the file":
        text = input("Please add your text: ")
        with open(filename, "a") as append_file: 
            append_file_write(text + "\n")
            
        