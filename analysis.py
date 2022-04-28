
#Title - Project for PANDS Submission 2022
#Author - Ruth Keady 

# lines 7 - 26 display the modules that were imported for testing. 

from struct import pack
from sys import displayhook
from tkinter.tix import Tk #tkinter used for creating radio buttons. 
from matplotlib.font_manager import FontProperties #Used to create graphs 
import numpy as np 
import pandas as pd #Used for reading files 
from scipy import rand 
import seaborn as sns #Used to create visual grpahs 
import selenium as se
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import tkinter as tk
import easygui as eas #Used to cerate popup message boxes 
from setuptools import Command
import sys
import matplotlib.pyplot as plt #Library for matplotlib
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
from sklearn.cluster import KMeans

#first the file name must be defined - I created a varibale here that will be used through out the code.Variable are covered in week 1-3 of the lectures.  

file = 'iris.data' 
titles = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species'] 
sns.set(style="whitegrid")
#This piece of code allows the file to be open and read in order for the data to be extracted and also allows for error handling. If the file cannot be found this code will return the text a text statement. The pandas module (pd) allows for the file to be open.  This covers topics from week 7 (files), week 9 (error handling), week 6(modueles). I had a problem with importing pandas - it was not recognised by my PC. I had to run the code from a virtual environment to enable pandas to run correctly reference to how I resolved that issue is found here:  https://stackoverflow.com/questions/65084318/trouble-installing-pandas-on-new-macbook-air-m1
try:
    with open (file, "rt") as f: 
        data = pd.read_csv(file, header=None, names=titles)
except FileNotFoundError:
    eas.msgbox("file was not found - please ensure nameing convention is correct 'irisi.data'", title = "Error")


#Requirement 1 - Output a summary of the Iris Fisher data 
#I wanted to incorporate an if/elif/else statment and also allow the user to have an input on what data was generated to make it more interactive and user friendly. By allowing the end user to select what data is generated the aim is to get a cleaner, data focused result. I thought this could reduce the running time - however no great reduction in running time was noticed between selecting y or n.  This section of code uses objects to group the data associated with generating the radio buttons together. Objects were covered in week 10 of lectures. 

# The object class is called RadioButton - the tk module is used in order to support the generation of the radio buttons. The window requirements are defined (title, size, and color). 
class RadioButton(tk.Tk):
  def __init__(self):
    super().__init__()
    #Box qualities 
    self.title("Report")
    self.geometry("500x400")
    self.config(bg="Gray")

    # define IntVar() for selected value
    self.selected_value = tk.IntVar()
    self.create_widgets()
   #Radio button design
  def create_widgets(self):
    self.intro_label = tk.Label(self, text= "Would you like to generate a Summary Report for Iris Data? ",font="Calib", bg = 'White').pack()
    self.rb1 = tk.Radiobutton(self,text= "Yes",font="Calib", bg = 'White', padx=5, pady=5,variable=self.selected_value,value=1).pack() 
    self.rb2 = tk.Radiobutton(self, text="No",font="Calib", bg = 'White', padx=5,pady=5,variable=self.selected_value,value=2).pack()
    self.text_label = tk.Label(self,font="Calib", bg = 'White', text="Option selected is:",pady=15).pack()
    self.value_label = tk.Label(self,bg = 'White', textvariable=self.selected_value,padx=5,pady=5).pack()
 #Defining that the selected value will be used as the answer. The variable 'answer' will be used for the function 'calc' which will calculate if the report is generated or not based on the answer above . 
    answer = self.selected_value
       # Function for a close button to exit the pop-up screen. 
    def Close():
        self.destroy()

      # Function for calculation: if the answer given in the radio is a yes this will be recorded as a 1. This value will be extracted using .get(). If yes is selected a report will be generated - the data will be printed and grouped by species. The summary will first generate a count of each species using the value_count attribute, the describe attribute will include count, mean, std, min, max as well as lower, 50 and upper percentiles. 

      #This fucntion uses if/else/elif statements that was covered in week 4 of lectures and functions are covered in week 6 of lectures. 

    def calc():
      if answer.get() == 1:
        print(' ')
        print ('Iris Data Summary')
        print('-------------------------------')
        print('Number of Samples in the Study under each Species Type')
        print(' ')
        print (data ['Species'].value_counts())
        print(' ------------------------------')
        print ('Summary of analysis - Count, Mean, Standard Deviation, min, max, and 25th/50th/75th percentiles.')
        print(' ')
        print (data.describe())
        print(' ------------------------------')
        print ('Data of Sepal Length , Sepal Width, Petal Length, and Petal Width - Grouped by Species')
        print(' ')
        print (data .groupby('Species').corr())
        print(' ------------------------------')
        print ('Summary of statistical analysis grouped by species')
        print(' ')
        print('min')
        print(data.groupby('Species').min())
        print(' ')
        print('max')
        print(data.groupby('Species').max())
        print(' ')
        print('mean')
        print(data.groupby('Species').mean())
        print(' ')
        print('median')
        print(data.groupby('Species').median()) 
        print(' ')
        print('std')
        print(data.groupby('Species').std())
        print(' ------------------------------')
        
