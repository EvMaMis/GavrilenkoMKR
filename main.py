def openFile(name):
    file = open(f"{name}.txt", 'r')
    return file

def printLines(file):
    for line in file:
        print(line, end="")

def getLinesMassive(file):
    linesMassive = []
    for line in file:
        linesMassive.append(line)
    return linesMassive

firstFile = openFile("firstFile")
secondFile = openFile("secondFile")
firstMassive = getLinesMassive(firstFile)
print(firstMassive[2])

