# Importing timeit to measure performance

import timeit


# Title

print("\n\n .:. Fibonacci's counting machine .:. \n\n")


# User input & Exception handling

while True:
    try:
        limitNumberInput = (int(input("How many Fibonnaci's number do you need? ___")))
        if limitNumberInput < 0:
            limitNumberInput = -limitNumberInput
        break
    except ValueError:
        print("\n\n/!\ Invalid number, try again!\n\n")


# Timing performance

start = timeit.default_timer()


# list production & printing

print("\n\n---> Here's your customized Fibonacci's list:\n")

a, b, c = 1, 1, 0    # a&b for counting succesive terms, c is a counter

while c < limitNumberInput:
    print (b)
    a, b, c = b, a+b, c + 1

# Timing performance

stop = timeit.default_timer()

# PROGRAM ENDS HERE

print("\n\t\t | Generated " + str(limitNumberInput) + " numbers in " + str(int((stop-start))) + " seconds and " + str(int((stop-start)*1000)%1000) + " ms")

try:
    print("\n\t\t | Performance: " + str((stop-start)*1000//limitNumberInput) + " ms per number")
except ZeroDivisionError:
    print("\n\t\t | Performance per number not computed (input=" + str(limitNumberInput) + ")")

print("\n\t\t | @neve.loic\n\n\n")
