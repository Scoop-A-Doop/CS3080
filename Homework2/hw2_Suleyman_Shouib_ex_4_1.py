'''
Homework 2, Exercise 4, Part 1
Name: Suleyman Shouib
Date: 2/16/23
Description of your program: A game of "Guess the number" is played. Using random.randint, a number between 1 and 20 is generated
    and the user must guess the number correctly within 10 tries. The users will receive hints after each guess to help them guess
    the number correctly
'''

import random

answer = random.randint(1, 20)
print("I am thinking of a number between 1 and 20 (both inclusive). You have 10 tries.")
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
