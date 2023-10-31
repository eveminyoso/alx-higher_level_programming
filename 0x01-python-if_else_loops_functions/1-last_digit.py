#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ldt1 = number % 10000
    ldt2 = ldt1 % 1000
    ldt3 = ldt2 % 100
    last = number  %10

    if last == 0:
        print("The last digit of %d is %d and is zero" % (number, last))
    elif last > 5:
        print("The last digit of %d is %d and is greater than 5" % (number, last))
    elif last < 6 & last != 0:
        print("The last digit of %d is %d and  is less than 6 and not 0" % (number, last))
else:
    ldt1 = number % -10000
    ldt2 = ldt1 % -1000
    ldt3 = ldt2 % -100
    last = ldt3 % -10

    if last == 0:
        print("The last digit of %d is %d and is zero" % (number, last))
    else:
        print("The last digit of %d is %d and  is less than 6 and not 0" % (number, last))
