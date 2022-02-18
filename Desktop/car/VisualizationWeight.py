import pandas
import numpy
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model

#*******************************    Reading and Dataset    ***************************************)

dataSet = pandas.read_csv("carcpy.csv")
Weight= dataSet["Weight"]
Gas = dataSet["GSG"]
# print(Weight.min()) 
# print(Weight.max())
#********************************Working with Linear Regression Equation **********************************
    
slope,intercept,r,p,stderr = stats.linregress(Weight,Gas)

def lin(Weight):
    return slope * Weight + intercept # Y = SLOPE * x + INTERCEPT

 #*******************Data Visualization with LinearRegression *****************

def visualW():
    model = list(map(lin,Weight))
    plt.plot(Weight,model) 
    plt.ylabel("Greenhouse Gas")
    plt.xlabel("Car Weight")
    plt.title("Car Weight Vs Greenhouse Gas")
    plt.scatter(Weight,Gas,marker="*" ,color = "g") 
    plt.show()

#****************************** getting input   ************************************************

def calculate():
    print ("slope between Weight and Greenhouse gas :",slope)
    print (f'intercept value between Weight and Greenhouse gas: {intercept} ')
    i = input("enter Weight of car: \n")
    a = int(i)  
    ans =  0.0444836445679839* a +  66.15265918885231 
    answer = int(ans)
    print ("the resulting greenhouse gas depended upon Weight of car is  ",answer,"g/km")
# visualW()
# calculate()