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
        self.tail = None ##CHANGE
        self.size = 0 ##CHANGE


    ## As for stacks and queues, we don't usually print entire linked lists.
    ## But as we learn, here is a __str__ method that does that.
    def __str__(self):
        if self.size == 0 :
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

    ## add(item) prepends an item to the front of list.
    ## It needs the item and returns nothing. 
    def add(self,item):
        temp = Node(item)    ##create a new node
        temp.setNext(self.head)    ## Cause new node to point to current head
        self.head = temp  ## Cause new node to be new head
        self.size += 1 ##CHANGE


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
            self.tail = current.setNext( temp )     #current now is 'tail'. Cause new node to be new tail
            self.size += 1 ##CHANGE

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
        if self.size > 0:   #can only remove from a list with items
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
                self.size -= 1 ##CHANGE

    
    ## pop() removes and returns the last item in the list.
    ## It needs nothing and returns an item.
    ## If the linked list is empty it returns None
    def pop(self):
        if self.size == 0:   #could do self.head == None
            return None
        if self.size == 1:
            item = self.head.getData()
            self.head = None
            return item
        
        previous = None     #like remove, we need know who is behind us
        current = self.head
    
        while current.getNext() != None:   #work our way to the end
            previous = current
            current = current.getNext()
        #current is now 'tail', and previous is 2nd-to-last (and will be new last)
            
        item = current.getData()    #save last 'data' 
        previous.setNext( None)   #make previous the new end = new tail
        self.size -= 1 ##CHANGE
        return item

        
    ## index(item) returns the position of item in the list.
    ## It needs the item and returns the index.
    ## If item is not in the list, returns -1
    def index(self, item):
        current = self.head
        ivalue = 0
        while current.getNext() != None and current.getData() != item:
            current = current.getNext()
            ivalue += 1
        
        if current.getData() == item :
            return ivalue
        else:
            return -1
    

    ## insert(pos,item) adds a new item to the list at position pos.
    ## Note: Position 0 is the head
    ## It needs the position and the item
    ## If pos is off the end of the list, put item last
    def insert(self, pos, item):
        if pos >= self.size:
            self.append(item)

        temp = Node(item)  #what we want to insert
        previous = None   #need 'before' and a 'current' pointers
        current = self.head
        count = 0   #our 'index' counter. want count == pos

        while count < pos: 
            previous = current
            current = current.getNext()
            count += 1
        previous.setNext ( temp )
        temp.setNext( current )
        self.size += 1 ##CHANGE

    def reverse(self):
        if self.size == 0:   
            return None
        if self.size == 1:
            item = self.head.getData()
            self.head = None
            return item
        previous = None
        current = self.head

        while current.getNext() != None:
            previous = current
            current = current.getNext()
        self.head = current