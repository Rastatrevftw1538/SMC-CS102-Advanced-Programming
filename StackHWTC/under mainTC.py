# Trevor Cardoza
# CS 102 Spring 2020
# March 24th
# Program: Under
# A program that takes one stack and places
# it under another stack.

from stackprint import Stack


# under
# Places the first stack under the second stack.
#
# It takes a two Stacks as inputs.
#
# It prints nothing.
#
# It returns the new stack with the first stack input
# under the second stack input.

def under(underStack, topStack):
    tempStack = Stack()
    newStack = Stack()
    for i in range(0,underStack.size()): # Reverses the Stack
        tempStack.push(underStack.pop())
    for i in range(0,tempStack.size()): # Then puts the Reverse of temp into final stack 
        newStack.push(tempStack.pop())
    for i in range(0,topStack.size()): # Reverses the Stack
        tempStack.push(topStack.pop())
    for i in range(0,tempStack.size()): # Then puts the Reverse of temp into final stack
        newStack.push(tempStack.pop())
    return newStack

def main():
    letters = "ABCDEFG"
    st1 = Stack()
    for c in letters:
        st1.push(c)

    moreletters = "RSTUVW"
    st2 = Stack()
    for c in moreletters:
        st2.push(c)

    st1 = under(st2, st1)
    print(st1, " =RSTUVWABCDEFG")

    print(st2, " = RSTUVW")


main()
