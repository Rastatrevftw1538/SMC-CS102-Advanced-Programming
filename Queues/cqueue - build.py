## Circular queues
## CS 102 Spring 2020
## Goal -- design a class that implements 'circular queues'

class CQueue:
    def __init__(self, maxsize = 10):   # so a CQueue has 10 spots by default (so we can see them all)
        self.maxsize = maxsize
        self.items = [None]*maxsize # all the entries start life as None = empty
        self.front = maxsize - 1    #point to the 'right hand end' as the front of the cqueue
        self.rear = maxsize -1
        self.size = 0  #let's keep track ourselves

    def isEmpty(self):
        return self.size == 0





    
    def enqueue(self, item): # version 1
        if self.isEmpty():  #self.size == 0
            self.items[ self.front ] = item   #make front point to the new item
            self.size += 1
        elif self.size == 1: # front and rear pointing at same spot
            self.rear -= 1
            self.items[ self.rear ] = item
            self.size += 1
        else:   #not pointing at same spot. 
            self.rear -= 1
            self.items[ self.rear ] = item
            self.size += 1








#Good start! Note that lots of the code is duplicated. So we can combine.
#Also when our storage list is empty, front & rear are the same,
# so let's use rear for visual simplicity. 
    def enqueue(self, item):  #version 2
        if not self.isEmpty():  
            self.rear -= 1
        self.items[ self.rear ] = item
        self.size += 1









#One more detail: what happens when we are full? ie size = maxsize?
#We are going to avoid errors by then ignoring the request.
#(Not very nice, but better than crashing)
    def enqueue(self, item):  #version 3
        if self.size == maxsize:
            print("Queue is Full! Item was not enqueued!")
        else:
            if not self.isEmpty():  
                self.rear -= 1
            self.items[ self.rear ] = item
            self.size += 1
#In a different semester we might add the ability to 'grow' our queue/lists
# but this is not that term            








#Ok. How about dequeue? 
    def dequeue(self): #version 1
        if self.isEmpty():#simple error management. Not good, but fine for today
            print("Queue is Empty! None was returned")
            return None    #dequeue expects a return. This is the "nothing" return
        else:
            val = self.items[self.front]
            self.items[self.front] = None #make that spot 'empty'
            self.front -= 1
            self.size -= 1
        return val












#Seems good! Wait - what if there was only one item in our storage
#list? Then front&rear were pointing at the same spot, and now rear
#is in front of front!! I guess we better handle that case separately. 
    def dequeue(self): #version 2
        if self.isEmpty():
            print("Queue is Empty! None was returned")
            return None  
        elif self.front == self.rear:   #size == 1
            val = self.items[self.front]
            self.items[self.front] == None
            self.size -= 1
            return val
        else:
            val = self.items[self.front]
            self.items[self.front] == None
            self.front -= 1
            self.size -= 1
            return val







#Lots of duplicated code. Let's combine
    def dequeue(self): #version 3
        if self.isEmpty():
            print("Queue is Empty! None was returned")
            return None    #simple error management (toda our goal is the circular bits, not the errors)
        else:
            val = self.items[self.front]
            self.items[self.front] = None
            if self.front != self.rear:
                self.front -= 1
            self.size -= 1
            return val






        
#So far so good! Now the 'circular' part.
#Eventually (perhaps) our front and or rear pointer will become 0,
#i.e. be at the very front of our storage list. What to do when they back up?
#Then we wrap around so that the previous spot is [-1], i.e. maxsize-1!
    def enqueue(self, item):  #version last
        if self.size == maxsize:
            print("Queue is Full! Item was not enqueued!")
        else:
            if not self.isEmpty():
                if self.rear == 0:
                    self.rear = maxsize - 1
                else:
                    self.rear -= 1
            self.items[ self.rear ] = item
            self.size += 1

    def dequeue(self): #version last
        if self.isEmpty():
            print("Queue is Empty! None was returned")
            return None    #simple error management (toda our goal is the circular bits, not the errors)
        else:
            val = self.items[self.front]
            self.items[self.front] = None
            if self.front != self.rear:
                if self.front == 0:
                    self.front = maxsize -1
                else:
                    self.front -= 1
            self.size -= 1
            return val

