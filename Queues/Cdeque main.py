from CircleDequeueTC import CDeque

#### YOUR CDEQUE GOES HERE
'''class CDeque:

    

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


'''
def main():
    print("A main for testing your Circular Deque")
    print("It likely requires a couple changes from you in order for it to work.")
    print("1) You should have 'pointers' variabls telling you where the 'front' and 'rear' of your CDeque is")
    print("In the __str__ function above adjust the final return statement to use your variables.")
    print("2) Your CDeque should have a default size. For the code below to test it, that size should be 10")
    print()

    d = CDeque()

    print("Start by filling the CD")
    letters = "ABCDEFGHIJ"
    i=0    
    while i<10:
        d.addRear(letters[i])
        d.addFront(letters[i+1])
        i+=2
        print(d)
    print(d)

    print("\nTry another letter - should get error messages")
    d.addRear("Z")
    d.addFront("Z")

    print("\nMake some room")
    d.removeFront()
    d.removeRear()
    print(d)
    d.removeFront()
    d.removeRear()
    print(d)

    print("\nWalk the letters 'forward'")
    for i in range(5):
        d.addFront(d.removeRear())
        print(d)
    
    print("\nWalk the letters 'backward'")
    for i in range(5):
        d.addRear(d.removeFront())
        print(d)

    print("\nMake it go away")
    while not d.isEmpty(): 
        d.removeFront()
        print(d)
    print("Try final remove - should get error messages")
    d.removeRear()
    d.removeFront()
    

main()

    
