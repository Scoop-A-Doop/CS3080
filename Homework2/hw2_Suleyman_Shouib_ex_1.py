'''
Homework 2, Exercise 1
Name: Suleyman Shouib
Date: 2/16/23
Description of your program: This program runs the Collatz Sequence on a number the user inputs.
    The Collatz Sequence takes a number and if it is even, it is divided by 2.
    If it is odd, it is multiplied by 3 and added by 1. This sequence keeps running until the number ends up being 1,
    which it always ends up as if the sequence runs long enough.
'''

'''
Function collatz takes in integer number as argument. An if/else statement determines whether number is even or odd.
If even, // by 2. If odd, multiply by 3 and add 1. After this is calculated, another if/else statement checks to see
if the number is 1 or not. If it is 1, then the function returns number (1). If it is not 1, then it uses recursion and
calls the function again, passing in the current value of number as the argument for collatz 
'''
def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
    else:
        number = 3 * number + 1
        print(number)
    if number != 1:
        collatz(number)
    else:
        return number

print("Please enter an integer and I will run the Collatz Sequence on it")
print("Enter number:")
collatz(int(input()))
