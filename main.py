def openFile(name):
    file = open(f"{name}.txt", 'r')
    return file

def printLines(file):
    for line in file:
        print(line, end="")

firstFile = openFile("firstFile")
secondFile = openFile("secondFile")
printLines(firstFile)
