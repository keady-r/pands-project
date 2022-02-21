#Writing code to test variables and variable types#
#Author Ruth Keady#

#List below specifies the variables#
i = 3
fl = 3.5 
isa = True 
memo = "How now Brown Cow"
lots = []

#Instructions below instruct the system to print the variables listed above and to give the variables a type#
print('variable {} is of type:{} and value:{}'.format('i', type(i), i))
print('variable {} is of type:{} and value:{}'.format('fl', type(fl), fl))
print('variable {} is of type:{} and value:{}'.format('is', type(isa), isa))
print('variable {} is of type:{} and value:{}'.format('memo', type(memo), memo))
print('variable {} is of type:{} and value:{}'.format('lots', type(lots), lots))

#Program to subtract one number from another#
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer= x-y
print("{} minus {} is {} ".format(x, y, answer))

#Program for dividing numbers #
x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division
remainder = x%y # % gives the remainder
print("{} divided by {} is {} with remainder {}".format( x, y,
answer, remainder))

#Random Number#
import random
number = random.randint(1,10)
print("here is a random number {}".format(number))

#Random Fruits and Lists #

import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))

#Neater Randon Fruits#

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')

index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))

#Fix the expression#
#Looking at it before running I would guess that the 99 needs to be turned into a string.#
message = 'I have eaten ' + str(99) + ' burritos.'
print (message)

#In the above expression Why is eggs a valid variable name while 100 is invalid? - the code will not recognise 100 as a variable, must start with a letter or _#
#8. What three functions can be used to get the integer, floating-point number, or string version of a value? - you can add a type in, fl, str before the value to get integer, floating-point number, or string retrospectively.  #