'''
Homework 2, Exercise 4, Part 2
Name: Suleyman Shouib
Date: 2/16/23
Description of your program: A game of "Guess the number" is played. Using random.randint, to generate random boundaries given a defined limit, this version
    has a computer playing the game. The user's guesses are randomly generated, boundaries adjusting depending on answers from their prior guesses (i.e if the
    computer guessed a number higher than the answer, that guess becomes the upper boundary for the computers next guess). A system is also in place to make sure
    the computer does not guess the same number again by storing it all guesses in a list, and when a new guess is made to check the list to ensure it is unique.
'''

import random

limit = 1000
upperBound = random.randint(3, limit)     # minimum is 3 that way for lowerBound, if upperBound is 3, can range from 1-2
lowerBound = random.randint(1, upperBound-1)    # upperBound-1 is so that the answer can't be greater or equal to the number generated from upperBound
answer = random.randint(lowerBound, upperBound)
print("I am thinking of a number between "+str(lowerBound)+" and "+str(upperBound)+" (both inclusive). You have 10 tries.")

# Defines the boundaries that the computer can guess inbetween (both inclusive)
computerUpperGuess = upperBound
computerLowerGuess = lowerBound

listOfGuesses = []  # List keeps tracks of all guesses the computer will make

for i in range(10):
    '''
    If the user is on the first guess, then the computer doesn't have to worry about guessing a 
    number it has already guessed, so generate the guess. Else, there is a possibility that a guess could be repeated so set 
    alreadyGuessed to False and generate a random number. Go through listOfGuesses and check to see if the current guess is is in listOfGuesses
    since the list keeps track of all prior guesses. If the guess is not unique, then repeat the while loop and generate a new number and check it.
    If the guess is unique, then break out of the while loop and go through the rest of the turn
    '''
    if i == 0:
        userGuess = random.randint(computerLowerGuess, computerUpperGuess)
    else:
        while True:
            alreadyGuessed = False
            userGuess = random.randint(computerLowerGuess, computerUpperGuess)
            for j in range(len(listOfGuesses)):
                if listOfGuesses[j] != userGuess and not alreadyGuessed:
                    alreadyGuessed = False
                else:
                    alreadyGuessed = True
            if not alreadyGuessed:
                break
    listOfGuesses.append(userGuess)
    print("I guess "+str(userGuess))

    # Depending on the users answer, tell the user if their guess is too high, too low,
    # or if the guess is correct, break out of the for loop and give the user a victory message
    if userGuess > answer:
        print("Your guess is too high.")
        computerUpperGuess = userGuess
    elif userGuess < answer:
        print("Your guess is too low.")
        computerLowerGuess = userGuess
    else:
        print("Good job! You guess my number in " + str(i + 1) + " guesses!")
        break

    # By reaching to this if statement, if the turn number is 9, that means 10 guesses has been made (i starts at 0).
    # At this point, the user has failed to guess the number, therefore the game is over and the user loses
    if i == 9:
        print("Sorry, the number I was thinking of was "+str(answer))
