# Trevor Cardoza
# CS 102 Spring 2020
# April 1st
# Program: Circle Dequeue

# A program that can add and remove items
# from the front and the back of a line.



class Deque:

    # __init__
    # The initializing function that determines the
    # format of the class and it's inputs.
    #
    # Inputs of self and max line size
    # that defaults to 200.
    #
    # It does not print.
    #
    # It does not return.

    def __init__(self, maxsize = 200):
        self.maxsize = maxsize
        self.items = [None]*maxsize 
        self.front = maxsize - 1   
        self.rear = maxsize -1
        self.size = 0 

    # isEmpty
    # Checks to see if Queue is empty or not.
    #
    # Inputs of self.
    #
    # It does not print.
    #
    # It returns True or False.

    def isEmpty(self):
        return self.size == 0



    def addFront(self, item):
        if self.size == self.maxsize:
            print("Line is Full! Person was not added to line!")
        else:
            if not self.isEmpty():
                    if self.front == 0:
                        self.front = self.maxsize - 1
                    else:
                        self.front -= 1
        self.cust[ self.front ] = item
        self.size += 1

    # join
    # Adds a item to the rear of the line.
    #
    # Inputs of self and single value (float,int,str,etc).
    #
    # It does not print.
    #
    # It does not return.

    def addRear(self, item):
        if self.size == self.maxsize:
            print("Line is Full! Person was not added to line!")
        else:
            if not self.isEmpty():
                    if self.rear == 0:
                        self.rear = self.maxsize - 1
                    else:
                        self.rear -= 1
        self.cust[ self.rear ] = item
        self.size += 1

    def removeFront(self):
        if self.isEmpty():
            print("Queue is Empty! None was returned")
            return None    
        else:
            val = self.items[self.front]
            self.items[self.front] = None
            if self.front != self.rear:
                if self.front == 0:
                    self.front = self.maxsize -1
                else:
                    self.front -= 1
            self.size -= 1
            return val

    def removeRear(self):
        if self.isEmpty():
            print("Queue is Empty! None was returned")
            return None    
        else:
            val = self.items[self.rear]
            self.items[self.rear] = None
            if self.rear != self.front:
                if self.rear == 0:
                    self.rear = self.maxsize -1
                else:
                    self.rear -= 1
            self.size -= 1
            return val

    # size
    # Checks the size of the whole line.
    #
    # Inputs of self.
    #
    # It does not print.
    #
    # It returns the size of the line.

    def size(self):
        return self.size