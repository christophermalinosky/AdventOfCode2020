import os

def solveExpense(fileName, goal):
    folderPath = os.path.dirname(os.path.abspath(__file__))
    inputFile = os.path.join(folderPath, "input.txt")
    input = open(inputFile, "r")

    inputSet = set()
    for inputNumber in input:
        inputSet.add(int(inputNumber[:-1]))

    for inputNumber in inputSet:
        if goal - inputNumber in inputSet:
            return inputNumber * (goal - inputNumber)

print(solveExpense("input.txt", 2020))
        