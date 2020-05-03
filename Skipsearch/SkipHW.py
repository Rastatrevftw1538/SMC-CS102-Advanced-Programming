#TREVOR CARDOZA

import math

def skipsearch(mylist, target, skip):
    for i in mylist[0:-1:skip]:
        print(i,"i")
        if i > target:
            for x in mylist[mylist.index(i):0:-1]:
                print(x,"x")
                if x == target:
                    return True
                elif x < target:
                    return False
        elif i == target:
            return True
    for x in mylist[-1:0:-1]:
            print(x,"x")
            if x == target:
                return True
            elif x < target:
                return False
    return False

def leapsearch(mylist, target, leap, skip):
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


def bigO(n):
    bigOForm = 2*math.sqrt(n)
    return bigOForm

def main():
    print(leapsearch([1,8,17,63,64,90,107,108],90,6,4))
    print(bigO(len([1,8,17,63,64,90,107,108])))

main()