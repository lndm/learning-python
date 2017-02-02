# Guess Game : can you find out the number I am thinking of?

import random

print('\n\nWelcome to the Guess Game\n\n\tI have a number in mind between 0 and 99, can you find it?')

# global variables
numberToFind = random.randint(0,99)
maxTries = numberTried = -1;
numberOfTries = 0

# setting the number of guesses
while(maxTries <= 0):
    try:
        maxTries = int(input('\nHow many guesses do you need? '))
    except:
        print('/!\ You should enter a number equal to or greater than 1. Try again!')

print('\n\nOK, now try to find out my number! It is between 0 and 99.')

# trying to find the number
while(numberOfTries != maxTries):
    numberOfTries = numberOfTries + 1;

    # making sure the input is valid
    while 1:
        try:
            numberTried = int(input('\n\tEnter your best guest : '))
        except:
            print('Hey, this is not a valid number - Try between 0 and 99, both included')
            continue
        if (0<=numberTried & numberTried<=99):
            break
        print('\nInvalid! Try a number between 0 and 99 included')

    # giving hints about the number
    if(numberTried > numberToFind):
        print('\nAlmost, but NO! Try a smaller number')
    elif(numberTried < numberToFind):
        print('\nAlmost, but NO! The number is greater')
    else:
        break

    print('You have '+str(maxTries-numberOfTries)+' guesses left!')

# result
if (numberTried == numberToFind):
    print('\n\t\t/!\ WELL DONE! The number was '+str(numberToFind)+'\nYou found it in '+str(numberOfTries)+' tries.\n\n')
else:
    print('\n\t\tHmmm.. The number was '+str(numberToFind)+'. Try with more guesses!\n\n')
