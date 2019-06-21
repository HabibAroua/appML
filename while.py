#!/usr/bin/env python
print "Example normal"
c=0
while c<5:
    print c
    c=c+1
print "Example using break"
c=0
while c<5:
    if c==3:
        break
    print c
    c=c+1
print "Example using continue"
c=0
while c<5:
    c=c+1
    if c==3:
        continue
    print c
print "Example using pass"
c=0
while c<5:
    c=c+1
    if c==3:
        pass
    print c