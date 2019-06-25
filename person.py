#!/usr/bin/env python

class Person:
    def __init__(self, name , age):
        self.name=name
        self.age=age
        
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name=name
        
    def getAge(self):
        return self.age
    
    def setAge(self , age):
        self.age = age
        
p=Person("Sana",25)
p.setName("Eya")
p.setAge(23)
print "name is ",p.getName()
print "age is ",p.getAge()