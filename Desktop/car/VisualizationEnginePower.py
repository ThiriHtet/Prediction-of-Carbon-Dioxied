import pandas
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
import sklearn

#*******************************    Reading the Dataset    ***************************************

dataSet = pandas.read_csv("carcpy.csv")
enginePower = dataSet["Power"]
Gas = dataSet["GSG"]

#********************************Working with Linear Regression Equation **********************************
slope,intercept,r,p,stderr = stats.linregress(enginePower,Gas)

def lin(enginePower):
        return slope * enginePower + intercept # Y = SLOPE * x + INTERCEPT

    
#*******************Data Visualization with LinearRegression *****************
def visualP():    
    model = list(map(lin,enginePower))
    plt.plot(enginePower,model) 
    plt.ylabel("GreenHouse Gas")
    plt.xlabel("enginePower of car")
    plt.title("EnginePower of car Vs GreenHouse Gas")
    plt.scatter(enginePower,Gas,marker="*" ,color = "aqua") 
    plt.show()

#****************************** getting input   ************************************************
def calculatePower(): 
    print("slope between Engine Power and Greenhouse gas :",slope)
    print("intercept value between Engine Power and Greenhouse gas :",intercept)
    i = input("enter engine power: \n")
    a = int(i)  
    ans = 0.27777092402319314* a + 77.36033153149523
    answer = int(ans)
    print ("the resulting greenhouse gas depended upon engine power is  ",answer,"g/km")
# visualP()
# calculatePower()