'''
Homework 2, Exercise 4, Part 2
Name: Suleyman Shouib
Date: 2/16/23
Description of your program: A game of "Guess the number" is played. Using random.randint, a number between 3 and a defined limit is generated
    at random using randint() to define the upper bound. Then a random number inbetween 1 and upperBound-1 is generated to define the lower bound.
    Given the two randomly generated bounds, an answer is randomly generated. The user then must guess the number correctly within 10 tries.
    The users will receive hints after each guess to help them guess the number correctly.
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
