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
for i in range(10):
    print("Take a guess.")
    userGuess = int(input())

    # Depending on the users answer, tell the user if their guess is too high, too low,
    # or if the guess is correct, break out of the for loop and give the user a victory message
    if userGuess > answer:
        print("Your guess is too high.")
    elif userGuess < answer:
        print("Your guess is too low.")
    else:
        print("Good job! You guess my number in " + str(i + 1) + " guesses!")
        break

    # By reaching to this if statement, if the turn number is 9, that means 10 guesses has been made (i starts at 0).
    # At this point, the user has failed to guess the number, therefore the game is over and the user loses
    if i == 9:
        print("Sorry, the number I was thinking of was "+str(answer))
