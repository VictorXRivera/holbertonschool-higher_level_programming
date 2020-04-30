#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif num % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        elif num % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif num != 101:
            print("{:d}".format(num), end=" ")
