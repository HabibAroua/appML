#!/usr/bin/env python
# a use of raw_input() 

import urllib.request 
import urllib.parse 
import sys
sys.path.append('HTMLtoJSONParser.py')
import HTMLtoJSONParser
from HTMLtoJSONParser import *

def readFile(fileName):
    try:
        with open(fileName,'r') as f:
            for line in f:
                print(line, end= '')
    except Exception as e : 
        print(str(e))

def writeFile(fileName,line):
    try:
        with open(fileName,'w') as f:
            f.write(line)
    except Exception as e : 
        print("This file is not found : "+str(e))
        
def addNewLineInFile(fileName,line):
    try:
        hs = open(fileName,"a")
        hs.write(line+"\n")
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
        choice = input("Do you want to create new file Y/N ? : ")
        if choice == 'Y' or choice == 'y':
            createNewFile(input("File name : "))
        c='Y'
        while c=='y' or c=='Y' :
            url = input("Enter an URL : ")
            x = urllib.request.urlopen(url)
            s=x.read()
            print(s)
            choice='N'
            choice = input ("Do you want to store this content in file ? : Y/N ")
            if choice == 'Y' or choice == 'y' :
                addNewLineInFile(input('File name : '),str(s))
            c = input("Continue ? Y/N : ")
        print ('Show the content of file')
        readFile(input("Show content of file : "))
  
    except Exception as e : 
        print(str(e))
        main()
content = '<html><body><div class="an_example"><p>one paragraph</p></div></body></html>'
js = HTMLtoJSONParser.to_json(content)
print (js)
main()