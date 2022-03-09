#Author Ruth Keady 
#Task 3 

#Write a program that asks a user to input a string and outputs every second letter in reverse order.
#Please enter a sentence: The quick brown fox jumps over the lazy dog - .o zletrv pu o wr cu h

#Here we are defining a function x, splicing it and returning every second number#

#What happens if we take the '-' sign away = Every second letter is returned but it is not reversed#

#What happens if I do return x[-2]. All that is returned is g i.e. the second element. 

#What happends if I do return x[:-2]. Whole sentence is printed in order but the 'g' is removed



def my_function(x):
  return x[::-2]

mytxt = my_function("The quick brown fox jumps over the lazy dog ")

print(mytxt)