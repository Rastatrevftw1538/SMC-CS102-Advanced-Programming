##Sums of sum program Solution
##CS 102 Spring 2020
##Main supplied by Sauerberg

## SUBSET
# Will test all possible combinations from the set of numbers given
# and will try to sum to the given target value. If the target value
# is reached, it will return True, otherwise, it will return False.
#### INPUTS
# myset = set of numbers can use to build target with
# target = target number
# ans = solution set
## OUTPUT
# returns True = target can be a sum of a subset of myset
# return False = target cannot be a sum of a subset of myset

def subset(myset,target,ans = []):
    if target == 0:
        return True
    elif myset == []:
        return False
    elif len(myset) == 1:
        if myset[0] == target:
            return True
        return False
    else:
        n = myset[0]
        return subset(myset[1:],target - n,ans + [n]) or subset(myset[1:],target,ans)


## NSUBSET
# Will test all possible combinations from the set of numbers given
# and will try to sum to the given target value. It will then return the
# amount of combinations that sum to the target value.
## INPUTS
# myset = list of weights to use
# target = value trying to build using subsets of mylist
## RETURNS
# the number of ways.

def nsubset(myset, target,ans = []):
    if target == 0:
        return 1
    elif myset == []:
        return 0
    elif len(myset) == 1:
        if myset[0] == target:
            return 1
        return 0
    else:
        n = myset[0]
        return nsubset(myset[1:],target - n,ans + [n]) + nsubset(myset[1:],target,ans)
## subsetWeight
# This will try to take the target value and see if it is possible to reach 0
# if it is possible, it will return True, otherwise it will return False.
## INPUTS
# myset = list of weights
# target = value list is trying to reach to 0
## RETURNS
# True if it was able to reach 0 
# False if it was not able to reach 0 

def subsetWeight(myset,target ,ans = []):
    if target == 0:
        return True
    elif myset == []:
        return False
    elif len(myset) == 1:
        if myset[0] == target:
            return True
        return False
    else:
        n = myset[0]
        return subsetWeight(myset[1:],target - n,ans +[n]) or subsetWeight(myset[1:],target) or subsetWeight(myset[1:],target + n,ans +[n])

## MISSING
# Checking to see the smallest number that the set cannot reach
# and then returning that number to the main function.
## INPUTS
# myset = list of weights
## RETURNS
# target = the smallest value the target cannot reach


def missing(myset):
    target = 1
    
    go_on = True
    
    while go_on:
        check = subsetWeight(myset,target)
        
        if not check:
            return target
        elif target == sum(myset):
            return sum(myset) + 1
        else:
            target += 1


#Printer
#nicely prints a list.
# [3,5,7] --> "3 + 5 + 7"


def printer(ans, target):
    for i in ans[:-1]:
        print(i, "+", end=" ")
    print(ans[-1], "=", target)

from random import randrange
def main():
    print("Fun with weights! Give me the size of the set. (probably <=10)")
    #size = int(input("How large is our set? "))
    size = 6
    #s = set of positive integers
    s = []
    #maxx is the largest integer possible in our set
    maxx = 100

    #now create a list of size-many integers from 1 to maxx
    #Use a for loop with a test to the entries are unique
    #sort it at end, for pretty
    while len(s)<size: 
        newint = randrange(1, maxx)
        if not newint in s:
            s.append(newint)
    s.sort()

    #target1 = use about half of the elements of s
    target = randrange(size*maxx)//4
    ans = [] #the answer set
    print("The set s is", s)
    ssum = subset(s, target, ans)
    if ssum: 
        answer = "possible"
    else:
        answer = "impossible"
    print("It is", answer, "to make", target, "as a subset sum of s.")
    
    #if ssum:
        #printer(ans, target)
    print("The integer", target, "is possible in", nsubset(s, target, ans), "ways.")

    print("The smallest weight not measurable with s is", missing(s))
main()
