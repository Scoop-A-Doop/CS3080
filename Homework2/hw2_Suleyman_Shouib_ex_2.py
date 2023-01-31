'''
Homework 2, Exercise 2
Name: Suleyman Shouib
Date: 2/16/23
Description of your program: This program runs the Collatz Sequence on a number the user inputs. A feature is added
    as to make sure the user does not input anything that isn't an integer. This is done via a try/except statement.
    Until the user enters the appropriate data type, the user will continue being asked to input an integer.
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
# Keep looping until the user input an integer data type. The try/except is used to catch ValueError incase the user doesn't input an Integer
while True:
    try:
        collatz(int(input()))
        break
    except ValueError:
        print("Please enter an INTEGER value")

