


theBoard = {'top-L':'X','top-M':'O', 'top-R':'X',
            'mid-L':' ','mid-M':' ', 'mid-R':' ',
            'low-L':' ','low-M':' ', 'low-R':' '
            }

import pprint

#pprint.pprint(theBoard)

#inputvalue = 
print(type(inputvalue))

def printTheBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
printTheBoard(theBoard)
