'''
Homework 1
Name: Suleyman Shouib
Date: 2/2/23
Description of your program: This program asks the user several security questions all contained in a while loop.
    Upon answering all security questions correctly in a row, a secret will be revealed.
    The purpose of this program is to demonstrate understanding the many features and syntax of Python, so each question
    will be unique in that they demonstrate something that the other questions has not already. This may be the use of
    a new command, the use of a new data type etc. Only one module is imported, that being the random module so that
    I can demonstrate the use of the randInt function.
'''

import random

print("You have accessed the super secret vault containing super secret information.\n"
      "If you want to get the super secret information, you must answer several security questions correctly in a row.\n"
      "The security questions will get harder as you answer them. On the bright side, you may have unlimited tries.\n"
      "Good luck!\n")

while True:
    '''
    The user is asked to input their age using input() casted to int via int(), divide it and round down. 
    The answer is calculated using the // operator and the users answer will be verified via an if/else statement.
    '''
    print("How old are you?")
    age = int(input())
    print("Halve your age and round down. What is it?")
    dividedAgeAnswer = input()
    if dividedAgeAnswer == str(age//2):
        print("Correct!")
    else:
        print("Incorrect. Back to the beginning!")
        continue

    '''
    The user is asked what the mass of the earth is. 3 answers may be submitted, a correct answer, an incorrect answer,
    or the user may ask for a hint. An if/elif/else command is used to determine the users answer.
    '''
    print('What is the mass of the earth? Answer format must be (base number to the thousandths)x10^(exponent). '
          'Okay, this is kind of a leap in difficulty. I will be nice just this once!, if you do not know, just say "idk"')
    earthMassAnswer = input()
    if earthMassAnswer == "5.972x10^24":
        print("Correct!")
    elif earthMassAnswer == "idk":
        print('The hint is.. that the answer is "5.972x10^24"! But you still have to go back to the beginning. Sorry!')
        continue
    else:
        print("Incorrect. Back to the beginning!")
        continue

    '''
    A for loop iterates 10 times and in each iteration, a random number between 1 and 0 is generated.
    If the number is a 0, it will print Tomato. If it is 1, it will print Potato. This demonstrates Truthy/Falsey values.
    Whenever it prints Potato, the potatoCounter variable will increment to keep track of the number of times Potato was printed.
    If the user correctly answers the number of times Potato was printed, the code will progress, otherwise the user will start from the beginning
    '''
    print('How many times did the word "Potato" print?')
    potatoCounter = 0
    for i in range(10):
        if random.randint(0, 1):
            print("Potato")
            potatoCounter = potatoCounter + 1
        else:
            print("Tomato")
    potatoCountAnswer = int(input())
    if potatoCounter == potatoCountAnswer:
        print("Correct!")
    else:
        print("Incorrect. Back to the beginning!")
        continue

    '''
    Three "riddle" type questions will be asked, with each riddle question being associated with a number.
    Using a for loop ranging from 1-3 (0-2), A series of if/elif statements will be used to verify the current value of i to ask the correct riddle.
    The user then inputs their answer and is then checked to see if its correct. If the user answers any question incorrectly,
    it will be flagged by incorrectAnswer and the program will break out of the for loop, and the while loop will repeat.
    This question is to satisfy requirement #5 in hw1.pdf
    '''
    print("For the following 3 questions, you will be given a word and you must answer with the number that corresponds to said word.")
    incorrectAnswer = False
    for i in range(3):
        if i == 0:
            print("One Hundred Minus Thirty Three")
            riddleAnswer = int(input())
            if riddleAnswer == 67:
                print("Correct!")
            else:
                print("Incorrect. Back to the beginning!")
                incorrectAnswer = True
                break
        elif i == 1:
            print("Snowman")
            riddleAnswer = int(input())
            if riddleAnswer == 8:
                print("Correct!")
            else:
                print("Incorrect. Back to the beginning!")
                incorrectAnswer = True
                break
        elif i == 2:
            print("Pie (Hint: Answer should go to the nearest hundredths place)")
            pieValue = 3.14
            riddleAnswer = float(input())
            if riddleAnswer == pieValue:
                print("Correct!")
            else:
                print("Incorrect. Back to the beginning!")
                incorrectAnswer = True
                break
    if incorrectAnswer:
        continue

    '''
    Two words of varying sizes will be generated using a random generator and the multiplication operator in conjunction 
    with a base word "Potato" and "Tomato". The user must answer by correctly subtract the lengths of those words.
    Answering this question correctly will break out of the for loop to reveal the "secret information" 
    '''
    print("Final Question... Subtract the lengths of word 1 with word 2.")
    wordOne = "Potato" * random.randint(4, 7)
    wordOneLength = len(wordOne)
    wordTwo = "Tomato" * random.randint(1, 3)
    wordTwoLength = len(wordTwo)
    wordLengthDifference = wordOneLength - wordTwoLength
    print(wordOne + "\n" + wordTwo)
    wordDifferenceAnswer = int(input())
    if wordDifferenceAnswer == wordLengthDifference:
        print("Correct!")
        break
    else:
        print("Incorrect. Back to the beginning!")
        continue

print("\nSecurity Questions Complete!")
print("The secret information is... that I'm really hungry right now... "
      "I should probably turn in this assignment and get something to eat.")