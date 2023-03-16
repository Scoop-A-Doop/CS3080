'''
Homework 6 Exercise 1
Name: Suleyman Shouib
Date: 4/6/23
Description of your program: Demonstrates usage of Decorators. Calling the decorator will cause a countdown to occur
                            counting down with a timer inbetween. The timer interval is decided through a parameter.
                            If there is no parameter, it will default to counting down via 1 second inbetween.
'''
import functools
import time

# Referenced this: https://www.geeksforgeeks.org/decorators-with-parameters-in-python/

def rateDecorator(rate=None):
    # Checks to see if the argument is none or not. If it is none, set the time sleep rate to one.
    # Else, it'll just be whatever the custom parameter is
    if rate is None:
        rate = 1

    def slowdown(func):
        """Sleep rate # of seconds before calling the function"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(rate)    # Sleep whatever rate it is number of seconds
            return func(*args, **kwargs)    # Then call the passed in func (countdown)
        return wrapper
    return slowdown

# If you want to adjust the rate, change the parameter inside @rateDecorator
@rateDecorator(rate=3)
def countdown(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown(fromNumber - 1)

countdown(5)
