## Circular queues
## CS 102 Spring 2020
## Goal -- design a class that implements 'circular queues'

class CQueue:
    def __init__(self, maxsize = 30000):
        self.maxsize = maxsize
        self.items = [None]*maxsize 
        self.front = maxsize - 1   
        self.rear = maxsize -1
        self.size = 0 

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):  #version last
        if self.size == self.maxsize:
            print("Queue is Full! Item was not enqueued!")
        else:
            if not self.isEmpty():
                if self.rear == 0:
                    self.rear = self.maxsize - 1
                else:
                    self.rear -= 1
            self.items[ self.rear ] = item
            self.size += 1

    def dequeue(self): #version last
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


    def __str__(self):
    ## we don't print queues but to see how we did in our design
    ## this let's us see the queue. 
        temp = CQueue()
        stringy = "["
        for a in self.items:
            if a == None:
                stringy += "_"
            else:
                stringy += str(a)
        return stringy+")" + " size =" + str(self.size) + ", f=" + str(self.front) +", r=" + str(self.rear)


def main():
    q = CQueue()
    print(q)
    input() #pause
    print("\nEnqueue! the letters 'CDEFGH'")
    for a in "CDEFGH":
        q.enqueue(a)
        print(q)


    input()
    print("\nDequeue! four items")
    for a in range(4):
        print("removed", q.dequeue())
        print(q)

    input()
    print("\nRe-EnQueue! the letters 'MNOPQRSTU'")
    for a in "MNOPQRSTU":
        q.enqueue(a)
        print(q)


    input()
    print("\nFinally DQ eleven things")
    for a in range(11):
        q.dequeue()
        print(q)
main()

