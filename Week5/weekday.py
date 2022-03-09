#Author Ruth Keady - Extracted from https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python

#Write a program that outputs whether or not today is a weekday.(You will need to search the web to find how you work out what day it is)An example of running this program on a Thursday is given below.Yes, unfortunately today is a weekday.An example of running it on a Saturday is as follows:It is the weekend, yay!

# How to Find the Current Day is Weekday or Weekends in Python

# Import Module
import datetime

# To Get the Week Number
weekNumber = datetime.datetime.today().weekday()

if weekNumber < 5:
    print("Today's DateTime is {0} and it's a Weekday".format(datetime.datetime.today()))
else:
    print ("Today's DateTime is {0} and it's a Weekend".format(datetime.datetime.today()))
