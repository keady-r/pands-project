#Author Ruth Keady 

#Task 2:
#1Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py
#The inputs are the person's height in centimetres and weight in kilograms.
#The output  their BMI (You may need to look up how this is calculated)

#Enter weight(kg): 65
#Enter height(cm): 180
#The BMI is (kg/m2) 20.06

#1. thing is to allow user to input values use unput function
#2. need to assign a type - in this case it's a float. Decimal point needed 
#3. define the calculation for the BMI (weight kg / height meters squared )
#4. Use print function to display value. 

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in cm: "))

BMI = (weight /((height/100)**2))


print(BMI)

#Alternative approach - using functions 
def my_function(x):
    return ((x/100)**2)

weight2 = float(input("Enter weight in kg: "))
height2 = float(input("Enter height in cm: "))
convert = my_function(height2)
BMI2 = (weight2 /convert)


print(BMI2)

#adding rounding 
def my_function(x):
    return ((x/100)**2)

weight3 = float(input("Enter weight in kg: "))
height3 = float(input("Enter height in cm: "))
convert3 = my_function(height2)
BMI3 = round((weight /convert3),2)


print(BMI3)

#END