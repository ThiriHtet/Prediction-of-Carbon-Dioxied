import pandas
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
import sklearn

#*******************************    Reading and printing Dataset    ***************************************

dataSet = pandas.read_csv("carcpy.csv")
Volume = dataSet["Volume"]
Gas = dataSet["GSG"]

#********************************Working with Linear Regression Equation **********************************
slope,intercept,r,p,stderr = stats.linregress(Volume,Gas)

def lin(Volume):
    return slope * Volume + intercept # Y = SLOPE * x + INTERCEPT
        
#*******************Data Visualization with LinearRegression *****************
def VisualV():
    model = list(map(lin,Volume))
    plt.plot(Volume,model) 
    plt.ylabel("GreenHouse Gas")
    plt.xlabel("Car Cylinder Volume")
    plt.title("Cylinder Volume of car Vs GreenHouse Gas")
    plt.scatter(Volume,Gas,marker="*" ,color = "r") 
    plt.show()

#****************************** getting input   ************************************************
def calculateVolume():
    print("slope between Volume and Greenhouse gas :",slope)
    print("intercept value between Volume and Greenhouse gas :",intercept) 
    i = input("enter Volume of car: \n")
    a = int(i)  
    ans =  0.052839951865222626* a + 43.74824651882413# ans = slope * a + intercept
    answer = int(ans)
    print ("the resulting greenhouse gas depended upon Volume is  ",answer,"g/km")
# VisualV()
# calculateVolume()