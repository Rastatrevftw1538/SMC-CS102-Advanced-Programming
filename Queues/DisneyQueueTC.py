# Trevor Cardoza
# CS 102 Spring 2020
# April 1st
# Program: Disney Queues and Circular Dequeues
#
# Disney Queues:
#
# A program that assigns riders into a line
# (to the back if they are normal customers and 
# to the back of the FastPass line if they have 
# a FastPass).
# 
# Circular Dequeues:
# 
# .
from random import randint
class DSQueue:
     # __init__
     # The initializing function that determines the
     # format of the class and it's inputs.
     #
     # Inputs of self and max line size
     # that defaults to 40.
     #
     # It does not print.
     #
     # It does not return.
     
     def __init__(self, maxsize = 200):
          self.maxsize = maxsize
          self.cust = [None]*maxsize
          self.front = self.maxsize - 1   
          self.rear = self.maxsize -1
          self.sizefp = 0
          self.size = 0
          self.rearfp = self.maxsize - self.sizefp -1
          
          
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
     
     
     # FPsize
     # Checks the size of the FastPass line.
     #
     # Inputs of self.
     #
     # It does not print.
     #
     # It returns the size of the FastPass line.
     
     def FPsize(self):
          return self.sizefp
     
     
     # join
     # Adds a normal customer to the back of the line.
     #
     # Inputs of self and single value (float,int,str,etc).
     #
     # It does not print.
     #
     # It does not return.
     
     def join(self, cust):
          if self.size == self.maxsize:
               print("Line is Full! Person was not added to line!")
          else:
               if not self.isEmpty():
                    if self.rear == 0:
                         self.rear = self.maxsize - 1
                    else:
                         self.rear -= 1
          self.cust[ self.rear ] = cust
          self.size += 1
     
     
     # joinfp
     # Adds a FastPass customer to the back of the front line.
     #
     # Inputs of self and single value (float,int,str,etc).
     #
     # It does not print.
     #
     # It does not return.
     
     def joinfp(self, cust):
          if self.size == self.maxsize:
               print("Line is Full! Person was not added to line!")
          else:
               if not self.isEmpty():
                    if self.rearfp == 0:
                         self.rearfp = self.maxsize - 1
          for p in range(self.maxsize - self.size,self.maxsize-self.sizefp):
               custMove = self.cust[p]
               if self.sizefp > 1 and p > self.maxsize -self.sizefp+self.sizefp:
                    self.cust[p-self.sizefp+1] = custMove
               else:
                    self.cust[p-1] = custMove
          self.cust[self.rearfp] = cust
          self.size += 1
          self.sizefp += 1
          self.rear = self.maxsize - self.size
          self.rearfp -= 1
     
     
     # ride
     # Removes and returns the person in the front of the line
     # then, moves the line up so the front is not empty.
     #
     # Inputs of self.
     #
     # It does not print.
     #
     # It returns the rider who left the line.
     
     def ride(self):
          if self.isEmpty():
               print("Line is Empty! None was returned")
               return None    
          else:
               rider = self.cust[self.front]
               moved = self.cust[self.front-1]
               count = 1
               self.cust[self.front] = None
               while moved != None:
                    self.cust[self.front-count+1] = moved
                    count += 1
                    moved = self.cust[self.front-count]
               self.cust[self.rear] = None
               if self.rear >= self.maxsize - 1:
                    self.rear += 1
               if self.sizefp != 0:
                    self.rearfp += 1
          self.size -= 1
          if self.sizefp != 0:
               self.sizefp -= 1
          return rider
     
     
     # __str__
     # Formats the Queue when printed.
     #
     # Inputs of self.
     #
     # It does not print.
     #
     # It returns the format for the Queue, the size,
     # the FastPass size, the front num, the rear num,
     # and the FastPass rear num.
     
     def __str__(self):
          stringy = "["
          for a in self.cust:
               if a == None:
                    stringy += "_"
               else:
                    stringy += str(a)
          return stringy+")" + " size =" + str(self.size) + " FPsize =" + str(self.sizefp) + ", f=" + str(self.front) +", rear=" + str(self.rear)+", FPrear=" + str(self.rearfp)
'''
def randomizer(ratios):
     ride, front, back = ratios
     total = ride + front + back
     num = randint(1, 100)
     if num < ride*100/total:
          return 'r'
     elif num < (ride+front)*100/total:
          return 'f'
     else:
          return 'b'

## Function update
## uses a DSQueue and probabilities to update the DSQ.
##
## INPUT: theDSQ = the ds-queue we are working on
##      ratios = %s of time people ride, joinFP, join
## OUTPUT: nothing, but updates the DSQ with the proper event

def update(theDSQ, ratios):
     c = randomizer(ratios)
     if c == 'r' and not theDSQ.isEmpty() :
          theDSQ.ride()
     elif c == 'f':
          theDSQ.joinfp(["F "])
     else:
          theDSQ.join(["P "])



def main():
     l = DSQueue()
     person = "i"
     fpperson = "p"
     busy = (.33, .33, .33) # % of time 'ride', 'joinFP', 'join' occur 
     for i in range(50):
          update(l, busy)
          print(l)
     print("After", str(i), " events, there are", l.size, "people in line.")
     print(l)
main()
'''