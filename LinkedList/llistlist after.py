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
        self.head = None

    ## As for stacks and queues, we don't usually print entire linked lists.
    ## But as we learn, here is a __str__ method that does that.
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
            

    ## isEmpty() tests to see whether the list is empty.
    ## It needs no parameters and returns a boolean value.        
    def isEmpty(self):
        return self.head == None

    ## size() is the number if items in the list.
    ## It needs no parameters and returns a non-negative int.
    def size(self):
        if self.head == None:   #if list is empty, answer is 0
            return 0
        count = 1
        current = self.head   #current is like a cursor, 'pointing' at a node
                            # it starts at the head of the list

        while current.getNext() != None:  #IMPORTANT test for llists
            count += 1
            current = current.getNext()
        return count


    ## add(item) prepends an item to the front of list.
    ## It needs the item and returns nothing. 
    def add(self,item):
        temp = Node(item)    ##create a new node
        temp.setNext(self.head)    ## Cause new node to point to current head
        self.head = temp      ## Cause new node to be new head


    ## append(item) adds a new item as the last item in the list 
    ## It needs the item and returns nothing. 
    def append(self, item):
        temp = Node(item)   #create the node we want to append

        if self.isEmpty():
            self.head = temp
        else:
            current = self.head     #get cursor that will march through list
            while current.getNext() != None:    # here is that test again
                current = current.getNext()
            current.setNext( temp )     #current now is 'tail'. Cause new node to be new tail


    ## search(item) searches for the item in the list.
    ## It needs the item and returns True/False depending on if item is found 
    def search(self, item):
        if self.isEmpty():
            return False
        current = self.head
        while current.getData() != item and current.getNext() != None:
            current = current.getNext()
        return current.getData() == item   #Only if we found it is the answer TRUE


    ## remove(item) removes the item from the list.
    ## It needs the item and modifies the list.
    ## If the item is not found, nothing happens
    ##
    ## Think about people holding hands. To remove 'Tina' need to know BOTH people
    ## Tina is holding hands with. So need TWO cursors that march through our list
    def remove(self, item):
        if self.size() > 0:   #can only remove from a list with items
            if self.head.getData() == item: #if is in the first Node
                self.head = self.head.getNext()
            else:   
                current = self.head  #where we are looking. The person we are looking at
                previous = None    #the 'person' just behind them

                #use same finder-method as .search(), but also update 'previous'
                while current.getData() != item and current.getNext() != None:
                    previous = current
                    current = current.getNext()

                if current.getData() == item:
                    previous.setNext( current.getNext() )  




    

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

    
