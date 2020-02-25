# CS 102 Spring 2020
# Fun with Functions

# GOAL: Build out most of these functions, which includes both their code
#  and the full function comments.

# It is not necessarily clear which of the functions work for which of
# strings, tuples and lists. Some maybe for all, some maybe only for
# one or two. Figuring out which, and the clearly indicating this, is
# part of the work.

import random

# make_list function
# makes a list of integers
# INPUT: size = the desired length of the list
# limit = integers will be in range [1, limit]
## PRINTS: nothing
# RETURNS: a list of length 'size' containing integers chosen
# randomly in the range [1, limit]


def make_list(size, limit):
    mylist = []
    for i in range(size):
        mylist.append(random.randint(1, limit+1))
    return mylist

# make_list_alpha function
# makes a list of lower case letters
# INPUT: size = the desired length of the list
## PRINTS: nothing
# RETURNS: a list of length 'size' containing lower case letters
# that is, chosen randomly from 'a' to 'z'


def make_alpha_list(size):
    mylist = []
    for i in range(size):
        num = random.randint(1, 100) % 26
        char = chr(97+num)
        mylist.append(char)
    return mylist

# takes a collection of objects and returns the sum of
# the objects in that collection


def summer(objList):
    ans = 0
    for i in objList:
        ans += i
    return(ans)

# takes a linear collection of objects and returns the product
# the objects in that collection


def producter(objList):
    ans = 1
    for i in objList:
        ans *= i
    return(ans)

# takes a linear collection of objects and returns the largest of
# the objects in that collection
# Do with a loop, not with 'max' function


def maxxy(objList):
    largest = 0
    for i in objList:
        if i > largest:
            largest = i
    return (largest)

# takes a linear collection of objects and returns the 2nd largest of
# the objects in that collection
# Do with a loop, not with 'max' function


def second_max(objList):
    largest = 0
    sec_largest = 0
    past_larg_num = 0
    past_sec_larg_num = 0
    for i in objList:
        if i > largest:
            past_larg_num = largest
            largest = i
        if largest <= past_larg_num:
            largest = past_larg_num
        if i < largest:
            if i > sec_largest:
                past_sec_larg_num = sec_largest
                sec_largest = i
            if sec_largest <= past_larg_num:
                sec_largest = past_larg_num
            if sec_largest <= past_sec_larg_num:
                sec_largest = past_sec_larg_num
    return (sec_largest)

# takes a linear collection of o and removes from it all the even
# numbers in the collection


def remove_evens(objList):
    new_list = objList.copy()
    for i in objList:
        if i % 2 == 0:
            new_list.remove(i)
    return(objList)

# takes a linear collection of objects and integer and returns a new
# collection composed of all elements of the original collection that
# at least as large as the given object


def large(objList, num):
    new_list = []
    for i in objList:
        if i >= num:
            new_list.append(i)
    return(new_list)
    # takes a linear collection of objects, and one object, and prints the number
    # times that object occurs in the collection
    # do via a loop, not with the count function


def counter(objList, find):
    num = 0
    for i in objList:
        if i == find:
            num += 1
    return(num)
# takes a linear collection of objects modifies it so that the first
# and last elements have been swapped. So 1-3-5-7 becomes 7-3-5-1


def swapper(objList):
    new_list = objList.copy()
    new_list[0] = objList[-1]
    new_list[-1] = objList[0]
    return(new_list)

# takes a linear collection of objects and two other objects obj1 and obj2
# replaces all the obj1 by obj2 (if any) and then prints the result
# do via a loop


def exchanger(objList, find, replace):
    new_list = objList.copy()
    for i in objList:
        if i == find:
            new_list[new_list.index(i)] = replace
    return(new_list)


def main():
    ###### START OF CODE ##############
    size = 11    # length of the lists we are dealing with
    height = 12     # our numbers will be in the range [1,height]
    list1 = make_list(size, height)
    list2 = make_alpha_list(size)
    print(list1)
    print(list2)
    input()  # is like a 'pause'

    # SUMMER
    summer(list1)
    print("The sum of the elements of", list1, "is", summer(list1))
    ans = summer(list1)
    print(ans)

    print(producter(list1))
    print(maxxy(list1))
    print(second_max(list1))
    print(remove_evens(list1))
    print(large(list1, random.randint(1, 5)))
    print(counter(list2, input("Enter a letter: ")))
    print(swapper(list2))
    print(exchanger(list2, input("Enter a letter to find: "),
                    input("Enter a letter to replace: ")))


main()
