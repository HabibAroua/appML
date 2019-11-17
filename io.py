def readFile(fileName):
    try:
        with open(fileName,'r') as f:
            for line in f:
                print(line, end='')
    except Exception as e : 
        print(str(e))

def writeFile(fileName,line):
    try:
        with open(fileName,'w') as f:
            f.write(line)
    except Exception as e : 
        print("This file is not found : "+str(e))
        
def addNewLineInFile(fileName,name):
    try:
        hs = open(fileName,"a")
        hs.write(name+"\n")
        hs.close()
    except Exception as e : 
        print(str(e))
        
def createNewFile(fileName):
    f= open(fileName,"w+")
    
addNewLineInFile("test.txt","Habib")
readFile("test.txt")
#createNewFile('hello.txt')