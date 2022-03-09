#Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.Have the program end if the current value is one.
#Please enter a positive integer: 10
#10 5 16 8 4 2 1

#Break this down into pieces 1. input values 

number = int(input("PLease enter a positive integer:"))
if (number % 2) == 0:
 print ("{} is an even number".format(number))
else:
 print("{} is an odd number".format(number))