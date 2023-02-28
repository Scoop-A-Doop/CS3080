'''
Homework 4 Exercise 2
Name: Suleyman Shouib
Date: 3/9/23
Description of your program: This program requires the user to enter a password given that the password is 8 characters long,
                            has an upper/lowercase character and at least one digit. The password is checked via regexes
                            and the user will be prompted to enter a password until they enter a valid one
'''
import re
print("Please enter a password.")
print("It must be at least 8 characters long")
print("It must contain both uppercase and lowercase characters")
print("It must also have at least one digit")

while True:
    password = input()

    if re.search("[0-9a-zA-Z]{8}", password):
        if re.search("[a-z]", password) and re.search("[A-Z]", password):
            if re.search("[0-9]", password):
                break
            else:
                print("Password must include at least one digit!")
        else:
            print("Password must contain a lowercase AND an uppercase character!")
    else:
        print("Password must be AT LEAST 8 characters long!")

print("Thank you for entering the valid password", password)
