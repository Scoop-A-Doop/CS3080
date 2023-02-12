'''
Homework 3 Exercise 1
Name: Suleyman Shouib
Date: 2/23/23
Description of your program: This program takes a 2d array of a sideways heart and prints it out so that the heart is
    right side up using a nested for loop
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Source used for end="": https://www.guru99.com/print-without-newline-python.html
# First, iterate through the columns grid[0], then iterate through the rows grid
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end="")
    print()

