largest = None #this variable is null
smallest = None #this variable is null

while True:
    value = raw_input("Enter a number:")
    if value == "done": break #break the loop while
    try: 
       number = int(value) #convert the value to Integer
    except: 
       print "Please a valid input"
       continue
    
    #Test each input
    
    if largest is None:
        largest = number
    elif number >  largest:
        largest = number

    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number

#show the result
print "Maximum is", largest
print "Minimum is", smallest
