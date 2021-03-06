from DisneyQueueTC import DSQueue
from random import randint








# we test the DSQueue with a model of the day. The DSQueue starts empty.
# 
# BUSY: During the morning the ride is "busy" and more people are joining the
# line that are getting on the ride.
# We model this by assuming for every person who gets to ride() there are two people
# who join the lines. We assume that about half have FastPasses.
#
# BALANCED: Then for a while it is 'balanced', and about the same number of people
# are getting on the ride as are joining the lines.
#
# LESS BUSY: Finally, near nighttime the ride gets less busy, and more people get
# on the ride than join the line.
# We reverse the morning's proportions and assume that two people get to
# ride for every new person in the line. 

## Function Randomizer
##    auxillary function that 'randomly' decides the next action - does a person
##    		get on the ride, or does someone new join the lines
##
## INPUT: Three percentages. ride = % of time the next action is "get on the ride!"
## 	  front = % of the time the next action is "new FastPass person joins line"
##	  back = % of the time the next action is "new non-FP person joins line"
##
## Print: nothing
## OUTPUT: A letter 'r', 'f' or 'b', indicating whether ride, front or back is next action
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
        theDSQ.joinfp("FP")
    else:
        theDSQ.join("nonFP")
    

def main():
    myq = DSQueue()

    busy = (.33, .33, .33) # % of time 'ride', 'joinFP', 'join' occur 
    for i in range(200):
        update(myq, busy)
    print("After", str(i), " events, there are", myq.size, "people in line.")
    print(myq)
    balanced = (.5, .25, .25)  #half the time 'ride', the other half split between joinFP and join
    for i in range(200):
        update(myq, balanced)
    print("After 400 events, there are", myq.size, "people in line.")
    print(myq)
    quiet = (.66, .16, .16)  #twice as many 
    for i in range(200):
        update(myq, quiet)
    print("After 600 events, there are", myq.size, "people in line.")
    print(myq)

main()
