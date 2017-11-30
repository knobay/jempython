""" Exercise 9 M03 Lottery """

import math
import random

def lotterynumbers():
    "Get 7 numbers and print on the screen"
    # initialize drum, 45 numbers. 1 to 9 five times.
    # the ceil function rounds up to the next whole number,
    # so the way I've done it you always get numbers between 1 and 9.
    # since i is varying between 1 and 45.
    drum = []
    for i in range(1, 46):
        drum.append(math.ceil(i/5))
    # draw out the numbers and print on screen

    for i in range(0, 6):
        myrandom = random.randint(0, (44-i))
        print("Ball number {0} is {1}".format(i+1, drum[myrandom]))
        del drum[myrandom]

def bonusball():
    "Get another random number and print on the screen"
    #initialize new drum
    drum = []
    for i in range(1, 13):
        drum.append(math.ceil(i/2))
    #pull out a number
    myrandom = random.randint(0, 11)
    print('and the bonus ball is...', drum[myrandom])

lotterynumbers()
bonusball()
