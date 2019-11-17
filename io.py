def readFile(fileName):
    with open(fileName,'r') as f:
        for line in f:
            print(line, end='')

def writeFile(fileName,line):        
    with open(fileName,'w') as f:
        f.write(line)
        
def addNewLineInFile(fileName,name):
    hs = open(fileName,"a")
    hs.write(name+"\n")
    hs.close()
    
    
addNewLineInFile("test.txt","Habib")
readFile("test.txt")