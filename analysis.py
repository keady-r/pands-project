
#Title - Project for PANDS Submission 2022
#Author - Ruth Keady 
#Aim - The aim of this project was to incorporate all the learnings from the lectures through week 1-13 to show as much of an understanding of the code. I aimed to cover all the asks of the project 1) extract data into file  2) Create histograms 3) scatter plots 4) additional analysis but also make the code suitable for end user use - I tried to imiage how this code could be used in a system. In alot of the cases I've added check-points or input options so that the code does not run all at once - this was intentional to create an end user interface and also to explore new options and chalenge my ability. 

# lines - display the modules that were imported. Through reviewing each one online I gained a greater insight as to how I can apply each one to create differnt coding outcome. 
from curses import BUTTON1_CLICKED
from struct import pack
from tkinter.tix import Tk
from matplotlib.font_manager import FontProperties
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import selenium as se
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import tkinter as tk
import colorama as col
from colorama import Fore
import easygui as eas

from setuptools import Command
#first the file name must be defined - I created a varibale here that will be used through out the code.Variable are covered in week 1-3 of the lectures.  

file = 'iris.data' 
titles = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species'] 
#This piece of code allows the file to be open and read in order for the data to be extracted and also allows for error handling. If the file cannot be found this code will return the text a text statement. The pandas module (pd) allows for the file to be open.  This covers topics from week 7 (files), week 9 (error handling), week 6(modueles). 
try:
    with open (file, "rt", "a") as f: 
        data = pd.read_csv(file, header=None, names=titles)
except FileNotFoundError:
    print("file was not found - please ensure nameing convention is correct/'irisi.data'")


#Requirement 1 - Output a summary of the Iris Fisher data 
#I wanted to incorporate an if/elif/else statment and also allow the user to have an input on what data was generated to make it more interactive and user friendly. By allowing the end user to select what data is generated the aim is to get a cleaner, data focused result. I thought this could reduce the running time - however no great reduction in running time was noticed between selecting y or n.  This section of code uses objects to group the data associated with generating the radio buttons together. Objects were covered in week 10 of lectures. 

