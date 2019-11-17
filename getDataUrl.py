#!/usr/bin/env python
# a use of raw_input() 

import urllib.request 
import urllib.parse 

def readFile(fileName):
    with open(fileName,'r') as f:
        for line in f:
            print(line, end='')

def writeFile(fileName,line):        
    with open(fileName,'w') as f:
        f.write(line)
        
def addNewLineInFile(fileName,name):
    hs = open(fileName,"a")
    hs.write(name+"\n")
    hs.close()
    
def createNewFile(fileName):
    f= open(fileName,"w+")
    
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