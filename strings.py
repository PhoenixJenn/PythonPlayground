mystr = 'hello world'
print(mystr.upper())

print('type yes')
answer = input()

if answer == 'yes':
    print('ok!')
          
if answer.isupper():
    print('why do you not follow directions. Lower case!')

#isalpha()
    #isalnum() -- letters and numbers only
    #isdecimal()
    #isspace
    #istitle --- titlecase
    #startswith()
    #endswith()

print('Hello World'.startswith('Hello'))


s = ','.join(['cats','rats','bats'])
print(s)

#adds 2 line breaks between each letter
print('\n\n'.join(s))

m = 'My name is simon'
print(m.split())
#.split('m') will give it something weird to split on


# string.rjust(10) adds whitespace ot make chars = 10
# ljust(20)   left justifies
# ljust(20,'--')
# string.center(20,'=') pads with equal signs
# string.strip() -- removes white space to print, but doesn't alter original string
# lstrip and rstrip removes whtiespace
# .lstrip('wordsToRemoveHere')
# string.replace('e','XYZ')
# pip piperclip
#find python folder \scripts


