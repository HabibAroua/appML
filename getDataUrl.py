#!/usr/bin/env python
# a use of raw_input() 

import urllib.request 
import urllib.parse 

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