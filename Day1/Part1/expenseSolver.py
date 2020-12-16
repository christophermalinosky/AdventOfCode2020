import os

def solveExpense(fileName, goal):
    folderPath = os.path.dirname(os.path.abspath(__file__))
    inputFile = os.path.join(folderPath, "input.txt")
    input = open(inputFile, "r")

    halfs = 0
    inputSet = set()
    for inputNumber in input:
        number = int(inputNumber[:-1])
        inputSet.add(number)
        if goal % 2 == 0 and goal / 2 == number:
            halfs += 1

    for inputNumber in inputSet:
        if goal % 2 == 0 and goal / 2 == inputNumber:
            if halfs >= 2:
                return inputNumber * (goal - inputNumber)
        elif goal - inputNumber in inputSet:
            return inputNumber * (goal - inputNumber)

print(solveExpense("input.txt", 2020))
        