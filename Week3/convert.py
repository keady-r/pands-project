#convert#
import math
number = float(input("Enter a number:"))
absoluteValue = abs(number)
answer = (float(absoluteValue) * 100)
print('The absolute value of {} is {}'.format(number, absoluteValue))
print ('When converted into cents {} is equal to {}' .format (absoluteValue, answer))