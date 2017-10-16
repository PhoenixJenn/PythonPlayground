# This program says hello and asks for my name
import random
import time


def displayIntro():
    print('some stuff intro blah')
    print()


def chooseSomething():
    something = ''
    while something != '1' and something != '2':
        print('choose 1 or 2 or 3')
        something = input()
    return something

def checkSomething(something):
    print('Hello world!')
    time.sleep(2)
    print('what is your name?')
    myName = input()
    print("good to meet you," + myName)
    print(len(myName))
    if myName == 'Jenn':
        print('Hi Jenn!')

    theThing = random.randint(1,3)
    
    if str(something) == str(theThing):
        print('Good job.')
    else:
        print('better luck next time, I chose:' + str(theThing))


displayIntro()

numSomething = chooseSomething()

checkSomething(numSomething)

tryThis = 10
while  tryThis > 0:
    tryThis -=1
    print(tryThis)
    if tryThis == 4:
        continue #skip this part for ONLY 4, jump back to start
    print('keep going')
    if tryThis ==2:
        break


for i in range(5):
    print(i)
    

# elif a==b:
    