#Message box to signify that the code has been ran and the report generated. 
        eas.msgbox("Iris Data Summary Report was Successfully generated - Please close the windows to continue", title = "Report Complete")
        

 # if No is enetered in the radio button this will be recorded as a 2. A result of 2 will generate a pop-up message which will state the message below. 
      elif answer.get() ==2:
          eas.msgbox("No was selected - report was not generated", title = "information box - No")
    
#if no radio is selected and nothing is submitted a second message box will open with the message below. 
      else:
          eas.msgbox("No option was selected - report was not generated", title = "information box- Invalid")

#Two buttons were created - one to submit the entry and the second to exit the screen. I attempted to add the close function to the submit button however it appears that two commands cannot be included in the same line. I also attempted to add "sys.exit()" while this allowed the button to close after being selected, the code seemed to stop and did not progress onto requirement 2. 
    self.btn = tk.Button(self,text="click to submit_",padx=5,pady=5,command = calc).pack()
    self.btn = tk.Button(self,text="EXIT_",padx=5,pady=5,command = Close).pack()
#The code below marks the end of the class radio button - without this line of code the window would not display. 
if __name__ == "__main__":
    app = RadioButton()
    app.mainloop()
    


#REQUIREMENT 2:
# Next is to generate a hsitogram - again, i wanted the end user to be considered when writing this code. How would it be applied in the real world? I wanted to create selectable options again - this time, using radio buttons and incorporating functions. An issue I had with this was that when I selected 'yes' for the graph and had them appear on the screen using show() the information boxes generated under requirement 1 appeared - they were blank with no selectable options but you had to close them in order for the code to continue. A workaround for this was not to have the graphs display on the screen but rahter save them to the PC instead. I researched out to remove the information boxes however I did not find a successful solution. 

#Histogram. Origionally tried to enter the height and wigth of the diagram however an error message occured to say that those commands are no longer supported by 3.3. Through research it was found that the dpi can be used for size adjustment. Histograms and plots are covered in week 8 of lectures. 
report = input("Would you like to generate a histogram for the Iris data set? (y/n): ")

if report == 'y' or report =='Y':
    p_length = sns.FacetGrid(data,hue = "Species", height=3)
    p_length.map(sns.histplot,"Petal Length").add_legend()
    plt.savefig('rkPetalLength.png', dpi = 750)
    
    p_width = sns.FacetGrid(data,hue = "Species",height=3)
    p_width.map(sns.histplot,"Petal Width").add_legend()
    plt.savefig('Histogram:PetalWidth.png', dpi = 750)
    
    s_length=sns.FacetGrid(data,hue = "Species",height=3)
    s_length.map(sns.histplot,"Sepal Length").add_legend()
    plt.savefig('Histogram:SepalLength.png', dpi = 750)
    
    s_width=sns.FacetGrid(data,hue = "Species", height=3)
    s_width.map(sns.histplot,"Sepal Width").add_legend()
    plt.savefig('Histogram:SepalWidth.png', dpi = 750)

elif report == 'n' or report == 'N':
    #print("Ok, No was selected - Histogram was not generated") 
    eas.msgbox("Ok, No was selected - Histogram was not generated - Please close the windows to continue", title = "Report Complete")
else:
    #print("No Valid entry was inputted - Histogram was not generated") 
    eas.msgbox("Ok, No valid value was selected - Histogram was not generated - Please close the windows to continue", title = "Report Complete") 
#plt.show()
plt.clf()

#REQUIREMENT 3 - Generate scatter plots. Similar to requirement 2 I incorporated radio buttons, imformation messages, else/if/elis statments, and object classes to enable graph selection. I noticed that I could get more detailed scatter grpahs using seaborn however they were not recognised within the else/if/else statements in combination with the radio buttons. To show both functionality, I've included additional scatter plots using sns under the section requirement 4. 


