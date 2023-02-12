'''
Homework 3 Exercise 2
Name: Suleyman Shouib
Date: 2/23/23
Description of your program: This program takes any given string, and using a dictionary, counts the number of times each
    character was used in the given string. Characters include letters, punctuations, and white spaces.
     Letter characters are case-sensitive.
'''
import pprint

test = "The quick brown fox jumps over the lazy dog."
dictionary = {}

# For every char in test, if that char is a key in the dictionary, update the value. Else, it is new so add it to the dictionary
for i in range(len(test)):
    if test[i] in dictionary.keys():
        dictionary[test[i]] = dictionary[test[i]] + 1
    else:
        dictionary.update({test[i]: 1})

pprint.pprint(dictionary)



