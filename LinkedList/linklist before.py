## NODE Class. Consists only of (a) a box for data called "data", and
# (b) a 'pointer' to another node called "next".
#
# We implement two "getter" methods and two "setter" methods

class Node:
    def __init__(self,initdata=""):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkList:
    ## LinkList() creates a new list that is empty.
    ## It needs no parameters and returns an empty list.
    def __init__(self):
        pass

    ## isEmpty() tests to see whether the list is empty.
    ## It needs no parameters and returns a boolean value.        
    def isEmpty(self):
        pass

    ## size() is the number of items in the list.
    ## It needs no parameters and returns a non-negative int.
    def size(self):
        pass
        
    ## add(item) prepends an item to the front of list.
    ## It needs the item and returns nothing. 
    def add(self,item):
        pass
    
    ## append(item) adds a new item as the new last item in the list 
    ## It needs the item and returns nothing.
    def append(self, item):
        pass

    ## search(item) searches for the item in the list.
    ## It needs the item and returns True/False depending on if item is found 
    def search(self, item):
        pass

    ## remove(item) removes the item from the list.
    ## It needs the item and modifies the list.
    ## If the item is not found, nothing happes
    def remove(self, item):
        pass

    # PRACTICE #1
    ## index(item) returns the position of item in the list.
    ## It needs the item and returns the index.
    ## If item is not in the list, returns -1
    ##
    ## HINT: Finding "where" an item is is a lot like finding "if" an item is present
    def index(self, item):
        pass

    # PRACTICE #2
    ## insert(pos,item) adds a new item to the list at position pos.
    ## Note: Position 0 is the head
    ## It needs the position and the item
    ## If pos is off the end of the list (ie > size() ), put item last
    ##
    ## HINT: Draw a motion picture first. This one is harder because you will
    ## need to carry with you _two_ pointers. Review "remove" before starting
    def insert(self, pos, item):
        pass
    
    # PRACTICE #3
    ## pop() removes and returns the last item in the list.
    ## It needs nothing and returns an item.
    ## If the linked list is empty it returns None
    ##
    ## HINT: Draw a picture first -- what steps in what order must
    ## happen for pop() to work. 
    def pop(self):
        pass






    ## Nice form of printed linked-list
    def __str__(self):
        if self.size() == 0 :
            return "empty"
        current = self.head
        mystring = str (current.getData() )

        while current.getNext() != None:
            current = current.getNext()
            mystring +=" -> "
            mystring += str(current.getData())
        return mystring 



