def openFile(name):
    file = open(f"{name}.txt", 'r')
    return file

def printLines(file, numberOfFile):
    print(f"======={numberOfFile}=======")
    for line in file:
        print(line)
    print("\n========================")

def getLinesMassive(file):
    linesMassive = []
    for line in file:
        linesMassive.append(line)
    return linesMassive

def writeToFile(fileName, line):
    with open(f"{fileName}.txt", 'r+') as file:
        file.seek(0, 2)
        file.write(line)

def compareMassives(first, second):
    for line in first:
        for secondLine in second:
            if line == secondLine:
                first.remove(line)
                second.remove(secondLine)
                writeToFile("same", line)
    for line in first:
        writeToFile("diff", line)
    for secondLine in second:
        writeToFile("diff", secondLine)

def closeFile(name):
    with open(f"{name}.txt", 'r+') as f:
        f.seek(0, 0)

firstFile = openFile("firstFile")
secondFile = openFile("secondFile")

firstMassive = getLinesMassive(firstFile)
secondMassive = getLinesMassive(secondFile)

printLines(firstMassive, "First Massive")
printLines(secondMassive, "Second Massive")

compareMassives(firstMassive, secondMassive)

closeFile("diff")
closeFile("same")