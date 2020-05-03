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

    def doACheck(num):
        if num == target:
            return True
        elif num < target:
            return False


    for i in mylist[0:-1:leap]:
        if doACheck(i) != True:
            for x in mylist[mylist.index(i):0:-skip]:
                if doACheck(x) == True:
                    return True
                else:
                    for y in mylist[mylist.index(x):-1:1]:
                        if doACheck(y) == True:
                            return True
        else:
            return True
    for x in mylist[mylist.index(i):0:-skip]:
        if doACheck(x) == True:
            return True
        else:
            for y in mylist[mylist.index(x):-1:1]:
                if doACheck(y) == True:
                    return True
                else:
                    return False
    return False

def bigO(n):
    bigOForm = 2*math.sqrt(n)
    return bigOForm

def main():
    print(leapsearch([1,8,17,63,64,90,107,108],90,6,4))
    print(bigO(len([1,8,17,63,64,90,107,108])))

main()