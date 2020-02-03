#!/usr/bin/env python
class Parent:
    def __init__(self):
        print "This is the parent class"

    def parentFunction(self):
        print "This is the parent function"

p=Parent()

class Child(Parent):
    def __init__(self):
        print "This is the child class"

    def childFunction(self):
        print "This is the dhild function"