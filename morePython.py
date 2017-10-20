a = 'AAA'
b = 'BBB'
a,b = b,a
print('a='+ a)
print('b='+ b)


mylist = ['Jenn', 'Keira', 'Lucy']
print(mylist.index('Keira'))

#adds to the end of list
mylist.append('Spiderman')

#bumps list
mylist.insert(1, 'Iron Man')

print()

print(mylist)

mylist.remove("Iron Man")
print(mylist)

del mylist[3]

print(mylist)

mylist.sort()
print('now sort')
#Python sorts uppercase before lowerase, Ascii-betical
#mylist.sort(key=str.lower) will fix this
print(mylist)
mylist.sort(reverse=True)
print('reverse sort')
print(mylist)

#you can slice strings too
myname = 'Jennifer'
print(myname[0:4])

for letter in myname:
    print(letter)


#strings are immutable; they cannot be changed

    #when you assigna  list to another list, it just assigns a reference.
    #they both get changed when you cahgne one of them
