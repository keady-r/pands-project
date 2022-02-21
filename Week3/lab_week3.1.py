#Fun with Numbers#
#Write a program called round.py. The program take in a float and outputs an int (rounded up or down)#

#Author Ruth Keady#
lab = "week 3"


print ('The following is Ruth Keady\'s attempt at {}' . format (lab))

numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound,roundedNumber))

print ('The following is lab {} exercise 2' . format (lab))

number = float(input("Enter a number:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))

print ('The following is lab {} exercise 3' . format (lab))

import math
numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))

print ('The following is lab {} exercise 4' . format (lab))

#convert#
import math
number = float(input("Enter a number:"))
absoluteValue = abs(number)
answer = (float(absoluteValue) * 100)
print('The absolute value of {} is {}'.format(number, absoluteValue))
print ('When converted into cents {} is equal to {}' .format (absoluteValue, answer))