import os

def solveExpense(fileName, goal):
    folderPath = os.path.dirname(os.path.abspath(__file__))
    inputFile = os.path.join(folderPath, "input.txt")
    input = open(inputFile, "r")

    inputList = []
    for inputNumber in input:
        inputList.append(int(inputNumber[:-1]))

    input.close()

    numNumbers = len(inputList)
    for firstIndex in range(numNumbers):
        for secondIndex in range(firstIndex + 1, numNumbers):
            for thirdIndex in range(secondIndex + 1, numNumbers):
                firstNumber = inputList[firstIndex]
                secondNumber = inputList[secondIndex]
                thirdNumber = inputList[thirdIndex]
                if firstNumber + secondNumber + thirdNumber == goal:
                    return firstNumber * secondNumber * thirdNumber

print(solveExpense("input.txt", 2020))
        