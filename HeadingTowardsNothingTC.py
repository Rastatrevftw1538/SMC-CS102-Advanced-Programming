# Trevor Cardoza
# CS 102 Spring 2020
# March 3rd
# Program: HeadingTowardsNothing
# A program that takes a list of numbers
# in a geometric shape and goes around clockwise
# subtracting and taking the absolute value until
# all of the values equal zero.
import random

# Main
# The main organization of all the functions and the order
# in which they are called.
#
# It doesn't take any input.
#
# It prints the inputs for initial(), amount of rounds,
# and prints the information for total rounds,
# current list of numbers, and the information
# for original list, final list and how many rounds
# it took to equal all the numbers in the list to Zero.
#
# It returns nothing.


def main():
    numOfRounds = 0
    rounds = 1
    numList = initial(
        int(input("Type how many numbers you want to calculate: ")))
    currentList = update(numList)
    numOfRounds += 1
    rounds = int(input("How many more rounds should be executed?: "))
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
    print(f"Final list is: {currentList}")
    print(f"The original list is: {numList}")
    raise Exception("End of program!")

# Initial
#
# Controls the beginning of the program and asks for how
# many random numbers should be in the list.
#
# It takes a int for the number of random numbers to add.
#
# It prints the starting list of random numbers of
# the given length that was asked as a input.
#
# It returns the list of random numbers.


def initial(num):
    numList = []
    for i in range(num):
        numList.append(random.randint(0, 40))
    print(f"Your starting list is: {numList}")
    return numList


def update(numList):
    newList = numList.copy()
    backNum = 0
    for i in range(0, len(numList)):
        sub = abs(numList[i-1] - numList[i])
        newList[i] = sub
    return newList


def finished(finalList):
    numOfZeros = 0
    for i in finalList:
        if i == 0:
            numOfZeros += 1
            if numOfZeros == len(finalList):
                return True
        else:
            return False


main()
