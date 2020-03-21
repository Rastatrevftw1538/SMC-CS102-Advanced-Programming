# Trevor Cardoza
# CS 102 Spring 2020
# March 24th
# Program: Remove
# A program that removes the instance
# of a stack closest to the top and returns the
# stack still in order.


from stackprint import Stack

# remove
# Removes the target item from the top of the stack.
#
# It takes a Stack and a target item as inputs.
#
# It prints nothing.
#
# It returns the new stack in it's original order with
# the target removed.

def remove(stack,target):
    tempStack = Stack()
    newStack = Stack()
    count = 0
    for entry in stack.items[::-1]:
        if entry != target:
                tempStack.push(entry)
        else:
            if count > 0:
                tempStack.push(entry)
            else:
                count += 1
    for rev in tempStack.items[::-1]:
        newStack.push(rev)
    return newStack

def main():
    letters = "ABCDEFG"
    st = Stack()
    for c in letters:
        st.push(c)

    first = "D"
    st = remove(st, first)   #now st should be [ABCEFG)
    print("after first", st)  #cheating a bit - the stack is a list so we print it

    second = "H"
    st = remove(st, second)  #st should still be [ABCEFG)
    print("after second", st)

    third = "A"
    st = remove(st, third) #st should now be [BCEFG)
    print("after third", st)
main()
