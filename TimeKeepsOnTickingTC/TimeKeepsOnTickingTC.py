# Trevor Cardoza
# CS 102 Spring 2020
# March 10th
# Program: TimeKeepsOnTicking
# A program that uses the Time class to
# convert any number, int or float into 
# time in hours and minutes.

from TimeKeepsOnTickingTC.TimeClassTC import Time

# Variables and print statements 
# that are used as test cases.

time0 = Time()
print(time0)
time1 = Time(6)
print(time1)
time2 = Time(3,30)
print(time2)
time3 = Time(30,75)
print(time3)
time4 = Time(3.5)
print(time4)
print(time3 + time4)
print(time3)
print(time1 + 10)
print(0.75 + time2)