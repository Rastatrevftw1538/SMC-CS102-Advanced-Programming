# Trevor Cardoza
# CS 102 Spring 2020
# March 3rd
# Program: HeadingTowardsNothing
# A solitare game that you roll or hold to get summed points
# until you hold. The goal is to reach the goal in as little
# turns as possible.
import random


def initial():
    numList = []
    num = int(input("Type how many numbers you want to calculate: "))
    for i in range(num):
        numList.append(random.randint(0, 40))
    print(f"Your starting list is: {numList}")
    return numList


def main():
    numOfRounds = 0
    rounds = 1
    numList = initial()

    currentList = update(numList)
    numOfRounds += 1
    rounds = moreRounds(
        int(input("How many more rounds should be executed?: ")))
    print(f"Your current list of numbers is: {currentList}")
    print(f"The total number of rounds to run is: {rounds}")
    while rounds > 0:
        currentList = update(currentList)
        fin = finished(currentList)
        if fin:
            print(f"Final list is: {currentList}")
            print(f"The original list is: {numList}")
            print(f"It took {numOfRounds} to reach all Zeros")
            raise Exception("End of program!")
        else:
            numOfRounds += 1
            rounds -= 1
    raise Exception("End of program!")


def finished(finalList):
    numOfZeros = 0
    for i in finalList:
        if i == 0:
            numOfZeros += 1
            if numOfZeros == len(finalList):
                return True
        else:
            return False


def update(numList):
    newList = numList.copy()
    backNum = 0
    for i in range(0, len(numList)):
        sub = abs(numList[i-1] - numList[i])
        #print(f"{numList[i-1]} - {numList[i]} = {sub}")
        newList[i] = sub
    # print(newList)
    return newList


def moreRounds(num):
    return abs(num)


main()
