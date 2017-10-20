def eggs(someParameter):
    someParameter.append('Hello')

#reference to spam
spam = [1,2,3]
eggs(spam)

print(spam)


import copy
#creates a copy, not a reference; immutable
#lists are mutable, strings are immutable.
cheese = copy.deepcopy(spam)

fruits = ['apples',
          'bananas',
          'oranges']


myquote = 'Four score and seven' + \
          ' years ago blah blah blah'

print(myquote)

