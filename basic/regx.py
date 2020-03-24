import re

#pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
#user_input = input()
#if(re.search(pattern,user_input)):
#    print('this an email')
#else:
#    print('this is not email')
    
#test image file

pattern = "[a-zA-Z0-9]\.(jpeg|gif|png)"
user_input = input()
if(re.search(pattern,user_input)):
    print('this a picture')
else:
    print('this is not a picture')