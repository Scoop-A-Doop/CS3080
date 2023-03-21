'''
Homework 6 Exercise 3
Name: Suleyman Shouib
Date: 4/6/23
Description of your program: This program acts as a "multi copy" script where you are able to paste multiple contents
                            into a text file, and by running the code as a script, be able to retrieve the contents you
                            copied given the keyword. The contents will automatically be saved into your computer for
                            when you do ctrl+v. There are 3 options, the user can enter "save" following another argument
                            that will act as the keyword that is associated with the stuff currently copied in your clipboard.
                            The user can enter "list" which will print all the keywords that have been saved. Finally, the user
                            can input any keyword that will be searched in the file. If the keyword is found, it'll take the contents
                            associated with that keyword and copy that into your clipboard.
'''
# Referenced: https://www.geeksforgeeks.org/command-line-arguments-in-python/

import pyperclip, sys, os.path

path = os.path.exists("./clipboard.txt")

# If clipboard.txt does not exist, then create it
if not path:
    f = open("clipboard.txt", "x")
    f.close()

# sys.argv[1] = Keyword that denotes what to do.
# Save = Save whatever is in your clipboard under a keyword that is the third argument (args[2]).
# List = Lists all saved keywords.
# Else, load whatever the saved contents of that keyword.
if sys.argv[1] == "save":
    f = open("clipboard.txt", "a")  # Opens file to append
    f.write(sys.argv[2]+"\n"+pyperclip.paste()+"\n")    # Appends the keyword, and underneath it pastes the contents
    f.close()
elif sys.argv[1] == "list":
    f = open("clipboard.txt", "r")  # Opens file to read
    counter = 0
    for i in f:
        counter += 1    # counter keeps track of what line number its in
        # With how the text file is formatted, all the keywords are on odd numbered lines and the contents are underneath it in even numbers
        if counter % 2 != 0:
            print(i)
    f.close()
else:
    f = open("clipboard.txt", "r")
    keyword = sys.argv[1]+"\n"    # Without adding a new line, the program is unable to find the keyword
    found = False
    for i in f:
        # if the keyword is found, set found to True. The elif will be skipped this iteration and on the next iteration,
        # the contents will be the stuff associated with the keyword
        if i == keyword:
            found = True
        elif found:
            pyperclip.copy(i)
            break
    f.close()