# The object class is called RadioButton - the tk module is used in order to support the generation of the radio buttons. The window requirements are defined (title, size, and color). 
class RadioButton(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Do you wish to generate a report ?")
    self.geometry("500x400")
    self.config(bg="Gray")

    # define IntVar() for selected value
  
    self.selected_value = tk.IntVar()
    self.create_widgets()

  def create_widgets(self):
    self.intro_label = tk.Label(self, text= "Would you like to generate a report ",font="Calib", bg = 'White').pack()
    self.rb1 = tk.Radiobutton(self,text= "Yes",font="Calib", bg = 'White', padx=5, pady=5,variable=self.selected_value,value=1).pack() 
    self.rb2 = tk.Radiobutton(self, text="No",font="Calib", bg = 'White', padx=5,pady=5,variable=self.selected_value,value=2).pack()
    self.text_label = tk.Label(self,font="Calib", bg = 'White', text="Option selected is:",pady=15).pack()
    self.value_label = tk.Label(self,bg = 'White', textvariable=self.selected_value,padx=5,pady=5).pack()

    answer = self.selected_value
       # Function for a close button to exit the pop-up screen. 
    def Close():
        self.destroy()

      # Function for calcularion: if the answer given in the radio is a yes this will be recorded as a 1. This value will be extracted using .get(). If yes is selected a report will be generated - the data will be printed and grouped by species. The summary will first generate a count of each species using the value_count attribute, the describe attribute will include count, mean, std, min, max as well as lower, 50 and upper percentiles. 

      #This fucntion uses if/else/elif statements that was covered in week 4 of lectures and functions are covered in week 6 of lectures. 

    def calc():
      if answer.get() == 1:
        print (data ['Species'].value_counts())
        print(' ')
        print (data.describe())
        print (' ') 
        print (data .groupby('Species').corr())
 # if No is enetered in the radio button this will be recorded as a 2. A result of 2 will generate a pop-up message which will state the message below. 
      elif answer.get() ==2:
          eas.msgbox("No was selected - report was not generated", title = "information box")
#if no radio is selected and nothing is submitted a second message box will open with the message below. 
      else:
          eas.msgbox("No option was selected - report was not generated", title = "information box")
#Two buttons were created - one to submit the entry and the second to exit the screen. I attempted to add the close function to the submit button however it appears that two commands cannot be included in the same line. 
    self.btn = tk.Button(self,text="click to submit_",padx=5,pady=5,command = calc).pack()
    self.btn = tk.Button(self,text="EXIT_",padx=5,pady=5,command = Close).pack()

if __name__ == "__main__":
    app = RadioButton()
    app.mainloop()
   


#REQUIREMENT 2:
# Next is to generate a hsitogram - again, i wanted the end user to be considered when writing this code. How would it be applied in the real world? I wanted to create selectable options again - this time, using radio buttons and incorporating functions. 
'''''
i_setosa = data.loc[data["Species"]=="I.setosa"] 
i_virginica = data.loc[data["Species"]=="I.virginica"]
i_versicolor = data.loc[data["Species"]=="I.versicolor"] 
'''

#Histogram. Origionally tried to enter the height and wigth of the diagram however an error message occured to say that those commands are no longer supported by 3.3. Through research it was found that the dpi can be used for size adjustment. Histograms and plots are covered in week 8 of lectures. 
report = input("Would you like to generate a histogram for the Iris data set? (y/n): ")

if report == 'y' or report =='Y':
    p_length = sns.FacetGrid(data,hue = "Species", height=3)
    p_length.map(sns.histplot,"Petal Length").add_legend()
    plt.savefig('rkPetalLength.png', dpi = 700)
    
    p_width = sns.FacetGrid(data,hue = "Species",height=3)
    p_width.map(sns.histplot,"Petal Width").add_legend()
    plt.savefig('rkPetalWidth.png', dpi = 700)
    
    s_length=sns.FacetGrid(data,hue = "Species",height=3)
    s_length.map(sns.histplot,"Sepal Length").add_legend()
    plt.savefig('rkSepalLength.png', dpi = 700)
    
    s_width=sns.FacetGrid(data,hue = "Species", height=3)
    s_width.map(sns.histplot,"Sepal Width").add_legend()
    plt.savefig('rkSepalWidth.png', dpi = 700)
elif report == 'n' or report == 'N':
    print ("Ok, no histogram was generated")
else:
    print ("An invlaid result was inputted - no histogram was generated")

plt.show()
#REQUIREMENT 3 - Generate scatter plots 
scatter = input("would you like to generate a scatter report?(y/n):")
if scatter == 'y':
    class RadioButton(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Scatter Plot Graph Selection")
            self.geometry("500x400")
            self.config(bg="Gray")
            
            self.selected_value = tk.IntVar()
            self.create_widgets()
            
        def create_widgets(self):
            self.intro_label = tk.Label(self, text= "Choose what data you wish to use to show on the scatter plot",font="Calib", bg = 'White').pack()
            self.rb1 = tk.Radiobutton(self,text= "Scatter Plot for Pettals (width vs length)",font="Calib", padx=5, pady=5,variable=self.selected_value,value=1).pack()
            self.rb2 = tk.Radiobutton(self, text="Scatter Plot for Sepal (width vs length)",font="Calib", padx=5,pady=5,variable=self.selected_value,value=2).pack()
            self.text_label = tk.Label(self,font="Calib", text="Option selected is:",pady=15).pack()
            self.value_label = tk.Label(self, textvariable=self. selected_value,padx=5,pady=5).pack()
            endresult = self.selected_value

            def calc():
                if endresult.get() == 1:
                    data.plot(kind='scatter', x = 'Sepal Length', y = 'Sepal Width' )
                    plt.show()
                elif endresult.get() ==2:
                    data.plot(kind='scatter', x = 'Petal Length', y = 'Petal Width' )
                    plt.show()
                else:
                    print ("No Selection was made and therefore no graph was produced")
            def Close():
                self.destroy()
            self.btn = tk.Button(self,text="click to submit_",padx=5,pady=5,command = calc).pack()
            self.btn = tk.Button(self,text="EXIT_",padx=5,pady=5,command = Close).pack()
elif scatter == 'n':
    print ("no scatter plot was created")
else:
    print ("No Valid result was entered and hence no scatter plot was generated")

if __name__ == "__main__":
    app = RadioButton()
    app.mainloop()

