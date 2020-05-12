#TREVOR CARDOZA

import math

def skipsearch(mylist, target, skip):
    for i in mylist[0:-1:skip]:
        if i > target:
            for x in mylist[mylist.index(i):0:-1]:
                if x == target:
                    return True
                elif x < target:
                    return False
        elif i == target:
            return True
    for x in mylist[-1:0:-1]:
            if x == target:
                return True
            elif x < target:
                return False
    return False

"""def leapsearch(mylist, target, leap, skip):
    count = 0
    number = mylist[0]
    Done = False
    step = 1
    fOb = -1
    direcList = [leap,-skip,step]
    def doLoop(num=0,forOrBack = [],frontOrBack=-1):
        for loopNum in mylist[mylist.index(num):frontOrBack:forOrBack]:
            if frontOrBack == -1:
                if loopNum > target:
                    return(loopNum)
                elif loopNum == target:
                    return  True
            else:
                if loopNum < target:
                    return(loopNum)
                elif loopNum == target:
                    return  True
        return False

    while Done != True:
        number = doLoop(number,direcList[count],fOb)
        if number == True:
            Done == True
            return number
        elif number == False:
            Done == True
            return number
        if count % 2 == 0:
            fOb = 0
        else:
            fOb = -1
        count += 1

"""
def bigO(n):
    bigOForm = 2*math.sqrt(n)
    return bigOForm

# AUX
#
# Desc:
# loops through the list till it finds or goes higher then the list and then
# returns the index. if the index (i) is higher then 0, then go back by 
# the skip or step value till you land on target.
# 
# Input:
# inputs include:
#
# mylist (a list)
# Target (int)
# value, which is the step value
# and i for index which defaults to 0
# 
# Returns:
# 
# Will either return the index if it is higher then the target,
# True if it is equal to the target or False is it is higher then 
# the target and the step value is equal to 1.


def aux(mylist, target, value, i=0):
    #assume value = leap, skip, or 1
    #If i is not zero then go back by value before i was greater.
    if i != 0:
        i -= value
    #Loops through the list to find the target.
    while mylist[i] <= target:
        if mylist[i]== target:
            return True
        else:
            i += value
    if mylist[i] > target:
        #if you pass the target and the step value is equal to 1
        # then the target is not in the list.
        if value == 1:
            return False
        return i 


def leapsearch(mylist, target, leap, skip):
    i = 0

    i1 = aux(mylist, target, leap, i)

    i2 = aux(mylist, target, skip, i1)

    return aux(mylist, target, 1, i2)

