'''
Homework 5 Exercise 2
Name: Suleyman Shouib
Date: 3/23/23
Description of your program: Using a generator, by passing in a number it is able to find the first "n" number of
                            pythagorean triplets. The generator brute forces through every single combination
                            via a double nested for loop.
'''
import math

# Structure of the generator is taken from the CS3080 Iterators Google CoLab
def myRange(n):
    i = 0
    while i < n:
        yield i
        i + 1

def integers():
    i = 1
    while True:
        yield i
        i = i + 1

def triplets():
    # This will increment last and will end up being the largest number of the pair, since the next for loops are dependent on this one
    # This is why this is "Z"
    for z in integers():
        # This is the second-largest number, so I refer to it as y
        for y in range(z):
            # This is the smallest number, so I refer to it as x. This makes the triplet ordered by default
            for x in range(y):
                # Only add the triplet IF they are a true pythagorean triplet.
                # The generator will keep going until a true triplet is found, incrementing i in take(n,seq) until it reaches n
                if ((x*x) + (y*y)) == (z*z):
                    answer = (x, y, z)
                    yield answer

def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

pyt = triplets()
print(take(10, pyt))
