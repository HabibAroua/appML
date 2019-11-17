#!/usr/bin/env python
# a use of raw_input() 

import urllib.request 
import urllib.parse 

def readFile(fileName):
    try:
        with open(fileName,'r') as f:
            for line in f:
                print(line, end='')
    except Exception as e : 
        print(str(e))

def writeFile(fileName,line):
    try:
        with open(fileName,'w') as f:
            f.write(line)
    except Exception as e : 
        print("This file is not found : "+str(e))
        
def addNewLineInFile(fileName,name):
    try:
        hs = open(fileName,"a")
        hs.write(name+"\n")
        hs.close()
    except Exception as e : 
        print(str(e))
        
def createNewFile(fileName):
    try:
        f= open(fileName,"w+")
    except Exception as e : 
        print(str(e))
    
def main():
    try:
        c='Y'
        while c=='y' or c=='Y' :
            url = input("Enter an URL : ")
            x = urllib.request.urlopen(url) 
            print(x.read())
            c = input("Continue ? Y/N : ")
  
    except Exception as e : 
        print(str(e))
        main()
        
main()