class Fraction:

     # constructor -- create a fraction
     def __init__(self, top = 0 , bottom = 0):
          self.num = top
          self.den = bottom
     # used as >>> myfrac = Fraction(3, 8)

     # num and den are "instance variables". Each example of
     # of a Fraction will have these two pieces of data in it .
     def simp(self):
          theGCD = self.gcd()
          newnum = self.num//theGCD
          newden = self.den//theGCD
          return Fraction(newnum, newden)
     
     def gcd(self):
          dividend = None
          divisor = None
          quotient = None
          remainder = None
          if self.num < self.den:
               divisor = self.num
               dividend = self.den
          elif self.num > self.den:
               divisor = self.den
               dividend = self.num
          while remainder != 0:
               quotient = dividend // divisor
               remainder = dividend % divisor
               #print(f"{dividend}//{divisor}={quotient}Remainder{remainder}")
               if remainder == 0:
                    return divisor
               else:
                    dividend = divisor
                    divisor = remainder
          #return Fraction(newnum,newden)
     # would like to see what a fraction looks like
     # our first example of a "method"
     def show(self):
          print(self.num, "/", self.den)
     # used as >>> myfrac.show()

     # 'show' is fine, but we'd expect >>>print(myfrac) to work
     # need a special method to do that.
     def __str__(self):
          return str(self.num) + "/" + str(self.den)
     # now can use >>> print(frac)

     # add two fractions.
     def add(self, other):
          newnum = self.num * other.den + self.den * other.num
          newden = self.den * other.den
          return Fraction(newnum, newden)
     # used >>> myfrac.add(otherfrac)
     # or, if a, b, c, are fractions, a = b.add(c)

     # .mult(),
     def multiply(self, other):
          newnum = self.num * other.num
          newden = self.den * other.den
          return Fraction(newnum, newden)
     # .subtract(),

     def subtract(self, other):
          if self.den != other.den:
               if self.den > other.den:
                    thing = self.den // other.den
                    other.den *= thing
                    other.num *= thing
                    newden = other.den
               else:
                    thing = other.den // self.den
                    self.den *= thing
                    self.num *= thing
                    newden = self.den
          else:
               newden = self.den
          newnum = self.num - other.num
          newden = self.den * other.den
          return Fraction(newnum, newden)
     # .divide()

     def divide(self, other):
          self.num, self.den = self.den, self.num
          newnum = self.num * other.num
          newden = self.den * other.den
          return Fraction(newnum,newden)
     # .equals(),
     # .lessthan(),
     # .greaterthan()
     # .lessequal(
     # , .greaterequal()
