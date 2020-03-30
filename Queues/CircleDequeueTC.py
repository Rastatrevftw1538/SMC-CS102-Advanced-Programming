# Trevor Cardoza
# CS 102 Spring 2020
# March 31st
# Program: Circle Dequeue
#
# A program that can add and remove items
# from the front and the back of a Queue
# while having the front and back be connected.



class CDeque:

    # __init__
    # The initializing function that determines the
    # format of the class and it's inputs.
    #
    # Inputs of self and max Queue size
    # that defaults to 10.
    #
    # It does not print.
    #
    # It does not return.

    def __init__(self, maxsize = 10):
        self.maxsize = maxsize
        self.items = [None]*maxsize 
        self.front = self.maxsize - 1   
        self.rear = self.maxsize -1
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

    # addFront
    # Adds a item to the front of the Queue then
    # moves the line backward by removing the last
    # item and equaling it to the item in front
    # of it.
    #
    # Inputs of self and single value (float,int,str,etc).
    #
    # It does not print.
    #
    # It does not return.

    def addFront(self, item):
        if self.size == self.maxsize:
            print("Queue is Full! Item was not added to Queue!")
        else:
            if self.front == 0:
                self.front = self.maxsize - 1
            else:
                for p in range(self.rear,self.maxsize):
                    itemMove = self.items[p]
                    if self.size > 0 and p > self.maxsize -self.size+self.size:
                        self.items[p-self.size+1] = itemMove
                    else:
                        self.items[p-1] = itemMove
            if self.items[0] != None:
                self.rear = 0
            self.items[ self.front ] = item
            '''if self.front != self.maxsize - 1:
                self.front -= 1'''
            if self.items[self.rear-1] != None and self.rear != 0:
                self.rear -= 1
            self.size += 1

    # addRear
    # Adds a item to the rear of the Queue then
    # moves the forward by removing the first item 
    # and equaling it to the item behind it.
    #
    # Inputs of self and single value (float,int,str,etc).
    #
    # It does not print.
    #
    # It does not return.

    def addRear(self, item):
        if self.size == self.maxsize:
            print("Queue is Full! Item was not added to Queue!")
        else:
            for p in range(self.front,self.rear-1,-1):
                itemMove = self.items[p]
                if self.size > 0 and p > self.maxsize -self.size+self.size:
                    self.items[p-self.size+1] = itemMove
                elif self.front != self.maxsize-1:
                    self.items[p+1] = itemMove
            if self.rear != self.front and self.items[self.rear] != self.items[self.rear+1]:
                self.rear -= 1
            if self.items[0] != None:
                self.rear = 0
            self.items[ self.rear ] = item
            if self.front < self.maxsize-1:
                if self.items[self.front+1] != None:
                    self.front += 1
            self.size += 1

    # removeFront
    # Removes and returns the item in the front of the Queue.
    #
    # Inputs of self.
    #
    # It does not print.
    #
    # It returns the item that was removed.

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

    # removeRear
    # Removes and returns the item in the back of the Queue.
    #
    # Inputs of self.
    #
    # It does not print.
    #
    # It returns the item that was removed.

    def removeRear(self):
        if self.isEmpty():
            print("Queue is Empty! None was returned")
            return None    
        else:
            val = self.items[self.rear]
            self.items[self.rear] = None
            if self.rear != self.front:
                    self.rear += 1
            self.size -= 1
            return val

    # size
    # Checks the size of the whole Queue.
    #
    # Inputs of self.
    #
    # It does not print.
    #
    # It returns the size of the Queue.

    def size(self):
        return self.size
    
    #### KEEP THIS
    def __str__(self):
    ## we don't print queues but to see how we did in our design
    ## this let's us see the queue. 
        temp = CDeque()
        stringy = "["
        for a in self.items:
            if a == None:
                stringy += "_"
            else:
                stringy += str(a)
        #return stringy+")" + " size =" + str(self.size) + ", f=" + str(self.front) +", r=" + str(self.rear)
        return stringy+")" 