#AUtomateTheBOringStuff.com

#Regular Expressions

def isPhoneNumber(text):
    if len(text) !=12:
        return False #not sized right for phone
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
            return False #Misisng dash
    for i in range(4,7):
            if not text[i].isdecimal():
                return False # no first 3 digits
    if text[7] != '-':
        return False #missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #missing last 4 digits
    return True

print(isPhoneNumber('415-555-1234'))
      
#this is crazy too long. use RegEx instead

message = 'Call me at 617-867-5309 tomorrow, or at 123-456-7890 after work'

import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchobject = phoneNumRegex.search(message)
print(matchobject.group())

 
print(phoneNumRegex.findall(message))
