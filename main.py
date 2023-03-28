def openFile(name):
    file = open(f"{name}.txt", 'r')
    return file

def printLines(file, numberOfFile):
    print(f"======={numberOfFile}=======")
    for line in file:
        print(line, end="")
    print("\n========================")

def getLinesMassive(file):
    linesMassive = []
    for line in file:
        linesMassive.append(line)
    return linesMassive

firstFile = openFile("firstFile")
secondFile = openFile("secondFile")
printLines(firstFile, "First File")
printLines(secondFile, "Second File")
firstMassive = getLinesMassive(firstFile)

