'''
Homework 3 Exercise 4
Name: Suleyman Shouib
Date: 2/23/23
Description of your program: This code contains the logic to play a game of Tic-Tac-Toe. It is NOT a fully playable version of the game,
    it only contains code to print the game board, and for the user to enter their moves. The game is ended when either player types "Quit"
'''

# Dictionary containing the tic-tac-toe board
gameBoard = {"top-L": ' ', "top-M": ' ', "top-R": ' ',
               "mid-L": ' ', "mid-M": ' ', "mid-R": ' ',
               "low-L": ' ', "low-M": ' ', "low-R": ' '}

# Prints the tic-tac-toe board. The format was taken from the chapter 4 notes
def printBoard():
    print(gameBoard["top-L"]+"|"+gameBoard["top-M"]+"|"+gameBoard["top-R"])
    print("-+-+-")
    print(gameBoard["mid-L"] + "|" + gameBoard["mid-M"] + "|" + gameBoard["mid-R"])
    print("-+-+-")
    print(gameBoard["low-L"] + "|" + gameBoard["low-M"] + "|" + gameBoard["low-R"])

# Given the location the user inputted, if that space is empty place the current turns symbol in the specified location
def playersMove(symbol, location):
    if location == "top-L" and gameBoard["top-L"] == ' ':
        gameBoard["top-L"] = symbol
    elif location == "top-M" and gameBoard["top-M"] == ' ':
        gameBoard["top-M"] = symbol
    elif location == "top-R" and gameBoard["top-R"] == ' ':
        gameBoard["top-R"] = symbol
    elif location == "mid-L" and gameBoard["mid-L"] == ' ':
        gameBoard["mid-L"] = symbol
    elif location == "mid-M" and gameBoard["mid-M"] == ' ':
        gameBoard["mid-M"] = symbol
    elif location == "mid-R" and gameBoard["mid-R"] == ' ':
        gameBoard["mid-R"] = symbol
    elif location == "low-L" and gameBoard["low-L"] == ' ':
        gameBoard["low-L"] = symbol
    elif location == "low-M" and gameBoard["low-M"] == ' ':
        gameBoard["low-M"] = symbol
    elif location == "low-R" and gameBoard["low-R"] == ' ':
        gameBoard["low-R"] = symbol

print("To play Tic-Tac-Toe, when it is your turn, type where you want to place your symbol.")
print("Example: Top left = 'top-L', Middle middle = 'mid-M', bottom right = 'low-R'. To quit, type 'Quit'")

while True:
    printBoard()
    print("Turn for X. Move on which space?")
    xTurn = input()
    if xTurn == "Quit":
        break
    else:
        playersMove("X", xTurn)

    printBoard()
    print("Turn for O. Move on which space?")
    yTurn = input()
    if yTurn == "Quit":
        break
    else:
        playersMove("O", yTurn)
