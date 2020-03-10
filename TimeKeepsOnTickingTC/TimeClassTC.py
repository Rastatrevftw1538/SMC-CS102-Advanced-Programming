# Trevor Cardoza
# CS 102 Spring 2020
# March 10th
# Program: TimeClass
# A class that converts any number
# into a int of time in hours and
# minutes.

class Time:
     
     # __init__
     # The initializing function that determines the
     # format of the class and it's inputs.
     #
     # Inputs of self and two numbers hours and minutes
     # that default to 0.
     #
     # It does not print.
     #
     # It returns None.
     
     def __init__(self,hours=0,minutes=0):
          self.hrs = hours
          self.mins = minutes
          if str(self.hrs).find(".") != -1:
               hours = round(hours,2)
               minVar = float("0"+str(hours)[str(hours).find("."):])
               self.hrs = int(str(hours)[:str(hours).find(".")])
               self.mins = int(minVar * 60)
          if str(self.mins).find(".") != -1:
               self.mins = int(self.mins)
          while self.mins >= 60:
               newMins = minutes - 60
               self.hrs += 1
               self.mins = newMins
          return None
     
     # __str__
     # The function that formats the output if
     # it is put into a string or printed.
     #
     # Inputs are self.
     #
     # It does not print.
     #
     # It returns a string of hours and mins in a sentence.
     
     def __str__(self):
          return str(self.hrs)+" hours, "+str(self.mins)+" minutes"
     
     # __add__
     # The function that deals with the addition
     # of itself and any other number it is next
     # to.
     #
     # Inputs are self and other being the number next to
     # it.
     #
     # It does not print.
     #
     # It returns Time of hours and mins from the 
     # two combined inputs.
     
     def __add__(self,other):
          if isinstance(other,int):
               newHr = self.hrs + other
               newMin = self.mins
          elif isinstance(other,float):
               other = Time(other)
               newHr = self.hrs + other.hrs
               newMin = self.mins + other.mins
          else:
               newHr = self.hrs + other.hrs
               newMin = self.mins + other.mins
          return Time(newHr,newMin)
     
     # __radd__
     # The function is the same as __add__ but
     # only when any number that isn't Time comes
     # first then followed by Time.
     #
     # Inputs are self and other being the number next to
     # it.
     #
     # It does not print.
     #
     # It returns Time of hours and mins from the 
     # two combined inputs.
     
     def __radd__(self,other):
          other = Time(other)
          newHr = self.hrs + other.hrs
          newMin = self.mins + other.mins
          return Time(newHr,newMin)
