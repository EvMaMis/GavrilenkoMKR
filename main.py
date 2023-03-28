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

def writeToFile(fileName, line):
    with open(f"{fileName}.txt", 'r+') as file:
        file.seek(0, 2)
        file.write(line)

def compareMassives(first, second):
    for line in first:
        for secondLine in second:
            if line == secondLine:
                print(line)
                first.remove(line)
                second.remove(secondLine)
                writeToFile("same", line)
        

firstFile = openFile("firstFile")
secondFile = openFile("secondFile")


firstMassive = getLinesMassive(firstFile)
secondMassive = getLinesMassive(secondFile)

print(firstMassive)

compareMassives(firstMassive, secondMassive)