print ("Please select an option in the 'Scatter' dialog, submit, and close the window") 
class RadioButton2(tk.Tk):
  def __init__(self1):
    super().__init__()
    self1.title("Scatter")
    self1.geometry("500x400")
    self1.config(bg="lightblue")
    self1.selected_value2 = tk.IntVar()
    self1.create_widgets2()

  def create_widgets2(self1):
    self1.intro_label = tk.Label(self1, text= "Scatter Plot ",font="Calib", bg = 'White').pack()
    self1.rb1 = tk.Radiobutton(self1,text= "Yes",font="Calib", bg = 'White', padx=5, pady=5,variable=self1.selected_value2,value=1).pack() 
    self1.rb2 = tk.Radiobutton(self1, text="No",font="Calib", bg = 'White', padx=5,pady=5,variable=self1.selected_value2,value=2).pack()
    self1.text_label = tk.Label(self1,font="Calib", bg = 'White', text="Option selected is:",pady=15).pack()
    self1.value_label = tk.Label(self1,bg = 'White', textvariable=self1.selected_value2,padx=5,pady=5).pack()

    scatter = self1.selected_value2
       # Function for a close button to exit the pop-up screen.

    def calc2():
        if scatter.get() == 1:
            sns.scatterplot(data = data, x= "Petal Length", y = "Petal Width", legend = True, hue = "Species" )
            plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])
            

            filename = "Scatter Plot: Petal Length vs Petal Width.jpg"
            #plt.show()
            plt.savefig(filename)
            plt.clf()

            sns.scatterplot(data = data, x= "Sepal Length", y = "Sepal Width", legend = True, hue = "Species" )
            plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])
            
            filename = "Scatter Plot: Sepal Length vs Sepal Width.jpg"
            #plt.show()
            plt.savefig(filename)
            plt.clf()

            sns.scatterplot(data = data, x= "Petal Length", y = "Sepal Length", legend = True, hue = "Species" )
            plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])
            
            filename = "Scatter Plot: Petal Length vs Sepal Length.jpg"
            #plt.show()
            plt.savefig(filename)
            plt.clf()

            sns.scatterplot(data = data, x= "Petal Width", y = "Sepal Width", legend = True, hue = "Species" )
            plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])
           
            filename = "Scatter Plot: Petal Width vs Sepal Width.jpg"
            #plt.show()
            plt.savefig(filename)
            plt.clf()

            sns.scatterplot(data = data, x= "Petal Width", y = "Sepal Length", legend = True, hue = "Species" )
            plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])
            
            filename = "Scatter Plot: Petal Width vs Sepal Length.jpg"
            #plt.show()
            plt.savefig(filename)
            plt.clf()

            sns.scatterplot(data = data, x= "Petal Length", y = "Sepal Width", legend = True, hue = "Species" )
            plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])
            
            filename = "Scatter Plot: Petal Length vs Sepal Width.jpg"
            #plt.show()
            plt.savefig(filename)
            plt.clf()

            eas.msgbox("Scatter Plots were Saved - Please close the windows to continue", title = "Report Complete")

        elif scatter.get() ==2:
            eas.msgbox("Ok, No was selected - scatter plot was not generated", title = "information box - No Scatter")
        else:
            eas.msgbox("Ok, No was selected - scatter plot was not generated", title = "information box - Invalid Scatter")

    def Close2():
        self1.destroy()

    self1.btn = tk.Button(self1,text="click to submit_",padx=5,pady=5,command = calc2).pack()
    self1.btn = tk.Button(self1,text="EXIT_",padx=5,pady=5,command = Close2).pack()

if __name__ == "__main__":
    app = RadioButton2()
    app.mainloop()

#REQUIREMENT 4:
# Add aditional data for analysing - I first looked at what other plots were available using seaborn, sklearn, and matlibpot. Through this I found jointplots, line pots, additional scatter plots, and 3D cluster plots. I combined to if/else/elif statements to support end user interface. 
join_reps = input ("Would you like to generate and save jointplot reports? (y/n):")

