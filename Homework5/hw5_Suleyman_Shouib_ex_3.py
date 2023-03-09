'''
Homework 5 Exercise 3
Name: Suleyman Shouib
Date: 3/23/23
Description of your program: This program essentially recreates the range() function but in the form
                            of a generator. Given a stop argument and optional start and step arguments,
                            iterate through the numbers given the appropriate arguments. This results in
                            a much lower memory cost while still iterating through numbers just like
                            a standard range() call.
'''

def genrange(stop, start=None, step=None):
    iteration = 0   # Iteration starts at 0 by default. This will be overwritten by start when appropriate

    # If there is NO start AND there IS a step
    if start is None and step is not None:
        while iteration <= stop:
            yield iteration
            iteration += step

    # If there is NO start AND NO step
    elif start is None:
        while iteration <= stop:
            yield iteration
            iteration += 1

    # If there IS A start AND NO step
    elif step is None:
        iteration = start
        while iteration <= stop:
            yield iteration
            iteration += 1

    # There IS a stop, start and a step
    else:
        iteration = start
        while iteration <= stop:
            yield iteration
            iteration += step

pyt = genrange(10, -2, 5)

# How I figured out how to print yield values: https://www.guru99.com/python-yield-return-generator.html
for i in pyt:
    print(i)
