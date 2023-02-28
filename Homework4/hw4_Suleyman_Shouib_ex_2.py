'''
Homework 4 Exercise 2
Name: Suleyman Shouib
Date: 3/9/23
Description of your program: Upon running, the program reads what is currently copied into your clipboard given what is
                            in your clipboard, reads through it all and extracts every mention of a valid phone and
                            email.
                            Valid phone formats are ###-###-####, ###.###.####, (###) ###-#### and ###-###-#### (x, ext, ext.)##.
                            Valid email formats may contain upper/lower case letters, numbers periods, hyphens,
                                underscores, pluses/minuses and percents, followed by an @, then followed by anything
                                with upper/lower case letters, numbers and underscores, and finally followed with a
                                .com, .net, .org, .edu or .gov.
                            The Phone numbers and emails then filter out duplicate entries and finally prints out every
                            unique instance of a phone number and email.
'''
import pyperclip
import re

'''
For testing I used this sting: 
You have a boring task of finding every phone number and email address in a long web page or document. If you manually 
scroll through the page, you 125-123-5126 might end up searching for a long time. But if you had a program that could search the 
text 630-915-0489 in your clipboard 630.915.0489 for (630) 915-0489 630-915-0489 x99 630-915-0489 ext.42 phone 513-241-6095 numbers and 
email addresses, you could simply do ctrl-A to select all the text, ctrl-C to copy it to the clipboard, and then  run  
your  program.  It sShouib2@uccs.com could  replace  the  entire  text _s+s-H%o.uib2@uccs.edu on  the 
sshouib2@uC2_cs.net clipboard  with  just _s+s-H%o.uib2@uC5_cs.org the _s+s-H%o.uib2@uC5_cs.gov phone numbers and email addresses it finds.  

Expected results for Phone Numbers are: 125-123-5126, 630-915-0489, 513-241-6095, (630) 915-0489, 630.915.0489, 630-915-0489 x99, 630-915-0489 ext.42
Expected results for Emails are: sShouib2@uccs.com, _s+s-H%o.uib2@uC5_cs.org, sshouib2@uC2_cs.net, _s+s-H%o.uib2@uccs.edu, _s+s-H%o.uib2@uC5_cs.gov
'''

text = pyperclip.paste()

# Obtains phonenumbers of formats:  ###-###-####, ###.###.####, (###) ###-#### and ###-###-#### x##
phoneNumbers = re.findall("\d\d\d-\d\d\d-\d\d\d\d", text)
phoneNumbers += re.findall("\(\d\d\d\) \d\d\d-\d\d\d\d", text)
phoneNumbers += re.findall("\d\d\d.\d\d\d.\d\d\d\d", text)
phoneNumbers += re.findall("\d\d\d.\d\d\d.\d\d\d\d x\d\d", text)
phoneNumbers += re.findall("\d\d\d.\d\d\d.\d\d\d\d ext\d\d", text)
phoneNumbers += re.findall("\d\d\d.\d\d\d.\d\d\d\d ext\.\d\d", text)

'''
Obtains emails that contain: upper/lower case letters, numbers periods, hyphens, underscores, pluses/minuses and 
percents, followed by an @, then followed by anything with upper/lower case letters, numbers and underscores, 
and finally followed with a .com, .net, .org, .edu or .gov.
'''
emailList = re.findall("[0-9a-zA-Z._%+-]+@[0-9a-zA-Z_]+\.com", text)
emailList += re.findall("[0-9a-zA-Z._%+-]+@[0-9a-zA-Z_]+\.org", text)
emailList += re.findall("[0-9a-zA-Z._%+-]+@[0-9a-zA-Z_]+\.net", text)
emailList += re.findall("[0-9a-zA-Z._%+-]+@[0-9a-zA-Z_]+\.edu", text)
emailList += re.findall("[0-9a-zA-Z._%+-]+@[0-9a-zA-Z_]+\.gov", text)

# I got the below code from here (Method 2): https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
# This just gets rid of duplicate values that may have accidentally been recorded using the regex search commands above
finalPhoneNumberList = []
[finalPhoneNumberList.append(x) for x in phoneNumbers if x not in finalPhoneNumberList]

finalEmailList = []
[finalEmailList.append(x) for x in emailList if x not in finalEmailList]

print("Phone Numbers: ")
print(finalPhoneNumberList)
print("Emails: ")
print(finalEmailList)
