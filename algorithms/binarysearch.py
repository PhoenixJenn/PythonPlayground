

import random

thenumber = random.randrange(0, 101, 2)
print('The Guess is:' + str(thenumber))
print()


def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = int((low+high)/2)
        guess = list[mid]
        if guess == item:
            #print(mid)
            print('The guess is : ' + str(list[mid]))
            return mid
        if guess > item:
            high = mid-1
            #print(high)
            print('Guess is lower than mid of ' + str(list[high]))
        else:
            low = mid + 1
            #print(low)
            print('Guess is higher than mid of ' + str(list[low]))

            
valuelist  = list(range(0,100,2))

binary_search(valuelist, thenumber)

    
