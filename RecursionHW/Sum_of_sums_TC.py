##Sums of sum program Solution
##CS 102 Spring 2020
##Main supplied by Sauerberg

## SUBSET
# can target be build with a subset of myset??
#### INPUTS
# myset = set of numbers can use to build target with
# target = target number
# ans = solution set
## OUTPUT
# returns True = target can be a sum of a subset of myset
# return False = target cannot be a sum of a subset of myset
## SIDE EFFECT
# lists are mutable. So if an element from myset is useful, add it total
# the list ans. This will (eventually) allow us to see how target is built

def subset(myset,target,ans = []):
    if target == 0 and ans != []:
        return True
    for i in range(len(myset)):
        if subset(myset[:i] + myset[i+1:],target - myset[i]):
            return True
    return False
print(subset([1,3,4,5],5))
'''
def isSubsetSum(set,n, sum) : 
    
    # Base Cases 
    if (sum == 0) : 
        return True
    if (n == 0 and sum != 0) : 
        return False
   
    # If last element is greater than 
    # sum, then ignore it 
    if (set[n - 1] > sum) : 
        return isSubsetSum(set, n - 1, sum); 
   
    # else, check if sum can be obtained 
    # by any of the following 
    # (a) including the last element 
    # (b) excluding the last element    
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1]) 

## NSUBSET
# how many ways can target be built as a subset of myset??
## INPUTS
# myset = list of weights to use
# target = value trying to build using subsets of mylist
## RETURNS
# the number of ways.

def nsubset(myset, target,ans,count = 0, listThing = []):
    if (target == 0) :
        return count +1
    if (ans == 0 and target != 0) : 
        return 0

    if (myset[ans - 1] > target) : 
        return nsubset(myset, target, ans -1,count);
    
    #if nsubset(myset, target, ans -1,count):
        #print(myset[ans-1])
    #return 
    #if nsubset(myset, target-myset[ans-1], ans-1,count):
        #print(myset[ans-1])
    return nsubset(myset, target, ans -1,count) or nsubset(myset, target-myset[ans-1], ans-1,count)
    #return nsubset(myset, target, ans -1,count)

#print(nsubset([2, 34, 35, 46, 49, 67, 78],85,7))
## MISSING
# function producing 'first weight that can't be weighed'
## Input: myset = list of weights
def missing(myset):
    pass

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
    print("The integer", target, "is possible in", nsubset(s, target ,size), "ways.")

    print("The smallest weight not measurable with s is", missing(s))
main()
'''