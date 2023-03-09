'''
Homework 5 Exercise 1
Name: Suleyman Shouib
Date: 3/23/23
Description of your program: This program demonstrates a very simple Iteration Object.
                            The iteration object simply prints out the elements of an array in reverse.
                            If the counter goes past 0, then raise an error.
'''

class ReverseIter:
    def __init__(self, array):
        self.array = array
        self.counter = len(array)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= 0:
            result = self.array[self.counter]
            self.counter -= 1
            return result
        else:
            raise StopIteration()

it = ReverseIter([1, 2, 3, 4])

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
