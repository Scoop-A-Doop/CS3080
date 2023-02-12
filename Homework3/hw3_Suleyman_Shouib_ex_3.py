'''
Homework 3 Exercise 3
Name: Suleyman Shouib
Date: 2/23/23
Description of your program: This program has an inventory contained in a dictionary.
    There are 3 methods, 1 method prints the dictionary, another adds an item to the dictionary and the third deletes an item.

'''

myInventory = {"Hand sanitizer": 10, "Soap": 6, "Kleenex": 22, "Lotion": 16, "Razors": 12}

# Prints a given inventory
def printInventory(inventory):
    for i in inventory.items():
        print(i)

# If the item added is already in the inventory, increment the stock. Else it is unique so add it to the inventory
def addItem(inventory, item):
    if item in inventory.keys():
        inventory[item] = inventory[item] + 1
    else:
        inventory.update({item: 1})

# Removes 1 stock of an item in the inventory. If the stock is 0, don't decrement anymore. If item was never recorded in the inventory, print an error
def deleteItem(inventory, item):
    if item in inventory.keys():
        if inventory[item] == 0:
            print("Item cannot be deleted any further!")
        else:
            inventory[item] = inventory[item] - 1
    else:
        print("Item was never recorded in the inventory.")

printInventory(myInventory)
addItem(myInventory, "Advil")
addItem(myInventory, "Lotion")
deleteItem(myInventory, "Advil")
deleteItem(myInventory, "Advil")
deleteItem(myInventory, "Tylenol")
printInventory(myInventory)
