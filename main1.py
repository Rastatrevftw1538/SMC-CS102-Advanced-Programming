from fraction import Fraction


def main():
    a = Fraction(2, 3)
    print("a is the fraction ", a)

    b = Fraction(4, 8)
    print("b is the fraction ", b)

    c = a.add(b)
    print("c is the fraction ", c)
    
    print("c*b=", c.multiply(b))

    print("c-a=", c.subtract(a))

    print("c/a=", c.divide(a))
    
    print(c.simp())
##
##    print("a<b is ", a.lessthan(b))
##
##    d = Fraction(8, 10)
##    print("c=d is", c.equals(d))


main()