if join_reps == 'y' or join_reps =='Y':
    sns.jointplot(data=data, x = "Petal Length", y = "Sepal Length", kind= "reg", height=7, ratio=2, marginal_ticks=True)
    plt.suptitle("Petal Length vs Sepal length")
    filename = "Joint Plots: Petal Length vs Sepal length.jpg"
    plt.savefig(filename)

    sns.jointplot(data=data, x = "Petal Length", y = "Sepal Length", hue = "Species", height=7, ratio=2, marginal_ticks=True)
    plt.suptitle("Petal Length vs Sepal length")
    filename = "Joint Plots: Petal Length vs Sepal length.jpg"
    plt.savefig(filename)

    sns.jointplot(data=data, x = "Petal Width", y = "Sepal Width", kind= "reg", height=7, ratio=2, marginal_ticks=True)
    plt.suptitle("Petal Width vs Sepal Width")
    filename = "Joint Plots: Petal Width vs Sepal Width.jpg"
    plt.savefig(filename)

    sns.jointplot(data=data, x = "Petal Width", y = "Sepal Width", hue = "Species", height=7, ratio=2, marginal_ticks=True)
    plt.suptitle("Petal Width vs Sepal Width")
    
    filename = "Joint Plots: Petal Width vs Sepal Width.jpg"
    plt.savefig(filename)
    #plt.show()
    plt.clf()

elif join_reps == 'n' or join_reps == 'N':
    print("Ok, No was selected - additional graphs were generated")
else:
    print("No valid option was selected - additional graphs were generated")

line_rep = input ("Would you like to generate and save line reports? (y/n):")
if line_rep == 'y' or line_rep =='Y':
    sns.set_theme(style="darkgrid") #Setting backgrond color

    sns.lineplot(x="Petal Length", y="Petal Width",hue="Species",data=data) 
    #Defining x and y attributes and to color them by species. 
    plt.suptitle("Petal Length vs Sepal Width")
    #plt.show() 
    filename = "Line Graphs: Petal Length vs Petal Width.jpg"
    plt.savefig(filename)
    plt.clf()

    sns.lineplot(x="Sepal Length", y="Sepal Width", hue="Species",data=data)
    plt.suptitle("Sepal Length vs Sepal Width")
    filename = "Line Graphs: Sepal Length vs Sepal Width.jpg"
    plt.savefig(filename)
    #plt.show()
    plt.clf()
    
    sns.lineplot(x="Petal Length", y="Sepal Length",hue="Species",data=data)
    plt.suptitle("Petal Length vs Sepal length")
    filename = "Line Graphs: Petal Length vs Sepal Length.jpg"
    plt.savefig(filename)
    #plt.show()
    plt.clf()
    
    sns.lineplot(x="Petal Width", y="Sepal Width",hue="Species",data=data)
    plt.suptitle("Petal Width vs Sepal Width")
    filename = "Line Graphs: Petal Width vs Sepal Width.jpg"
    plt.savefig(filename)
    #plt.show()
    plt.clf()
    
elif line_rep == 'n' or line_rep == 'N':
    print("Ok, No was selected - additional graphs were generated")
else:
    print("No valid option was selected - additional graphs were generated")

cluster_rep = input ("Would you like to generate a cluster report? (y/n):")
if cluster_rep == 'y' or cluster_rep =='Y':
    
    #Requirement 4 - Additional Data #3D Cluster plots using sklearn
    np.random.seed(5)
    iris = datasets.load_iris() #the sklearn module already has teh iris dataset and therefore does not have to be imported from a file. 
    X = iris.data
    y = iris.target


    fig = plt.figure("3D Cluster plot", figsize=(7, 8)) #Defining figure name and size
    ax = fig.add_subplot(111, projection="3d", elev= -150, azim= 100)  
    ax.set_position([0, 0, 0.90, 1]) #alternating the axis of the graph

#Assigning the labels to each data set 
    for name, label in [("I.Setosa", 0), ("I.Versicolour", 1), ("I.Virginica", 2)]:
        ax.text3D(
            X[y == label, 3].mean(),
            X[y == label, 0].mean(),
            X[y == label, 2].mean() + 2,
            name,
            horizontalalignment="center",
            bbox=dict(alpha=0.2, edgecolor="w", facecolor="w"),
        )
    # Reordering  the labels to have colors matching the cluster results
    y = np.choose(y, [1, 2, 0]).astype(float)
    ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=y, edgecolor="blue")

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel("Petal width")
    ax.set_ylabel("Sepal length")
    ax.set_zlabel("Petal length")
    ax.set_title("3D Cluster Plot")
    ax.dist = 12

    filename = "3D Cluster Graph: Petal width, Sepal Length, Petal Width.jpg"
    
    plt.savefig(filename)
    #plt.show()
    plt.clf()
    
elif cluster_rep == 'n' or cluster_rep == 'N':
    print("Ok, No was selected - additional graphs were generated")
else:
    print("No valid option was selected - additional graphs were generated")


eas.msgbox("You have reached the end of the Project - thank you!  ", title = "Code Complete")

