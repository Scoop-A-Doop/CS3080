'''
Homework 6 Exercise 2
Name: Suleyman Shouib
Date: 4/6/23
Description of your program: Demonstrates usage of caching with decorators by creating a fibonacci sequence calculator
                            effectively and efficiently through the use of decorators.
Conclusion: When running a fibonacci sequence of 25 values, by using the cache method, there are 49 calls that are run
            When NOT using the cache method, there are 242785 (and my laptop fan goes crazy for a second).
            So the difference in using the two is that one is incredibly inefficient and the other is incredibly efficient.
'''

import functools

# Referenced this: https://www.geeksforgeeks.org/memoization-using-decorators-in-python/?ref=rp

def cache(func):
    # This will hold onto the already calculated numbers in the format of num | sum
    cacheDictionary = {}

    # *args and **kwargs is left because of the requirement in paragraph 1: "Please make the decorator work for functions with any number of arguments"
    # According to https://realpython.com/python-kwargs-and-args/, they allow for passing multiple arguments to a function, so I'm assuming this is all I need
    def wrapper(num, *args, **kwargs):
        passFunc()  # Keeps track of the number of times this is going through

        # If a number is found in the dictionary, just return the value of the num. No need to recalculate.
        # If you want to see how long it'll take to calculate a sequence WITHOUT caching, comment out the next 2 lines.
        #if num in cacheDictionary:
        #    return cacheDictionary[num]

        # Else, calculate the number and add it to the dictionary for future use
        fibSum = func(num, *args, **kwargs)
        cacheDictionary.update({num: fibSum})
        return fibSum
    return wrapper

@cache
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


# countCalls provided by professor
def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {} ".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)

    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls

@countCalls
def passFunc():
    pass

print(fibonacci(25))
