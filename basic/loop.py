#!/usr/bin/env python
list1=["Nada","Sana","Mariem","Siwar"]
tup1=(5,8,2)

#First loop
for item in list1:
    print item
#Second loop
for item in tup1:
    print item
#Third loop
for i in range(0,10):
    print i
#4th loop
print "Element of array using index"
#5th loop
for i in range(0,len(list1)):
    print list1[i]
#6th loop
print "Example"
#7th loop
for i in range(0,11,2):
    print i
    
print "Double loop"
#last loop
for i in range(0,5):
    for j in range(0,3):
        print i*j