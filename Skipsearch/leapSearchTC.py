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

