#do math

total = 0

for num in range(101):
    total = total + num


print(total)

print('Running a loop 12-16')

for i in range(12,16) :
    print('The number is...' + str(i))

print('Running a loop 0-10 with increments')
for i in range(0,10,1) :
    print('The number is...' + str(i))

print('Running a loop 0-10 with step increments')
for i in range(0,10,2) :
    print('The number is...' + str(i)) 


smap = 'global variable'


def newfunction():
    smap = 'local variable'



print(smap)    
