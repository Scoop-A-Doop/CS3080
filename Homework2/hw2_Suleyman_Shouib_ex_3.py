'''
Homework 2, Exercise 3
Name: Suleyman Shouib
Date: 2/16/23
Description of your program: This program demonstrates the many functions and features that lists in Python
    are able to do. The very last thing in this program is a function called strList. This function takes
    all the elements of the list and turns it into a string separated by commas and spaces.
'''

# Create list then print it
items = ["Wallet", "Phone", "Keys"]
print(items)

# Sort the list and then print it
items.sort()
print(items)

# Prints everything from the second index to the last index, skipping the first
print(items[1:len(items)])

# Prints the very last element
print(items[-1])

# Gets the index of where element "Keys" is from
print(items.index("Keys"))

# Appends "Tablet" at the end of the list, then prints
items.append("Tablet")
print(items)

# Inserts Mask at the second index and prinits it
items.insert(1, "Mask")
print(items)

# Removes the element "Phone" and prints it
items.remove("Phone")
print(items)

# Reverses the indexes of the list and prints it
items.reverse()
print(items)

'''
Takes any list and concatenates all elements in said list via a for loop into a string separated by commas
only if the for loop has not reached the final element of the list. If the for loop is at the final element,
then instead of concatenating ", " do "and (last index)." instead.
'''
def strList(newList):
    stringList = ""
    for i in range(len(newList)):
        if i != len(newList)-1:
            stringList = stringList + str(newList[i]) + ", "
        else:
            stringList = stringList + "and " + str(newList[i]) + "."
    return stringList

print(strList(items))
