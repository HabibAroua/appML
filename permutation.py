x=int(input("enter x \n"))
y=int(input("enter y \n"))

if(x>=y):
    x=x-y
    y=x+y
    x=y-x
    
else:
    y=y-x
    x=y+x
    y=x-y
        
print ("the value is ",x,y)