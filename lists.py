
myarray = ['a','b','c','d']
print(myarray[0])
print(myarray[-1]) #refers to the last item in the list
print(myarray[1:3]) #slice
print(myarray[:3])
del myarray[2]
print(myarray)

mylist = [['cat','bat'], [1,2,3],['third', 'list']]
print(mylist[0])


print(mylist[:1])


print()

print('Hello'*5)

print()
print([1,2,3]+[4,5,6])

#string manipulation is the same as list maniupulation

print(list('Hello'))


print()

print('howdy' in ['hello', 'hi', 'howdy', 'heya'])
print()

print('howdy' not in ['hello', 'hi', 'howdy', 'heya'])


for i in range(4):
    print(i)
print()
 
print(range(4))

print()
print(list(range(4)))
print()
spam = list(range(0,100,2))
print(spam)


#
supplies = ['pens', 'staples','notebooks','binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

