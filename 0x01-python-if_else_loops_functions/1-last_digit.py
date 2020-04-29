#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modder = 10
if (number < 0):
    modder *= -1
lastdigit = number % (modder)

script = "Last digit of {:d} is {:d}".format(number, lastdigit)

if lastdigit < 6 and lastdigit != 0:
    print("{} and is less than 6 and not 0".format(script))
elif lastdigit > 5:
    print("{} and is greater than 5".format(script))
elif lastdigit == 0:
    print("{} and is 0".format(script))
